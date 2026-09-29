# Repository roadmap

Planned implementation only. PRs remain scoped to this repository; dependencies are evidence gates, not permission to edit another owner.

## ING-01 - Birth bounded source workflow and admission-neutral profiles

Prerequisites: AG-01, STATE-01, EVID-01, MEM-01, GATE-01

1. Reuse donor logic only after source/host assumptions are removed.
2. Validate artifact/ref/digest/purpose before parsing.
3. Apply byte, decompression, page, runtime and redaction bounds.
4. Keep job state behind State and source evidence behind Evidence.

**Acceptance:** No local canonical job database or direct memory provider access. Profile forbids inappropriate source retention/embedding before model calls.

**Required negatives:** Archive traversal/zip bomb refused. Malformed source cannot be labeled successfully captured.

## ING-02 - Implement deterministic transforms and source profiles

Prerequisites: ING-01, STATE-03, EVID-02

1. Start with structured source then document/repository evidence; add media references through same source contract.
2. Use LlamaIndex only behind transformation port; disable direct remote-node storage sinks.
3. Distinguish transform evidence from assertion truth; reuse memory owner extraction when target semantics belong there.
4. Generate versioned representation/projection intents with exact source locators.

**Acceptance:** Same source/profile/transform identity produces stable outputs. No repeated embedding of unchanged view contract.

**Required negatives:** Unsupported modality is explicit not silently textualized. No fabricated character/page/line coordinates.

## ING-03 - Deliver per-destination intents and close replay lifecycle

Prerequisites: ING-02, MEM-02, EVID-03, GATE-02

1. Commit candidate delivery intents before calls using State-owned durable mechanics.
2. Assign stable per-destination operation identities.
3. Reconcile unknown owner response before retry and retain rejected/quarantined dispositions.
4. Replay only approved projections, never operational effects.

**Acceptance:** One successful destination is not replayed because another failed. Complete requires every required destination settled with authoritative receipt.

**Required negatives:** Timeout after memory admission does not create a duplicate fact under a new key. Privacy-erased source cannot resurrect through replay.
