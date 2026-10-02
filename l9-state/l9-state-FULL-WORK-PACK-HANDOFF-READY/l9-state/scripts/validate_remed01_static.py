#!/usr/bin/env python3
from __future__ import annotations

import ast
import importlib.util
import json
import sys
from pathlib import Path

from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src" / "l9_state"
SCHEMAS = ROOT / "contracts" / "schemas"
REVIEW = Path("/mnt/data/l9_state_review01_pack")
EXPECTED_AUTHORITY = "7d31438a32bf1ce7783b1b896d359e6eb34063d0"
EXPECTED_GATE_RELEASE = "1.2.0"
EXPECTED_GATE_COMMIT = "d3241de11a5a48f952a0cf5bc3ec7c051c472476"

checks: list[dict[str, str]] = []


def record(check_id: str, condition: bool, detail: str) -> None:
    checks.append({"id": check_id, "status": "PASS" if condition else "FAIL", "detail": detail})


def text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def load_models_module():
    # Import the leaf module directly so validation does not need optional runtime deps.
    path = SRC / "models.py"
    spec = importlib.util.spec_from_file_location("l9_state_models_remed_validation", path)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


service = text(SRC / "service.py")
ports = text(SRC / "ports.py")
gate = text(SRC / "bindings" / "gate.py")
reason_codes = text(ROOT / "contracts" / "ERRORS_AND_REASON_CODES.yaml")
pyproject = text(ROOT / "pyproject.toml")

# GAR-F-001: explicit authorization boundary and reauthorization before receipt disclosure.
record("F001-AUTH-PORT", "class ScopeAuthorizationPort(Protocol):" in ports, "ScopeAuthorizationPort exists")
record("F001-AUTH-INJECT", "authorization: ScopeAuthorizationPort | None = None" in service, "StateService accepts authorization port")
record("F001-AUTH-CALL", "await self._authorization.authorize(request)" in service, "scope authorization is invoked")
record("F001-RETRY-GATED", service.find("authorized = await self._authorize(") < service.find("existing = await self._existing_operation("), "mutation authorizes before exact retry lookup")
inspect_start = service.index("async def inspect_operation")
inspect_block = service[inspect_start:]
record("F001-INSPECT-GATED", "authorized = await self._authorize(" in inspect_block and inspect_block.index("authorized = await self._authorize(") < inspect_block.index("get_operation("), "operation inspection authorizes before receipt lookup")
record("F001-CONSUMER-GATED", "consumer_ref=consumer_ref" in service and "consumer_ref=request.consumer_ref" in service, "consumer identity is authorization input")
auth_fn = gate.split("def _tenant_base_authorization_ref", 1)[1].split("\ndef _caller", 1)[0]
record("F001-AUTH-EVIDENCE", "TENANT_BASE_AUTHORIZATION_POLICY" in auth_fn and "state.authz.tenant-base:" in auth_fn and "packet.header.packet_id" not in auth_fn, "authorization ref is policy/evidence-derived, not packet id")

# GAR-F-002: brand-new consumer vs stale retained position.
record("F002-PRIOR-POSITION", "has_prior_position" in service, "events distinguishes prior position")
record("F002-NEW-CONSUMER", "after_seq = page.retained_from_seq - 1" in service, "brand-new consumer starts immediately before earliest retained event")
record("F002-STALE-RESYNC", "if has_prior_position:" in service and 'coverage="resync_required"' in service, "stale prior position still forces resync")

# GAR-F-003/F-004: canonical problems and effect-aware retry.
record("F003-HISTORY-PROBLEM", 'code="OBJECT_NOT_FOUND", retry_class="no"' in inspect_block[:1] or 'code="OBJECT_NOT_FOUND", retry_class="no"' in service[service.index("async def history"):inspect_start], "missing history returns canonical OBJECT_NOT_FOUND problem")
record("F003-INGRESS-PARSE", "def _parse_request(" in gate and "except ValidationError:" in gate and '"code": "INVALID_REQUEST"' in gate, "malformed domain payload becomes INVALID_REQUEST")
record("F003-IDEMPOTENCY-PROBLEM", "STATE_MUTATION_ACTIONS" in gate and "packet.header.idempotency_key != operation_id" in gate and "_invalid_request_problem(request)" in gate, "transport idempotency mismatch becomes INVALID_REQUEST")
record("F004-READ-LATER", 'if effect == "read":' in service and '= "later"' in service, "read infrastructure failures retry later")
record("F004-AMBIGUOUS-INSPECT", 'exc.code == "OUTCOME_UNKNOWN"' in service and '"inspect_then_same_operation"' in service, "ambiguous mutation requires inspection")
record("F004-PRECOMMIT-SAME", 'retry_class = "same_operation"' in service, "definite mutation infrastructure failure reuses same operation")
record("F004-DOC", "infrastructure_retry_by_effect:" in reason_codes and "mutation_ambiguous: inspect_then_same_operation" in reason_codes, "retry taxonomy documentation is effect-aware")

# GAR-F-005: generated schema/runtime requiredness parity, plus schema meta-validation.
models = load_models_module()
parity_failures = []
meta_failures = []
compared = 0
for path in sorted(SCHEMAS.glob("*.schema.json")):
    schema = json.loads(text(path))
    try:
        Draft202012Validator.check_schema(schema)
    except Exception as exc:  # pragma: no cover - report only
        meta_failures.append(f"{path.name}: {exc}")
    model_name = path.name.removesuffix(".schema.json")
    model = getattr(models, model_name, None)
    if model is None:
        parity_failures.append(f"missing runtime model {model_name}")
        continue
    schema_required = set(schema.get("required", []))
    runtime_required = {name for name, field in model.model_fields.items() if field.is_required()}
    if schema_required != runtime_required:
        parity_failures.append(f"{model_name}: schema={sorted(schema_required)} runtime={sorted(runtime_required)}")
    compared += 1
record("F005-REQUIREDNESS-PARITY", compared == 24 and not parity_failures, f"compared={compared}; failures={parity_failures}")
record("F005-SCHEMA-META", not meta_failures, f"24 Draft 2020-12 schemas; failures={meta_failures}")
for cls_name, field_name in (
    ("StateReceipt", "reason_codes"),
    ("StateClaimReceipt", "reason_codes"),
    ("StateAckReceipt", "reason_codes"),
    ("StateProblem", "reason_codes"),
    ("StateListPage", "states"),
    ("StateEventPage", "events"),
    ("StateHistoryPage", "events"),
):
    record(f"F005-REQUIRED-{cls_name}-{field_name}", getattr(models, cls_name).model_fields[field_name].is_required(), f"{cls_name}.{field_name} required")

# GAR-F-006: one mutation set and startup fail-closed validation.
tree = ast.parse(gate)
mutation_actions = None
registered: set[str] = set()
for node in ast.walk(tree):
    if isinstance(node, ast.Assign):
        for target in node.targets:
            if isinstance(target, ast.Name) and target.id == "STATE_MUTATION_ACTIONS":
                if isinstance(node.value, ast.Call):
                    mutation_actions = set(ast.literal_eval(node.value.args[0]))
    if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
        for dec in node.decorator_list:
            if isinstance(dec, ast.Call) and isinstance(dec.func, ast.Name) and dec.func.id == "register_handler" and dec.args and isinstance(dec.args[0], ast.Constant):
                registered.add(str(dec.args[0].value))
expected_mutations = {
    "state.create", "state.transition", "state.tombstone", "state.restore",
    "state.claim", "state.renew", "state.release", "state.ack",
}
record("F006-MUTATION-SET", mutation_actions == expected_mutations, f"actions={sorted(mutation_actions or [])}")
record("F006-ACTIONS-REGISTERED", expected_mutations <= registered, "all mutations are registered Gate actions")
record("F006-STARTUP-FAIL-CLOSED", "STATE_MUTATION_ACTIONS - required" in gate and "_validate_gate_runtime_config(resolved_config)" in gate, "runtime config validates mutation idempotency before app creation")

# GAR-F-007: successor manifest remains moving @v1; successor metadata must be current.
record("F007-MOVING-V1", "Gate_SDK.git@v1" in pyproject and EXPECTED_GATE_COMMIT not in pyproject, "manifest keeps Gate moving-major v1 contract")
authority_binding_path = ROOT / "build_state" / "REMED-01_AUTHORITY_BINDING.yaml"
authority_binding = text(authority_binding_path) if authority_binding_path.exists() else ""
record("F007-CURRENT-GITHUB", EXPECTED_AUTHORITY in authority_binding, "successor binds current .github authority revision")
record("F007-CURRENT-GATE-RELEASE", f"observed_package_version: {EXPECTED_GATE_RELEASE}" in authority_binding and EXPECTED_GATE_COMMIT in authority_binding, "successor records current Gate v1 release evidence")
record("F007-HISTORICAL-RULE", "historical STATE receipts unchanged" in authority_binding or "are not rewritten" in authority_binding, "successor declares historical receipt immutability")

# No architecture expansion.
client = text(SRC / "client.py")
handlers = sorted(registered)
record("NO-NEW-ACTIONS", len(handlers) == 13 and "state.internal.hard_erase" not in registered, f"public Gate actions={len(handlers)}")
record("NO-HARD-ERASE-CLIENT", "hard_erase" not in client, "private erase remains absent from public client")
record("NO-MONGO-CORE", all(token not in (service + ports + gate).lower() for token in ("pymongo", "mongodb", "bson")), "provider syntax remains outside core/binding")

# Remediation contract coverage is exact.
remed = text(REVIEW / "REMEDIATION_CONTRACT.yaml")
for i in range(1, 8):
    record(f"CONTRACT-GAR-F-{i:03d}", f"GAR-F-{i:03d}" in remed, f"GAR-F-{i:03d} represented in remediation contract")

failed = [c for c in checks if c["status"] == "FAIL"]
result = {
    "schema": "l9.state.remed01-static-validation/v1",
    "contract_id": "L9-STATE-REMED-01-COMBINED-REVIEW",
    "authority_revision_expected": EXPECTED_AUTHORITY,
    "gate_release_observed": EXPECTED_GATE_RELEASE,
    "gate_release_commit_observed": EXPECTED_GATE_COMMIT,
    "pass": len(checks) - len(failed),
    "fail": len(failed),
    "checks": checks,
}
print(json.dumps(result, indent=2))
raise SystemExit(1 if failed else 0)
