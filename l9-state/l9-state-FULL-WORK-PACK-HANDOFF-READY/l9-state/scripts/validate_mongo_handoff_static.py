from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MONGO = (ROOT / "src/l9_state/adapters/mongodb.py").read_text()
CONTRACT = (ROOT / "src/l9_state/adapters/mongodb_contract.py").read_text()
DOC = (ROOT / "docs/MONGODB_RUNTIME.md").read_text()
checks: list[dict[str, str]] = []

def check(cid: str, ok: bool, detail: str) -> None:
    checks.append({"id": cid, "status": "PASS" if ok else "FAIL", "detail": detail})

check("MONGO-NO-WITH-TRANSACTION", "with_transaction" not in MONGO, "State owns transaction retry/ambiguity policy")
check("MONGO-SNAPSHOT-READ", 'ReadConcern("snapshot")' in MONGO, "snapshot read concern configured")
check("MONGO-MAJORITY-WRITE", 'WriteConcern("majority")' in MONGO, "majority write concern configured")
check("MONGO-PRIMARY-READ", "ReadPreference.PRIMARY" in MONGO, "primary read preference configured")
check("MONGO-BUDGETED-COMMIT", "max_commit_time_ms=max_commit_time_ms" in MONGO and "budget.mutation_remaining_ms()" in MONGO, "commit bounded by ExecutionBudget")
check("MONGO-AMBIGUOUS-RECONCILE", 'UnknownTransactionCommitResult' in MONGO and "_reconcile_after_commit" in MONGO, "ambiguous commit enters receipt reconciliation")
check("MONGO-TIMEOUT-RECONCILE", "except TimeoutError as exc:" in MONGO and "return await self._reconcile_after_commit(" in MONGO, "client commit timeout reconciles instead of replaying semantics")
check("MONGO-TRANSIENT-BOUNDED-RETRY", "_is_transient_transaction" in MONGO and "budget.can_start_mutation()" in MONGO, "transient whole-transaction retry is budget bounded")
check("MONGO-SERVER-TIME", '"$$NOW"' in CONTRACT, "claim predicates and pipelines use Mongo server time")
check("MONGO-NO-TTL-AUTHORITY", "TTL" not in CONTRACT and "TTL cleanup is not used as authority" in DOC, "claim/lifecycle truth does not depend on TTL indexes")
check("MONGO-OP-UNIQUE", '"uq_state_operation"' in CONTRACT, "OperationKey uniqueness index declared")
check("MONGO-REV-UNIQUE", '"uq_state_revision"' in CONTRACT, "revision uniqueness index declared")
check("MONGO-JOURNAL-UNIQUE", '"uq_scope_journal_seq"' in CONTRACT, "scope journal sequence uniqueness declared")
check("MONGO-CLAIM-UNIQUE", '"uq_state_claim_lineage"' in CONTRACT, "one claim lineage document per StateKey")
he = MONGO[MONGO.index("    async def hard_erase("):MONGO.index("    async def claim(", MONGO.index("    async def hard_erase("))]
check("MONGO-ERASE-DEDICATED-FENCE", "_guard_hard_erase_claim" in he and "holder_ref=" not in he, "hard erase uses claim/fence coordination without holder authorization")
check("MONGO-ERASE-SCRUB", "self._revisions.update_many" in he and '{"$set": {"payload": None}}' in he, "hard erase scrubs retained revision payloads")
check("MONGO-ERASE-DEACTIVATE", '"active": False' in he and '"released_at": "$$NOW"' in he, "hard erase deactivates claim while preserving lineage")
check("MONGO-ERASE-EVENT", "self._events.insert_one" in he and "_next_journal_seq" in he, "hard erase appends canonical event in transaction callback")
check("MONGO-ERASE-RECEIPT", "self._operations.insert_one" in he, "hard erase persists terminal OperationKey receipt in transaction callback")
check("MONGO-ERASE-REPLAY", "_resolve_existing" in he and "HardEraseReceipt" in he, "exact hard-erase retry resolves immutable stored receipt")

passed = sum(c["status"] == "PASS" for c in checks)
failed = len(checks) - passed
print(json.dumps({"schema":"l9.state.mongo-handoff-static/v1","pass":passed,"fail":failed,"checks":checks}, indent=2))
raise SystemExit(1 if failed else 0)
