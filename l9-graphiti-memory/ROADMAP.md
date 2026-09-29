# Repository roadmap

Planned implementation only. PRs remain scoped to this repository; dependencies are evidence gates, not permission to edit another owner.

## MEMCORE-01 - Probe existing public facade and node principal mapping

Prerequisites: BASE-01, AG-01

1. Inspect current MemorySDK/MemoryService/generated-data public contracts.
2. Check signed/authenticated node delegated identity cannot default to all-powerful local principal.
3. Verify response selectors, idempotency, consent and deletion obligations.
4. Record no-change disposition when facade already suffices; do not manufacture changes.

**Acceptance:** Every wrapper operation has an exact current public owner target. Any missing operation becomes narrow owner change, not wrapper internals access.

**Required negatives:** Missing principal claims never become wildcard namespace. Projection down remains explicit and cannot redefine canonical write success.

## MEMCORE-02 - Close only demonstrated public contract gaps

Prerequisites: MEMCORE-01

1. Implement only verified gaps from prior unit.
2. Preserve canonical lifecycle/outbox identity and source taxonomy.
3. Publish installed model/schema parity and typed failures.
4. Version incompatible changes explicitly.

**Acceptance:** No duplicate RecordStore/lifecycle service outside owner. Admitted write, duplicate, quarantine, refusal and projection status remain distinct.

**Required negatives:** Cross-scope candidate rejected. Deletion incomplete remains incomplete under projection outage.
