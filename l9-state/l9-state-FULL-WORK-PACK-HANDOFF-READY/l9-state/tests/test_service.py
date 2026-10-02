import pytest

from l9_state.adapters.memory import InProcessStateStore
from l9_state.catalog import ConfiguredContractCatalog
from l9_state.cursor import CursorCodec
from l9_state.execution import ExecutionBudget
from l9_state.models import (
    StateCreateRequest,
    StateOperationInspectRequest,
    StateProblem,
    StateReadRequest,
    StateReceipt,
    StateTransitionRequest,
)
from l9_state.ports import ScopeAuthorizationDecision
from l9_state.service import CallerContext, StateService

SCHEMA = "a" * 64
RET = "b" * 64


class ToggleAuthorization:
    def __init__(self) -> None:
        self.allowed = True
        self.calls = []

    async def authorize(self, request):
        self.calls.append(request)
        if not self.allowed:
            return ScopeAuthorizationDecision(
                allowed=False,
                authorization_ref="policy.denied",
                reason_code="SCOPE_FORBIDDEN",
            )
        suffix = request.consumer_ref or request.scope_ref
        return ScopeAuthorizationDecision(
            allowed=True,
            authorization_ref=f"policy.scope:{request.action}:{suffix}",
        )


@pytest.fixture
def svc():
    catalog = ConfiguredContractCatalog()
    validator = lambda p: isinstance(p.get("value"), int)
    catalog.admit_schema("urn:test:v1", SCHEMA, validator)
    catalog.admit_schema("urn:other:v1", SCHEMA, validator)
    catalog.admit_retention("retention.test", RET)
    return StateService(InProcessStateStore(), catalog, cursor_codec=CursorCodec(b"x" * 32))


def caller():
    return CallerContext(
        "tenant-a",
        "agent-a",
        "state.authz.tenant-base:test",
        ExecutionBudget.start(30_000),
        "packet:test",
    )


def create_req(op="op.create.1", value=1):
    return StateCreateRequest(
        contract_version="1.0",
        object_id="object.1",
        scope_ref="scope.1",
        schema_ref="urn:test:v1",
        schema_digest=SCHEMA,
        payload={"value": value},
        operation_id=op,
        retention_policy_ref="retention.test",
        retention_policy_digest=RET,
    )


@pytest.mark.asyncio
async def test_create_get_named_revision_and_exact_retry(svc):
    first = await svc.create(caller(), create_req())
    retry = await svc.create(caller(), create_req())
    assert isinstance(first, StateReceipt)
    assert first == retry and first.state_ref.revision == 0
    got = await svc.get(
        caller(),
        StateReadRequest(
            contract_version="1.0", object_id="object.1", scope_ref="scope.1", revision=0
        ),
    )
    assert got.payload == {"value": 1}


@pytest.mark.asyncio
async def test_idempotency_collision_is_canonical_problem_and_has_no_effect(svc):
    original = await svc.create(caller(), create_req())
    collision = await svc.create(caller(), create_req(value=2))
    assert collision.code == "IDEMPOTENCY_COLLISION"
    assert collision.retry_class == "no"
    inspected = await svc.inspect_operation(
        caller(),
        StateOperationInspectRequest(
            contract_version="1.0", scope_ref="scope.1", operation_id="op.create.1"
        ),
    )
    assert inspected.status == "found"
    assert inspected.receipt["receipt_id"] == original.receipt_id
    got = await svc.get(
        caller(),
        StateReadRequest(contract_version="1.0", object_id="object.1", scope_ref="scope.1"),
    )
    assert got.payload == {"value": 1}


@pytest.mark.asyncio
async def test_transition_cas_full_replacement_and_inspect(svc):
    created = await svc.create(caller(), create_req())
    req = StateTransitionRequest(
        contract_version="1.0",
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
    receipt = await svc.transition(caller(), req)
    assert receipt.state_ref.revision == 1
    named = await svc.get(
        caller(),
        StateReadRequest(
            contract_version="1.0", object_id="object.1", scope_ref="scope.1", revision=0
        ),
    )
    assert named.payload == {"value": 1}
    current = await svc.get(
        caller(),
        StateReadRequest(contract_version="1.0", object_id="object.1", scope_ref="scope.1"),
    )
    assert current.payload == {"value": 2}
    inspected = await svc.inspect_operation(
        caller(),
        StateOperationInspectRequest(
            contract_version="1.0", scope_ref="scope.1", operation_id="op.transition.1"
        ),
    )
    assert inspected.status == "found" and inspected.receipt["receipt_id"] == receipt.receipt_id


@pytest.mark.asyncio
async def test_revision_conflict_and_schema_refusal_are_durable_receipts(svc):
    created = await svc.create(caller(), create_req())
    bad = StateTransitionRequest(
        contract_version="1.0",
        object_id="object.1",
        scope_ref="scope.1",
        expected_revision=9,
        expected_state_digest=created.state_ref.state_digest,
        expected_schema_ref="urn:test:v1",
        expected_schema_digest=SCHEMA,
        payload={"value": 2},
        transition_label="advance",
        operation_id="op.bad.1",
    )
    conflict = await svc.transition(caller(), bad)
    assert conflict.status == "conflict"
    assert conflict.reason_codes == ("REVISION_CONFLICT",)
    assert await svc.transition(caller(), bad) == conflict

    schema_bad = bad.model_copy(
        update={
            "expected_revision": 0,
            "expected_schema_ref": "urn:other:v1",
            "operation_id": "op.bad.2",
        }
    )
    refused = await svc.transition(caller(), schema_bad)
    assert refused.status == "refused"
    assert refused.reason_codes == ("SCHEMA_BINDING_IMMUTABLE",)


@pytest.mark.asyncio
async def test_catalog_refusal_is_durable_terminal_operation(svc):
    bad = create_req(op="op.create.refused").model_copy(update={"schema_digest": "c" * 64})
    first = await svc.create(caller(), bad)
    second = await svc.create(caller(), bad)
    assert first == second
    assert first.status == "refused"
    assert first.reason_codes == ("SCHEMA_DIGEST_MISMATCH",)
    inspected = await svc.inspect_operation(
        caller(),
        StateOperationInspectRequest(
            contract_version="1.0", scope_ref="scope.1", operation_id="op.create.refused"
        ),
    )
    assert inspected.status == "found"
    assert inspected.receipt["status"] == "refused"


@pytest.mark.asyncio
async def test_create_conflict_is_durable_and_does_not_mutate_state(svc):
    first = await svc.create(caller(), create_req())
    conflict_req = create_req(op="op.create.conflict", value=9)
    conflict = await svc.create(caller(), conflict_req)
    assert conflict.status == "conflict"
    assert conflict.reason_codes == ("OBJECT_ALREADY_EXISTS",)
    assert await svc.create(caller(), conflict_req) == conflict
    current = await svc.get(
        caller(),
        StateReadRequest(contract_version="1.0", object_id="object.1", scope_ref="scope.1"),
    )
    assert current.state_ref == first.state_ref
    assert current.payload == {"value": 1}


@pytest.mark.asyncio
async def test_revision_conflict_remains_sticky_after_world_changes(svc):
    created = await svc.create(caller(), create_req())
    blocked = StateTransitionRequest(
        contract_version="1.0",
        object_id="object.1",
        scope_ref="scope.1",
        expected_revision=1,
        expected_state_digest="c" * 64,
        expected_schema_ref="urn:test:v1",
        expected_schema_digest=SCHEMA,
        payload={"value": 99},
        transition_label="blocked",
        operation_id="op.transition.sticky-conflict",
    )
    first = await svc.transition(caller(), blocked)
    assert first.status == "conflict"
    assert first.reason_codes == ("REVISION_CONFLICT",)

    advance = StateTransitionRequest(
        contract_version="1.0",
        object_id="object.1",
        scope_ref="scope.1",
        expected_revision=0,
        expected_state_digest=created.state_ref.state_digest,
        expected_schema_ref="urn:test:v1",
        expected_schema_digest=SCHEMA,
        payload={"value": 2},
        transition_label="advance",
        operation_id="op.transition.advance-world",
    )
    advanced = await svc.transition(caller(), advance)
    assert advanced.status == "committed"
    assert advanced.state_ref.revision == 1

    # The original operation is an attempt identity, not an open-ended intention.
    assert await svc.transition(caller(), blocked) == first


@pytest.mark.asyncio
async def test_current_authorization_gates_exact_retry_and_operation_inspection():
    catalog = ConfiguredContractCatalog()
    catalog.admit_schema("urn:test:v1", SCHEMA, lambda p: isinstance(p.get("value"), int))
    catalog.admit_retention("retention.test", RET)
    authorization = ToggleAuthorization()
    service = StateService(
        InProcessStateStore(),
        catalog,
        cursor_codec=CursorCodec(b"a" * 32),
        authorization=authorization,
    )

    first = await service.create(caller(), create_req(op="op.authz.retry"))
    assert isinstance(first, StateReceipt)
    assert first.authorization_ref == "policy.scope:state.create:scope.1"

    authorization.allowed = False
    retry = await service.create(caller(), create_req(op="op.authz.retry"))
    assert isinstance(retry, StateProblem)
    assert retry.code == "SCOPE_FORBIDDEN"

    inspected = await service.inspect_operation(
        caller(),
        StateOperationInspectRequest(
            contract_version="1.0", scope_ref="scope.1", operation_id="op.authz.retry"
        ),
    )
    assert isinstance(inspected, StateProblem)
    assert inspected.code == "SCOPE_FORBIDDEN"
