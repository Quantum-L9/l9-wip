from __future__ import annotations

import argparse
import asyncio
from datetime import UTC, datetime
from uuid import uuid4

from pymongo import AsyncMongoClient
from pymongo.server_api import ServerApi

from l9_state.adapters.mongodb import MongoStateStore
from l9_state.catalog import ConfiguredContractCatalog
from l9_state.cursor import CursorCodec
from l9_state.execution import ExecutionBudget
from l9_state.models import (
    StateClaimRequest,
    StateCreateRequest,
    StateReleaseRequest,
    StateTombstoneRequest,
    StateTransitionRequest,
)
from l9_state.retention import prepare_hard_erase_plan
from l9_state.service import CallerContext, StateService

SCHEMA_DIGEST = "a" * 64
RETENTION_DIGEST = "b" * 64
SCHEMA_REF = "urn:l9:state:validate:v1"
RETENTION_REF = "retention.validate"


def caller(name: str) -> CallerContext:
    return CallerContext(
        tenant_org_id="tenant-validate",
        principal_ref=name,
        authorization_ref=f"state.authz.tenant-base:{name}",
        execution_budget=ExecutionBudget.start(30_000),
        causation_ref=f"validate:{name}",
    )


def create_req(object_id: str, op: str) -> StateCreateRequest:
    return StateCreateRequest(
        contract_version="1.0",
        object_id=object_id,
        scope_ref="scope.validate",
        schema_ref=SCHEMA_REF,
        schema_digest=SCHEMA_DIGEST,
        payload={"value": 1},
        operation_id=op,
        retention_policy_ref=RETENTION_REF,
        retention_policy_digest=RETENTION_DIGEST,
    )


async def run(uri: str, database: str) -> None:
    client: AsyncMongoClient = AsyncMongoClient(
        uri,
        server_api=ServerApi("1"),
        serverSelectionTimeoutMS=5000,
        tz_aware=True,
        retryWrites=True,
    )
    store = MongoStateStore(client, database)
    catalog = ConfiguredContractCatalog()
    catalog.admit_schema(SCHEMA_REF, SCHEMA_DIGEST, lambda p: isinstance(p.get("value"), int))
    catalog.admit_retention(RETENTION_REF, RETENTION_DIGEST)
    service = StateService(store, catalog, cursor_codec=CursorCodec(b"v" * 32))

    try:
        hello = await client.admin.command("hello")
        assert hello.get("setName"), "VALIDATE-FAIL: MongoDB target is not a replica set"
        assert hello.get("isWritablePrimary") is True, "VALIDATE-FAIL: no writable primary"
        await client.drop_database(database)
        await store.ensure_indexes()

        # MONGO-01: index creation and uniqueness names.
        required = {
            "uq_state_key", "uq_state_revision", "uq_state_operation", "uq_scope_journal_seq",
            "uq_event_id", "uq_state_claim_lineage", "uq_consumer_cursor", "uq_scope_counter",
        }
        observed: set[str] = set()
        for name in (
            "state_objects", "state_revisions", "state_operations", "state_events",
            "state_claims", "state_consumer_cursors", "state_scope_counters",
        ):
            async for idx in client[database][name].list_indexes():
                if idx.get("name") in required:
                    observed.add(str(idx["name"]))
        assert observed == required, f"VALIDATE-FAIL: index set mismatch {sorted(observed)}"
        print("PASS MONGO-01 indexes")

        # MONGO-02: concurrent CAS, exactly one winner.
        created = await service.create(caller("agent-a"), create_req("object.cas", "op.cas.create"))
        assert created.status == "committed" and created.state_ref is not None
        requests = [
            StateTransitionRequest(
                contract_version="1.0", object_id="object.cas", scope_ref="scope.validate",
                expected_revision=0, expected_state_digest=created.state_ref.state_digest,
                expected_schema_ref=SCHEMA_REF, expected_schema_digest=SCHEMA_DIGEST,
                payload={"value": n}, transition_label=f"cas_{n}", operation_id=f"op.cas.{n}",
            )
            for n in (2, 3)
        ]
        cas = await asyncio.gather(
            service.transition(caller("agent-a"), requests[0]),
            service.transition(caller("agent-b"), requests[1]),
        )
        statuses = sorted(x.status for x in cas)
        assert statuses == ["committed", "conflict"], f"VALIDATE-FAIL: CAS statuses {statuses}"
        print("PASS MONGO-02 concurrent CAS")

        # MONGO-03: competing claim acquisition, exactly one winner.
        created_claim = await service.create(caller("agent-a"), create_req("object.claim", "op.claim.create"))
        assert created_claim.status == "committed"
        claim_reqs = [
            StateClaimRequest(
                contract_version="1.0", object_id="object.claim", scope_ref="scope.validate",
                expected_revision=0, operation_id=f"op.claim.{who}", ttl_seconds=30,
            )
            for who in ("a", "b")
        ]
        claims = await asyncio.gather(
            service.claim(caller("agent-a"), claim_reqs[0]),
            service.claim(caller("agent-b"), claim_reqs[1]),
        )
        claim_statuses = sorted(x.status for x in claims)
        assert claim_statuses == ["claimed", "conflict"], f"VALIDATE-FAIL: claim statuses {claim_statuses}"
        winner = next(x for x in claims if x.status == "claimed")
        assert winner.fencing_token == 1
        print("PASS MONGO-03 competing claims")

        # MONGO-04: server-authoritative claim time is close to server localTime.
        hello_after = await client.admin.command("hello")
        server_time = hello_after.get("localTime")
        assert isinstance(server_time, datetime) and winner.issued_at.tzinfo is not None
        if server_time.tzinfo is None:
            server_time = server_time.replace(tzinfo=UTC)
        delta = abs((winner.issued_at - server_time).total_seconds())
        assert delta < 10, f"VALIDATE-FAIL: claim issued_at not server-time aligned delta={delta}s"
        print("PASS MONGO-04 server-time lease authority")

        # MONGO-05/06: exact active fence permits retention executor hard erase; replay is immutable.
        created_erase = await service.create(caller("agent-a"), create_req("object.erase", "op.erase.create"))
        assert created_erase.status == "committed" and created_erase.state_ref is not None
        claim = await service.claim(
            caller("agent-a"),
            StateClaimRequest(
                contract_version="1.0", object_id="object.erase", scope_ref="scope.validate",
                expected_revision=0, operation_id="op.erase.claim", ttl_seconds=300,
            ),
        )
        assert claim.status == "claimed" and claim.claim_id and claim.fencing_token
        tomb = await service.tombstone(
            caller("agent-a"),
            StateTombstoneRequest(
                contract_version="1.0", object_id="object.erase", scope_ref="scope.validate",
                expected_revision=0, expected_state_digest=created_erase.state_ref.state_digest,
                operation_id="op.erase.tomb", reason_code="retired",
                claim_id=claim.claim_id, fencing_token=claim.fencing_token,
            ),
        )
        assert tomb.status == "committed"
        current = await store.get_revision("tenant-validate", "scope.validate", "object.erase")
        assert current is not None
        plan = prepare_hard_erase_plan(
            current=current,
            operation_id="op.erase.hard",
            principal_ref="retention-executor",
            authorization_ref="retention-decision:live-validation",
            budget=ExecutionBudget.start(30_000),
            claim_id=claim.claim_id,
            fencing_token=claim.fencing_token,
        )
        erased = await store.hard_erase(
            revision=plan.revision,
            expected_revision=plan.expected_revision,
            expected_state_digest=plan.expected_state_digest,
            expected_retention_policy_ref=plan.expected_retention_policy_ref,
            expected_retention_policy_digest=plan.expected_retention_policy_digest,
            claim_id=plan.claim_id,
            fencing_token=plan.fencing_token,
            operation=plan.operation,
            event=plan.event,
            budget=plan.budget,
        )
        assert erased.status == "committed"
        assert erased.principal_ref == "retention-executor"
        assert erased.authorization_ref == "retention-decision:live-validation"
        replay = await store.hard_erase(
            revision=plan.revision,
            expected_revision=plan.expected_revision,
            expected_state_digest=plan.expected_state_digest,
            expected_retention_policy_ref=plan.expected_retention_policy_ref,
            expected_retention_policy_digest=plan.expected_retention_policy_digest,
            claim_id=plan.claim_id,
            fencing_token=plan.fencing_token,
            operation=plan.operation,
            event=plan.event,
            budget=ExecutionBudget.start(30_000),
        )
        assert replay == erased
        lineage = await store.get_claim("tenant-validate", "scope.validate", "object.erase")
        assert lineage is not None and lineage.active is False and lineage.highest_fence == claim.fencing_token
        for rev in (0, 1, 2):
            historical = await store.get_revision("tenant-validate", "scope.validate", "object.erase", rev)
            assert historical is not None and historical.payload is None
        print("PASS MONGO-05 hard erase fencing")
        print("PASS MONGO-06 hard erase replay/scrub")

        # MONGO-07: inactive lineage permits claimless erase and keeps highest fence.
        created_release = await service.create(caller("agent-a"), create_req("object.release", "op.release.create"))
        assert created_release.status == "committed" and created_release.state_ref is not None
        release_claim = await service.claim(
            caller("agent-a"),
            StateClaimRequest(
                contract_version="1.0", object_id="object.release", scope_ref="scope.validate",
                expected_revision=0, operation_id="op.release.claim", ttl_seconds=300,
            ),
        )
        assert release_claim.status == "claimed" and release_claim.claim_id and release_claim.fencing_token
        release_tomb = await service.tombstone(
            caller("agent-a"),
            StateTombstoneRequest(
                contract_version="1.0", object_id="object.release", scope_ref="scope.validate",
                expected_revision=0, expected_state_digest=created_release.state_ref.state_digest,
                operation_id="op.release.tomb", reason_code="retired",
                claim_id=release_claim.claim_id, fencing_token=release_claim.fencing_token,
            ),
        )
        assert release_tomb.status == "committed"
        released = await service.release(
            caller("agent-a"),
            StateReleaseRequest(
                contract_version="1.0", claim_id=release_claim.claim_id,
                object_id="object.release", scope_ref="scope.validate",
                fencing_token=release_claim.fencing_token, operation_id="op.release.release",
            ),
        )
        assert released.status == "released"
        current = await store.get_revision("tenant-validate", "scope.validate", "object.release")
        assert current is not None
        claimless = prepare_hard_erase_plan(
            current=current, operation_id="op.release.erase", principal_ref="retention-executor",
            authorization_ref="retention-decision:claimless", budget=ExecutionBudget.start(30_000),
        )
        erased2 = await store.hard_erase(
            revision=claimless.revision,
            expected_revision=claimless.expected_revision,
            expected_state_digest=claimless.expected_state_digest,
            expected_retention_policy_ref=claimless.expected_retention_policy_ref,
            expected_retention_policy_digest=claimless.expected_retention_policy_digest,
            claim_id=None, fencing_token=None, operation=claimless.operation,
            event=claimless.event, budget=claimless.budget,
        )
        assert erased2.status == "committed"
        lineage2 = await store.get_claim("tenant-validate", "scope.validate", "object.release")
        assert lineage2 is not None and lineage2.highest_fence == release_claim.fencing_token and not lineage2.active
        print("PASS MONGO-07 claimless-after-release")

        print("PASS LIVE-MONGO CORE MATRIX")
    finally:
        try:
            await client.drop_database(database)
        finally:
            await store.close()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--uri", required=True)
    parser.add_argument("--database", default=f"l9_state_validate_{uuid4().hex[:8]}")
    args = parser.parse_args()
    asyncio.run(run(args.uri, args.database))


if __name__ == "__main__":
    main()
