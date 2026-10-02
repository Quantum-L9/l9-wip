# ADR-012: Durable terminal operation outcomes

Status: Accepted
Date: 2026-09-27

## Decision

Every admitted mutation OperationKey has at most one immutable terminal receipt. `committed`, `conflict`, and `refused` are terminal receipt states.

Expected logical mutation negatives are represented as canonical receipts. For state-dependent negatives, the authoritative observation and receipt insertion share the transaction boundary. Exact retries return the exact stored receipt and never re-evaluate changed world state. A changed-world retry requires a new `operation_id`.

`IDEMPOTENCY_COLLISION` is not persisted as a second receipt because the OperationKey is already owned by different semantics. It is surfaced canonically as `StateProblem(retry_class=no)`.

## Consequences

- Gate receives canonical State outcomes rather than generic failures for expected conflicts/refusals.
- Operation reconciliation works identically for successful and negative terminal outcomes.
- Operation identity is an attempt identity, not an open-ended intention.
