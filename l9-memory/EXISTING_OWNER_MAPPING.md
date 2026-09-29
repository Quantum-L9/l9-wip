# Existing memory owner mapping

| Proposed Gate capability | Existing semantic owner to bind | Required proof |
|---|---|---|
| memory.write | MemorySDK.write / MemoryService.write | Principal, namespace, operation identity and receipt parity |
| memory.ingest | GeneratedDataService.ingest_governed_candidate through public facade | Preserve candidate evidence/consent/scope and actual admission status |
| memory.search | Public search / RetrievalPlanner | Required selectors, canonical hydration and strategy failure accounting |
| memory.hydrate | Public hydrate / ContextBudgetAllocator | Bound budget and complete/partial/failed output |
| memory.close | Existing close operation, if retained for legacy clients | Do not repurpose as AgentOS Work Item checkpoint |
| memory.phase-lock | Existing phase-lock/verification operation | Snapshot binding, expiry and conflict semantics |
| memory.delete | Verified deletion | Immediate visibility block plus required projection erasure receipts |
| memory.rebuild-projection | Existing rebuild/outbox owner | No external effect replay or resurrection of deleted records |

Exact current public method signatures are a baseline gate; the table is a semantic mapping, not a claim that all proposed Gate action names exist. The wrapper cannot flatten lifecycle semantics into generic CRUD.

`projections/contracts.py`, `compiler.py`, `render.py` and facts-v8 define deterministic projection/embedding identities. The inspected ADR-063 explicitly limits that compiler phase: its presence does not prove runtime multi-target fan-out or versioned index promotion is wired. Keep current scalar provider behavior until separately proved. Do not describe the example model revision string as a real deployed immutable model pin.
