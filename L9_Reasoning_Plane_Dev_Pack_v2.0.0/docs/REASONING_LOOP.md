# Reasoning Loop Protocol

`ReasoningLoop` is a protocol/composition pattern, not an executor.

## Basic triplet path

```text
Formal -> FeasibleRegion / AdmissibleSupport
Probabilistic -> BeliefState
Numerical -> value / optimization
optional Formal verification -> consequence/conflict receipt
```

## General next-action loop

```text
CURRENT STATE
 -> authorized ACT / LEARN / COMPUTE / WAIT / STOP candidates
 -> Formal pruning
 -> Probabilistic outcome beliefs
 -> Numerical StrategicValue
 -> consumer selects/executes authorized action
 -> state changes
 -> re-evaluate if material
```

## Strategic interaction loop

```text
State(t)
 -> Formal feasible strategies
 -> Probabilistic hidden-state / ActorModel beliefs
 -> bounded strategic response/lookahead composition
 -> Numerical StrategicValue
 -> Action(t)
 -> other actors/world
 -> Observation(t+1)
 -> admitted evidence / belief update
 -> State(t+1)
```

## Information refinement

Numerical sensitivity/VOI may identify a high-value LEARN action. Consumer dispatches Research, Memory, File, Human, Test, API, Enrichment, Sensor, Database or WAIT-for-evidence as authorized.

## Computation refinement

COMPUTE competes against STOP. Additional reasoning ends when marginal VOC is non-positive or a mandatory hard bound fires.

## Convergence law

Every episode binds question/objective/policy/state/model revisions, maximum passes, resource/deadline budgets, belief depth/horizon where applicable, and explicit terminal status.
