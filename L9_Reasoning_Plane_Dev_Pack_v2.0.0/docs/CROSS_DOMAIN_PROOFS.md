# Cross-Domain Architecture Proofs

The shared contracts are stress-tested conceptually against four materially different consumers to reduce domain-overfitting risk.

## 1. Poker-like adversarial interaction

- Visible state: board, stack, position, action history.
- Hidden state: cards/range, strategy, bluff/value line, tell authenticity.
- Signals: check, sizing, timing, body language, revealed hands.
- Formal: legal actions, impossible cards, betting constraints.
- Probabilistic: range/hidden-state posterior.
- Strategic: incentive-conditioned signal interpretation, exploitability, mixed strategy.
- Numerical: pot/stack utility, expected value, Strategic Value over bounded future actions.

Shared conclusion: surface action is evidence, not rule; later observations can invert earlier interpretation.

## 2. Bilateral plastics brokerage negotiation

- Visible state: supplier ask, buyer quote/counter, freight, quantity, material, transaction history.
- Hidden state: supplier floor, buyer willingness-to-pay, urgency, alternatives, inventory pressure, relationship weighting.
- ActorModel: context-scoped tendencies and credibility.
- Strategic interaction spans both buy and sell side; realized spread is partly an outcome of strategic interaction.
- Odoo owns commercial events; Graph Memory owns derived interaction hypotheses/patterns.

Shared conclusion: persuasion playbooks are unnecessary as a core primitive; perception + belief update + strategic response reasoning + valuation are reusable.

## 3. Emma / executive-assistant interaction

Candidate actions: search, query memory, inspect file, ask human, compute more, wait, act, stop.

- VOI determines whether information is worth acquiring.
- human attention is a scarce resource/cost;
- Systemic Future Value can justify asking a high-cost human question when the answer establishes reusable policy and eliminates future work;
- VOC terminates optional reasoning when another pass is not worth it.

Shared conclusion: “only bother the human when consequences are material” is a decision problem, not a confidence threshold.

## 4. L-CTO / software architecture

Candidate actions: patch symptom, fix upstream contract, build shared adapter, defer, ask architect, compute more.

- Formal enforces architecture invariants/scope;
- Probabilistic represents uncertainty about consequence/reuse when needed;
- Numerical Strategic Value recognizes future work elimination and reusable capability;
- mesh/circular effects are valued through time-indexed state deltas and attribution, not a scalar leverage score.

Shared conclusion: upstream architectural repair can dominate local patching because future reachable work changes.

## Result

No new domain-specific rule is required by the shared core in any of the four cases. Differences are expressed through consumer state, models, objectives, observations, and authorized actions. This supports keeping Strategic Interaction as a composed plane pattern rather than a domain or fourth sibling.
