# Strategic Value Framework

## Canonical machine vocabulary

Human discussion may describe high future propagation as “leverage.” Machine contracts use `StrategicValue` and `SystemicFutureValue`.

## Strategic Value

For action `a` under the declared objective:

```text
StrategicValue(a)
= ImmediateExpectedValue(a)
+ SystemicFutureValue(a)
- DirectCost(a)
- ExpectedRiskLoss(a)
- OpportunityCost(a)
```

The consumer declares the utility/objective unit. Cross-action comparison is valid only when candidate values share compatible utility semantics.

## Systemic Future Value

> The expected counterfactual improvement in future reachable utility caused by an intervention, excluding value already counted as its immediate effect.

Conceptually:

```text
SystemicFutureValue(a)
= E[ Σ future_time discount(time) ×
     ( Utility(State_with_a) - Utility(State_baseline) ) ]
```

This is a trajectory comparison, not a fuzzy multiplier.

## Explanatory value dimensions

- `CAPABILITY_UNLOCK`
- `RECURRING_COST_REDUCTION`
- `FUTURE_WORK_ELIMINATION`
- `FUTURE_DECISION_IMPROVEMENT`
- `REUSABLE_ASSET_VALUE`
- `DEPENDENCY_UNLOCK`
- `FUTURE_INFORMATION_IMPROVEMENT`
- `ACTION_SPACE_EXPANSION`
- `RELATIONSHIP_OR_REPUTATION_EFFECT`
- `OTHER_DECLARED`

Dimensions explain value; they are not blindly additive. A single downstream gain may manifest in multiple descriptions.

## Topology

Systemic value may propagate through:
- `ONE_WAY`
- `BILATERAL`
- `CLOSED_LOOP`
- `MESH`

Topology changes propagation and attribution, not the definition of value.

## Universal computation rule

Cycles are unrolled through time into causal state transitions. Value each new incremental state delta once. Loops stop at convergence, novelty exhaustion, value threshold, horizon, or budget.

## Attribution

For mesh/multi-causal effects, each downstream value delta must carry an attribution model. V1 may use explicit marginal counterfactual contribution and overlap groups. Shapley-style or other cooperative-game attribution methods may be admitted later as method families when multiple contributors jointly create value.

## Prediction vs realization

Predicted Strategic Value is ex ante. Realized value is ex post evidence. They must never be silently conflated. Observed outcomes calibrate future predictions.
