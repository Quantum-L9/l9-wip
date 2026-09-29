# Reasoning Method Taxonomy

Use the following five-layer vocabulary to prevent architecture from being named after implementation mechanics.

```text
Reasoning Family
  -> Method Family
      -> Method / Algorithm
          -> Primitive
              -> Provider / Engine
```

## Examples

### Probabilistic
- Reasoning family: Probabilistic Reasoning
- Method family: Bayesian Inference
- Method: finite exact inference, MCMC, NUTS, variational inference
- Primitive: multiply, normalize, marginalize, sample, log-sum-exp
- Provider: ExactReferenceProvider, future PyMC/NumPyro/Stan adapters

### Numerical
- Reasoning family: Numerical Reasoning
- Method family: Optimization / Information Value / Strategic Value
- Method: gradient descent, simplex, branch-and-bound, bounded lookahead evaluator
- Primitive: dot product, argmax, tensor contraction, integration
- Provider: NumPy/SciPy/JAX/etc. behind explicit ports

### Formal
- Reasoning family: Formal Reasoning
- Method family: Stable Model Reasoning / SMT / Constraint Programming
- Method: answer-set solving, DPLL(T), propagation/search
- Primitive: predicates, logical connectives, equality, constraint propagation
- Provider: Clingo/Clorm v1, future versioned adapters

### Strategic interaction
- Composition pattern: Strategic Interaction Reasoning
- Method family: Game-Theoretic Analysis
- Algorithm family: BoundedStrategicLookahead / best-response iteration / equilibrium solver
- primitives/providers: implementation dependent

## Contract rule

Callers depend on the highest stable semantic contract, not the current method, primitive, or provider.
