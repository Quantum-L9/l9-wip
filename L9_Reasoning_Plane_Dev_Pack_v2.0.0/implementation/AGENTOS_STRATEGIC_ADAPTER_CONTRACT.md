# AgentOS StrategicReasoningAdapter Contract

## Inputs

- current authoritative state refs;
- objective/policy refs;
- candidate actions and authorization refs;
- ActorModel / BeliefState refs;
- interaction history refs;
- max belief depth;
- strategic horizon;
- compute/resource budget;
- desired composed question.

## Outputs

- plane-native request plan;
- joined Formal/Probabilistic/Numerical receipts;
- StrategicInteractionResult;
- decision boundaries / uncertainty requirements;
- recommended next MetaAction or strategy candidate;
- no side effect.

## Invariants

- transport still uses Gate/Gate_SDK;
- no direct sibling URLs;
- adapter does not become a fourth reasoner;
- same semantic input -> same projection digest;
- missing ActorModel degrades explicitly;
- action authorization stays outside the adapter;
- LLM interpretation may propose observations/hypotheses but cannot silently promote them to admitted fact.
