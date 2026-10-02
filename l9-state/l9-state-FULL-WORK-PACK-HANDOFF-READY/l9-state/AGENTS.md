# Agent contract

Implementation authority is `l9-state-final-dev-pack-v2.0.0`, augmented only by the user-approved STATE-02A operation-execution architecture delta and the settled organization semantic foundation frozen for this build at `Quantum-L9/.github@08912f391c0a6672957f40cbd9b0db285f82ed86`.

The upstream semantic foundation classifies State as `product.kind=node` with `l9.node-archetype/authoritative-state@1`. Product-specific State meaning remains owned here; upstream patterns constrain architecture without becoming State domain semantics.

Do not expand architecture. Gate_SDK owns transport and request-budget authority. State owns provider-neutral state mechanics, durable OperationKey outcomes, claims/fencing, the canonical pull journal, consumer checkpoints, and bounded reconciliation. MongoDB is a private provider. Mongo `$$NOW` owns lease time. Public cursors are State-issued and provider-independent. Pull journal recovery defines v1 correctness; Change Streams may not define correctness.

Node birth/admission may proceed later but is not a blocker to continued staging implementation. This repository does not own birth machinery. No publish, merge, release, deployment, or sibling-repository mutation is authorized by this staging build.
## STATE-04 retention boundary

State owns tombstone, retained restore, erased identity representation, provider-neutral hard-erasure mechanics, payload scrubbing, and replay/ABA preservation. State does not own retention periods, legal holds, deletion schedules, or external policy decisions. `hard_erase` is internal-only and MUST NOT be registered with Gate or exposed by `StateClient`. A RetentionExecutor MUST remain unbound until an exact externally owned retention-decision contract is available.
