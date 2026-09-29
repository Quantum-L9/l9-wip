# Bounded Strategic Lookahead

## Role

`BoundedStrategicLookahead` is an algorithm family implementing Strategic Interaction Reasoning over a finite action/reaction horizon. It is not the architecture itself.

## Inputs

- time-indexed current state;
- focal objective and policy revision;
- formal feasible actions;
- ActorModels / BeliefStates;
- candidate response models;
- strategic horizon;
- maximum belief depth;
- computation/resource budget;
- terminal and convergence criteria.

## Recurrence

Conceptually:

```text
Q(s_t, b_t, a_i)
  = E over other-actor responses and next state [
      immediate value
      + discounted future V(s_{t+1}, b_{t+1})
    ]

b_{t+1}
  = Bayesian / probabilistic update from new observation

V(s_t, b_t)
  = best Strategic Value over formally admissible actions
```

The implementation may use enumeration, dynamic programming, game-tree search, equilibrium methods, approximate search, or future providers, but public semantics remain provider-neutral.

## Pruning and stopping

Formal impossibility prunes branches before probabilistic/numerical work.

Low-probability/low-value branches may be pruned only under declared approximation policy.

Stop when any applicable condition holds:
- terminal interaction state;
- horizon exhausted;
- no feasible actions;
- convergence/no material strategy change;
- mandatory budget exhausted;
- marginal Value of Computation ≤ marginal computation cost.

## Output

The result is a strategy or policy recommendation with branch probabilities, Strategic Value, material assumptions, decision boundaries, receipts, and uncertainty. It must not claim that another actor *will* take a predicted action.
