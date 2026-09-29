# Repository roadmap

Planned implementation only. PRs remain scoped to this repository; dependencies are evidence gates, not permission to edit another owner.

## EVID-01 - Birth source/evidence retention contract

Prerequisites: AG-01, SDK-02, GATE-01

1. Finalize evidence identity, exact locator and artifact provenance.
2. Separate source-owned truth from retained copies and view indexes.
3. Implement staged blob finalize with integrity and quarantine on partial commit.
4. Authenticate every resolve/get independent of reference possession.

**Acceptance:** Accepted evidence resolves exact authorized bytes or a typed unavailable state. Evidence append does not authorize actions.

**Required negatives:** Mismatched bytes/digest rejected. Bearer-like source URL cannot bypass policy or SSRF controls.

## EVID-02 - Implement Mongo metadata and versioned search views

Prerequisites: EVID-01

1. Pin storage/search product versions and approved deployment compatibility.
2. Choose exact owner/executor for each view; accept deterministic representation from Ingest.
3. Bind model revision, dimension, distance, normalization, scope and transform digest.
4. Enforce filter-before-ranking and canonical evidence lifecycle recheck.

**Acceptance:** Changing model/view contract builds a new view identity with controlled cutover. Raw observations cannot opt themselves into embedding.

**Required negatives:** Wrong embedding space/query pair is refused. Same text across private scopes cannot share an unauthorized cache entry.

## EVID-03 - Prove erasure, invalidation and rebuild behavior

Prerequisites: EVID-02, GATE-02

1. Enumerate evidence derivatives and required erasure targets.
2. Make replay consult tombstone/retention state before materialization.
3. Invalidate searchable copies without claiming upstream domain deletion.
4. Demonstrate cache and source-version invalidation to Context.

**Acceptance:** Erased evidence cannot reappear by source replay or stale view switch. Legal/policy hold is explicit state, not silent success.

**Required negatives:** Simulated failed vector deletion leaves incomplete erasure receipt. Denied object remains inaccessible via context diagnostics.

## EVID-04 - Retain and revoke communication/formal derivation artifacts

Prerequisites: EVID-03, EXT-01

1. Admit receipt, source-coordinate and bounded witness/core artifact kinds without new truth ownership.
2. Enforce artifact parent/source lineage and current rights.
3. Propagate revocation to derived copies and cache references.
4. Test optional no-raw-retention behavior and retained replay limitations.

**Acceptance:** Media and proof artifacts share the existing Evidence authority. Deletion includes derived excerpts/witnesses when policy requires it.

**Required negatives:** Receipt hash alone cannot restore revoked content. Provider retention disabled cannot be bypassed via an Evidence copy.
