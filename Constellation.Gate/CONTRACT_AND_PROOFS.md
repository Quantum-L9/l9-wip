# Constellation.Gate: behavioral delta

Admit and route the six node action families while enforcing distinct authenticated consumer/node roles and unique semantic ownership.

## Required proof obligations
1. Every proposed action resolves to exactly one owner.
2. Unknown action differs from temporarily unavailable owner.
3. Unauthorized client cannot become node or receive worker dispatch.
4. Node -> Gate -> node preserves one deadline and ancestry.
5. Optional callbacks/provider input cannot impersonate node work.

## Cross-owner rule
A missing guarantee becomes a scoped upstream contract change with negative tests. It does not become a consumer-specific bridge, duplicated state owner or unchecked fallback. Test the actual installed package and Gate boundary where relevant, not just source imports.

## Evidence and release
Record tested base/head, dependency versions, schema digests, actual commands and outputs, refusal cases and explicit skipped/blocked checks. A source inspection finding is not a deployed-system claim.
