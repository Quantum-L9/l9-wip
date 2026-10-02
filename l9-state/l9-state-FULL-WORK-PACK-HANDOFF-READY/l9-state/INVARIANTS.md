# L9 State invariants

`invariants.yaml` is the machine-readable index. Product-specific State law remains bound to Dev Pack v2.0.0 plus the user-approved STATE-02A operation-execution delta. Organization-level architecture law is frozen for this checkpoint at `Quantum-L9/.github@08912f391c0a6672957f40cbd9b0db285f82ed86`, including `l9.node-archetype/authoritative-state@1` and the provider-neutral / immutable-revisioned-state patterns. The upstream foundation constrains realization without taking ownership of State-specific semantics.

The nine operation-execution invariants below resolve F-003, F-004, and A-001 without widening State's mission or changing the public receipt schemas.

## Locked invariants

1. **STATE-ATOMIC-001** - A state payload/lifecycle mutation atomically commits the next revision, current projection, immutable revision record, canonical event, and operation receipt.
2. **STATE-DOMAIN-001** - State has zero branches on WorkItem kind, agent profile, domain lifecycle, or consumer business type.
3. **STATE-FENCE-001** - Fencing is monotonically increasing per StateKey and stale/expired/superseded claim holders cannot mutate.
4. **STATE-IDEMP-001** - One OperationKey identifies one semantic mutation request. Collision never produces an effect.
5. **STATE-REV-001** - Revisions start at 0, increase by exactly 1 for state mutations, never reset, and object IDs are never reused.
6. **STATE-SCHEMA-001** - Schema binding is immutable for a v1 object's lifetime; State validates but does not own schema meaning.
7. **STATE-PROVIDER-001** - No provider syntax or identity crosses the stable State contract.
8. **STATE-JOURNAL-001** - One canonical State event journal is the authoritative mutation-event/outbox source. No second canonical outbox truth exists.
9. **STATE-CURSOR-001** - Public cursors are State-issued and provider-independent; provider resume tokens never escape adapters.
10. **STATE-CLAIM-001** - Claims are coordination metadata, not business ownership or authorization grants.
11. **STATE-TENANT-001** - Trusted tenant organization comes only from validated transport context and is always part of persistence identity.
12. **STATE-READ-001** - Reads do not create durable operation receipts merely to prove observation.
13. **STATE-RETENTION-001** - TTL is never the semantic authority for lease expiry, operation identity, tombstone, or erasure.
14. **STATE-RECOVERY-001** - Unknown completion is reconciled by authoritative operation receipt; blind semantic replay is forbidden.
15. **STATE-EVENT-001** - Event order is total only within one State scope journal, not globally across the constellation.
16. **STATE-GATE-001** - Every inter-node call uses Gate_SDK/Constellation.Gate; no peer URLs or shadow transport.
17. **STATE-BIRTH-001** - State code must not implement or modify repository/node birth machinery.
18. **STATE-EVENT-OPT-001** - Pull journal recovery is sufficient for v1; push/change-stream wakeups are optional later optimizations and cannot define correctness.
19. **STATE-BUDGET-001** - Gate timeout is the sole request-budget authority. State may shrink it but never extend it.
20. **STATE-BUDGET-002** - No provider retry, transaction retry, commit attempt, or reconciliation attempt may outlive the State execution budget derived from Gate.
21. **STATE-OUTCOME-001** - An admitted OperationKey has at most one durable terminal receipt.
22. **STATE-OUTCOME-002** - `committed`, `conflict`, and `refused` are terminal receipt states; expected mutation outcomes are data, not exceptions at the transport boundary.
23. **STATE-OUTCOME-003** - An OperationKey is never re-evaluated after a terminal receipt. Changed-world retry requires a new `operation_id`.
24. **STATE-AMBIGUITY-001** - Once commit may have occurred, semantic execution stops and only authoritative OperationKey reconciliation is permitted.
25. **STATE-PROBLEM-001** - `StateProblem` is never persisted as an authoritative operation receipt.
26. **STATE-RETRY-001** - `retry_class` describes retry safety, not workflow recovery.
27. **STATE-RETRY-002** - Workflow recovery after a terminal receipt is expressed by reason-code guidance and uses a new operation identity.

## Imported generalized L9 laws

- One semantic authority per concern.
- Derived representations introduce zero semantic authority.
- Provider mechanics remain behind stable capability contracts.
- Persistence records durable facts; it does not invent semantic meaning.
- Event-driven machinery must earn its operational cost.
- Evidence and memory never substitute for State truth.

## STATE-04 lifecycle closure

- **STATE-LIFECYCLE-001** - v1 lifecycle is `active -> tombstoned -> active` only through retained restore; `erased` is terminal.
- **STATE-RESTORE-001** - Restore is legal only from an explicitly retained prior revision of the same currently tombstoned object and creates a new active revision rather than rewinding history.
- **STATE-ERASE-001** - Hard erase removes retained payload bytes while preserving minimal object identity, monotonic revision/fence lineage, canonical journal metadata, and operation replay safety.
- **STATE-RETENTION-002** - State owns erasure mechanics but not retention policy; hard-erasure execution requires an externally authorized retention decision.
