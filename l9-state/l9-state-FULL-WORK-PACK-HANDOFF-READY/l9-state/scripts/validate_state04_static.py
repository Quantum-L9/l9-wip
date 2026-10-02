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


# 1. STATE-04 public schema/runtime parity. Public schemas are unchanged from Dev Pack v2.
state04_models = {
    "StateTombstoneRequest": "StateTombstoneRequest.schema.json",
    "StateRestoreRequest": "StateRestoreRequest.schema.json",
}
for model, filename in state04_models.items():
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

# 2. StateStorePort parity across reference and Mongo providers.
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

for lifecycle_method in ("tombstone", "restore", "hard_erase"):
    check(f"PORT-STATE04-{lifecycle_method}", lifecycle_method in port, "STATE-04 port operation exists")

# 3. Gate/client surface: 13 public actions; hard erase remains internal only.
gate_text = (SRC / "bindings" / "gate.py").read_text(encoding="utf-8")
client_text = (SRC / "client.py").read_text(encoding="utf-8")
client_methods = class_async_methods(SRC / "client.py", "StateClient")
actions = {
    "state.create": "create",
    "state.get": "get",
    "state.transition": "transition",
    "state.tombstone": "tombstone",
    "state.restore": "restore",
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
for action, request_model in (("state.tombstone", "StateTombstoneRequest"), ("state.restore", "StateRestoreRequest")):
    check(
        f"GATE-IDEMPOTENCY-{action}",
        request_model in gate_text
        and f'action="{action}"' in gate_text
        and "STATE_MUTATION_ACTIONS" in gate_text
        and "_require_operation_identity(packet, request.operation_id)" in gate_text,
        "mutation binds operation_id to Gate idempotency key through shared ingress parser",
    )
check("HARD-ERASE-NO-GATE", "state.internal.hard_erase" not in gate_text, "hard erase has no Gate handler")
check("HARD-ERASE-NO-CLIENT", "hard_erase" not in client_text, "hard erase has no public StateClient method")
root_init = (SRC / "__init__.py").read_text(encoding="utf-8")
check("PUBLIC-EXPORT-STATE04", "StateTombstoneRequest" in root_init and "StateRestoreRequest" in root_init, "STATE-04 public request models are exported from package root")

# 4. Lifecycle semantics are explicit in domain/core and both providers.
models_text = (SRC / "models.py").read_text(encoding="utf-8")
lifecycle_text = (SRC / "lifecycle.py").read_text(encoding="utf-8")
retention_text = (SRC / "retention.py").read_text(encoding="utf-8")
memory_text = (SRC / "adapters" / "memory.py").read_text(encoding="utf-8")
mongo_text = (SRC / "adapters" / "mongodb.py").read_text(encoding="utf-8")
service_text = (SRC / "service.py").read_text(encoding="utf-8")
ports_text = (SRC / "ports.py").read_text(encoding="utf-8")
internal_text = (SRC / "internal_models.py").read_text(encoding="utf-8")

check("TOMBSTONE-REVISION-INCREMENT", "revision=current.state_ref.revision + 1" in lifecycle_text, "tombstone emits revision+1")
check("TOMBSTONE-RETAINS-PAYLOAD", "current.payload" in lifecycle_text and 'lifecycle="tombstoned"' in lifecycle_text, "tombstone retains payload bytes while lifecycle changes")
check("RESTORE-REVISION-INCREMENT", lifecycle_text.count("revision=current.state_ref.revision + 1") >= 2, "restore emits new revision rather than rewind")
check("RESTORE-SOURCE-PAYLOAD", "dict(source.payload)" in lifecycle_text, "restore copies explicitly retained source payload")
check("RESTORE-EVENT-LABEL", 'event_kind="restored"' in lifecycle_text and "transition_label=request.transition_label" in lifecycle_text, "restore event records transition label")
check("EVENT-RESTORE-LABEL-LAW", 'self.event_kind in {"transitioned", "restored"}' in models_text and "requires transition_label" in models_text, "runtime model enforces restored transition label")

for provider, text in (("MEMORY", memory_text), ("MONGO", mongo_text)):
    check(f"{provider}-TOMBSTONED-TRANSITION-REFUSED", 'OBJECT_TOMBSTONED' in text, "ordinary transition cannot mutate tombstoned state")
    check(f"{provider}-ERASED-TERMINAL", 'OBJECT_ERASED' in text, "erased lifecycle is refused")
    check(f"{provider}-REUSE-FORBIDDEN", 'OBJECT_ID_REUSE_FORBIDDEN' in text, "previous object identity cannot be recreated")
    check(f"{provider}-RESTORE-SOURCE-PRIOR", "source_revision" in text and "RESTORE_SOURCE_UNAVAILABLE" in text, "restore requires retained prior revision")
    check(f"{provider}-RETENTION-BINDING", "RETENTION_POLICY_NOT_ADMITTED" in text, "hard erase validates immutable retention binding")

check("CURRENT-TOMBSTONE-READ-BLOCKED", 'stored.state_ref.lifecycle == "tombstoned"' in service_text and "OBJECT_NOT_FOUND" in service_text, "ordinary current read hides tombstoned state")
check("ERASED-READ-NO-PAYLOAD", '"payload_status": "erased" if stored.payload is None else "present"' in service_text, "erased/scrubbed revisions return no payload")

# 5. Hard erase is private, durable, atomic, and identity-preserving.
check("HARD-ERASE-PRIVATE-RECEIPT", "class HardEraseReceipt" in internal_text and 'state.internal.hard_erase' in internal_text, "private receipt family exists")
check("HARD-ERASE-PRIVATE-SCHEMA-REF", "HARD_ERASE_RECEIPT_SCHEMA_REF" in ports_text and "urn:l9:state:internal:HardEraseReceipt:1.0" in ports_text, "private receipt schema ref is explicit")
check("HARD-ERASE-OP-INSPECT", 'action == "state.internal.hard_erase"' in mongo_text and "HardEraseReceipt.model_validate" in mongo_text, "private receipt is replayable through operation inspection")
check("HARD-ERASE-PAYLOAD-SCRUB-MEMORY", "payload=None" in memory_text and "Scrub retained payload bytes" in memory_text, "reference store scrubs retained payload bytes")
check("HARD-ERASE-PAYLOAD-SCRUB-MONGO", 'self._revisions.update_many' in mongo_text and '"payload": None' in mongo_text, "Mongo scrubs retained revision payloads in transaction")
check("HARD-ERASE-CURRENT-ERASED", 'lifecycle="erased"' in retention_text and "current.state_ref.revision + 1" in retention_text, "hard erase creates terminal erased revision")
check("HARD-ERASE-FENCE-PRESERVED-MEMORY", "highest_fence=guarded_claim.highest_fence" in memory_text and "active=False" in memory_text, "reference store preserves fence lineage while deactivating claim")
check("HARD-ERASE-FENCE-PRESERVED-MONGO", '"active": False' in mongo_text and 'released_at' in mongo_text, "Mongo preserves claim document/fence lineage while deactivating it")
check("HARD-ERASE-JOURNALED-MONGO", "_next_journal_seq" in mongo_text and 'event_kind="erased"' in retention_text, "hard erase participates in canonical journal")
check("HARD-ERASE-OP-RECEIPT-MONGO", "self._operations.insert_one" in mongo_text and "hard_erase_terminal_receipt" in mongo_text, "hard erase persists/reconciles immutable operation receipt")
check("HARD-ERASE-NO-TTL", "ttl" not in retention_text.lower(), "hard erase plan does not use TTL semantics")

# 6. External retention policy boundary remains unresolved and fail-closed.
auth04 = (ROOT / "build_state" / "SEMANTIC_AUTHORITY_BINDING_STATE04.yaml").read_text(encoding="utf-8")
contract04 = (ROOT / "build_state" / "STATE-04_BUILD_CONTRACT.yaml").read_text(encoding="utf-8")
check("AUTHORITY-REVISION", AUTH_REV in auth04, f"STATE-04 bound to .github@{AUTH_REV}")
check("AUTHORITY-RETENTION-UNKNOWN", "RETENTION_EXECUTION_POLICY_INTERFACE" in auth04 and "unresolved" in auth04.lower(), "external retention decision interface remains explicit unresolved authority")
check("RETENTION-EXECUTOR-NOT-ACTIVATED", "class RetentionExecutor" not in "\n".join(p.read_text(encoding="utf-8") for p in SRC.rglob("*.py")), "no invented retention executor or policy engine")
check("RETENTION-PLAN-REQUIRES-AUTH-REF", "authorization_ref" in retention_text and "external retention-policy decision/evidence" in retention_text, "hard erase plan requires external authorization evidence reference")
check("STATE04-CONTRACT-NO-POLICY-INVENTION", "invented_retention_policy" in contract04 or "invent" in contract04.lower(), "build contract forbids inventing external retention policy")

# 7. STATE-04 invariants are committed.
invariants_text = (ROOT / "invariants.yaml").read_text(encoding="utf-8")
for invariant in [
    "STATE-LIFECYCLE-001",
    "STATE-RESTORE-001",
    "STATE-ERASE-001",
    "STATE-RETENTION-001",
    "STATE-RETENTION-002",
    "STATE-REV-001",
    "STATE-FENCE-001",
    "STATE-IDEMP-001",
]:
    check(f"INVARIANT-{invariant}", invariant in invariants_text, "required lifecycle/retention invariant preserved")

# 8. Existing STATE-03 recovery contract remains intact.
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
check("NO-CHANGE-STREAMS", ".watch(" not in "\n".join(p.read_text(encoding="utf-8") for p in SRC.rglob("*.py")), "no Change Streams dependency introduced")

# 9. Provider/public dependency boundaries.
public_src = "\n".join((SRC / name).read_text(encoding="utf-8") for name in ["models.py", "ports.py", "service.py", "client.py", "lifecycle.py", "retention.py"])
check("PUBLIC-NO-MONGO", "pymongo" not in public_src.lower() and "bson" not in public_src.lower(), "domain/public layers contain no Mongo/BSON dependency")
check("NO-DIRECT-PEER-HTTP", "httpx" not in public_src and "requests." not in public_src, "State domain/client introduces no direct peer HTTP")

# 10. Source/test syntax compilation.
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
    "unit": "STATE-04_RETENTION_LIFECYCLE_MECHANICS",
    "authority_revision": AUTH_REV,
    "pass": sum(item["status"] == "PASS" for item in checks),
    "fail": len(failed),
    "blocked": sum(item["status"] == "BLOCKED" for item in checks),
    "checks": checks,
}
print(json.dumps(summary, indent=2))
raise SystemExit(1 if failed else 0)
