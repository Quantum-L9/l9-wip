# L9-Ops-MCP: scoped convergence workstream

**Intended repository:** `Quantum-L9/L9-Ops-MCP`. This is not authorization for unrestricted repository changes. The exact current base, open PRs and path inventory must be revalidated before mutation.

## Goal
Be one governed source and example consumer, not a universal context/memory subsystem.

## Included changes
- Expose/retain authored artifact identities and exact source authority without moving them into a semantic database.
- Replace generic memory access with owner capabilities through Gate.
- Replace generic context assembly with Context capability consumption.
- Retain deterministic source-specific kernel authority only where it is the current canonical owner; reconcile overlap with cognitive-runtime explicitly.
- Retire any locally defined packet shape used as an alternate L9 wire format.

## Excluded
- Direct Graphiti memory admission
- Ops-only universal Context API
- Copied authority schemas promoted from retrieval
- A per-source registry becoming a second Gate router

## Build relation
This repo retains its existing semantic ownership. It is not cloned into AgentOS. Each required delta is a separate PR unit in execution_contract.yaml. If the required seam already conforms at the current head, record a no-change proof rather than editing it to match an old plan.
