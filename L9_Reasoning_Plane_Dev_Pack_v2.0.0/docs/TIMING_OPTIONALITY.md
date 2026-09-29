# Timing, Commitment, and Optionality

## Value of waiting

Some states change without active evidence acquisition: buyer response, capacity reopening, price movement, approval, dependency completion, natural evidence arrival.

A WAIT candidate compares expected future best utility against acting now plus delay/opportunity cost.

```text
ValueOfWaiting
= ExpectedBestFutureValue
- ValueOfActingNow
- CostOfDelay
```

## Commitment / reversibility

Actions with similar immediate value may consume very different future option sets. Model reversibility, switching/exit cost, commitment duration, locked resources, and action-space expansion/contraction.

## Strategic commitment

Strategic Interaction adds an important inverse: deliberately reducing our own future options may improve another actor's response when the commitment is credible. Commitment Value and Optionality Value can therefore oppose one another.

## Booking law

Option/reversibility effects are not automatically a separate additive term in StrategicValue. The DecisionModel/effect ledger declares where each underlying future state delta is booked so the same benefit/loss is not counted again in SystemicFutureValue or OpportunityCost.
