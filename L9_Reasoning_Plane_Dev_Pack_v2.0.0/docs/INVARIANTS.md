# L9 Reasoning Plane Invariants v2.0

This document is the canonical human-readable invariant companion to `architecture/INVARIANTS.yaml`.

## Plane

**RP-001** Reasoning Plane is an architectural and contract plane, not a merged runtime or super-reasoner.

**RP-002** Formal, Probabilistic, and Numerical Reasoning are current sibling families and remain independently deployable, replaceable, and degradable.

**RP-003** Consumers remain outside the plane and own domain meaning, question framing, objectives, policy, orchestration, authorization, and action execution.

**RP-004** Gate/Gate_SDK owns inter-node transport; siblings do not use peer URLs or import other node codebases.

**RP-005** A future sibling is admitted only for a distinct semantic claim not faithfully composable from existing siblings and only after recurring consumers and independent failure semantics are demonstrated.

**RP-006** A composed reasoning pattern is not a sibling merely because it is reusable or mathematically rich.

**RP-007** Reasoning outputs are evidence/recommendation surfaces and never become operational authority by themselves.

## Formal

**FR-001** Formal Reasoning owns symbolic admissibility, constraint satisfaction, deductive consequence, and conflict semantics.

**FR-002** Formal output may express MUST, MAY, IMPOSSIBLE, SAT, UNSAT, MULTIPLE, or explicit unknown/conflict states under versioned contracts.

**FR-003** MAY means formally admissible and does not imply probability, preference, or priority.

**FR-004** Unverified memory/context is not automatically admitted as fact.

**FR-005** Contradictory admitted facts that affect a query produce explicit conflict/UNSAT handling when supported.

**FR-006** Formal Reasoning does not own business utility, ranking, probability estimation, or final decision authority.

**FR-007** Formal provider failure has explicit degraded semantics and never authorizes another family to impersonate formal truth.

## Probabilistic

**PR-001** Probabilistic Reasoning owns belief updating, predictive distributions, uncertainty quantification, and information-gain semantics over admitted models/evidence.

**PR-002** Bayesian inference is a method family, not the architectural identity.

**PR-003** No hidden prior is permitted; prior representation, provenance, scope, revision, and source kind are explicit.

**PR-004** Probabilistic Reasoning consumes admitted evidence; it does not acquire evidence or silently promote retrieved context.

**PR-005** Evidence confidence metadata is not automatically a likelihood weight.

**PR-006** Formal AdmissibleSupport may remove logically impossible states before probabilistic normalization.

**PR-007** Probability does not promote a proposition to formal truth.

**PR-008** Probability zero is not equivalent to Formal IMPOSSIBLE unless the zero derives from an admitted hard support restriction.

**PR-009** Missing model/prior/evidence never silently becomes uniform probability, 0.5, or another arbitrary default.

**PR-010** BeliefState is immutable/versioned evidence bound to model, prior, evidence, support, provider and diagnostics.

**PR-011** A prior posterior may become a new prior only through explicit compatibility and evidence anti-double-counting checks.

**PR-012** Approximate/sampling providers expose inference mode, seed/reproducibility inputs where applicable, and diagnostics.

**PR-013** Raw unbounded samples do not cross public contracts inline; use bounded summaries and artifact references.

**PR-014** Information gain measures belief change; Value of Information measures decision utility and is not owned by Probabilistic Reasoning alone.

**PR-015** Better information may increase or decrease certainty; calibrated belief is the objective, not maximum confidence.

## Numerical

**NR-001** Numerical Reasoning owns quantitative decision evaluation under a declared objective and compatible utility units.

**NR-002** DecisionModel/cartridge remains quantitative authority; the numerical core contains no hidden domain formulas, weights, thresholds, or scoring fallbacks.

**NR-003** Numerical Reasoning installed without a DecisionModel is domain-empty.

**NR-004** einsum, matrix multiplication, optimization libraries and similar mechanics are primitives/providers, never architectural identities.

**NR-005** Execution and optimization providers are replaceable without changing DecisionModel semantics.

**NR-006** Required unknown numerical inputs do not silently become zero, false, average, default weights, or fabricated empirical parameters.

**NR-007** Numerical validation is evidence, not authorization.

**NR-008** Numerical Reasoning may consume BeliefState but may not mutate posterior belief.

**NR-009** Numerical optimum is conditional on the admitted model/state/objective and never implies formal feasibility unless bound to applicable formal constraints.

**NR-010** Answer shape follows question shape; allocation/frontier problems may return vectors or sets rather than one winner.

## Taxonomy

**TAX-001** Canonical vocabulary is Reasoning Family -> Method Family -> Method/Algorithm -> Primitive -> Provider.

**TAX-002** Callers depend on the highest stable semantic contract and not on a current method, primitive, or provider.

**TAX-003** Strategic Interaction Reasoning is a composition pattern; Game-Theoretic Analysis is a method family; BoundedStrategicLookahead is an algorithm family.

**TAX-004** A provider name must never become the reasoning-family identity unless that provider itself is intentionally the product boundary.

## Dynamic State

**DYN-001** Decision state is time-indexed; state at t and state at t+1 are distinct revisions.

**DYN-002** Material actions, observations, natural evolution, policy changes, or objective changes may invalidate prior reasoning outputs.

**DYN-003** Implementations may reuse incremental solver/inference state but may not reuse stale semantics when a material premise changed.

**DYN-004** Material observations and derived patterns carry temporal scope, freshness, validity, and supersession where applicable.

**DYN-005** One-off interaction outcomes do not silently become permanent actor traits.

**DYN-006** Predicted future state and realized state remain distinct evidence classes.

## Signal Bridge

**SIG-001** A signal has no globally fixed meaning; evidentiary value is conditional on state, history, actor model, timing, provenance, reliability, correlation, and incentives.

**SIG-002** More signals do not automatically imply more information or certainty; duplicates and correlated manifestations must not be treated as independent evidence.

**SIG-003** Strategically generated signals require incentive-aware likelihood modeling when material.

**SIG-004** Signal Leverage remains external semantic owner of signal propagation, meaning preservation, eligibility, topology, reconvergence and evidence-bound write-back.

**SIG-005** Probabilistic Reasoning owns what admitted signals imply for belief; Signal Leverage does not infer hidden state.

**SIG-006** SignalOpportunity stages distinguish unobserved, unrecognized, unrouted, degraded, admitted-unused and realized signal states.

**SIG-007** Signal metrics must preserve uncertainty in partially unknowable denominators; estimated capture efficiency is not ground truth.

**SIG-008** A signal is realized as learning only when it changes an eligible future belief, decision, capability, cost, constraint, or behavior.

**SIG-009** Hard safety, privacy, authority and required audit signals are not discarded merely because expected economic value is low.

## Actor Model

**AM-001** ActorModel is versioned derived belief state, not authoritative identity, personality truth, or a moral label.

**AM-002** Behavioral variables are overlapping and context-scoped; do not flatten them into one mutually exclusive opponent-type enum.

**AM-003** ActorObservation is immutable evidence; ActorModel is a supersedable inference over observations and context.

**AM-004** New outcomes may reinforce, weaken, broaden, narrow, or contradict an ActorModel.

**AM-005** Reservation values, urgency, alternatives, strategy, credibility and response tendencies are beliefs unless directly authoritative.

**AM-006** Graph Memory may retain relational/temporal hypothesis state but never becomes authoritative commercial truth.

**AM-007** Odoo owns authoritative commercial facts/events when in scope and may expose a concise human-facing Negotiating Style projection.

**AM-008** Dense inferred cognitive state is not duplicated into hidden Odoo columns merely to avoid a memory dependency.

**AM-009** Odoo may retain opaque ActorModel reference/revision metadata without depending on Graph Memory for startup correctness.

**AM-010** Human-facing summaries are derived projections and must not be re-promoted as stronger evidence than their underlying observations/model.

## Higher Order Belief

**HOB-001** Belief depth 0 is world/hidden-state belief; depth 1 models another actor; depth 2 models the other actor model of the focal actor; deeper levels recurse explicitly.

**HOB-002** Every strategic request declares a maximum belief depth.

**HOB-003** Belief depth is a computational resource, not an intelligence score.

**HOB-004** Value of Computation may terminate deeper higher-order reasoning when marginal decision improvement no longer justifies cost.

**HOB-005** Higher-order belief remains belief and never becomes fact by nesting or confidence alone.

## Strategic Interaction

**STR-001** Other actors are endogenous parts of the decision environment when their behavior can respond to our choices.

**STR-002** Assertions made by strategic actors are observations, not automatically facts.

**STR-003** Strategically generated evidence must account for sender incentives when material.

**STR-004** A best response is conditional on an explicit other-actor strategy or belief model.

**STR-005** An equilibrium is a solution concept under declared models, not truth, policy, or execution authority.

**STR-006** A deterministic engine may return a mixed strategy; stochastic execution requires explicit authorization and reproducibility/seed receipts where applicable.

**STR-007** Repeated-interaction effects such as reputation, relationship capital and future bargaining position belong in future-state valuation when material.

**STR-008** Commitment may create positive strategic value while destroying optionality; both effects must be modeled without double counting.

**STR-009** Information acquisition and information disclosure are distinct decision problems.

**STR-010** Recursive beliefs and action/reaction lookahead are bounded by explicit depth, horizon, resource, and Value-of-Computation controls.

**STR-011** Strategic Interaction Reasoning is currently a composed triplet pattern and not a fourth sibling.

**STR-012** Game theory is a method family, not a node identity.

**STR-013** Predictions about another actor are distributions/hypotheses and not promises of behavior.

**STR-014** Zero-sum, constant-sum, positive-sum, mixed-motive and coordination structures must not be silently conflated when they change strategy.

**STR-015** Strategic influence does not require deception; truthful signaling, sequencing, commitment, framing, option structuring and incentive design may create cooperative value.

**STR-016** The stronger signal may be the mismatch between observed action and what would make sense under competing hidden-state hypotheses.

**STR-017** Strategic Lookahead evaluates bounded trajectories and may not claim perfect prediction of future actor actions.

**STR-018** No ML model is required for v2 strategic reasoning; explicit priors/response models and calibrated history are valid first implementations.

## Strategic Value

**SV-001** StrategicValue is a Numerical valuation composition, not an independent reasoning sibling.

**SV-002** Canonical decomposition is ImmediateExpectedValue + SystemicFutureValue - DirectCost - ExpectedRiskLoss - OpportunityCost.

**SV-003** Machine contracts do not use an undefined leverage score; leverage may remain human shorthand for high systemic future value.

**SV-004** SystemicFutureValue is expected counterfactual improvement in future reachable utility caused by an intervention, excluding value already counted as immediate effect.

**SV-005** Future work elimination is a first-class SystemicFutureValue dimension.

**SV-006** Capability unlock, recurring cost reduction, future decision improvement, reusable asset value, dependency unlock, future information improvement and action-space expansion are explanatory dimensions, not blindly additive terms.

**SV-007** Each underlying state delta is booked once; anti-double-counting is mandatory.

**SV-008** Predicted StrategicValue and realized value remain distinct; realized outcomes calibrate future estimates.

**SV-009** Systemic future effects may use ONE_WAY, BILATERAL, CLOSED_LOOP or MESH topology without changing what value means.

**SV-010** Cycles are unrolled through time and each new incremental state delta is valued once until convergence/horizon/budget.

**SV-011** Multi-causal mesh effects require explicit attribution and overlap handling.

**SV-012** Attribution shares may not create more value than the underlying counterfactual state delta.

**SV-013** Propagation drag, latency, maintenance, stale context, transformation loss and coordination burden are negative effects when material.

**SV-014** StrategicValue comparisons require compatible objective/utility semantics or an explicit conversion model.

## Meta Decision

**META-001** Business actions and cognitive actions may both be represented as candidate MetaActions.

**META-002** Canonical v2 MetaAction kinds are ACT, LEARN, COMPUTE, WAIT, STOP.

**META-003** Consumer/runtime owns candidate generation, authorization, sequencing, dispatch, and action authority.

**META-004** STOP is a first-class candidate when continuation is optional; hard ceilings remain independent mandatory bounds.

**META-005** Reasoning should replace bespoke procedural branching when the branch depends on uncertain consequences, competing costs, information/computation value, timing, optionality, strategic response, allocation, or future systemic effects.

**META-006** Security, authorization, protocol, schema/type, non-negotiable policy and resource ceilings remain hard constraints and are never overridden by utility.

## Information Value

**VOI-001** Positive VOI identifies a valuable LEARN action; it does not hard-code Research as executor.

**VOI-002** Research, Memory, File, Human, Test, API, Enrichment, Sensor, Database, WAIT-for-evidence and other authorized sources may compete as LEARN actions.

**VOI-003** Information value depends on whether new evidence can change decision utility, not merely whether it reduces entropy.

## Computation Value

**VOC-001** Value of Computation compares expected decision improvement plus non-overlapping SystemicFutureValue against compute, latency, opportunity and risk costs.

**VOC-002** Optional further computation should stop when the best authorized COMPUTE action has non-positive marginal StrategicValue, subject to hard validation/resource bounds.

## Timing

**TIME-001** WAIT is a deliberate action whose value depends on state evolution, natural evidence arrival, delay cost, lost opportunity and preserved options.

## Optionality

**OPT-001** Reversibility and preserved future options must be modeled without double counting the same future state effect in SystemicFutureValue or OpportunityCost.

## Allocation

**ALLOC-001** Resource allocation is Numerical optimization over Formal constraints and Probabilistic outcomes and may return a portfolio/vector/frontier.

## Decision Boundary

**BOUND-001** Decision-boundary analysis identifies conditions that would change the preferred decision; it does not predict those conditions will occur.

**BOUND-002** Decision-relevant uncertainty has priority over uncertainty reduction for its own sake.

## Adapter

**ADP-001** StrategicReasoningAdapter is a shared consumer-side projection/join adapter, not a reasoning node.

**ADP-002** StrategicReasoningAdapter may compile plane-native requests and join receipts but owns no policy, orchestration state, action execution or hidden truth.

**ADP-003** Stable adapter contracts belong with plane semantics; consumer runtimes own execution wiring.

## Failure

**FAIL-001** Failure of one reasoning family never authorizes semantic substitution by another.

**FAIL-002** Graph Memory unavailability degrades actor-model reasoning but does not break authoritative Odoo/business operation.

**FAIL-003** Missing ActorModel or response model state is explicit Unknown/insufficient model and is not fabricated.

**FAIL-004** Reasoning loops terminate with explicit status and receipt.

## Naming

**NAME-001** Einesium is historical lineage; canonical architecture identity is L9 Numerical Reasoning.

**NAME-002** Bayesian inference is a method family beneath L9 Probabilistic Reasoning.

**NAME-003** Clingo, Clorm, PyMC, NumPyro, Stan, einsum, NumPy, SciPy, JAX, Torch, Z3 and similar tools/providers are not node identities.

**NAME-004** Canonical machine value terms are StrategicValue and SystemicFutureValue; legacy ExpectedLeverageValue/LeverageProjection/NetStrategicValue names are superseded.

**NAME-005** Signal Leverage is retained only as the proper name of the external constitutional signal component unless separately renamed by its owner.

## Validation

**VAL-001** Reference fixtures must validate against current JSON Schemas.

**VAL-002** Probabilistic exact reference math must be hand-computable and independently checked.

**VAL-003** StrategicValue arithmetic must be independently recomputed from components.

**VAL-004** SystemicFutureValue topology fixtures must prove one-way, bilateral, closed-loop and mesh behavior without double counting.

**VAL-005** Strategic interaction fixtures must prove bounded depth/horizon and probability normalization.

**VAL-006** Pack validation includes stale-vocabulary, ownership-collision, cache/junk, parse, schema, example and SHA integrity scans.
