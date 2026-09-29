# BeliefState

`BeliefState` is the canonical cross-family probabilistic output.

It must be rich enough to preserve uncertainty without forcing downstream consumers to understand provider internals.

## Required semantics

Each `BeliefState` binds:

- model identity + version + digest
- prior identity/digest
- evidence-set digest
- optional `AdmissibleSupport` digest
- provider identity/version and inference mode
- target random variables/propositions
- posterior distribution representation
- posterior/predictive summaries
- uncertainty/credible intervals where meaningful
- diagnostics status
- provenance
- receipt digest

## Distribution representations

The v1 contract supports bounded provider-neutral representations:

1. `analytic` — family + canonical parameters.
2. `discrete_pmf` — finite support/value-probability pairs.
3. `empirical_summary` — normalized summary plus external sample-artifact reference; raw unbounded samples do not cross the public wire contract.

## Why scalar confidence is insufficient

This is intentionally rejected:

```text
close_probability = 0.73
```

without model/evidence/uncertainty provenance.

The same mean can represent radically different evidence strength. Downstream numerical decisions must be able to distinguish high-confidence and low-confidence estimates.

## Immutability

A BeliefState is immutable evidence. A new posterior creates a new `belief_state_id` and digest. Supersession is explicit; prior states remain addressable for audit.
