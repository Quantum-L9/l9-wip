# Causal Attribution and Propagation Topology

## Why topology matters

An intervention can improve one consumer, improve a second actor that returns value upstream, form a productive feedback loop, or propagate across a mesh. Naively summing every path double-counts shared downstream effects and can make cycles mathematically explode.

## Universal solution

Unroll topology through time into state transitions:

```text
A0 -> B1 -> A2 -> B3
```

or

```text
A0 -> B1 -> C2 -> A3 -> ...
```

Each distinct state delta is valued once against the declared baseline.

## Bilateral

Bilateral value is not `benefit_A × benefit_B`. It is the discounted sequence of new counterfactual state improvements caused by each turn in the interaction.

## Closed loop

A productive loop requires changed future state. Echoes, duplicate messages, and unchanged recirculation have zero incremental future value and should converge immediately.

## Mesh

When multiple paths contribute to the same outcome:
- assign one effect identity to the downstream gain;
- track causal contributor refs;
- declare overlap groups;
- choose an attribution method;
- ensure attribution shares do not produce value greater than the underlying counterfactual delta.

## Drag

Propagation cost, latency, stale context, transformation loss, coordination burden, maintenance, and failure risk are negative state effects and must be included in Strategic Value when material.
