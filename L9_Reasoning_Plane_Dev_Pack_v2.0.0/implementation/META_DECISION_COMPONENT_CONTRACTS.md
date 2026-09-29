# Meta-Decision Component Contracts

## Shared plane repo

Own stable schemas and semantics for `MetaAction`, `StrategicValueAssessment`, `SystemicFutureValueProjection`, `InformationValueAssessment`, `ComputationValueAssessment`, `ResourceAllocationResult`, `DecisionBoundary`, and receipts.

It does not own scheduling or side effects.

## Numerical node

Owns valuation arithmetic, objective compatibility checks, optimization/frontier methods, VOI/VOC, allocation, decision-boundary analysis, and Systemic Future Value trajectory math under declared models.

It does not invent unsupported future effects, action permissions, or domain policy.

## Consumer/runtime

Owns candidate generation, policy, authorization, sequencing, action dispatch, and post-action state mutation through the actual system of record/capability owner.
