from __future__ import annotations

import pytest

from l9_state.adapters.memory import InProcessStateStore
from l9_state.catalog import ConfiguredContractCatalog
from l9_state.cursor import CursorClaims, CursorCodec
from l9_state.execution import ExecutionBudget
from l9_state.models import (
    StateAckRequest,
    StateCreateRequest,
    StateEventReadRequest,
    StateHistoryRequest,
    StateListRequest,
    StateOperationInspectRequest,
    StateProblem,
    StateReadRequest,
    StateTransitionRequest,
)
from l9_state.ports import ScopeAuthorizationDecision
from l9_state.service import CallerContext, StateService

SCHEMA = "a" * 64
RET = "b" * 64


class DelegatedConsumerAuthorization:
    async def authorize(self, request):
        if request.consumer_ref is None or request.consumer_ref == request.principal_ref:
            return ScopeAuthorizationDecision(
                allowed=True, authorization_ref=f"policy.scope:{request.action}:{request.scope_ref}"
            )
        if request.consumer_ref == "consumer-delegated":
            return ScopeAuthorizationDecision(
                allowed=True,
                authorization_ref=f"policy.consumer:{request.consumer_ref}:{request.action}",
            )
        return ScopeAuthorizationDecision(
            allowed=False, authorization_ref="policy.denied", reason_code="SCOPE_FORBIDDEN"
        )


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
    codec = CursorCodec(b"j" * 32)
    return store, codec, StateService(store, catalog, cursor_codec=codec)


def create_req(object_id: str, op: str, value: int = 1) -> StateCreateRequest:
    return StateCreateRequest(
        contract_version="1.0",
        object_id=object_id,
        scope_ref="scope.1",
        schema_ref="urn:test:v1",
        schema_digest=SCHEMA,
        payload={"value": value},
        operation_id=op,
        retention_policy_ref="retention.test",
        retention_policy_digest=RET,
    )


async def transition(service: StateService, object_id: str, op: str, value: int):
    current = await service.get(
        caller(),
        StateReadRequest(
            contract_version="1.0", object_id=object_id, scope_ref="scope.1"
        ),
    )
    return await service.transition(
        caller(),
        StateTransitionRequest(
            contract_version="1.0",
            object_id=object_id,
            scope_ref="scope.1",
            expected_revision=current.state_ref.revision,
            expected_state_digest=current.state_ref.state_digest,
            expected_schema_ref=current.state_ref.schema_ref,
            expected_schema_digest=current.state_ref.schema_digest,
            payload={"value": value},
            transition_label="advance",
            operation_id=op,
        ),
    )


@pytest.mark.asyncio
async def test_cold_resume_list_then_events_catches_mid_enumeration_mutation(harness):
    _store, _codec, service = harness
    await service.create(caller(), create_req("object.1", "op.create.1"))
    await service.create(caller(), create_req("object.2", "op.create.2"))

    first = await service.list_states(
        caller(),
        StateListRequest(
            contract_version="1.0",
            scope_ref="scope.1",
            consumer_ref="agent-a",
            schema_refs=("urn:test:v1",),
            lifecycle="active",
            limit=1,
        ),
    )
    assert first.coverage == "bounded"
    assert len(first.states) == 1
    assert first.next_cursor is not None

    changed = await transition(service, "object.1", "op.transition.1", 2)
    assert changed.status == "committed"

    second = await service.list_states(
        caller(),
        StateListRequest(
            contract_version="1.0",
            scope_ref="scope.1",
            consumer_ref="agent-a",
            schema_refs=("urn:test:v1",),
            lifecycle="active",
            cursor=first.next_cursor,
            limit=1,
        ),
    )
    assert second.coverage == "complete"
    assert second.resume_event_cursor == first.resume_event_cursor

    catchup = await service.events(
        caller(),
        StateEventReadRequest(
            contract_version="1.0",
            scope_ref="scope.1",
            consumer_ref="agent-a",
            cursor=first.resume_event_cursor,
            limit=200,
        ),
    )
    assert [event.operation_id for event in catchup.events] == ["op.transition.1"]
    assert catchup.coverage == "complete"
    assert catchup.next_cursor is not None


@pytest.mark.asyncio
async def test_event_cursor_is_consumer_bound_and_successful_empty_page_is_ackable(harness):
    _store, codec, service = harness
    await service.create(caller(), create_req("object.1", "op.create.1"))
    page = await service.events(
        caller(),
        StateEventReadRequest(
            contract_version="1.0",
            scope_ref="scope.1",
            consumer_ref="agent-a",
            limit=200,
        ),
    )
    assert page.next_cursor is not None

    foreign = codec.issue(
        CursorClaims(
            purpose="events",
            scope_binding=codec.scope_binding("tenant-a", "scope.1"),
            consumer_binding=codec.consumer_binding("agent-b"),
            position=page.high_water_seq,
        )
    )
    refused = await service.events(
        caller(),
        StateEventReadRequest(
            contract_version="1.0",
            scope_ref="scope.1",
            consumer_ref="agent-a",
            cursor=foreign,
            limit=10,
        ),
    )
    assert isinstance(refused, StateProblem)
    assert refused.code == "CURSOR_CONSUMER_MISMATCH"

    ack = await service.acknowledge(
        caller(),
        StateAckRequest(
            contract_version="1.0",
            scope_ref="scope.1",
            consumer_ref="agent-a",
            cursor=page.next_cursor,
            operation_id="op.ack.1",
        ),
    )
    assert ack.status == "committed"

    empty = await service.events(
        caller(),
        StateEventReadRequest(
            contract_version="1.0",
            scope_ref="scope.1",
            consumer_ref="agent-a",
            limit=10,
        ),
    )
    assert empty.events == ()
    assert empty.coverage == "complete"
    assert empty.next_cursor is not None


@pytest.mark.asyncio
async def test_ack_is_exact_retry_monotonic_and_regression_is_non_durable_problem(harness):
    _store, _codec, service = harness
    await service.create(caller(), create_req("object.1", "op.create.1"))
    first_page = await service.events(
        caller(),
        StateEventReadRequest(
            contract_version="1.0",
            scope_ref="scope.1",
            consumer_ref="agent-a",
            limit=1,
        ),
    )
    ack_req = StateAckRequest(
        contract_version="1.0",
        scope_ref="scope.1",
        consumer_ref="agent-a",
        cursor=first_page.next_cursor,
        operation_id="op.ack.1",
    )
    first_ack = await service.acknowledge(caller(), ack_req)
    assert await service.acknowledge(caller(), ack_req) == first_ack

    await transition(service, "object.1", "op.transition.1", 2)
    newer = await service.events(
        caller(),
        StateEventReadRequest(
            contract_version="1.0",
            scope_ref="scope.1",
            consumer_ref="agent-a",
            limit=10,
        ),
    )
    newer_ack = await service.acknowledge(
        caller(),
        ack_req.model_copy(update={"cursor": newer.next_cursor, "operation_id": "op.ack.2"}),
    )
    assert newer_ack.status == "committed"

    regression = await service.acknowledge(
        caller(),
        ack_req.model_copy(update={"operation_id": "op.ack.regression"}),
    )
    assert isinstance(regression, StateProblem)
    assert regression.code == "ACK_REGRESSION"
    inspected = await service.inspect_operation(
        caller(),
        StateOperationInspectRequest(
            contract_version="1.0",
            scope_ref="scope.1",
            operation_id="op.ack.regression",
        ),
    )
    assert inspected.status == "not_found"


@pytest.mark.asyncio
async def test_retention_beyond_event_cursor_requires_cold_resync(harness):
    store, _codec, service = harness
    await service.create(caller(), create_req("object.1", "op.create.1"))
    first = await service.events(
        caller(),
        StateEventReadRequest(
            contract_version="1.0",
            scope_ref="scope.1",
            consumer_ref="agent-a",
            limit=1,
        ),
    )
    await transition(service, "object.1", "op.transition.1", 2)
    await transition(service, "object.1", "op.transition.2", 3)
    await store._trim_events_before_for_test("tenant-a", "scope.1", 3)

    stale = await service.events(
        caller(),
        StateEventReadRequest(
            contract_version="1.0",
            scope_ref="scope.1",
            consumer_ref="agent-a",
            cursor=first.next_cursor,
            limit=10,
        ),
    )
    assert stale.coverage == "resync_required"
    assert stale.events == ()
    assert stale.next_cursor is None
    assert stale.retained_from_seq == 3


@pytest.mark.asyncio
async def test_history_pages_are_revision_ordered_and_retention_is_explicit(harness):
    store, _codec, service = harness
    await service.create(caller(), create_req("object.1", "op.create.1"))
    await transition(service, "object.1", "op.transition.1", 2)
    await transition(service, "object.1", "op.transition.2", 3)

    first = await service.history(
        caller(),
        StateHistoryRequest(
            contract_version="1.0", object_id="object.1", scope_ref="scope.1", limit=2
        ),
    )
    assert [event.state_ref.revision for event in first.events] == [0, 1]
    assert first.coverage == "bounded"
    second = await service.history(
        caller(),
        StateHistoryRequest(
            contract_version="1.0",
            object_id="object.1",
            scope_ref="scope.1",
            cursor=first.next_cursor,
            limit=2,
        ),
    )
    assert [event.state_ref.revision for event in second.events] == [2]
    assert second.coverage == "complete"

    await store._trim_events_before_for_test("tenant-a", "scope.1", 2)
    unavailable = await service.history(
        caller(),
        StateHistoryRequest(
            contract_version="1.0", object_id="object.1", scope_ref="scope.1", limit=10
        ),
    )
    assert unavailable.coverage == "history_unavailable"
    assert unavailable.events == ()
    assert unavailable.oldest_available_revision == 1
    assert unavailable.latest_revision == 2


@pytest.mark.asyncio
async def test_consumer_ref_cannot_impersonate_another_principal(harness):
    _store, _codec, service = harness
    result = await service.events(
        caller("agent-a"),
        StateEventReadRequest(
            contract_version="1.0",
            scope_ref="scope.1",
            consumer_ref="agent-b",
            limit=10,
        ),
    )
    assert isinstance(result, StateProblem)
    assert result.code == "SCOPE_FORBIDDEN"


@pytest.mark.asyncio
async def test_explicitly_authorized_delegated_consumer_is_isolated_to_its_own_cursor(harness):
    store, codec, _service = harness
    catalog = ConfiguredContractCatalog()
    catalog.admit_schema("urn:test:v1", SCHEMA, lambda p: isinstance(p.get("value"), int))
    catalog.admit_retention("retention.test", RET)
    service = StateService(
        store,
        catalog,
        cursor_codec=codec,
        authorization=DelegatedConsumerAuthorization(),
    )
    delegated = CallerContext(
        "tenant-a",
        "agent-a",
        "state.authz.tenant-base:delegated",
        ExecutionBudget.start(30_000),
        "packet:delegated",
    )
    await service.create(caller(), create_req("object.1", "op.create.1"))
    page = await service.events(
        delegated,
        StateEventReadRequest(
            contract_version="1.0",
            scope_ref="scope.1",
            consumer_ref="consumer-delegated",
            limit=10,
        ),
    )
    assert not isinstance(page, StateProblem)
    assert page.next_cursor is not None

    foreign = await service.events(
        delegated,
        StateEventReadRequest(
            contract_version="1.0",
            scope_ref="scope.1",
            consumer_ref="different-consumer",
            cursor=page.next_cursor,
            limit=10,
        ),
    )
    assert isinstance(foreign, StateProblem)
    assert foreign.code == "SCOPE_FORBIDDEN"


@pytest.mark.asyncio
async def test_exact_ack_retry_survives_cursor_key_rotation(harness):
    store, _codec, service = harness
    await service.create(caller(), create_req("object.rotate", "op.create.rotate"))
    page = await service.events(
        caller(),
        StateEventReadRequest(
            contract_version="1.0",
            scope_ref="scope.1",
            consumer_ref="agent-a",
            limit=10,
        ),
    )
    request = StateAckRequest(
        contract_version="1.0",
        scope_ref="scope.1",
        consumer_ref="agent-a",
        cursor=page.next_cursor,
        operation_id="op.ack.rotate",
    )
    first = await service.acknowledge(caller(), request)
    rotated_catalog = ConfiguredContractCatalog()
    rotated_catalog.admit_schema("urn:test:v1", SCHEMA, lambda p: isinstance(p.get("value"), int))
    rotated_catalog.admit_retention("retention.test", RET)
    rotated = StateService(
        store,
        rotated_catalog,
        cursor_codec=CursorCodec(b"r" * 32),
    )
    replay = await rotated.acknowledge(caller(), request)
    assert replay == first


@pytest.mark.asyncio
async def test_brand_new_consumer_after_retention_starts_at_earliest_retained_event(harness):
    store, _codec, service = harness
    await service.create(caller(), create_req("object.new", "op.create.new"))
    await transition(service, "object.new", "op.transition.new.1", 2)
    await transition(service, "object.new", "op.transition.new.2", 3)
    await store._trim_events_before_for_test("tenant-a", "scope.1", 3)

    page = await service.events(
        caller("agent-new"),
        StateEventReadRequest(
            contract_version="1.0",
            scope_ref="scope.1",
            consumer_ref="agent-new",
            limit=10,
        ),
    )
    assert page.coverage == "complete"
    assert [event.journal_seq for event in page.events] == [3]
    assert page.next_cursor is not None


@pytest.mark.asyncio
async def test_stale_durable_ack_after_retention_requires_resync(harness):
    store, _codec, service = harness
    await service.create(caller(), create_req("object.ack-stale", "op.create.ack-stale"))
    first = await service.events(
        caller(),
        StateEventReadRequest(
            contract_version="1.0", scope_ref="scope.1", consumer_ref="agent-a", limit=1
        ),
    )
    committed = await service.acknowledge(
        caller(),
        StateAckRequest(
            contract_version="1.0",
            scope_ref="scope.1",
            consumer_ref="agent-a",
            cursor=first.next_cursor,
            operation_id="op.ack.stale.1",
        ),
    )
    assert committed.status == "committed"

    await transition(service, "object.ack-stale", "op.transition.ack-stale.1", 2)
    await transition(service, "object.ack-stale", "op.transition.ack-stale.2", 3)
    await store._trim_events_before_for_test("tenant-a", "scope.1", 3)

    stale = await service.events(
        caller(),
        StateEventReadRequest(
            contract_version="1.0", scope_ref="scope.1", consumer_ref="agent-a", limit=10
        ),
    )
    assert stale.coverage == "resync_required"
    assert stale.retained_from_seq == 3
    assert stale.next_cursor is None


@pytest.mark.asyncio
async def test_missing_history_is_canonical_object_not_found_problem(harness):
    _store, _codec, service = harness
    result = await service.history(
        caller(),
        StateHistoryRequest(
            contract_version="1.0", object_id="missing", scope_ref="scope.1", limit=10
        ),
    )
    assert isinstance(result, StateProblem)
    assert result.code == "OBJECT_NOT_FOUND"
    assert result.retry_class == "no"
