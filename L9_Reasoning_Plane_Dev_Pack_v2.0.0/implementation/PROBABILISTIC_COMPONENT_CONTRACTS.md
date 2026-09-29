# Probabilistic Component Contracts

## `ProbabilisticReasoningService`

Owns one-request pipeline sequencing only.

Pseudo-signature:

```python
execute(request) -> ProbabilisticReasoningResult
```

Pipeline:

1. validate request identity/budget;
2. admit/validate model;
3. admit/validate prior;
4. admit/validate evidence;
5. validate optional support;
6. compile model/provider representation;
7. apply support restriction;
8. call adapter;
9. normalize diagnostics;
10. build `BeliefState`;
11. optionally compute information gain;
12. create immutable inference receipt/result.

## `AdmissionValidator`

Rejects semantic incompleteness. It does not infer missing values.

## `SupportProjector`

Maps `AdmissibleSupport` IDs/conditions into the declared probabilistic model support. It cannot invent new hypotheses or probabilities.

## `ModelCompiler`

Compiles provider-neutral `ProbabilisticModel` into provider-internal representation. Compilation must preserve variable IDs, prior bindings, likelihood semantics, query targets and support identity.

## `ProbabilisticReasoningAdapter`

Provider port. No domain or Gate dependency.

## `DiagnosticsGate`

Determines whether provider output satisfies the mode/provider's declared diagnostics policy. It never fabricates a posterior after diagnostics failure.

## `BeliefStateBuilder`

Normalizes provider output into provider-neutral immutable distributions/summaries.

## `InformationGainCalculator`

Optional. Computes belief-space change from prior to posterior using an explicitly declared measure supported by the model representation.

## `ReceiptBuilder`

Binds request, model, prior, evidence, support, provider, diagnostics, belief-state and budget observations into a canonical receipt digest.
