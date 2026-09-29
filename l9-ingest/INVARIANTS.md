# l9-ingest invariant enforcement

Local machine-readable owner: `invariants.yaml`. Global index points here and does not replace this owner. Imported routing/security invariants keep their original owners.

| ID | Invariant | Required negative proof |
| --- | --- | --- |
| L9-014 | Transformation produces candidates and source-processing receipts, never downstream admission claims. | Mixed destination success preserves separate results and retries only unresolved deliveries. |
| L9-019 | Sensitive source processing is purpose-limited; preserved source bytes never imply permission to embed or memorize. | Profile-forbidden raw body and transcript are rejected before external model or index use. |
| L9-029 | Embedding identity binds representation, model revision, dimensions, similarity space and privacy scope. | Mismatched query/index model or scope is rejected; unchanged content is not re-embedded. |

## Always preserve
One canonical transport; Gate-only inter-node requests; authenticated scope; no provider leakage; no claim of persistence, projection or execution without an owner receipt. Profile data is untrusted until compiled and admitted, and its authorization requests never outrank runtime grants.

## CI enforcement
Add architecture import/egress guards, payload schema tests, failed-path tests and explicit owner references. Test adapters use the same conformance surface as production. A test that only checks doc strings or fixture counts is not proof of runtime enforcement.
