# Priors, Evidence, and Admission

## No hidden priors

Probabilistic Reasoning may execute a prior. It may not invent why that prior is semantically valid.

Every prior declares:

- distribution/representation
- subject/scope
- source kind
- source reference or explicit assumption reference
- version/digest
- effective time where relevant

Allowed source kinds in v1:

```text
EMPIRICAL_BASELINE
PREVIOUS_POSTERIOR
DOMAIN_ASSUMPTION
POPULATION_BASELINE
EXTERNAL_MODEL
```

A missing required prior produces `INVALID_PRIOR` or `INSUFFICIENT_MODEL`, never a hidden uniform default.

## Evidence admission

Probabilistic Reasoning consumes **admitted evidence**. It does not crawl sources or decide that an observation is authoritative merely because it exists.

Each evidence item binds:

- evidence ID
- subject/scope
- observed variable/proposition
- observed value/category
- observed timestamp
- source/provenance reference
- evidence revision

Evidence confidence, if supplied, is metadata. It is not automatically converted to a likelihood weight. The declared probabilistic model owns how observations generate likelihood.

## Formal support

`AdmissibleSupport` may remove impossible hypotheses/states before inference.

Formal IMPOSSIBLE can set support mass to zero because it is a semantic support restriction.

A tiny posterior probability may **not** be promoted to Formal IMPOSSIBLE.

## Previous posterior reuse

A prior may be a previous `BeliefState` only when:

- model compatibility is explicit;
- subject/scope is identical or explicitly transformed;
- evidence is not double-counted;
- supersession/provenance is preserved.

Double-counting previous evidence is a blocking defect.
