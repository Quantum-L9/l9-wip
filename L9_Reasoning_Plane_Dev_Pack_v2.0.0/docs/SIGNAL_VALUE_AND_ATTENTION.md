# Signal Value and Rational Attention

Agents may perceive far more raw observations than deserve deep reasoning. Rational attention allocates processing to signals with material expected decision value.

## Expected Signal Value

```text
ExpectedSignalValue(s)
= ExpectedDecisionImprovement(s)
+ SystemicFutureValue(s)
- CaptureCost(s)
- ProcessingCost(s)
- PropagationCost(s)
- ExpectedMisleadingLoss(s)
```

`ExpectedDecisionImprovement` is decision-relevant information value, not mere entropy reduction.

`SystemicFutureValue` may include reusable ActorModel improvement, reduced future research, reduced human interruption, improved calibration, or future work elimination.

## Efficiency lens

```text
SignalValueEfficiency = ExpectedSignalValue / ResourceCost
```

This ratio is secondary. Tiny near-zero-cost signals can have huge ratios while remaining immaterial. Absolute Strategic Value determines materiality.

## Selective perception pipeline

```text
raw observations
 -> cheap relevance/eligibility filter
 -> candidate SignalOpportunity
 -> expected signal value
 -> high-value evidence admission
 -> memory / reasoning
```

Hard safety, authority, privacy and required audit signals are never discarded merely because their economic value is low.
