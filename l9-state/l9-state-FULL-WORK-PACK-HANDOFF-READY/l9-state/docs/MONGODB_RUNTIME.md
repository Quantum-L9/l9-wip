# MongoDB runtime contract

## Adapter and installation boundary

`l9_state.adapters.mongodb.MongoStateStore` is the first private `StateStorePort` provider.

Driver binding for this checkpoint: `pymongo==4.18.2`, using `AsyncMongoClient`. Motor is not used.

Mongo is deliberately **not** a base client dependency. Select server functionality explicitly:

```bash
pip install 'l9-state[server]'
```

Importing `l9_state`, its public models, or `StateClient` must not import PyMongo. Provider syntax remains under `src/l9_state/adapters/`.

## Transaction law

State mutations use the PyMongo core transaction API with:

- primary read preference
- snapshot transaction read concern
- majority transaction write concern
- an explicit `max_commit_time_ms` bounded by the remaining State mutation budget

MongoDB convenience `with_transaction()` is forbidden. State owns the retry and ambiguity policy because provider-managed retry horizons may outlive the trusted Gate request budget.

A `TransientTransactionError` before an ambiguous commit may retry the whole transaction while `ExecutionBudget` still allows a new mutation attempt. A commit timeout or `UnknownTransactionCommitResult` moves directly to reconciliation-only mode. No semantic callback may be replayed once commit may have occurred.

## Trusted execution budget

At validated Gate ingress, `TransportPacket.header.timeout_ms` becomes a provider-neutral `ExecutionBudget`. State may reserve part of that budget for authoritative reconciliation and response return, but may never extend it.

The monotonic clock used by `ExecutionBudget` measures only local budget consumption. It is never lease authority. MongoDB `$$NOW` remains the authority for claim acquisition, renewal, expiry, release, and transition fence predicates.

Budget policy is a private runtime injection through the Gate binding. It is not a public State protocol field.

## Coupled writes

A create transaction couples:

1. scope journal sequence allocation
2. immutable revision insert
3. current projection insert
4. persistent claim-lineage initialization
5. canonical event insert
6. terminal operation receipt insert

A transition transaction couples:

1. revision/digest/schema verification
2. server-time claim/fence guard and claim-lineage write
3. current projection CAS update
4. scope journal sequence allocation
5. immutable revision insert
6. canonical event insert
7. terminal operation receipt insert

A state-dependent `conflict` or `refused` outcome commits no state revision/event mutation and instead inserts the immutable terminal operation receipt inside the same transaction that observed the conflicting/refusing facts.

Claim acquire/renew/release couple the claim-lineage effect, or the authoritative logical negative observation, with the terminal claim receipt under the same OperationKey transaction.

Because claim operations and transitions write the same claim-lineage document, Mongo transaction conflict detection remains the intended concurrency seam preventing claim acquisition/renewal/release from silently crossing a concurrent state mutation.

## Claim time authority

Acquire, renew, release, and transition fence predicates use MongoDB `$$NOW` in provider-side expressions/pipelines. TTL cleanup is not used as authority and claim-lineage documents are not deleted on expiry or release.

## Durable terminal outcomes

For an admitted mutation, the terminal OperationKey result is one immutable receipt:

- `committed`
- `conflict`
- `refused`

An exact retry returns the stored receipt unchanged. Changed-world retry requires a new operation ID. `IDEMPOTENCY_COLLISION` remains non-durable because the requested OperationKey is already owned by different action/request semantics.

`StateProblem` is never persisted as an operation receipt.

## Ambiguous commit reconciliation

Once commit may have occurred, the adapter performs only majority-read OperationKey reconciliation within the reserved reconciliation budget. If the exact receipt is found, it is returned. If the budget expires without authoritative evidence, the adapter raises stable `OUTCOME_UNKNOWN`, which the service maps to `StateProblem(retry_class=inspect_then_same_operation)`.

A definite pre-commit budget exhaustion becomes `DEADLINE_EXCEEDED` with `retry_class=same_operation`. An unknown result is never persisted as authoritative truth.

## External validation still required

Before merge/release readiness, run against a real transaction-capable replica set and prove:

- index creation and uniqueness
- snapshot plus majority transaction behavior
- simultaneous CAS writers
- simultaneous claim acquisition
- server-time lease behavior under application clock skew
- restart/failover behavior
- pre-commit transient whole-transaction retry within budget
- commit timeout and `UnknownTransactionCommitResult` reconciliation without semantic replay
- exact terminal conflict/refusal receipt durability across changed world state
- no duplicate revision, event, claim effect, or receipt under retry

Also run the admitted repository toolchain for ruff, mypy, the complete pytest suite, Gate installed-package round trips, and base/server installed-package isolation.

These are external validation obligations. They are release-blocking evidence obligations but are not represented as local PASS results.
