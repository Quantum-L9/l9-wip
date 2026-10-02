# ADR-011: Gate-bound operation execution budget

Status: Accepted
Date: 2026-09-27

## Decision

Gate `TransportPacket.header.timeout_ms` is the sole trusted request-budget authority. The State binding converts it into a provider-neutral monotonic `ExecutionBudget`. State may reserve budget for reconciliation and return, but may never extend the Gate budget.

Provider retry loops must be explicit and budget-aware. MongoDB `with_transaction()` is forbidden. `TransientTransactionError` may retry the whole transaction only before an ambiguous commit and while mutation budget remains. Commit timeout or `UnknownTransactionCommitResult` enters reconciliation-only mode.

MongoDB `$$NOW` remains the authority for lease time and claim expiry. `ExecutionBudget` never participates in lease semantics.

## Consequences

- Request deadline authority stays at Gate.
- Provider retry policy cannot silently outlive the transport budget.
- Ambiguous commit cannot trigger blind semantic replay.
- Runtime budget policy remains private and injectable; it is not a public State protocol field.
