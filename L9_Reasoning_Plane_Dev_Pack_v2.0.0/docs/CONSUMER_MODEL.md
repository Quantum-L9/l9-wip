# Consumer Model

Consumers are not components of the Reasoning Plane. A consumer may be AgentOS, DomainOS, infrastructure/planning software, code systems, or human-facing applications.

The consumer owns:

```text
QUESTION
OBJECTIVE
DOMAIN CONTEXT
AUTHORITATIVE STATE SELECTION
CANDIDATE ACTION GENERATION
ACTION AUTHORIZATION
FORMAL RULE PROJECTION
PRIOR / MODEL SEMANTICS
PARAMETER SET
ORCHESTRATION
EXECUTOR SELECTION
FINAL ACTION AUTHORITY
```

The Reasoning Plane returns reasoning evidence, beliefs, valuations, frontiers, boundaries, strategy candidates, and receipts. It does not grant permission to act.

## Meta-action dispatch

- `ACT`: authorized domain capability;
- `LEARN`: selected evidence source/capability;
- `COMPUTE`: bounded additional computation;
- `WAIT`: external condition/time mechanism under consumer/runtime;
- `STOP`: terminate optional episode.

## Strategic consumer

For strategic interaction the consumer additionally supplies ActorModel refs, current interaction history, strategic horizon, belief depth bounds, response-model refs where available, and game-structure semantics. The shared `StrategicReasoningAdapter` may compile/join requests but still owns no execution.

## Integration

Constellation consumers use Gate/Gate_SDK. Nodes do not know peer URLs and do not directly invoke sibling endpoints as hidden orchestration.
