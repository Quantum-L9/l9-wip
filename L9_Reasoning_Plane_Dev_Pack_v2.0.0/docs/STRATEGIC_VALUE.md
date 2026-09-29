# Strategic Value

## Cardinal question

> Which admissible action has the highest expected total value under the declared objective, including immediate and future systemic consequences?

## Canonical decomposition

```text
StrategicValue(a)
= ImmediateExpectedValue(a)
+ SystemicFutureValue(a)
- DirectCost(a)
- ExpectedRiskLoss(a)
- OpportunityCost(a)
```

This is a valuation composition inside Numerical Reasoning, not another reasoning sibling.

## Anti-double-counting law

Every material effect is booked exactly once. Information value, option value, immediate utility, opportunity cost, and Systemic Future Value may describe overlapping consequences; the model must specify which term owns each underlying state delta.

## Answer shape follows question shape

- binary decision -> action vs baseline;
- candidate selection -> ranked actions/frontier;
- resource allocation -> allocation vector;
- timing -> act/wait frontier;
- strategic interaction -> policy/action with response-distribution paths;
- information/computation -> marginal value and stop/acquire decision.
