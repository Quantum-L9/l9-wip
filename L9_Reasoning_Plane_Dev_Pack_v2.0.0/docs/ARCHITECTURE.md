# Architecture

## Plane topology

```text
                         L9 REASONING PLANE

     FormalReasoningNode   ProbabilisticReasoningNode   NumericalReasoningNode
          admissibility              belief                    utility
                  \                    |                    /
                   \                   |                   /
                    +------ shared versioned contracts ---+
```

The plane is an architecture/contract plane, not a merged runtime. Siblings remain independently deployable, replaceable and degradable behind Gate/Gate_SDK.

## Consumers

AgentOS, Mack, Emma, L-CTO, PlasticOS, future DomainOS and other callers remain outside the plane. They own question semantics, state selection, objective, policy, orchestration, authorization, and execution.

## Dynamic state

Reasoning is bound to time-indexed state. Material observation or action changes `State(t)` to `State(t+1)` and may require re-evaluation.

## Composed reasoning patterns

### General meta-decision
`ACT | LEARN | COMPUTE | WAIT | STOP`

### Strategic Interaction Reasoning
A cross-triplet composition for environments with strategic actors. Game theory is a method family; bounded strategic lookahead is an algorithm family. No fourth sibling yet.

### Signal-to-belief loop
Signal Leverage -> evidence admission -> Probabilistic update -> strategic/numerical reasoning -> action -> outcome -> new signal.

## Strategic Value

Machine-facing value uses StrategicValue and SystemicFutureValue, not a generic leverage score. Systemic future effects are calculated from counterfactual future state trajectories and causal attribution under one-way/bilateral/closed-loop/mesh topologies.

## Memory

Graph Memory may hold derived ActorModels and interaction patterns. Authoritative facts remain with their owners. Odoo may expose a compressed Negotiating Style summary plus opaque model refs without mirroring dense inference state.

## Transport

Inter-node traffic uses Gate/Gate_SDK and canonical TransportPacket semantics. No peer URLs or cross-node code imports.
