# Formal Reasoning Node

## Mission

Provide deterministic, inspectable reasoning over admitted facts and laws through a provider-neutral `ReasoningAdapter`.

## v1 provider

```text
StableModelReasoning
  └── ClingoAdapter
      ├── clingo
      └── clorm
```

Clingo/Clorm is the locked first implementation, not the permanent architecture.

## Core contracts

### FactProjection

Assume/admit proposition P and derive bounded consequences including MUST/MAY/IMPOSSIBLE/UNSAT where representable.

### ConstraintQuery

Ask a bounded logical/constraint question against admitted facts and laws.

### FormalReasoningResult

Must identify:

- query
- admitted assumptions
- solver/backend identity/version
- result category
- derived conclusions
- supporting facts/rules
- conflicts/UNSAT core when available
- scope and boundedness receipt

## Admission law

Facts require sufficient scope, provenance, and authority for the query. Retrieved context, memory, model output, or Numerical Reasoning output is candidate evidence until explicitly admitted.

## Degraded semantics

Provider unavailability, timeout, resource exhaustion, unsupported program semantics, and ambiguous fact admission must fail explicitly. No fallback may silently change reasoning semantics.
