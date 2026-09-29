# Strategic Interaction Reasoning

## Identity

Strategic Interaction Reasoning is a **composed reasoning pattern** for environments containing other decision-makers whose actions depend on their own objectives, information, beliefs, incentives, and expectations about us.

It is not currently a fourth Reasoning Plane sibling.

## Cardinal question

> Given other decision-makers with their own objectives, information, beliefs, and possible responses, what strategy should I adopt?

## Triplet composition

```text
FORMAL
feasible actions / commitments / constraints
      ↓
PROBABILISTIC
hidden state / actor type / response belief
      ↕
STRATEGIC INTERACTION MODEL
how choices alter incentives, beliefs, signals, and responses
      ↕
NUMERICAL
payoffs / Strategic Value / best response / allocation
```

Strategic interaction couples Probabilistic and Numerical Reasoning across time. The actor's incentives affect the likelihood of signals and responses; the resulting response distribution affects action value.

## Game theory relationship

Game theory is a method family beneath Strategic Interaction Reasoning. Applicable subfamilies include:

- best-response analysis;
- equilibrium analysis;
- mixed-strategy analysis;
- Bayesian/incomplete-information games;
- sequential/extensive-form games;
- repeated games;
- signaling and credible commitment;
- exploitability/regret analysis;
- bargaining;
- mechanism design.

Method family does not equal architecture. No `GameTheoryNode` is created merely because these methods are useful.

## Zero-sum vs positive-sum

The interaction model must declare whether the modeled payoff structure is approximately `ZERO_SUM`, `CONSTANT_SUM`, `POSITIVE_SUM`, `MIXED_MOTIVE`, `COORDINATION`, or `UNKNOWN` when that classification affects strategy.

Business negotiation is often positive-sum or mixed-motive. Poker is approximately zero-sum. Mixed/randomized strategies may be valuable in adversarial settings while consistent behavior may create reputation and relationship value in repeated business interactions.

## Strategic influence vs deception

`StrategicInfluence` includes truthful signaling, framing, commitment, concession design, information disclosure, sequencing, option structuring, and incentive design.

Deception is not required for strategic behavior. A cooperative negotiation can increase both parties' utility by changing incentives or splitting surplus differently.

## Assertions by strategic actors

A statement such as “I cannot pay more than .31” is an observation in negotiation context, not automatic truth. The model may maintain a distribution over reservation value, urgency, alternatives, and bargaining strategy.
