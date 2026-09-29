# Target Filetrees

## Plane contract repo

```text
l9-reasoning/
├── AGENTS.md
├── README.md
├── INVARIANTS.md
├── contracts/
│   └── v2/
│       ├── formal-*.schema.json
│       ├── probabilistic-*.schema.json
│       ├── belief-state.schema.json
│       ├── numerical-*.schema.json
│       ├── meta-action.schema.json
│       ├── dynamic-state.schema.json
│       ├── state-transition.schema.json
│       ├── actor-observation.schema.json
│       ├── actor-model.schema.json
│       ├── higher-order-belief.schema.json
│       ├── response-model.schema.json
│       ├── strategic-state.schema.json
│       ├── strategic-interaction-*.schema.json
│       ├── strategic-lookahead-*.schema.json
│       ├── strategic-value-assessment.schema.json
│       └── systemic-future-value-projection.schema.json
├── docs/
│   ├── ownership.md
│   ├── convergence.md
│   ├── method-taxonomy.md
│   └── strategic-interaction.md
└── tests/contracts/
```

## Formal node

Independent deployable node preserving Formal contracts and provider adapters.

## Probabilistic node

See `implementation/PROBABILISTIC_FILETREE.md`.

## Numerical node

Independent successor identity to Einesium. Adds StrategicValue/SystemicFutureValue, VOI/VOC, resource allocation, decision-boundary and strategic numerical methods without taking consumer policy authority.

## Strategic interaction shared surfaces

See `implementation/STRATEGIC_INTERACTION_FILETREE.md` and `implementation/AGENTOS_STRATEGIC_ADAPTER_CONTRACT.md`.

No new runtime node is introduced by v2.
