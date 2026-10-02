from __future__ import annotations

import ast
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
checks: list[dict[str, str]] = []

def check(cid: str, ok: bool, detail: str) -> None:
    checks.append({"id": cid, "status": "PASS" if ok else "FAIL", "detail": detail})

def method_args(path: Path, cls: str, method: str) -> list[str]:
    tree = ast.parse(path.read_text())
    for node in tree.body:
        if isinstance(node, ast.ClassDef) and node.name == cls:
            for item in node.body:
                if isinstance(item, (ast.FunctionDef, ast.AsyncFunctionDef)) and item.name == method:
                    return [a.arg for a in item.args.args + item.args.kwonlyargs]
    raise RuntimeError(f"{cls}.{method} not found")

ports = (ROOT / "src/l9_state/ports.py").read_text()
retention = (ROOT / "src/l9_state/retention.py").read_text()
memory = (ROOT / "src/l9_state/adapters/memory.py").read_text()
mongo = (ROOT / "src/l9_state/adapters/mongodb.py").read_text()
mongo_contract = (ROOT / "src/l9_state/adapters/mongodb_contract.py").read_text()
tests = (ROOT / "tests/test_lifecycle.py").read_text()

for cls, path in [
    ("StateStorePort", ROOT / "src/l9_state/ports.py"),
    ("InProcessStateStore", ROOT / "src/l9_state/adapters/memory.py"),
    ("MongoStateStore", ROOT / "src/l9_state/adapters/mongodb.py"),
]:
    args = method_args(path, cls, "hard_erase")
    check(f"F001-NO-HOLDER-{cls}", "holder_ref" not in args, f"hard_erase args={args}")
    check(f"F001-FENCE-{cls}", "claim_id" in args and "fencing_token" in args, "claim/fence retained")

check("F001-PLAN-NO-HOLDER", "holder_ref: str" not in retention and "holder_ref=principal_ref" not in retention, "erase plan separates executor principal from claim holder")
check("F001-MEMORY-DEDICATED-GUARD", "def _guard_hard_erase(" in memory and "self._guard_hard_erase(" in memory, "memory uses retention-specific claim guard")
check("F001-MEMORY-NO-HOLDER-CHECK", "claim.holder_ref != holder_ref" not in memory[memory.index("def _guard_hard_erase"):memory.index("def _persist_state_terminal")], "hard-erase guard does not compare holder")
check("F001-MONGO-FENCE-FILTER", "def exact_claim_fence_filter(" in mongo_contract and '"holder_ref"' not in mongo_contract[mongo_contract.index("def exact_claim_fence_filter"):mongo_contract.index("def claimless_transition_guard_filter")], "Mongo erase filter binds claim/fence only")
check("F001-MONGO-DEDICATED-GUARD", "async def _guard_hard_erase_claim(" in mongo and "await self._guard_hard_erase_claim(" in mongo, "Mongo hard erase uses dedicated guard")
check("F001-MONGO-NO-HOLDER-CLASSIFY", "holder_ref=None" in mongo[mongo.index("async def _guard_hard_erase_claim"):mongo.index("def _has_error_label")], "Mongo failure classification suppresses holder ownership check")
check("F001-EXACT-FENCE-TEST", "test_hard_erase_scrubs_payload_preserves_fence_and_makes_identity_terminal" in tests and 'principal_ref="retention-executor"' in tests, "exact fence with different retention principal covered")
check("F001-STALE-FENCE-TEST", "test_hard_erase_rejects_stale_fence_without_requiring_holder_identity" in tests, "stale fence negative covered")
check("F001-CLAIMLESS-ACTIVE-TEST", "test_hard_erase_requires_fence_when_claim_is_active" in tests, "active claim requires fence")
check("F001-CLAIMLESS-RELEASED-TEST", "test_hard_erase_allows_claimless_after_release_and_preserves_fence" in tests, "inactive lineage permits claimless erase")
check("F001-REPLAY-TEST", "assert replayed == erased" in tests, "exact hard-erase OperationKey replay covered")
check("F001-RECEIPT-PROVENANCE", 'assert erased.principal_ref == "retention-executor"' in tests and 'assert erased.authorization_ref == "retention-decision:42"' in tests, "executor and external authorization remain on receipt")
check("F001-PUBLIC-STILL-PRIVATE", 'state.internal.hard_erase' not in (ROOT / "src/l9_state/client.py").read_text() and '@register_handler("state.internal.hard_erase")' not in (ROOT / "src/l9_state/bindings/gate.py").read_text(), "hard erase remains private")

passed=sum(c["status"]=="PASS" for c in checks); failed=len(checks)-passed
result={"schema":"l9.state.validate-f001-static/v1","pass":passed,"fail":failed,"checks":checks}
print(json.dumps(result, indent=2))
raise SystemExit(1 if failed else 0)
