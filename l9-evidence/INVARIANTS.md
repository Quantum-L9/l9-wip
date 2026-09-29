# l9-evidence invariant enforcement

Local machine-readable owner: `invariants.yaml`. Global index points here and does not replace this owner. Imported routing/security invariants keep their original owners.

| ID | Invariant | Required negative proof |
| --- | --- | --- |
| L9-012 | Evidence/projections do not replace source systems or become universal operational truth. | Retrieved source projection cannot satisfy a live approval or business-state requirement. |
| L9-025 | Privacy erasure covers owned raw evidence, derived text, vectors, caches and retrieval visibility with receipts. | Deleted evidence is not recreated by replay or reachable through a stale cached context. |

## Always preserve
One canonical transport; Gate-only inter-node requests; authenticated scope; no provider leakage; no claim of persistence, projection or execution without an owner receipt. Profile data is untrusted until compiled and admitted, and its authorization requests never outrank runtime grants.

## CI enforcement
Add architecture import/egress guards, payload schema tests, failed-path tests and explicit owner references. Test adapters use the same conformance surface as production. A test that only checks doc strings or fixture counts is not proof of runtime enforcement.
