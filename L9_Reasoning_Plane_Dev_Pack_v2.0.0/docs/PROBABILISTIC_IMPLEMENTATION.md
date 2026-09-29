# Probabilistic Reasoning — Implementation Design

## Implementation objective

Build `Quantum-L9/l9-probabilistic-reasoning` as an independently deployable reasoning node whose core can be exercised as a pure Python service without Gate, network, CRM, memory, or domain dependencies.

## Component decomposition

```text
Public contracts
      │
      ▼
RequestParser / AdmissionValidator
      │
      ├── validates model
      ├── validates prior
      ├── validates evidence
      ├── validates support restriction
      └── validates budget
      │
      ▼
SupportProjector
      │
      ▼
ModelCompiler
      │
      ▼
ProbabilisticReasoningAdapter
      │
      ▼
ProviderInferenceResult
      │
      ▼
DiagnosticsGate
      │
      ▼
BeliefStateBuilder
      │
      ├── posterior summaries
      ├── predictive summaries
      ├── optional information gain
      └── canonical digests
      │
      ▼
InferenceReceiptBuilder
```

## Public service contract

Conceptual Python surface:

```python
class ProbabilisticReasoningService:
    def execute(
        self,
        request: ProbabilisticReasoningRequest,
    ) -> ProbabilisticReasoningResult: ...
```

The service owns orchestration **inside one probabilistic inference request only**. It never sequences Formal or Numerical siblings.

## Provider port

```python
class ProbabilisticReasoningAdapter(Protocol):
    def capabilities(self) -> ProviderCapabilities: ...

    def compile(
        self,
        model: ProbabilisticModel,
        support: AdmissibleSupport | None,
    ) -> CompiledProbabilisticModel: ...

    def infer(
        self,
        compiled: CompiledProbabilisticModel,
        prior: PriorState,
        evidence: EvidenceSet,
        query: InferenceQuery,
        budget: RuntimeBudget,
    ) -> ProviderInferenceResult: ...
```

Provider-specific model objects, traces, chain handles, graph nodes, tensors, seeds, and raw samples stay behind the adapter.

## Provider inference result

The internal provider result must include enough information to normalize into public semantics:

```text
status
posterior representation or artifact ref
predictive representation or artifact ref
diagnostics
provider identity/version
inference mode
random seed if stochastic
runtime/resource observations
```

## V1 exact reference provider

Package module: `providers/exact/`.

Required kernels:

### Finite hypothesis Bayes

Given finite hypotheses `H_i`, prior `P(H_i)`, and admitted likelihoods `P(E|H_i)`:

```text
posterior_i = prior_i * likelihood_i / Σ(prior_j * likelihood_j)
```

Invariants:

- support probabilities nonnegative;
- admitted support sums to 1 after normalization;
- formally excluded hypotheses are removed before normalization;
- zero normalization denominator is a typed failure, never division fallback.

### Beta-Binomial

```text
prior      Beta(alpha, beta)
observed   successes=s, failures=f
posterior  Beta(alpha+s, beta+f)
```

Produces posterior mean, variance, bounded credible summaries, and posterior predictive probability for the declared Bernoulli target.

### Dirichlet-Categorical

```text
prior      Dirichlet(alpha_1...alpha_k)
observed   category counts n_1...n_k
posterior  Dirichlet(alpha_i+n_i)
```

Used only as a generic exact conformance kernel, not a domain ontology.

## Canonicalization and digests

Before hashing:

- object keys sorted;
- arrays preserve semantic order unless contract declares set semantics;
- floating values encoded through a canonical numeric serializer;
- NaN/Infinity forbidden;
- provider-specific diagnostic blobs excluded from semantic `BeliefState` digest unless explicitly normalized;
- raw sample ordering does not define the semantic digest.

## Approximate provider admission

Future MCMC/SMC/variational providers must satisfy:

- explicit inference mode;
- explicit provider/model version;
- explicit seed where stochastic execution is seedable;
- resource budget enforcement;
- convergence/quality diagnostics normalized into common fields;
- no SUCCESS when required diagnostics fail policy;
- provider-neutral `BeliefState` output;
- bounded sample transport using artifact references rather than unbounded inline payloads;
- conformance against exact fixtures where an exact solution exists.

Provider selection is deployment/configuration policy, not caller semantics.

## Error taxonomy

```text
INVALID_REQUEST
INVALID_MODEL
INVALID_PRIOR
INVALID_EVIDENCE
INVALID_SUPPORT
INSUFFICIENT_EVIDENCE
INSUFFICIENT_MODEL
UNSUPPORTED_MODEL
ZERO_POSTERIOR_MASS
DIAGNOSTIC_FAILURE
BUDGET_EXHAUSTED
DEGRADED_PROVIDER
FAILED
```

Errors never silently convert to uniform priors, zero values, or Numerical fallbacks.
