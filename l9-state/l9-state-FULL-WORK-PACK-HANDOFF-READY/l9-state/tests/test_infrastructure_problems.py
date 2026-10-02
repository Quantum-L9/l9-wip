import pytest

from l9_state.adapters.memory import InProcessStateStore
from l9_state.catalog import ConfiguredContractCatalog
from l9_state.errors import StateInfrastructureFailure
from l9_state.cursor import CursorCodec
from l9_state.execution import ExecutionBudget
from l9_state.models import StateCreateRequest, StateOperationInspectRequest, StateProblem
from l9_state.service import CallerContext, StateService

SCHEMA = "a" * 64
RET = "b" * 64


class AmbiguousCreateStore(InProcessStateStore):
    async def create(self, *, revision, operation, event, budget):
        raise StateInfrastructureFailure(
            code="OUTCOME_UNKNOWN",
            message="commit acknowledgement lost",
            operation_id=operation.receipt.operation_id,
            scope_ref=revision.state_ref.scope_ref,
        )


class UnavailableInspectStore(InProcessStateStore):
    async def get_operation(self, tenant_org_id, scope_ref, operation_id):
        raise StateInfrastructureFailure(
            code="STORAGE_UNAVAILABLE",
            message="majority read unavailable",
            operation_id=operation_id,
            scope_ref=scope_ref,
        )


def service(store):
    catalog = ConfiguredContractCatalog()
    catalog.admit_schema("urn:test:v1", SCHEMA, lambda p: True)
    catalog.admit_retention("retention.test", RET)
    return StateService(store, catalog, cursor_codec=CursorCodec(b"x" * 32))


def caller():
    return CallerContext(
        "tenant-a",
        "agent-a",
        "state.authz.tenant-base:test",
        ExecutionBudget.start(30_000),
        "packet:test",
    )


def create_req():
    return StateCreateRequest(
        contract_version="1.0",
        object_id="object.1",
        scope_ref="scope.1",
        schema_ref="urn:test:v1",
        schema_digest=SCHEMA,
        payload={"value": 1},
        operation_id="op.create.ambiguous",
        retention_policy_ref="retention.test",
        retention_policy_digest=RET,
    )


@pytest.mark.asyncio
async def test_ambiguous_commit_maps_to_typed_problem_not_receipt():
    result = await service(AmbiguousCreateStore()).create(caller(), create_req())
    assert isinstance(result, StateProblem)
    assert result.code == "OUTCOME_UNKNOWN"
    assert result.retry_class == "inspect_then_same_operation"
    assert result.operation_id == "op.create.ambiguous"


@pytest.mark.asyncio
async def test_storage_unavailable_inspection_is_problem_not_not_found():
    result = await service(UnavailableInspectStore()).inspect_operation(
        caller(),
        StateOperationInspectRequest(contract_version="1.0", scope_ref="scope.1", operation_id="op.1"),
    )
    assert isinstance(result, StateProblem)
    assert result.code == "STORAGE_UNAVAILABLE"
    assert result.retry_class == "later"


class DeadlineCreateStore(InProcessStateStore):
    async def create(self, *, revision, operation, event, budget):
        raise StateInfrastructureFailure(
            code="DEADLINE_EXCEEDED",
            message="budget expired before commit attempt",
            operation_id=operation.receipt.operation_id,
            scope_ref=revision.state_ref.scope_ref,
        )


@pytest.mark.asyncio
async def test_definite_precommit_deadline_is_same_operation_problem_not_receipt():
    store = DeadlineCreateStore()
    svc = service(store)
    result = await svc.create(caller(), create_req())
    assert isinstance(result, StateProblem)
    assert result.code == "DEADLINE_EXCEEDED"
    assert result.retry_class == "same_operation"
    inspected = await svc.inspect_operation(
        caller(),
        StateOperationInspectRequest(
            contract_version="1.0",
            scope_ref="scope.1",
            operation_id="op.create.ambiguous",
        ),
    )
    assert inspected.status == "not_found"
