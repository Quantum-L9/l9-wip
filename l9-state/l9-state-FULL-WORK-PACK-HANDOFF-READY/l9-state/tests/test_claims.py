from __future__ import annotations

import asyncio
from datetime import UTC, datetime, timedelta

import pytest

from l9_state.adapters.memory import InProcessStateStore
from l9_state.catalog import ConfiguredContractCatalog
from l9_state.cursor import CursorCodec
from l9_state.execution import ExecutionBudget
from l9_state.models import (
    StateClaimReceipt,
    StateClaimRequest,
    StateCreateRequest,
    StateOperationInspectRequest,
    StateReleaseRequest,
    StateRenewRequest,
    StateTransitionRequest,
)
from l9_state.ports import CLAIM_RECEIPT_SCHEMA_REF
from l9_state.service import CallerContext, StateService

SCHEMA = "a" * 64
RET = "b" * 64


class Clock:
    def __init__(self) -> None:
        self.value = datetime(2026, 9, 27, 20, 0, tzinfo=UTC)

    def now(self) -> datetime:
        return self.value

    def advance(self, seconds: int) -> None:
        self.value += timedelta(seconds=seconds)


def caller(name: str = "agent-a") -> CallerContext:
    return CallerContext(
        "tenant-a",
        name,
        f"state.authz.tenant-base:{name}",
        ExecutionBudget.start(30_000),
        f"packet:{name}",
    )


def create_req(object_id: str = "object.1", operation_id: str = "op.create.1") -> StateCreateRequest:
    return StateCreateRequest(contract_version="1.0", 
        object_id=object_id,
        scope_ref="scope.1",
        schema_ref="urn:test:v1",
        schema_digest=SCHEMA,
        payload={"value": 1},
        operation_id=operation_id,
        retention_policy_ref="retention.test",
        retention_policy_digest=RET,
    )


@pytest.fixture
def harness():
    clock = Clock()
    store = InProcessStateStore(now=clock.now)
    catalog = ConfiguredContractCatalog()
    catalog.admit_schema("urn:test:v1", SCHEMA, lambda p: isinstance(p.get("value"), int))
    catalog.admit_retention("retention.test", RET)
    return clock, store, StateService(store, catalog, cursor_codec=CursorCodec(b"x" * 32))


@pytest.mark.asyncio
async def test_claim_exact_retry_release_and_reacquire_monotonic_fence(harness):
    _clock, _store, service = harness
    await service.create(caller(), create_req())
    request = StateClaimRequest(contract_version="1.0", 
        object_id="object.1",
        scope_ref="scope.1",
        expected_revision=0,
        operation_id="op.claim.1",
        ttl_seconds=30,
    )
    first = await service.claim(caller(), request)
    retry = await service.claim(caller(), request)
    assert isinstance(first, StateClaimReceipt)
    assert retry == first
    assert first.fencing_token == 1

    released = await service.release(
        caller(),
        StateReleaseRequest(contract_version="1.0", 
            claim_id=first.claim_id,
            object_id="object.1",
            scope_ref="scope.1",
            fencing_token=first.fencing_token,
            operation_id="op.release.1",
        ),
    )
    assert isinstance(released, StateClaimReceipt)
    assert released.status == "released"

    second = await service.claim(
        caller(),
        request.model_copy(update={"operation_id": "op.claim.2"}),
    )
    assert isinstance(second, StateClaimReceipt)
    assert second.fencing_token == 2
    assert second.claim_id != first.claim_id


@pytest.mark.asyncio
async def test_active_claim_blocks_claimless_transition_and_exact_claim_allows(harness):
    _clock, _store, service = harness
    created = await service.create(caller(), create_req())
    assert created.state_ref is not None
    claim = await service.claim(
        caller(),
        StateClaimRequest(contract_version="1.0", 
            object_id="object.1",
            scope_ref="scope.1",
            expected_revision=0,
            operation_id="op.claim.1",
            ttl_seconds=60,
        ),
    )
    assert isinstance(claim, StateClaimReceipt)
    base = StateTransitionRequest(contract_version="1.0", 
        object_id="object.1",
        scope_ref="scope.1",
        expected_revision=0,
        expected_state_digest=created.state_ref.state_digest,
        expected_schema_ref="urn:test:v1",
        expected_schema_digest=SCHEMA,
        payload={"value": 2},
        transition_label="advance",
        operation_id="op.transition.1",
    )
    blocked = await service.transition(caller(), base)
    assert blocked.status == "conflict"
    assert blocked.reason_codes == ("CLAIM_REQUIRED",)

    result = await service.transition(
        caller(),
        base.model_copy(
            update={
                "operation_id": "op.transition.2",
                "claim_id": claim.claim_id,
                "fencing_token": claim.fencing_token,
            }
        ),
    )
    assert result.state_ref is not None
    assert result.state_ref.revision == 1


@pytest.mark.asyncio
async def test_renew_preserves_fence_and_holder_is_transport_derived(harness):
    _clock, _store, service = harness
    await service.create(caller(), create_req())
    claim = await service.claim(
        caller(),
        StateClaimRequest(contract_version="1.0", 
            object_id="object.1",
            scope_ref="scope.1",
            expected_revision=0,
            operation_id="op.claim.1",
            ttl_seconds=10,
        ),
    )
    assert isinstance(claim, StateClaimReceipt)
    renewed = await service.renew(
        caller(),
        StateRenewRequest(contract_version="1.0", 
            claim_id=claim.claim_id,
            object_id="object.1",
            scope_ref="scope.1",
            fencing_token=claim.fencing_token,
            operation_id="op.renew.1",
            ttl_seconds=50,
        ),
    )
    assert isinstance(renewed, StateClaimReceipt)
    assert renewed.fencing_token == claim.fencing_token
    assert renewed.expires_at > claim.expires_at

    wrong_holder = await service.renew(
        caller("agent-b"),
        StateRenewRequest(contract_version="1.0", 
            claim_id=claim.claim_id,
            object_id="object.1",
            scope_ref="scope.1",
            fencing_token=claim.fencing_token,
            operation_id="op.renew.bad",
            ttl_seconds=50,
        ),
    )
    assert wrong_holder.status == "refused"
    assert wrong_holder.reason_codes == ("CLAIM_HOLDER_MISMATCH",)


@pytest.mark.asyncio
async def test_expired_holder_cannot_write_after_reassignment(harness):
    clock, _store, service = harness
    created = await service.create(caller(), create_req())
    assert created.state_ref is not None
    old = await service.claim(
        caller("agent-a"),
        StateClaimRequest(contract_version="1.0", 
            object_id="object.1",
            scope_ref="scope.1",
            expected_revision=0,
            operation_id="op.claim.old",
            ttl_seconds=5,
        ),
    )
    assert isinstance(old, StateClaimReceipt)
    clock.advance(6)
    new = await service.claim(
        caller("agent-b"),
        StateClaimRequest(contract_version="1.0", 
            object_id="object.1",
            scope_ref="scope.1",
            expected_revision=0,
            operation_id="op.claim.new",
            ttl_seconds=30,
        ),
    )
    assert isinstance(new, StateClaimReceipt)
    assert new.fencing_token == old.fencing_token + 1

    stale_write = StateTransitionRequest(contract_version="1.0", 
        object_id="object.1",
        scope_ref="scope.1",
        expected_revision=0,
        expected_state_digest=created.state_ref.state_digest,
        expected_schema_ref="urn:test:v1",
        expected_schema_digest=SCHEMA,
        payload={"value": 2},
        transition_label="advance",
        operation_id="op.transition.stale",
        claim_id=old.claim_id,
        fencing_token=old.fencing_token,
    )
    stale = await service.transition(caller("agent-a"), stale_write)
    assert stale.status == "conflict"
    assert stale.reason_codes == ("CLAIM_STALE_FENCE",)


@pytest.mark.asyncio
async def test_simultaneous_acquire_yields_one_holder(harness):
    _clock, _store, service = harness
    await service.create(caller(), create_req())

    async def acquire(name: str, op: str):
        return await service.claim(
            caller(name),
            StateClaimRequest(contract_version="1.0", 
                object_id="object.1",
                scope_ref="scope.1",
                expected_revision=0,
                operation_id=op,
                ttl_seconds=60,
            ),
        )

    results = await asyncio.gather(
        acquire("agent-a", "op.claim.a"), acquire("agent-b", "op.claim.b")
    )
    claimed = [r for r in results if r.status == "claimed"]
    conflicts = [r for r in results if r.status == "conflict"]
    assert len(claimed) == 1
    assert len(conflicts) == 1
    assert conflicts[0].reason_codes == ("CLAIM_ACTIVE",)


@pytest.mark.asyncio
async def test_claim_operation_inspection_uses_claim_receipt_schema(harness):
    _clock, _store, service = harness
    await service.create(caller(), create_req())
    claim = await service.claim(
        caller(),
        StateClaimRequest(contract_version="1.0", 
            object_id="object.1",
            scope_ref="scope.1",
            expected_revision=0,
            operation_id="op.claim.inspect",
            ttl_seconds=30,
        ),
    )
    assert isinstance(claim, StateClaimReceipt)
    inspected = await service.inspect_operation(
        caller(), StateOperationInspectRequest(contract_version="1.0", scope_ref="scope.1", operation_id="op.claim.inspect")
    )
    assert inspected.status == "found"
    assert inspected.receipt_schema_ref == CLAIM_RECEIPT_SCHEMA_REF
    assert inspected.receipt["claim_id"] == claim.claim_id


@pytest.mark.asyncio
async def test_scope_journal_sequence_is_scope_global_not_revision_derived(harness):
    _clock, store, service = harness
    await service.create(caller(), create_req("object.1", "op.create.1"))
    await service.create(caller(), create_req("object.2", "op.create.2"))
    events = store._events[("tenant-a", "scope.1")]
    assert [e.journal_seq for e in events] == [1, 2]


@pytest.mark.asyncio
async def test_claim_conflict_is_sticky_and_changed_world_retry_requires_new_operation(harness):
    _clock, _store, service = harness
    await service.create(caller(), create_req())
    first = await service.claim(
        caller("agent-a"),
        StateClaimRequest(
            contract_version="1.0",
            object_id="object.1",
            scope_ref="scope.1",
            expected_revision=0,
            operation_id="op.claim.owner",
            ttl_seconds=60,
        ),
    )
    blocked_request = StateClaimRequest(
        contract_version="1.0",
        object_id="object.1",
        scope_ref="scope.1",
        expected_revision=0,
        operation_id="op.claim.blocked",
        ttl_seconds=60,
    )
    blocked = await service.claim(caller("agent-b"), blocked_request)
    assert blocked.status == "conflict"
    assert blocked.reason_codes == ("CLAIM_ACTIVE",)

    await service.release(
        caller("agent-a"),
        StateReleaseRequest(
            contract_version="1.0",
            claim_id=first.claim_id,
            object_id="object.1",
            scope_ref="scope.1",
            fencing_token=first.fencing_token,
            operation_id="op.release.owner",
        ),
    )

    assert await service.claim(caller("agent-b"), blocked_request) == blocked
    fresh = await service.claim(
        caller("agent-b"), blocked_request.model_copy(update={"operation_id": "op.claim.fresh"})
    )
    assert fresh.status == "claimed"
