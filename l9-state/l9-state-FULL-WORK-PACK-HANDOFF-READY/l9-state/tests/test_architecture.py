from pathlib import Path

import pytest


def test_no_provider_or_peer_transport_in_core():
    root = Path(__file__).parents[1] / "src/l9_state"
    core = "\n".join(p.read_text() for p in root.rglob("*.py") if "adapters" not in p.parts)
    lowered = core.lower()
    for forbidden in ("pymongo", "mongodb", "bson", "requests.post", "httpx", "peer_url"):
        assert forbidden not in lowered
    for domain in ("workitem", "agent_profile", "customer_order"):
        assert domain not in lowered

def test_mongodb_driver_is_server_optional_not_base_runtime_dependency():
    import tomllib

    root = Path(__file__).parents[1]
    config = tomllib.loads((root / "pyproject.toml").read_text())
    base = config["project"]["dependencies"]
    optional = config["project"]["optional-dependencies"]
    assert not any(dep.lower().startswith("pymongo") for dep in base)
    assert any(dep.lower().startswith("pymongo") for dep in optional["server"])


def test_core_import_surface_does_not_reexport_mongodb_adapter():
    root = Path(__file__).parents[1] / "src/l9_state"
    package_init = (root / "__init__.py").read_text().lower()
    client = (root / "client.py").read_text().lower()
    assert "adapters.mongodb" not in package_init
    assert "pymongo" not in package_init
    assert "pymongo" not in client



def test_gate_timeout_is_bound_to_provider_neutral_execution_budget():
    root = Path(__file__).parents[1] / "src/l9_state"
    gate = (root / "bindings/gate.py").read_text()
    execution = (root / "execution.py").read_text().lower()
    assert "ExecutionBudget.start(packet.header.timeout_ms, policy=budget_policy)" in gate
    for forbidden in ("pymongo", "mongodb", "bson"):
        assert forbidden not in execution


def test_operation_execution_invariants_are_committed_to_repo_contract():
    root = Path(__file__).parents[1]
    invariants = (root / "invariants.yaml").read_text()
    required = {
        "STATE-BUDGET-001",
        "STATE-BUDGET-002",
        "STATE-OUTCOME-001",
        "STATE-OUTCOME-002",
        "STATE-OUTCOME-003",
        "STATE-AMBIGUITY-001",
        "STATE-PROBLEM-001",
        "STATE-RETRY-001",
        "STATE-RETRY-002",
    }
    assert all(invariant in invariants for invariant in required)


def test_retry_taxonomy_matches_public_problem_schema_and_separates_recovery_guidance():
    root = Path(__file__).parents[1]
    reason_codes = (root / "contracts/ERRORS_AND_REASON_CODES.yaml").read_text()
    schema = (root / "contracts/schemas/StateProblem.schema.json").read_text()
    retry_classes = {
        "no",
        "same_operation",
        "refresh_then_decide",
        "cold_resync",
        "later",
        "inspect_then_same_operation",
    }
    for value in retry_classes:
        assert value in reason_codes
        assert value in schema
    assert "problem_retry_classes:" in reason_codes
    assert "terminal_receipt_recovery:" in reason_codes
    assert "bounded_same_operation" not in reason_codes
    assert "after_release_or_expiry" not in reason_codes


def test_state_problem_is_not_a_stored_operation_receipt_family():
    root = Path(__file__).parents[1] / "src/l9_state"
    ports = (root / "ports.py").read_text()
    assert "MutationReceipt = StateReceipt | StateClaimReceipt | StateAckReceipt | HardEraseReceipt" in ports
    assert "StateProblem" not in ports


def test_hard_erase_is_private_and_not_gate_routable():
    root = Path(__file__).parents[1] / "src/l9_state"
    gate = (root / "bindings/gate.py").read_text()
    client = (root / "client.py").read_text()
    retention = (root / "retention.py").read_text()
    assert '@register_handler("state.internal.hard_erase")' not in gate
    assert "hard_erase" not in client
    assert "external retention-policy decision contract is intentionally not defined here" in retention


def test_state04_lifecycle_invariants_are_committed():
    root = Path(__file__).parents[1]
    invariants = (root / "invariants.yaml").read_text()
    for invariant in (
        "STATE-LIFECYCLE-001",
        "STATE-RESTORE-001",
        "STATE-ERASE-001",
        "STATE-RETENTION-002",
    ):
        assert invariant in invariants


def test_authorization_boundary_is_explicit_and_packet_id_is_not_authorization_evidence():
    root = Path(__file__).parents[1] / "src/l9_state"
    gate = (root / "bindings/gate.py").read_text()
    ports = (root / "ports.py").read_text()
    service = (root / "service.py").read_text()
    auth_fn = gate.split("def _tenant_base_authorization_ref", 1)[1].split("\ndef _caller", 1)[0]
    assert "TENANT_BASE_AUTHORIZATION_POLICY" in auth_fn
    assert "packet.header.packet_id" not in auth_fn
    assert "state.authz.tenant-base:" in auth_fn
    assert "class ScopeAuthorizationPort(Protocol):" in ports
    assert "authorization: ScopeAuthorizationPort | None = None" in service
    assert "await self._authorization.authorize(request)" in service


def test_gate_runtime_idempotency_contract_covers_exact_mutation_action_set():
    import ast

    root = Path(__file__).parents[1] / "src/l9_state"
    source = (root / "bindings/gate.py").read_text()
    tree = ast.parse(source)
    mutation_actions = None
    registered = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name) and target.id == "STATE_MUTATION_ACTIONS":
                    mutation_actions = set(ast.literal_eval(node.value.args[0]))
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            for decorator in node.decorator_list:
                if (
                    isinstance(decorator, ast.Call)
                    and isinstance(decorator.func, ast.Name)
                    and decorator.func.id == "register_handler"
                    and decorator.args
                    and isinstance(decorator.args[0], ast.Constant)
                ):
                    registered.add(decorator.args[0].value)
    assert mutation_actions == {
        "state.create",
        "state.transition",
        "state.tombstone",
        "state.restore",
        "state.claim",
        "state.renew",
        "state.release",
        "state.ack",
    }
    assert registered == {
        "state.create",
        "state.get",
        "state.transition",
        "state.tombstone",
        "state.restore",
        "state.claim",
        "state.renew",
        "state.release",
        "state.list",
        "state.events",
        "state.ack",
        "state.history",
        "state.operation.inspect",
    }
    assert "_validate_gate_runtime_config(resolved_config)" in source
    assert "STATE_MUTATION_ACTIONS - required" in source


def test_infrastructure_retry_documentation_is_effect_aware():
    root = Path(__file__).parents[1]
    reason_codes = (root / "contracts/ERRORS_AND_REASON_CODES.yaml").read_text()
    assert "infrastructure_retry_by_effect:" in reason_codes
    assert "mutation_definite_precommit: same_operation" in reason_codes
    assert "mutation_ambiguous: inspect_then_same_operation" in reason_codes
    assert "read: later" in reason_codes


def test_gate_runtime_config_validation_fails_closed_when_mutation_idempotency_is_missing():
    from types import SimpleNamespace

    from l9_state.bindings.gate import STATE_MUTATION_ACTIONS, _validate_gate_runtime_config

    with pytest.raises(ValueError):
        _validate_gate_runtime_config(SimpleNamespace(require_idempotency_for_actions=()))
    _validate_gate_runtime_config(
        SimpleNamespace(require_idempotency_for_actions=tuple(sorted(STATE_MUTATION_ACTIONS)))
    )


def test_gate_ingress_validation_returns_canonical_invalid_request_problem():
    from constellation_node_sdk import create_transport_packet

    from l9_state.bindings.gate import _parse_request
    from l9_state.models import StateCreateRequest, StateProblem

    packet = create_transport_packet(
        action="state.create",
        payload={},
        tenant="tenant-a",
        idempotency_key="different-operation",
    )
    malformed = _parse_request(StateCreateRequest, {"contract_version": "1.0"}, packet, action="state.create")
    assert isinstance(malformed, StateProblem)
    assert malformed.code == "INVALID_REQUEST"
    assert malformed.retry_class == "no"

    valid_payload = {
        "contract_version": "1.0",
        "object_id": "object.1",
        "scope_ref": "scope.1",
        "schema_ref": "urn:test:v1",
        "schema_digest": "a" * 64,
        "payload": {"value": 1},
        "operation_id": "op.create.1",
        "retention_policy_ref": "retention.test",
        "retention_policy_digest": "b" * 64,
    }
    mismatch = _parse_request(StateCreateRequest, valid_payload, packet, action="state.create")
    assert isinstance(mismatch, StateProblem)
    assert mismatch.code == "INVALID_REQUEST"
    assert mismatch.operation_id == "op.create.1"
