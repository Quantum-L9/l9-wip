# l9-context invariant enforcement

Local machine-readable owner: `invariants.yaml`. Global index points here and does not replace this owner. Imported routing/security invariants keep their original owners.

| ID | Invariant | Required negative proof |
| --- | --- | --- |
| L9-013 | Mandatory reads, coverage, freshness and authority bounds are deterministic; missing data is explicit. | Disable a required source and fail the requirement without converting it to optional or zero hits. |
| L9-018 | A context bundle is an evidence view with source coordinates, not a globally atomic snapshot or permission. | Concurrent source change produces explicit mixed coordinates, stale/refresh status or bounded failure. |
| L9-022 | Circular reuse requires new evidence/revision, durable dedupe and bounded continuation budgets. | An unchanged refresh cannot create another ingest/refresh cascade. |
| L9-028 | Existing cognitive context-demand/compilation semantics are reused, not silently copied or redefined. | Expected context-plan identity is verified through owner-native contracts. |

## Always preserve
One canonical transport; Gate-only inter-node requests; authenticated scope; no provider leakage; no claim of persistence, projection or execution without an owner receipt. Profile data is untrusted until compiled and admitted, and its authorization requests never outrank runtime grants.

## CI enforcement
Add architecture import/egress guards, payload schema tests, failed-path tests and explicit owner references. Test adapters use the same conformance surface as production. A test that only checks doc strings or fixture counts is not proof of runtime enforcement.
