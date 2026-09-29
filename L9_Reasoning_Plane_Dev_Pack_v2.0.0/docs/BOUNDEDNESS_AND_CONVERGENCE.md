# Boundedness and Convergence

Every reasoning request and composite episode is explicitly bounded.

## Per-node bounds

Formal: query scope, solver budget, multi-shot scope.

Probabilistic: model/support size, evidence bounds, inference mode, runtime budget, sample/iteration budget for approximate providers, bounded public summaries.

Numerical: candidate/shape limits, scenario count, optimization budget, objective/horizon limits.

## Strategic bounds

- maximum belief depth;
- maximum action/reaction horizon;
- branch/candidate budget;
- explicit approximation/pruning policy;
- hard time/compute budget;
- terminal state conditions;
- convergence/no-material-change condition;
- marginal Value-of-Computation gate.

## Dynamic re-evaluation

A material state/model/objective/policy revision invalidates affected reasoning outputs. Incremental reuse is allowed only when semantic compatibility is proven.

## Meta-decision convergence

When continuation is optional, STOP competes against COMPUTE. Optional computation should terminate when the best authorized COMPUTE action has non-positive marginal StrategicValue, subject to mandatory obligations and hard ceilings.

## Composite terminal states

```text
CONVERGED
UNSAT
NO_FEASIBLE_REGION
NO_IMPROVEMENT
INSUFFICIENT_EVIDENCE
INSUFFICIENT_MODEL
BUDGET_EXHAUSTED
DEGRADED
STOP_SELECTED
HORIZON_EXHAUSTED
BELIEF_DEPTH_EXHAUSTED
FAILED
```
