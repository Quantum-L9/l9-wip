# Delta Report — v1.2.0 → v2.0.0

## Breaking semantic deltas

- `ExpectedLeverageValue` → `SystemicFutureValue`.
- `LeverageProjection` → `SystemicFutureValueProjection`.
- `NetStrategicValue` → `StrategicValue`.
- contracts moved from generation `v1` to `v2` with `contract_version: 2.0.0`.

## New foundational architecture

- dynamic time-indexed state and state transitions;
- hidden-state belief / context-conditioned signal interpretation;
- Strategic Interaction Reasoning composed across the triplet;
- Game-Theoretic Analysis method family;
- BoundedStrategicLookahead algorithm family;
- explicit higher-order belief depth;
- ActorObservation / ActorModel / ResponseModel / StrategicState contracts;
- Graph Memory ↔ Odoo projection boundary;
- bilateral buy/sell negotiation model;
- signal-value / rational-attention framework;
- Systemic Future Value one-way/bilateral/closed-loop/mesh topology;
- causal attribution/anti-double-counting;
- reusable StrategicReasoningAdapter contract for AgentOS consumers.

## Preserved architecture

- triplet sibling independence;
- consumer action authority;
- Gate/Gate_SDK transport;
- Formal/Probabilistic/Numerical semantic ownership;
- exact-first probabilistic reference strategy;
- provider neutrality;
- memory context not authority;
- bounded loops and explicit receipts.
