# l9-memory invariant enforcement

Local machine-readable owner: `invariants.yaml`. Global index points here and does not replace this owner. Imported routing/security invariants keep their original owners.

| ID | Invariant | Required negative proof |
| --- | --- | --- |
| L9-011 | Only the existing MemoryService owns canonical memory admission, lifecycle and persistence. | No AgentOS, Context, Ingest or Evidence path writes memory stores/providers. |

## Always preserve
One canonical transport; Gate-only inter-node requests; authenticated scope; no provider leakage; no claim of persistence, projection or execution without an owner receipt. Profile data is untrusted until compiled and admitted, and its authorization requests never outrank runtime grants.

## CI enforcement
Add architecture import/egress guards, payload schema tests, failed-path tests and explicit owner references. Test adapters use the same conformance surface as production. A test that only checks doc strings or fixture counts is not proof of runtime enforcement.
