# l9-state

Provider-neutral durable state authority for L9.

This checkout is a **local STAGING implementation** bound to `l9-state-final-dev-pack-v2.0.0`, the user-approved STATE-02A operation-execution architecture delta, and the settled L9 semantic foundation at `Quantum-L9/.github@08912f391c0a6672957f40cbd9b0db285f82ed86`.

The upstream foundation classifies `l9.state` as a **Node / authoritative-state archetype** and preserves the exact architecture this implementation follows: immutable revisioned state, Gate-mediated interaction, provider-neutral persistence, and State-owned journal/receipt semantics. Node birth/admission has not yet been performed, but by explicit user direction it is **not a blocker to continued staging implementation**. No publication, merge, deployment, or release is represented by this checkpoint.

## Implemented build slices

### STATE-01 core vertical slice

- `state.create`
- `state.get`
- `state.transition`
- `state.operation.inspect`
- RFC 8785 JCS + SHA-256 semantic digests
- exact operation identity/reconciliation semantics
- immutable schema binding
- configured `ContractCatalogPort`
- Gate handlers and Gate-only typed client

### STATE-02 Mongo atomicity + claims/fencing

- private PyMongo Async `MongoStateStore`
- required seven-collection layout and unique indexes
- primary + snapshot + majority transaction configuration
- immutable revisions and current projection
- scope-local monotonic journal sequence allocation
- transaction-coupled state/event/operation receipt writes
- persistent claim/fence lineage
- `state.claim`, `state.renew`, and `state.release`
- Mongo `$$NOW` lease authority
- claim-lineage write contention between state transitions and claim mutations

### STATE-02A operation execution contract

- Gate `timeout_ms` becomes provider-neutral `ExecutionBudget`
- explicit budgeted Mongo transactions and bounded reconciliation replace `with_transaction()`
- `committed`, `conflict`, and `refused` are immutable terminal OperationKey outcomes
- changed-world retry requires a new operation identity
- `IDEMPOTENCY_COLLISION` is canonical non-durable `StateProblem`
- retry safety remains separate from workflow recovery guidance

### STATE-03 journal + cold resume

- `state.list`
- `state.events`
- `state.ack`
- `state.history`
- State-issued HMAC-authenticated provider-independent cursors
- compact cursor bindings that remain within the public 512-character bound
- tenant/scope/consumer/purpose/filter cursor isolation
- first-page journal high-water capture for cold resume
- seek-based current-StateRef pagination without a second directory store
- successful event pages always return an ackable cursor, including empty/final pages
- retention-gap detection returns `resync_required`
- durable monotonic consumer checkpoints with atomic ack operation receipts
- object history reports `complete`, `bounded`, or `history_unavailable` without overstating retained coverage
- pull journal correctness only; no Change Streams dependency

See `docs/CURSOR_RUNTIME.md` for the cursor/runtime contract.

### STATE-04 retention + lifecycle mechanics

- `state.tombstone`
- `state.restore`
- tombstone current-read suppression while exact retained revision reads remain available
- retained prior-revision restore into a new active revision
- terminal `erased` lifecycle and permanent object-ID non-reuse
- private `StateStorePort.hard_erase` mechanics with a private durable receipt family
- hard erase scrubs retained payload bytes while preserving object identity, revision/fence lineage, journal metadata, and OperationKey replay safety
- active-claim hard erase requires the exact current claim/fence but never treats claim-holder identity as retention authority
- no public hard-delete/hard-erase Gate action
- external retention-policy decision interface remains unresolved; no RetentionExecutor or autonomous retention scheduler is active

See `docs/RETENTION_LIFECYCLE.md` for the lifecycle/retention boundary.

## Dependency boundary

The base package does **not** depend on a MongoDB driver. Client/contract consumers install the base package only. Mongo server functionality is selected explicitly:

```bash
pip install 'l9-state[server]'
```

The current server adapter is bound to `pymongo==4.18.2`. `rfc8785==0.1.4` remains a normal base runtime dependency because canonical State/request digests require it.

## Validation status

Current-container evidence is intentionally limited to checks this environment can actually prove: source/test syntax compilation, public schema inventory/parsing, deterministic static wiring checks, dependency/provider boundary checks, cursor-bound checks, invariant/authority-coordinate consistency, and package integrity.

Full dependency-backed pytest, ruff, mypy, installed-package parity, real Gate round-trip, and live Mongo replica-set/failover/ambiguity testing remain external validation debt unless separately evidenced. They are not represented as PASS.

See `build_state/RESUME.yaml`, `build_state/SEMANTIC_AUTHORITY_BINDING_STATE04.yaml`, and the STATE-04 execution receipt for current checkpoint truth.

Combined architecture/code review of STATE-01 through STATE-04 remains deferred by user direction.
