from __future__ import annotations

import pytest

from l9_state.adapters.memory import InProcessStateStore
from l9_state.catalog import ConfiguredContractCatalog
from l9_state.cursor import CursorCodec
from l9_state.execution import ExecutionBudget
from l9_state.models import (
    StateClaimRequest,
    StateCreateRequest,
    StateEventReadRequest,
    StateOperationInspectRequest,
    StateProblem,
    StateReadRequest,
    StateReleaseRequest,
    StateRestoreRequest,
    StateTombstoneRequest,
    StateTransitionRequest,
)
from l9_state.retention import prepare_hard_erase_plan
from l9_state.service import CallerContext, StateService

SCHEMA = "a" * 64
RET = "b" * 64


def caller(name: str = "agent-a") -> CallerContext:
    return CallerContext(
        "tenant-a",
        name,
        f"state.authz.tenant-base:{name}",
        ExecutionBudget.start(30_000),
        f"packet:{name}",
    )


@pytest.fixture
def harness():
    store = InProcessStateStore()
    catalog = ConfiguredContractCatalog()
    catalog.admit_schema("urn:test:v1", SCHEMA, lambda p: isinstance(p.get("value"), int))
    catalog.admit_retention("retention.test", RET)
    service = StateService(store, catalog, cursor_codec=CursorCodec(b"l" * 32))
    return store, service


def create_req(op: str = "op.create.1") -> StateCreateRequest:
    return StateCreateRequest(
        contract_version="1.0",
        object_id="object.1",
        scope_ref="scope.1",
        schema_ref="urn:test:v1",
        schema_digest=SCHEMA,
        payload={"value": 1},
        operation_id=op,
        retention_policy_ref="retention.test",
        retention_policy_digest=RET,
    )


@pytest.mark.asyncio
async def test_tombstone_blocks_current_read_and_restore_creates_new_active_revision(harness):
    _store, service = harness
    created = await service.create(caller(), create_req())
    assert created.status == "committed"
    assert created.state_ref is not None

    tombstone_request = StateTombstoneRequest(
        contract_version="1.0",
        object_id="object.1",
        scope_ref="scope.1",
        expected_revision=0,
        expected_state_digest=created.state_ref.state_digest,
        operation_id="op.tombstone.1",
        reason_code="retired",
    )
    tombstoned = await service.tombstone(caller(), tombstone_request)
    assert tombstoned.status == "committed"
    assert tombstoned.state_ref is not None
    assert tombstoned.state_ref.revision == 1
    assert tombstoned.state_ref.lifecycle == "tombstoned"
    assert await service.tombstone(caller(), tombstone_request) == tombstoned

    current_read = await service.get(
        caller(), StateReadRequest(contract_version="1.0", object_id="object.1", scope_ref="scope.1")
    )
    assert isinstance(current_read, StateProblem)
    assert current_read.code == "OBJECT_NOT_FOUND"

    original = await service.get(
        caller(),
        StateReadRequest(
            contract_version="1.0", object_id="object.1", scope_ref="scope.1", revision=0
        ),
    )
    assert original.payload_status == "present"
    assert original.payload == {"value": 1}

    tombstone_revision = await service.get(
        caller(),
        StateReadRequest(
            contract_version="1.0", object_id="object.1", scope_ref="scope.1", revision=1
        ),
    )
    assert tombstone_revision.payload_status == "present"
    assert tombstone_revision.payload == {"value": 1}

    transition = await service.transition(
        caller(),
        StateTransitionRequest(
            contract_version="1.0",
            object_id="object.1",
            scope_ref="scope.1",
            expected_revision=1,
            expected_state_digest=tombstoned.state_ref.state_digest,
            expected_schema_ref="urn:test:v1",
            expected_schema_digest=SCHEMA,
            payload={"value": 2},
            transition_label="illegal_after_tombstone",
            operation_id="op.transition.after.tombstone",
        ),
    )
    assert transition.status == "refused"
    assert transition.reason_codes == ("OBJECT_TOMBSTONED",)

    restored = await service.restore(
        caller(),
        StateRestoreRequest(
            contract_version="1.0",
            object_id="object.1",
            scope_ref="scope.1",
            expected_revision=1,
            expected_state_digest=tombstoned.state_ref.state_digest,
            source_revision=0,
            operation_id="op.restore.1",
            transition_label="restore_retained",
        ),
    )
    assert restored.status == "committed"
    assert restored.state_ref is not None
    assert restored.state_ref.revision == 2
    assert restored.state_ref.lifecycle == "active"

    current = await service.get(
        caller(), StateReadRequest(contract_version="1.0", object_id="object.1", scope_ref="scope.1")
    )
    assert current.payload_status == "present"
    assert current.payload == {"value": 1}

    events = await service.events(
        caller(),
        StateEventReadRequest(
            contract_version="1.0", scope_ref="scope.1", consumer_ref="agent-a", limit=20
        ),
    )
    assert [event.event_kind for event in events.events] == ["created", "tombstoned", "restored"]


@pytest.mark.asyncio
async def test_restore_requires_retained_prior_revision(harness):
    _store, service = harness
    created = await service.create(caller(), create_req())
    tombstoned = await service.tombstone(
        caller(),
        StateTombstoneRequest(
            contract_version="1.0",
            object_id="object.1",
            scope_ref="scope.1",
            expected_revision=0,
            expected_state_digest=created.state_ref.state_digest,
            operation_id="op.tombstone.1",
            reason_code="retired",
        ),
    )
    result = await service.restore(
        caller(),
        StateRestoreRequest(
            contract_version="1.0",
            object_id="object.1",
            scope_ref="scope.1",
            expected_revision=1,
            expected_state_digest=tombstoned.state_ref.state_digest,
            source_revision=1,
            operation_id="op.restore.bad-source",
            transition_label="restore_same_revision",
        ),
    )
    assert result.status == "refused"
    assert result.reason_codes == ("RESTORE_SOURCE_UNAVAILABLE",)


@pytest.mark.asyncio
async def test_hard_erase_scrubs_payload_preserves_fence_and_makes_identity_terminal(harness):
    store, service = harness
    created = await service.create(caller(), create_req())
    claimed = await service.claim(
        caller(),
        StateClaimRequest(
            contract_version="1.0",
            object_id="object.1",
            scope_ref="scope.1",
            expected_revision=0,
            operation_id="op.claim.1",
            ttl_seconds=300,
        ),
    )
    assert claimed.status == "claimed"

    tombstoned = await service.tombstone(
        caller(),
        StateTombstoneRequest(
            contract_version="1.0",
            object_id="object.1",
            scope_ref="scope.1",
            expected_revision=0,
            expected_state_digest=created.state_ref.state_digest,
            operation_id="op.tombstone.1",
            reason_code="retired",
            claim_id=claimed.claim_id,
            fencing_token=claimed.fencing_token,
        ),
    )
    assert tombstoned.status == "committed"

    current = await store.get_revision("tenant-a", "scope.1", "object.1")
    assert current is not None
    plan = prepare_hard_erase_plan(
        current=current,
        operation_id="op.erase.1",
        principal_ref="retention-executor",
        authorization_ref="retention-decision:42",
        budget=ExecutionBudget.start(30_000),
        claim_id=claimed.claim_id,
        fencing_token=claimed.fencing_token,
        causation_ref="decision:42",
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
    assert erased.state_ref is not None
    assert erased.state_ref.lifecycle == "erased"
    assert erased.state_ref.revision == 2
    assert erased.principal_ref == "retention-executor"
    assert erased.authorization_ref == "retention-decision:42"

    replayed = await store.hard_erase(
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
    assert replayed == erased

    lineage = await store.get_claim("tenant-a", "scope.1", "object.1")
    assert lineage is not None
    assert lineage.highest_fence == claimed.fencing_token
    assert lineage.active is False

    for revision in (0, 1, 2):
        historical = await service.get(
            caller(),
            StateReadRequest(
                contract_version="1.0",
                object_id="object.1",
                scope_ref="scope.1",
                revision=revision,
            ),
        )
        assert historical.payload_status == "erased"
        assert historical.payload is None

    current_result = await service.get(
        caller(), StateReadRequest(contract_version="1.0", object_id="object.1", scope_ref="scope.1")
    )
    assert current_result.state_ref.lifecycle == "erased"
    assert current_result.payload_status == "erased"

    restore = await service.restore(
        caller(),
        StateRestoreRequest(
            contract_version="1.0",
            object_id="object.1",
            scope_ref="scope.1",
            expected_revision=2,
            expected_state_digest=erased.state_ref.state_digest,
            source_revision=0,
            operation_id="op.restore.after.erase",
            transition_label="forbidden",
        ),
    )
    assert restore.status == "refused"
    assert restore.reason_codes == ("OBJECT_ERASED",)

    recreated = await service.create(caller(), create_req("op.create.reuse"))
    assert recreated.status == "refused"
    assert recreated.reason_codes == ("OBJECT_ID_REUSE_FORBIDDEN",)

    inspected = await service.inspect_operation(
        caller(),
        StateOperationInspectRequest(
            contract_version="1.0", scope_ref="scope.1", operation_id="op.erase.1"
        ),
    )
    assert inspected.status == "found"
    assert inspected.receipt_schema_ref == "urn:l9:state:internal:HardEraseReceipt:1.0"
    assert inspected.receipt["action"] == "state.internal.hard_erase"


async def _claimed_tombstone(harness):
    store, service = harness
    created = await service.create(caller(), create_req())
    claimed = await service.claim(
        caller(),
        StateClaimRequest(
            contract_version="1.0",
            object_id="object.1",
            scope_ref="scope.1",
            expected_revision=0,
            operation_id="op.claim.guard",
            ttl_seconds=300,
        ),
    )
    tombstoned = await service.tombstone(
        caller(),
        StateTombstoneRequest(
            contract_version="1.0",
            object_id="object.1",
            scope_ref="scope.1",
            expected_revision=0,
            expected_state_digest=created.state_ref.state_digest,
            operation_id="op.tombstone.guard",
            reason_code="retired",
            claim_id=claimed.claim_id,
            fencing_token=claimed.fencing_token,
        ),
    )
    assert tombstoned.status == "committed"
    current = await store.get_revision("tenant-a", "scope.1", "object.1")
    assert current is not None
    return store, service, claimed, current


@pytest.mark.asyncio
async def test_hard_erase_rejects_stale_fence_without_requiring_holder_identity(harness):
    store, _service, claimed, current = await _claimed_tombstone(harness)
    plan = prepare_hard_erase_plan(
        current=current,
        operation_id="op.erase.stale",
        principal_ref="retention-executor",
        authorization_ref="retention-decision:stale",
        budget=ExecutionBudget.start(30_000),
        claim_id=claimed.claim_id,
        fencing_token=claimed.fencing_token + 1,
    )
    result = await store.hard_erase(
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
    assert result.status == "conflict"
    assert result.reason_codes == ("CLAIM_STALE_FENCE",)
    current_after = await store.get_revision("tenant-a", "scope.1", "object.1")
    assert current_after is not None
    assert current_after.state_ref.lifecycle == "tombstoned"


@pytest.mark.asyncio
async def test_hard_erase_requires_fence_when_claim_is_active(harness):
    store, _service, _claimed, current = await _claimed_tombstone(harness)
    plan = prepare_hard_erase_plan(
        current=current,
        operation_id="op.erase.claimless-active",
        principal_ref="retention-executor",
        authorization_ref="retention-decision:claimless-active",
        budget=ExecutionBudget.start(30_000),
    )
    result = await store.hard_erase(
        revision=plan.revision,
        expected_revision=plan.expected_revision,
        expected_state_digest=plan.expected_state_digest,
        expected_retention_policy_ref=plan.expected_retention_policy_ref,
        expected_retention_policy_digest=plan.expected_retention_policy_digest,
        claim_id=None,
        fencing_token=None,
        operation=plan.operation,
        event=plan.event,
        budget=plan.budget,
    )
    assert result.status == "conflict"
    assert result.reason_codes == ("CLAIM_REQUIRED",)


@pytest.mark.asyncio
async def test_hard_erase_allows_claimless_after_release_and_preserves_fence(harness):
    store, service, claimed, current = await _claimed_tombstone(harness)
    released = await service.release(
        caller(),
        StateReleaseRequest(
            contract_version="1.0",
            claim_id=claimed.claim_id,
            object_id="object.1",
            scope_ref="scope.1",
            fencing_token=claimed.fencing_token,
            operation_id="op.release.before.erase",
        ),
    )
    assert released.status == "released"
    current = await store.get_revision("tenant-a", "scope.1", "object.1")
    assert current is not None
    plan = prepare_hard_erase_plan(
        current=current,
        operation_id="op.erase.after-release",
        principal_ref="retention-executor",
        authorization_ref="retention-decision:after-release",
        budget=ExecutionBudget.start(30_000),
    )
    erased = await store.hard_erase(
        revision=plan.revision,
        expected_revision=plan.expected_revision,
        expected_state_digest=plan.expected_state_digest,
        expected_retention_policy_ref=plan.expected_retention_policy_ref,
        expected_retention_policy_digest=plan.expected_retention_policy_digest,
        claim_id=None,
        fencing_token=None,
        operation=plan.operation,
        event=plan.event,
        budget=plan.budget,
    )
    assert erased.status == "committed"
    lineage = await store.get_claim("tenant-a", "scope.1", "object.1")
    assert lineage is not None
    assert lineage.highest_fence == claimed.fencing_token
    assert lineage.active is False
