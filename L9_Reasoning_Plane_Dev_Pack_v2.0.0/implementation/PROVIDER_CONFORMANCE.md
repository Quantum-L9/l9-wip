# Provider Conformance Contract

A future probabilistic provider is admissible only if all gates pass.

## Semantic gates

- accepts the same public `ProbabilisticModel` semantics or an explicitly versioned extension;
- does not require provider-specific syntax in consumer requests;
- honors explicit prior and support;
- does not fetch hidden evidence;
- can produce provider-neutral `BeliefState`.

## Boundedness gates

- enforces runtime/deadline budget;
- enforces model/evidence/sample limits declared by runtime policy;
- externalizes large traces/samples;
- reports resource observations.

## Reproducibility gates

For stochastic providers:

- reports seed/RNG algorithm where applicable;
- reports provider/version;
- reports inference mode;
- identical seed/config/input is reproducible within the provider's declared tolerance when the provider promises reproducibility.

## Diagnostic gates

Provider declares mandatory diagnostics for each inference mode. `SUCCESS` is forbidden when mandatory diagnostics fail.

## Oracle gates

Where an exact fixture exists, approximate posterior summaries must match the exact reference within declared fixture tolerance.

## No semantic downgrade

A provider with richer internal posterior representation may expose bounded artifact refs, but the normalized public `BeliefState` remains the minimum semantic contract.
