# StrategicReasoningAdapter for Agent Consumers

## Status

Earned shared adapter contract; **not** a new reasoning node.

## Why it exists

Mack, Emma, L-CTO, procurement agents, sales agents, coding agents, and future AgentOS children may all need the same compilation machinery:

```text
agent context
+ current state
+ objectives
+ ActorModels
+ history
+ constraints
+ belief depth
+ strategic horizon
 -> plane-native Formal / Probabilistic / Numerical requests
 -> joined receipts
 -> StrategicInteractionResult
```

Duplicating that projection/join logic per agent creates drift.

## Ownership

The adapter MAY own:
- pure request compilation;
- semantic projection from agent context to shared contracts;
- receipt joining;
- deterministic digests;
- no-op/degraded projections when a family is intentionally unused.

It MUST NOT own:
- final strategy authority;
- action authorization;
- tool execution;
- workflow scheduling;
- domain policy;
- hidden state truth;
- Graph Memory mutation authority;
- a fourth reasoning engine.

## Placement

`l9-reasoning` should own the stable adapter contract and reference pure compiler semantics. AgentOS/runtime owners may host execution-side wiring. Gate/Gate_SDK remains the transport boundary for node calls.
