# Cursor-Governance: scoped convergence workstream

**Intended repository:** `Quantum-L9/Cursor-Governance`. This is not authorization for unrestricted repository changes. The exact current base, open PRs and path inventory must be revalidated before mutation.

## Goal
Evict generic runtime implementations and retain coding-host governance, universal-profile assets and thin host bindings only.

## Included changes
- Map generic generated-data ingestion and delivery to l9-ingest; preserve host acceptance as a source trust boundary.
- Move generic context fulfillment to l9-context and memory semantics to the existing memory owner/wrapper.
- Extract generic autonomy evaluator/policy grammar to AgentOS-owned reusable code; express coding policy as profile content.
- Keep host event capture, host truth acceptance, editing rules and provider translation thin.
- Update generated host bindings through their existing generators; remove imports/dead shims only after replacement receipts.

## Excluded
- Bulk move of all autonomy/ without ownership analysis
- Stealing Program Execution controller, scheduler or task-state authority
- Restoring retired direct provider clients
- Making Cursor the mandatory entry point for constellation memory
- Leaving a compatibility shim that still owns generic policy or persistence

## Build relation
This repo retains its existing semantic ownership. It is not cloned into AgentOS. Each required delta is a separate PR unit in execution_contract.yaml. If the required seam already conforms at the current head, record a no-change proof rather than editing it to match an old plan.


## v1.1 cross-repository integration
This scope participates in the Communication/Formal Reasoning extension. Its exact added work is in `execution_contract.yaml` and `ROADMAP.md`; generic ownership remains unchanged. Refer to `../../02_architecture/COMMUNICATION_REASONING_INTEGRATION.md`. A new upstream consumer does not authorize importing another node's implementation or moving its policy into Cursor-Governance.
