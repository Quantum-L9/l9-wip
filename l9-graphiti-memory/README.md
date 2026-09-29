# l9-graphiti-memory: scoped convergence workstream

**Intended repository:** `Quantum-L9/l9-graphiti-memory`. This is not authorization for unrestricted repository changes. The exact current base, open PRs and path inventory must be revalidated before mutation.

## Goal
Remain the single memory domain owner and expose the smallest verified public-contract additions needed by the new node wrapper.

## Included changes
- Verify public facade/principal mapping for node-bound callers; add only missing public capability parity.
- Preserve exact scope, consent, source and receipt semantics through wrapper calls.
- Keep canonical store and optional projection ownership unchanged.
- Expose necessary operation status/selector metadata rather than forcing a wrapper to inspect internal tables.
- Add cross-repo fixtures asserting Gate-wrapper calls equal public SDK behavior.

## Excluded
- Replacing MemoryService
- Canonical memory moved to Evidence or State
- A new provider-managed embedding requirement on core writes
- Agent-specific hardcoded namespaces
- Promising compiler-only projection machinery is an active multi-target runtime

## Build relation
This repo retains its existing semantic ownership. It is not cloned into AgentOS. Each required delta is a separate PR unit in execution_contract.yaml. If the required seam already conforms at the current head, record a no-change proof rather than editing it to match an old plan.
