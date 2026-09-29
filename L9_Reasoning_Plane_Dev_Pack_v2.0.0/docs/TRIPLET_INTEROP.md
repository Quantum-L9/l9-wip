# Triplet Interoperability

## Plane claim types

- Formal -> admissibility/consequence
- Probabilistic -> belief/uncertainty
- Numerical -> utility/value

## Stable cross-family contracts

- Formal → Numerical: `FeasibleRegion`
- Formal → Probabilistic: `AdmissibleSupport`
- Probabilistic → Numerical: `BeliefState`
- Numerical → consumer: `UncertaintyRequirement`
- Numerical → Formal: `DecisionAssumption`
- Formal → consumer → Numerical: `ConstraintDelta`
- Consumer/evidence model → Numerical: `SystemicFutureValueProjection`
- Consumer → plane: `MetaAction` candidates

## Strategic composition

Strategic Interaction Reasoning compiles/joins Formal, Probabilistic and Numerical requests through shared ActorModel/StrategicState/Lookahead contracts. The composition does not transfer ownership:

- Formal constraints do not become probability;
- Probabilistic beliefs do not become facts;
- Numerical preferences do not become authority;
- Strategic response predictions do not become facts about another actor;
- Systemic future value is numerical valuation of evidence/modelled state deltas, not evidence creation.

## Dynamic invalidation

Every result binds the relevant state/model revisions. Material state, objective, policy, belief-model or actor-model changes require re-evaluation of affected outputs.
