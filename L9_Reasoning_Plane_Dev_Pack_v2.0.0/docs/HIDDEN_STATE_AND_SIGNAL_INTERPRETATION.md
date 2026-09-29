# Hidden State and Context-Conditioned Signal Interpretation

## Hidden-state model

Visible state is what is admitted as known. Hidden state is what matters but is not directly known. Probabilistic Reasoning maintains beliefs over hidden state rather than converting clues into brittle Boolean rules.

Example:

```text
HiddenStateBelief(t)
VALUE_HAND       .47
BLUFF            .28
TRAP_LINE        .14
MARGINAL_VALUE   .08
OTHER            .03
```

A new observation updates the distribution; it does not append a permanent rule such as `river_overbet = value`.

## Constitutional signal law

> A signal has no globally fixed meaning. Its evidentiary value is conditional on current state, prior observations, actor model, timing, provenance, reliability, correlation, and plausible incentives.

The old observation remains part of the evidence record; its interpretation may change as later evidence alters the joint context.

## Evidence dependence

More signals do not automatically imply more certainty. Correlated observations, duplicate sources, copied reports, or multiple manifestations of one latent cause must not be treated as independent evidence.

A better-informed posterior can be less certain than its prior. The goal is calibrated belief, not maximum confidence.

## Strategically generated signals

When another actor chooses an action partly to influence our behavior, the signal-generation process is endogenous:

```text
hidden state
+ actor objective
+ actor beliefs
+ incentives
-> chosen action/signal
```

Inference therefore asks not only “what state correlates with this signal?” but also “under which hidden states and objectives would choosing this signal be rational?”

This is the bridge between Probabilistic Reasoning and Strategic Interaction Reasoning.
