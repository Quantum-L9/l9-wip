# Value of Computation

## Cardinal question

> Is another bounded computation/reasoning step expected to improve the eventual decision enough to justify its cost?

## Conceptual valuation

```text
NetVOC(c)
= ExpectedDecisionImprovement(c)
+ SystemicFutureValue(c)
- ComputeCost(c)
- LatencyOpportunityCost(c)
- ExpectedComputationRisk(c)
```

`SystemicFutureValue` is included only when the computation creates reusable future value not already counted in ExpectedDecisionImprovement.

## STOP condition

When continuation is optional, STOP competes against COMPUTE actions. The semantic stop condition is non-positive marginal computation value; mandatory safety/validation/resource ceilings remain independent hard bounds.

## Strategic recursion

Belief depth and action/reaction lookahead use VOC to decide whether another level/step is worth evaluating. This prevents unbounded “I think that you think...” recursion and unbounded game-tree expansion.
