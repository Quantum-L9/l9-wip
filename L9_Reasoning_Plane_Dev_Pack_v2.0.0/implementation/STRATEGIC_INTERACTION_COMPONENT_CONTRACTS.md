# Strategic Interaction Component Contracts

## `StrategicReasoningAdapter`
Pure consumer-side compiler/joiner. Converts current state, objectives, ActorModels, action candidates, bounds and history into plane-native requests and joins receipts into `StrategicInteractionResult`.

**Forbidden:** policy invention, action execution, workflow ownership, hidden state truth, direct node calls outside Gate runtime wiring.

## `StrategicStateProjector`
Builds a bounded time-indexed strategic state from authoritative visible state plus versioned belief/model refs. Does not persist new facts.

## `ActorModelProjector`
Builds probabilistic model inputs from versioned ActorModel/Graph Memory context. ActorModel remains belief state, not truth.

## `ResponseTreeBuilder`
Enumerates or samples bounded plausible action/reaction paths according to explicit response models and approximation policy.

## `FormalBranchPruner`
Projects candidate branches into Formal Reasoning and excludes impossible/forbidden branches. It does not rank surviving branches.

## `StrategicPathValuator`
Projects branch outcome distributions and state deltas into Numerical Reasoning. It does not update posterior belief.

## `BeliefUpdateProjector`
After observations/outcomes, constructs a Probabilistic Reasoning request for belief revision. It does not acquire the evidence itself.

## `ConvergenceGate`
Applies horizon, belief depth, hard budget, convergence and Value-of-Computation terminal conditions.
