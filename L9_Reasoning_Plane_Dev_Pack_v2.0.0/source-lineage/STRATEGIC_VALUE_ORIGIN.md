# Strategic Value Origin and Terminology Supersession

Earlier reasoning-plane drafts used `ExpectedLeverageValue`, `LeverageProjection`, and `NetStrategicValue`. The architecture later converged on more rigorous machine vocabulary.

Canonical v2:
- `StrategicValue`
- `SystemicFutureValue`
- `SystemicFutureValueProjection`
- `StateDelta`
- `PropagationTopology`
- `Attribution`
- `RealizationProbability`
- `Recurrence`
- `Decay`
- `Convergence`

Human conversation may still describe an intervention as “high leverage.” The machine value is derived from counterfactual future state trajectories rather than an arbitrary score.

This change is breaking and justifies the pack/contract v2 boundary.
