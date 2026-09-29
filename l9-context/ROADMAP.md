# Repository roadmap

Planned implementation only. PRs remain scoped to this repository; dependencies are evidence gates, not permission to edit another owner.

## CTX-01 - Birth requirement fulfillment and evidence normalization

Prerequisites: COG-01, STATE-01, EVID-01, MEM-01, GATE-01

1. Compose owner demand contract with approved context-profile requirements.
2. Obtain scope/authenticated source selector constraints before any retrieval.
3. Call State/Evidence/Memory through Gate only and normalize typed evidence.
4. Preserve required/optional failures independently.

**Acceptance:** No copied cognitive compiler or direct provider/store clients. Required coverage cannot be traded away for token score.

**Required negatives:** Unavailable required source yields blocked/partial under explicit policy. High relevance never overrules source authority.

## CTX-02 - Implement bounded fusion, stable bundles and deltas

Prerequisites: CTX-01, STATE-03, EVID-03, MEM-02

1. Budget mandatory context before optional ranking/reranking.
2. Include every source coordinate and observation time; never claim globally atomic source snapshot.
3. Bind caches to scope, purpose, profile, source revisions and authorization generation.
4. Implement exact-base delta and current permission revalidation.

**Acceptance:** Oversized mandatory material blocks instead of dropping obligations. Delta is applicable only to exact authorized base bundle.

**Required negatives:** Wrong base/scope/profile delta rejected. Revoked source grant invalidates cache and explain output.

## CTX-03 - Bound reverse-ingest and execution-refresh loops

Prerequisites: CTX-02, ING-03

1. Emit only scoped allowed missing-source requests with approved ingestion profiles.
2. Track work epoch, causal dedupe, cost/latency/round ceilings.
3. Separate long-lived continuation from transport packet deadline.
4. Prefer no-change delta on unchanged source state.

**Acceptance:** No new source crawl or permission is invented by context gap. Fresh independent source evidence is required for improvement claims.

**Required negatives:** Repeated context output cannot self-corroborate. Context-Ingest feedback terminates under unchanged state.

## CTX-04 - Fulfill exact formal fact demand without top-k substitution

Prerequisites: CTX-02, EXT-01

1. Add owner-native FormalContextFulfillRequest/FactBundle contracts.
2. Probe exact source enumeration/snapshot/coverage contracts.
3. Implement predicate-level coverage and exclusion receipts with source coordinates.
4. Block recursive reasoning-dependent acquisition for the same demand.
5. Close only demonstrated upstream exact-read gaps through separately owned changes.

**Acceptance:** Formal coverage is stronger than ranked retrieval and independently evidenced. No global atomic snapshot is fabricated across owners.

**Required negatives:** Required source cap/denial yields incomplete, not empty. A recursive Context-to-Reasoning dependency is rejected.
