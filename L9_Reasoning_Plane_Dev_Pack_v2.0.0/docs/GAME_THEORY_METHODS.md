# Game-Theoretic Methods inside Strategic Interaction Reasoning

Game theory is admitted as a method family because other actors may adapt their behavior in response to our strategy. It is not a standalone semantic owner.

## Method families / questions

- **Best response:** what action/strategy maximizes our value given an explicit model of the other actor?
- **Response forecasting:** what response distribution follows from a candidate action under current ActorModel/BeliefState?
- **Equilibrium analysis:** what strategy profile is mutually resistant to unilateral deviation under the declared model?
- **Mixed strategy:** when strategic unpredictability matters, what action distribution is appropriate? Deterministic computation may output a distribution; execution randomness is separately governed.
- **Exploitability / regret:** does a predictable policy let another actor systematically improve at our expense?
- **Sequential/extensive-form analysis:** how do action order and information revelation change value?
- **Repeated interaction:** how do reputation, trust, retaliation/forgiveness, and future bargaining position alter present value?
- **Signaling:** what strategically generated observations are credible under sender incentives?
- **Commitment:** when does removing our own flexibility improve strategic outcomes?
- **Bargaining:** how is cooperative surplus created/split under asymmetric information, alternatives and urgency?
- **Mechanism design:** what rules/incentives make desired behavior individually rational? Deferred from execution until explicitly earned.

## Inverse strategic reasoning

Observed action can be used to infer hidden state by asking which hypotheses would make the action rational under the actor's believed context. This is especially useful when surface heuristics invert after conditioning on incentives.

Example pattern:

```text
observe action
 -> enumerate competing hidden states / actor objectives
 -> estimate P(action | hidden state, actor model, context)
 -> posterior update
 -> recompute best response
```

## No perfect-agent assumption

Other actors need not be perfectly rational. Response models may include bounded rationality, habitual tendencies, noise, or unknown behavior. Game-theoretic solution concepts are conditional tools, not claims that humans are optimal solvers.
