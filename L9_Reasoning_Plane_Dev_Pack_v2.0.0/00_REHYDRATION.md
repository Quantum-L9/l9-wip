# Rehydration — L9 Reasoning Plane v2.0.0

Read this file first when resuming the work.

## Canonical architecture

The plane has three current reasoning siblings:

1. **FormalReasoningNode** — symbolic admissibility, constraints, MUST/MAY/IMPOSSIBLE, SAT/UNSAT/MULTIPLE, conflict receipts.
2. **ProbabilisticReasoningNode** — priors, likelihoods, posterior belief, prediction, uncertainty, information gain.
3. **NumericalReasoningNode** — quantitative evaluation, optimization, sensitivity, frontier analysis, information/computation value, allocation, decision boundaries, Strategic Value.

Consumers remain outside the plane and own domain meaning, state selection, objectives, policy, orchestration, authorization, and action execution.

## Current composed patterns

### General decision substrate
`ACT | LEARN | COMPUTE | WAIT | STOP`

### Strategic Interaction Reasoning
A composed pattern spanning all three siblings for decisions involving other actors whose actions respond to ours. It is **not** a fourth sibling.

### Dynamic state
`State(t)` becomes `State(t+1)` after actions, observations, natural evolution, and belief updates. Material new evidence requires re-evaluation of the affected decision surface.

### Hidden state
Visible facts and latent states are separate. `BeliefState(t)` represents probability distributions over uncertain states. Signals are evidence, never globally fixed rules.

### Higher-order belief
Canonical L9 depth:
- depth 0: hidden/world-state belief;
- depth 1: my model of another actor;
- depth 2: my model of their model of me;
- depth 3+: further nesting only when explicitly justified.

Belief depth and strategic lookahead are bounded by hard ceilings and Value of Computation.

## Strategic Value lock

Do not reintroduce `ExpectedLeverageValue`, `LeverageProjection`, `NetStrategicValue`, or `leverage_score` as canonical machine vocabulary.

Use:

```text
StrategicValue
SystemicFutureValue
StateDelta
PropagationTopology
Attribution
RealizationProbability
Recurrence
Decay
Convergence
```

Human prose may call high Systemic Future Value “leverage.” `Signal Leverage` remains the proper name of the external signal-topology kernel.

## Signal bridge lock

A signal has no globally fixed meaning. Evidentiary value is conditioned on state, history, actor model, timing, provenance, reliability, correlation, and strategic incentives.

Signal Leverage owns signal movement and meaning preservation. Probabilistic Reasoning owns belief update. Strategic Interaction models why a strategic actor may generate a signal. Numerical Reasoning owns what to do about it.

## Memory boundary lock

Odoo owns authoritative business events and facts. Graph Memory may own derived contextual/relational hypothesis state such as ActorModel revisions and interaction patterns. A human-facing Odoo `Negotiating Style` is a compressed derived projection, not canonical cognitive truth.

## Build order

1. retain/finish Formal contracts and Clingo adapter;
2. retain/finish Probabilistic exact reference provider and admission semantics;
3. migrate Einesium identity to Numerical Reasoning without losing provider-neutral decision-model execution;
4. land v2 shared dynamic/strategic contracts;
5. implement pure StrategicReasoningAdapter compiler/joiner without action authority;
6. implement bounded synthetic strategic lookahead fixtures;
7. integrate Graph Memory and domain consumers only after contract proofs pass.

## Convergence status

Architecture is converged enough for implementation planning. Remaining unknowns are provider/mechanism choices and domain-specific projections, not plane ownership questions. See `audit/CONVERGENCE_REPORT.yaml`.
