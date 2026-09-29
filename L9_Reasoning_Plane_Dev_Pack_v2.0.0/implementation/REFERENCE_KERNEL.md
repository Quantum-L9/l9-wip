# Exact Reference Kernel

## Why exact first

An exact provider creates a trustworthy oracle for public contracts before adding Monte Carlo/variational complexity.

## Kernel A: finite hypotheses

Inputs:

```text
hypothesis IDs H[1..N]
prior probabilities p_i
likelihood values L_i for admitted evidence bundle
optional allowed support mask
```

Algorithm:

```text
1. reject negative/non-finite p_i or L_i
2. remove formally excluded hypotheses
3. verify surviving prior mass > 0
4. compute u_i = p_i * L_i
5. compute Z = Σu_i
6. if Z == 0: ZERO_POSTERIOR_MASS
7. posterior_i = u_i / Z
8. canonicalize and summarize
```

Required test properties:

- posterior sum within exact/numeric tolerance;
- excluded support remains zero;
- order changes do not alter semantic digest when hypothesis IDs preserve mapping;
- duplicate evidence is not silently deduplicated unless evidence-set contract declares same ID duplicate invalid.

## Kernel B: Beta-Binomial

Inputs:

```text
alpha > 0
beta > 0
success_count >= 0
failure_count >= 0
```

Posterior:

```text
alpha' = alpha + successes
beta'  = beta + failures
```

Predictive Bernoulli mean:

```text
alpha' / (alpha' + beta')
```

Credible interval implementation must use a tested distribution quantile routine or a separately validated numerical method. The reference pack does not require writing a custom inverse-beta algorithm.

## Kernel C: Dirichlet-Categorical

Inputs:

```text
alpha_i > 0
observed counts n_i >= 0
```

Posterior:

```text
alpha'_i = alpha_i + n_i
```

Predictive category probability:

```text
alpha'_i / Σ alpha'_j
```

## Reference/non-reference split

These kernels prove contracts. They are not the final ceiling for probabilistic capability and do not justify hard-coding these families into plane semantics.
