# Proposed l9-probabilistic-reasoning Filetree

```text
l9-probabilistic-reasoning/
├── AGENTS.md
├── README.md
├── INVARIANTS.md
├── pyproject.toml
├── uv.lock
├── .l9/
│   ├── architecture.yaml
│   ├── ownership.yaml
│   └── sdk-compatibility.yaml
├── contracts/
│   ├── probabilistic-model.schema.json
│   ├── prior-state.schema.json
│   ├── evidence-set.schema.json
│   ├── admissible-support.schema.json
│   ├── probabilistic-reasoning-request.schema.json
│   ├── belief-state.schema.json
│   ├── probabilistic-reasoning-result.schema.json
│   └── inference-receipt.schema.json
├── src/l9_probabilistic_reasoning/
│   ├── __init__.py
│   ├── service.py
│   ├── errors.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── common.py
│   │   ├── model_spec.py
│   │   ├── prior.py
│   │   ├── evidence.py
│   │   ├── support.py
│   │   ├── request.py
│   │   ├── belief.py
│   │   ├── result.py
│   │   └── receipt.py
│   ├── admission/
│   │   ├── __init__.py
│   │   ├── model.py
│   │   ├── prior.py
│   │   ├── evidence.py
│   │   ├── support.py
│   │   └── budget.py
│   ├── engine/
│   │   ├── __init__.py
│   │   ├── compiler.py
│   │   ├── support_projector.py
│   │   ├── diagnostics.py
│   │   ├── summarizer.py
│   │   ├── information_gain.py
│   │   ├── canonicalize.py
│   │   └── digest.py
│   ├── ports/
│   │   ├── __init__.py
│   │   └── provider.py
│   ├── providers/
│   │   ├── __init__.py
│   │   └── exact/
│   │       ├── __init__.py
│   │       ├── provider.py
│   │       ├── finite_hypothesis.py
│   │       ├── beta_binomial.py
│   │       └── dirichlet_categorical.py
│   └── gate/
│       ├── __init__.py
│       └── handler.py
├── tests/
│   ├── contracts/
│   ├── unit/
│   │   ├── test_admission.py
│   │   ├── test_support_projector.py
│   │   ├── test_finite_hypothesis.py
│   │   ├── test_beta_binomial.py
│   │   ├── test_dirichlet_categorical.py
│   │   ├── test_belief_state.py
│   │   ├── test_digest.py
│   │   └── test_failures.py
│   ├── integration/
│   │   ├── test_service_exact.py
│   │   └── test_gate_handler.py
│   └── conformance/
│       └── test_provider_contract.py
└── docs/
    ├── ARCHITECTURE.md
    ├── PROVIDER_CONTRACT.md
    ├── BELIEF_STATE.md
    ├── RUNBOOK.md
    └── FAILURE_SEMANTICS.md
```

## Dependency direction

```text
models/contracts
      ↑
admission + ports
      ↑
engine
      ↑
service
      ↑
gate handler

providers implement ports and may depend on models,
but core models/engine never import a provider implementation.
```
