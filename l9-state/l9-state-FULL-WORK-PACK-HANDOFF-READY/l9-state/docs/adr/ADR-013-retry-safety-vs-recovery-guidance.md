# ADR-013: Retry safety is separate from workflow recovery

Status: Accepted
Date: 2026-09-27

## Decision

The public `StateProblem.retry_class` vocabulary remains:

- `no`
- `same_operation`
- `refresh_then_decide`
- `cold_resync`
- `later`
- `inspect_then_same_operation`

It describes retry safety for non-terminal problems only. Workflow instructions after terminal receipts live in reason-code recovery guidance and require a new operation identity when a new attempt is made.

The prior documentation-only values `after_release_or_expiry`, `reacquire`, `acquire_current_claim`, and `bounded_same_operation` are not retry classes.

## Consequences

- Public schema remains authoritative and unchanged.
- Budget boundedness lives in ExecutionBudget, not error vocabulary.
- Claim recovery guidance does not pollute generic retry semantics.
