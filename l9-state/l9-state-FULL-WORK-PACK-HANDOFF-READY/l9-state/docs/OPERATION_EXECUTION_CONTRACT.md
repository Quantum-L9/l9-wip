# Operation execution contract

This document records the user-approved architecture delta applied after STATE-02 wiring audit findings F-003, F-004, and A-001.

## Authority flow

```text
validated Gate TransportPacket
  -> CallerContext
     -> ExecutionBudget + tenant/principal/authorization/operation identity
        -> StateService
           -> StateStorePort
              -> provider adapter
                 -> immutable OperationKey terminal receipt
```

Gate owns transport and supplies the trusted request budget. State owns State semantics. The provider adapter owns provider mechanics only.

## Execution budget

`TransportPacket.header.timeout_ms` is converted at Gate ingress into provider-neutral `ExecutionBudget` using a monotonic local clock. This clock measures only consumption of the trusted request budget. It is never lease authority.

State may reserve part of the incoming budget for reconciliation and response return. It may never extend the Gate budget. A mutation that cannot begin while preserving the configured reserves terminates as `StateProblem(DEADLINE_EXCEEDED, retry_class=same_operation)` before commit is attempted.

Provider retry behavior is explicit and bounded. Mongo convenience `with_transaction()` is forbidden because State, not the provider helper, owns the request-budget boundary.

## Commit ambiguity

Before commit is attempted, a definitely aborted transient transaction may be retried while mutation budget remains.

Once commit may have occurred, semantic execution stops. State may only reconcile the original OperationKey. If the immutable receipt is found, that exact receipt is returned. If authoritative reconciliation cannot establish the outcome before the reconciliation budget expires, State returns `StateProblem(OUTCOME_UNKNOWN, retry_class=inspect_then_same_operation)` and persists no problem receipt.

## Terminal operation outcomes

After admission, one OperationKey has at most one immutable terminal receipt:

- `committed`
- `conflict`
- `refused`

Expected logical mutation outcomes are receipt values, not generic Gate failures. The observation that causes a state-dependent `conflict` or `refused` receipt and insertion of that receipt share the same State atomicity boundary.

An exact retry of the same OperationKey, action, and canonical request digest returns the exact stored receipt. The world is not re-evaluated. If conditions later change, the caller creates a new operation ID.

`IDEMPOTENCY_COLLISION` is the exception: because the OperationKey is already owned by different semantics, State cannot persist a second authoritative receipt under it. It is returned canonically as a non-durable `StateProblem(retry_class=no)`, not as a generic Gate failure.

## Retry safety versus recovery guidance

`StateProblem.retry_class` answers only what is safe for a non-terminal failure. Its vocabulary remains the six values in the public StateProblem schema.

Terminal receipt reason codes explain why an admitted operation ended. Recovery guidance for those codes describes what a caller may change before creating a new operation. Workflow instructions such as acquiring a new claim or waiting for expiry are not retry classes.
