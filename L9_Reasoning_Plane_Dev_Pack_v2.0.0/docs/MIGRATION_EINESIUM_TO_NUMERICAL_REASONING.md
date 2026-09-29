# Migration: Einesium → L9 Numerical Reasoning

## Status

Architectural vocabulary supersession. Historical artifacts remain valid lineage/evidence.

## Rename map

| Historical | Canonical v1 |
|---|---|
| Einesium | L9 Numerical Reasoning |
| EinesiumNode | NumericalReasoningNode |
| Einesium cartridge | DecisionModel / cartridge |
| MathExecutionSpec | NumericalExecutionSpec |
| Einesium result | NumericalReasoningResult |
| Einesium receipt | NumericalReasoningReceipt |
| Einesium API | Numerical Reasoning capability API |

## Preserved invariants

- domain-empty without consumer DecisionModel
- semantic dimensions precede provider syntax
- einsum is one lowering primitive
- provider-neutral optimization/execution
- independent simple oracle
- validation is evidence, not authority
- Gate-owned transport

## New responsibilities gained through plane integration

- `FeasibleRegion` input
- `DecisionAssumption` output projection
- `ConstraintDelta` interoperability
- plane-level convergence receipts
- reasoning-family identity in evidence

## Explicitly not migrated

The Numerical node does not absorb Formal Reasoning, Clingo, formal law admission, or loop orchestration.
