# l9-state invariant enforcement

Local machine-readable owner: `invariants.yaml`. Global index points here and does not replace this owner. Imported routing/security invariants keep their original owners.

| ID | Invariant | Required negative proof |
| --- | --- | --- |
| L9-008 | A state mutation atomically commits new revision, operation receipt and transition/outbox intent. | Crash at every commit boundary yields all-or-none, never state without transition identity. |
| L9-009 | State has no Work Item domain logic; schemas and fences do not confer action authority. | Generic storage suite passes with commercial, assistance, technical and synthetic payloads. |
| L9-010 | Expired lease holders cannot write or effect stale work; fencing is monotonically checked. | Paused old worker resumes after reassignment and every conditional commit is refused. |

## Always preserve
One canonical transport; Gate-only inter-node requests; authenticated scope; no provider leakage; no claim of persistence, projection or execution without an owner receipt. Profile data is untrusted until compiled and admitted, and its authorization requests never outrank runtime grants.

## CI enforcement
Add architecture import/egress guards, payload schema tests, failed-path tests and explicit owner references. Test adapters use the same conformance surface as production. A test that only checks doc strings or fixture counts is not proof of runtime enforcement.
