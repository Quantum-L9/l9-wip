# l9-graphiti-memory: behavioral delta

Remain the single memory domain owner and expose the smallest verified public-contract additions needed by the new node wrapper.

## Required proof obligations
1. Canonical write works with optional projection down.
2. Projection hits resolve to allowed canonical records.
3. Consent/refusal/deletion survive wrapper transport unchanged.
4. No second memory lifecycle or shadow storage is introduced.
5. Exact request selector and operation identity receipts round trip.

## Cross-owner rule
A missing guarantee becomes a scoped upstream contract change with negative tests. It does not become a consumer-specific bridge, duplicated state owner or unchecked fallback. Test the actual installed package and Gate boundary where relevant, not just source imports.

## Evidence and release
Record tested base/head, dependency versions, schema digests, actual commands and outputs, refusal cases and explicit skipped/blocked checks. A source inspection finding is not a deployed-system claim.
