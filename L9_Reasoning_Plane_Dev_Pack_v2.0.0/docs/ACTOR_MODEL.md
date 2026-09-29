# ActorModel

## Purpose

`ActorModel` is a versioned, provenance-bound hypothesis state about another decision-maker. It is not a personality label and not authoritative truth about a person or organization.

## Canonical surfaces

An ActorModel may contain context-scoped belief distributions over:

- price sensitivity;
- countering tendency;
- urgency behavior;
- relationship weighting;
- inventory pressure;
- response latency;
- claim behavior;
- commitment credibility;
- concession behavior;
- walk-away behavior;
- repeat-purchase behavior;
- reservation-value ranges;
- outside-option strength;
- strategic hypotheses;
- response models;
- higher-order beliefs.

These variables may coexist. Do not flatten them into a single mutually exclusive `OpponentType` enum.

## Derivation chain

```text
ActorObservation
├── context
├── action
├── outcome
├── visible_state
├── inferred_state (optional hypothesis)
└── confidence / provenance
        ↓
Graph Memory pattern accumulation
        ↓
Probabilistic Reasoning
        ↓
ActorModel revision
```

## Context law

Actor behavior is contextual and temporal. “Price-sensitive on spot HDPE loads” is not equivalent to “price-sensitive everywhere.” Every derived tendency must carry scope, time, evidence, and uncertainty.

## Truth boundary

- Observed transaction/action facts may be authoritative elsewhere.
- ActorModel fields are derived beliefs.
- The model may be contradicted, superseded, narrowed, or made less certain by later evidence.
