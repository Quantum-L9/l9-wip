# Probabilistic Reasoning Node

## Mission

Provide bounded, inspectable, provider-neutral inference over explicitly declared probabilistic models, priors, admitted evidence, and optional formal support constraints.

Canonical question:

> Given this admitted uncertainty model, prior state, evidence, and support, what should we believe now?

## Public semantic boundary

```text
ProbabilisticReasoningRequest
    │
    ├── ProbabilisticModel
    ├── PriorState / prior BeliefState
    ├── EvidenceSet
    ├── optional AdmissibleSupport
    ├── QueryTargets
    └── RuntimeBudget
            │
            ▼
ProbabilisticReasoningNode
            │
            ├── admission validation
            ├── support restriction
            ├── model compilation
            ├── provider inference
            ├── diagnostics validation
            ├── belief summarization
            └── receipt generation
            │
            ▼
ProbabilisticReasoningResult
    ├── BeliefState
    ├── predictive summaries
    ├── information gain (optional)
    ├── diagnostics
    └── InferenceReceipt
```

## What it owns

- posterior inference
- predictive inference
- uncertainty quantification
- model-conditioned probability semantics
- information gain
- posterior parameter distributions
- provider-neutral inference receipts

## What it does not own

- source acquisition
- domain ontology
- business objectives
- final decisions
- operational state mutation
- formal truth
- hard-gate logic
- ranking/optimization
- hidden priors
- policy about whether new evidence should be collected

## Bayesian relationship

Bayesian inference is a first-class method family, not the architectural identity.

The stable contract permits future probabilistic methods only if their outputs can be represented faithfully as versioned `BeliefState` semantics without changing callers.

## First implementation family

V1 reference provider supports exact inference for bounded models:

- finite-hypothesis Bayes update
- Beta-Binomial
- Dirichlet-Categorical

These are not domain models. They are conformance kernels proving the public contracts.

Approximate/sampling providers are deferred until after the exact reference slice passes.
