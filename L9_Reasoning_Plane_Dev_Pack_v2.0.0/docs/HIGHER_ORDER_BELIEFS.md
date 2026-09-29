# Higher-Order Beliefs and Belief Depth

Strategic interaction may require reasoning not only about the world, but about what another actor believes and what they believe about us.

## Canonical L9 depth

- **Depth 0:** belief about hidden/world state.
- **Depth 1:** my model of another actor.
- **Depth 2:** my model of the other actor's model of me.
- **Depth 3:** my model of their model of my model of them.
- **Depth N:** further recursion only under explicit bounded justification.

This vocabulary is intentionally explicit rather than relying on ambiguous academic numbering conventions.

## Boundedness

Every strategic request declares `max_belief_depth`. Depth is not a measure of intelligence. It is a computational resource whose expected decision improvement must justify its cost.

Value of Computation may terminate deeper recursive reasoning when the expected improvement from another belief level is non-positive after compute, latency, and opportunity costs.

## Promotion law

A higher-order belief remains belief. It does not become a fact merely because it is nested, strongly held, or strategically useful.
