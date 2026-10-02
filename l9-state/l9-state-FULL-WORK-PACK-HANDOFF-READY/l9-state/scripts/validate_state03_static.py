from __future__ import annotations

import ast
import json
import runpy
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src" / "l9_state"
SCHEMAS = ROOT / "contracts" / "schemas"
AUTH_REV = "08912f391c0a6672957f40cbd9b0db285f82ed86"

checks: list[dict[str, object]] = []


def check(check_id: str, condition: bool, detail: str) -> None:
    checks.append({"id": check_id, "status": "PASS" if condition else "FAIL", "detail": detail})


def parse(path: Path) -> ast.Module:
    return ast.parse(path.read_text(encoding="utf-8"), filename=str(path))


def class_async_methods(path: Path, class_name: str) -> dict[str, list[str]]:
    tree = parse(path)
    for node in tree.body:
        if isinstance(node, ast.ClassDef) and node.name == class_name:
            result: dict[str, list[str]] = {}
            for child in node.body:
                if isinstance(child, ast.AsyncFunctionDef):
                    args = [a.arg for a in child.args.args]
                    args += [a.arg for a in child.args.kwonlyargs]
                    result[child.name] = args
            return result
    raise AssertionError(f"class {class_name} not found in {path}")


def class_fields(path: Path, class_name: str) -> set[str]:
    tree = parse(path)
    for node in tree.body:
        if isinstance(node, ast.ClassDef) and node.name == class_name:
            return {
                child.target.id
                for child in node.body
                if isinstance(child, ast.AnnAssign) and isinstance(child.target, ast.Name)
            }
    raise AssertionError(f"class {class_name} not found in {path}")


# 1. Public STATE-03 schema inventory and runtime model parity.
state03_models = {
    "StateListRequest": "StateListRequest.schema.json",
    "StateEventReadRequest": "StateEventReadRequest.schema.json",
    "StateAckRequest": "StateAckRequest.schema.json",
    "StateAckReceipt": "StateAckReceipt.schema.json",
    "StateHistoryRequest": "StateHistoryRequest.schema.json",
    "StateListPage": "StateListPage.schema.json",
    "StateEventPage": "StateEventPage.schema.json",
    "StateHistoryPage": "StateHistoryPage.schema.json",
}
for model, filename in state03_models.items():
    schema = json.loads((SCHEMAS / filename).read_text(encoding="utf-8"))
    model_fields = class_fields(SRC / "models.py", model)
    schema_fields = set(schema.get("properties", {}))
    check(
        f"MODEL-SCHEMA-{model}",
        model_fields == schema_fields,
        f"runtime fields match {filename}: {sorted(model_fields)}",
    )

schema_files = sorted(SCHEMAS.glob("*.schema.json"))
for path in schema_files:
    json.loads(path.read_text(encoding="utf-8"))
check("SCHEMA-JSON-PARSE", len(schema_files) == 24, f"parsed {len(schema_files)} public schemas")

try:
    import jsonschema  # type: ignore
except Exception:
    checks.append({"id": "SCHEMA-METAVALIDATION", "status": "BLOCKED", "detail": "jsonschema unavailable"})
else:
    for path in schema_files:
        jsonschema.Draft202012Validator.check_schema(json.loads(path.read_text(encoding="utf-8")))
    check("SCHEMA-METAVALIDATION", True, f"Draft 2020-12 meta-validation passed for {len(schema_files)} schemas")

# 2. StateStorePort parity across both providers.
port = class_async_methods(SRC / "ports.py", "StateStorePort")
memory = class_async_methods(SRC / "adapters" / "memory.py", "InProcessStateStore")
mongo = class_async_methods(SRC / "adapters" / "mongodb.py", "MongoStateStore")
for method, args in port.items():
    check(f"PORT-MEMORY-{method}", method in memory, "InProcessStateStore implements port method")
    check(f"PORT-MONGO-{method}", method in mongo, "MongoStateStore implements port method")
    if method in memory:
        check(f"PORT-MEMORY-SIG-{method}", memory[method] == args, f"signature args {args}")
    if method in mongo:
        check(f"PORT-MONGO-SIG-{method}", mongo[method] == args, f"signature args {args}")

# 3. Gate and client action wiring.
gate_text = (SRC / "bindings" / "gate.py").read_text(encoding="utf-8")
client_methods = class_async_methods(SRC / "client.py", "StateClient")
actions = {
    "state.create": "create",
    "state.get": "get",
    "state.transition": "transition",
    "state.claim": "claim",
    "state.renew": "renew",
    "state.release": "release",
    "state.list": "list_states",
    "state.events": "events",
    "state.ack": "acknowledge",
    "state.history": "history",
    "state.operation.inspect": "inspect_operation",
}
for action, client_method in actions.items():
    check(f"GATE-{action}", f'@register_handler("{action}")' in gate_text, "registered Gate action")
    check(f"CLIENT-{action}", client_method in client_methods, f"StateClient.{client_method} exists")
check(
    "ACK-GATE-IDEMPOTENCY",
    "StateAckRequest" in gate_text
    and 'action="state.ack"' in gate_text
    and "STATE_MUTATION_ACTIONS" in gate_text
    and '_require_operation_identity(packet, request.operation_id)' in gate_text,
    "state.ack binds operation_id to Gate idempotency_key through shared ingress parser",
)

# 4. Cursor correctness and public bound.
cursor_ns = runpy.run_path(str(SRC / "cursor.py"))
CursorCodec = cursor_ns["CursorCodec"]
CursorClaims = cursor_ns["CursorClaims"]
filter_digest = cursor_ns["filter_digest"]
codec = CursorCodec(b"z" * 32)
max_token = codec.issue(
    CursorClaims(
        purpose="list",
        scope_binding=codec.scope_binding("t" * 512, "s" * 512),
        consumer_binding=codec.consumer_binding("c" * 512),
        position=0,
        filter_digest=filter_digest(
            schema_refs=tuple(f"urn:schema:{i}:" + "x" * 490 for i in range(20)),
            lifecycle="active",
        ),
        resume_seq=9_223_372_036_854_775_807,
        last_object_id="o" * 200,
    )
)
check("CURSOR-MAX-BOUND", len(max_token) <= 512, f"worst-case list cursor length={len(max_token)}")
cursor_text = (SRC / "cursor.py").read_text(encoding="utf-8")
check("CURSOR-HMAC", "hmac.compare_digest" in cursor_text, "cursor authentication uses constant-time HMAC comparison")
check("CURSOR-NO-RAW-IDENTITY", '"tenant_org_id"' not in cursor_text.split("def issue", 1)[1].split("def decode", 1)[0], "issued cursor payload omits raw tenant identity")

service_text = (SRC / "service.py").read_text(encoding="utf-8")
check(
    "COLD-RESUME-CAPTURE-ORDER",
    service_text.index("current_journal_seq") < service_text.index("list_state_refs"),
    "list captures journal high-water before current-StateRef enumeration",
)
check("EVENT-FINAL-CURSOR", "successful event page requires ackable next_cursor" in (SRC / "models.py").read_text(encoding="utf-8"), "event page model requires cursor for complete/bounded pages")
check("CURSOR-CONSUMER-BINDING", "CURSOR_CONSUMER_MISMATCH" in service_text and "consumer_binding" in service_text, "consumer-bound cursor validation is wired")
check("CURSOR-FILTER-BINDING", "decoded.filter_digest != digest" in service_text, "list cursors bind filter digest")

# 5. Journal/read race boundaries and ack durability.
mongo_text = (SRC / "adapters" / "mongodb.py").read_text(encoding="utf-8")
check("EVENT-HIGHWATER-CAP", '"$lte": high_water' in mongo_text, "Mongo event page cannot leak beyond declared high-water")
check("HISTORY-REVISION-CAP", '"$lte": latest' in mongo_text, "Mongo history page cannot leak beyond observed latest revision")
check("ACK-CONSUMER-UPDATE", "self._consumer_cursors.update_one" in mongo_text, "ack callback writes consumer checkpoint")
check("ACK-OPERATION-RECEIPT", "ACK_RECEIPT_SCHEMA_REF" in mongo_text and "self._operations.insert_one" in mongo_text, "ack callback inserts immutable operation receipt")
check("ACK-REGRESSION-GUARD", "ACK_REGRESSION" in mongo_text and "cursor_seq" in mongo_text, "ack regression is rejected")
check("ACK-DESERIALIZATION", 'action == "state.ack"' in mongo_text, "stored ack receipt deserializes through operation inspection")
ack_method = service_text.split("    async def acknowledge(", 1)[1].split("    async def history(", 1)[0]
check(
    "ACK-EXACT-RETRY-BEFORE-CURSOR-REVALIDATION",
    ack_method.index("_existing_operation") < ack_method.index("_decode_cursor"),
    "exact durable ack receipt is recoverable before revalidating an old cursor token",
)

# 6. No provider leakage / no Change Streams correctness dependency.
all_src = "\n".join(path.read_text(encoding="utf-8") for path in SRC.rglob("*.py"))
public_src = "\n".join((SRC / name).read_text(encoding="utf-8") for name in ["models.py", "ports.py", "service.py", "client.py", "cursor.py"])
check("NO-CHANGE-STREAMS", ".watch(" not in all_src and "change_stream" not in all_src.lower(), "no Change Streams dependency in State correctness path")
check("PUBLIC-NO-MONGO", "pymongo" not in public_src.lower() and "bson" not in public_src.lower(), "public/domain layers contain no Mongo/BSON dependency")

# 7. Upstream semantic authority and invariant continuity.
authority_text = (ROOT / "build_state" / "SEMANTIC_AUTHORITY_BINDING_STATE03.yaml").read_text(encoding="utf-8")
check("AUTHORITY-REVISION", AUTH_REV in authority_text, f"STATE-03 bound to .github@{AUTH_REV}")
check("AUTHORITY-ARCHETYPE", "l9.node-archetype/authoritative-state@1" in authority_text, "authoritative-state archetype recorded")
invariants_text = (ROOT / "invariants.yaml").read_text(encoding="utf-8")
for invariant in ["STATE-JOURNAL-001", "STATE-CURSOR-001", "STATE-EVENT-001", "STATE-EVENT-OPT-001", "STATE-GATE-001"]:
    check(f"INVARIANT-{invariant}", invariant in invariants_text, "required STATE-03 invariant preserved")

# 8. Source/test syntax compilation.
compile_result = subprocess.run(
    [sys.executable, "-m", "compileall", "-q", "src", "tests"],
    cwd=ROOT,
    text=True,
    capture_output=True,
)
check("PY-COMPILE", compile_result.returncode == 0, compile_result.stderr.strip() or "source and tests compile")

failed = [item for item in checks if item["status"] == "FAIL"]
summary = {
    "schema": "l9.state.static-wiring-results/v1",
    "unit": "STATE-03_JOURNAL_COLD_RESUME",
    "authority_revision": AUTH_REV,
    "pass": sum(item["status"] == "PASS" for item in checks),
    "fail": len(failed),
    "blocked": sum(item["status"] == "BLOCKED" for item in checks),
    "checks": checks,
}
print(json.dumps(summary, indent=2))
raise SystemExit(1 if failed else 0)
