# Probabilistic Inference Modes

## Exact

Preferred whenever model family and boundedness permit analytic or complete finite computation.

Properties:

- deterministic for canonical input
- no Monte Carlo error
- ideal reference/oracle path
- strongest contract-validation surface

## Approximate / stochastic

Permitted behind provider adapter after v1 exact conformance.

Possible future families include sampling, sequential Monte Carlo, variational inference, or other probabilistic programming methods.

The architecture does not name a production provider yet.

## Determinism terminology

The plane must not mislabel stochastic approximate inference as numerically deterministic.

Instead receipts distinguish:

```text
EXACT_DETERMINISTIC
APPROXIMATE_SEEDED
APPROXIMATE_UNSEEDED_FORBIDDEN_BY_POLICY (unless explicitly authorized later)
```

The semantic object is a probability distribution; execution reproducibility and inference uncertainty are separate concerns.

## Diagnostics

Exact mode reports algebraic/normalization validation.

Approximate modes must provide provider-neutral quality fields and may additionally attach provider-specific diagnostics by reference.

No universal R-hat/ESS threshold is hard-coded into the plane contract because not all providers use those diagnostics. Provider admission policy must declare the diagnostics that gate SUCCESS.
