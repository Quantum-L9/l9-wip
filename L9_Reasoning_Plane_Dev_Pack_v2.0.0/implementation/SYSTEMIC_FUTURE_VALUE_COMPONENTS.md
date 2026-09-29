# Systemic Future Value Implementation Components

## `CounterfactualBaselineBinder`
Binds intervention trajectory and baseline trajectory to compatible state/objective revisions.

## `TopologyUnroller`
Converts ONE_WAY/BILATERAL/CLOSED_LOOP/MESH propagation descriptions into bounded time-indexed causal effect episodes.

## `StateDeltaValuator`
Maps each unique future state delta into declared utility units.

## `OverlapGuard`
Prevents one underlying downstream benefit from being booked through multiple explanatory dimensions.

## `AttributionEngine`
V1 supports direct counterfactual, marginal contribution and declared-share attribution. Advanced cooperative-game attribution is deferred until earned.

## `ConvergenceGate`
Stops propagation valuation at horizon, generation limit, novelty exhaustion, or incremental-value threshold.

## `RealizationComparator`
Compares ex ante predicted future value with ex post observed state changes for calibration. Never rewrites historical predictions.
