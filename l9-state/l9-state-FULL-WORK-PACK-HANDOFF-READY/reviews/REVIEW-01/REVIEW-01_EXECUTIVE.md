# L9 State REVIEW-01 Combined Architecture + Code Review

## Decision

**REOPEN_REQUIRED**

The approved architecture remains sound. State semantic ownership, Gate routing, provider isolation, revision/CAS/fencing, durable OperationKey outcomes, Mongo transaction structure, journal/cold-resume architecture, and lifecycle/erase mechanics all survive the combined review.

The implementation is **not ready to advance to VALIDATE-01** yet because seven bounded findings remain. Three are high severity and all are repairable without redesigning State.

## Target

- Checkpoint: `l9-state-STATE-04-retention-lifecycle-checkpoint.zip`
- SHA-256: `97dd1300a4749487a7a32e648cc0fd27099223a92beb3336ac6e6efe59ce0755`
- Historical semantic binding: `.github@08912f391c0a6672957f40cbd9b0db285f82ed86`
- Current semantic authority: `.github@7d31438a32bf1ce7783b1b896d359e6eb34063d0`
- State-relevant canonical files: byte-identical across those two revisions

## Governing assessment

The smallest sufficient explanation for the findings is **boundary enforcement lagging behind the core state machine**. The core mechanics are substantially coherent. The defects cluster where trusted transport becomes State authorization/failure semantics and where public contract details meet runtime models/recovery edge cases.

## Findings

1. **GAR-F-001 HIGH - Authorization and receipt-evidence boundary is not implemented.** No ScopeAuthorizationPort or explicit tenant authorization decision is wired; exact retry and operation inspection do not reauthorize; `authorization_ref` is the packet ID rather than authorization evidence.
2. **GAR-F-002 HIGH - Brand-new consumers after journal pruning incorrectly get `resync_required`.** Contract requires starting at earliest retained event when no prior cursor/ack exists.
3. **GAR-F-003 HIGH - Expected State failures can escape the StateProblem boundary.** Missing history, invalid payloads and idempotency mismatches can become Gate-generic errors/client validation failures.
4. **GAR-F-004 MEDIUM - Retry semantics are action-agnostic.** Read infrastructure failures are labeled `same_operation` even though reads have no durable operation identity.
5. **GAR-F-005 MEDIUM - Runtime models are weaker than public schema requiredness.** Seven required fields have runtime defaults.
6. **GAR-F-006 MEDIUM - Gate runtime idempotency precondition is not startup-validated.** Handler defense is present, but deployment config can omit Gate-level enforcement.
7. **GAR-F-007 LOW - Provenance coordinates are stale but compatible.** Rebind successor metadata; do not rewrite historical receipts.

## What does not need redesign

- StateStorePort and Mongo/provider boundary
- RFC8785 digest law
- durable terminal operation receipts
- budgeted transaction / ambiguity reconciliation architecture
- claim/fence lineage
- journal as canonical event/outbox truth
- provider-independent cursors and cold-resume capture model
- tombstone / retained restore / erased terminal mechanics
- private hard erase boundary

## Material Unknowns

- External retention-policy decision interface remains intentionally unbound. This blocks automated RetentionExecutor activation, not State-owned erase mechanics.
- Live Mongo/Gate/package behavior remains external validation debt.
- A formal `evidence.assessment/v1` producer receipt could not be emitted because the evidence-review capability is unavailable in this runtime; direct artifact evidence is preserved instead.

## Next authorized stage

Execute `L9-STATE-REMED-01-COMBINED-REVIEW` exactly as written in `REMEDIATION_CONTRACT.yaml`, then perform a delta review. Do **not** start VALIDATE-01 or ProductTopology compilation until the high findings are closed.
