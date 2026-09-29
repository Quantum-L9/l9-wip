# L9 Reasoning Plane Dev Pack v2.0.0

**State:** PRE-CODE SSOT / architecture-converged handoff

This pack formalizes the L9 Reasoning Plane as three independently deployable reasoning siblings plus shared contracts and composed reasoning patterns. It consolidates the Formal, Probabilistic, and Numerical architecture, the general decision substrate, Value of Information/Computation, dynamic state, signal-to-belief learning, strategic interaction/game-theoretic reasoning, Graph Memory boundaries, bounded higher-order beliefs, and a rigorous Strategic Value framework.

## North star

L9 does not hard-code intelligent behavior when the branch depends on uncertain consequences, competing costs, information value, computation value, timing, optionality, other actors, or future systemic effects. It represents the decision problem, invokes the appropriate reasoning families, and returns evidence-bound receipts to the consumer that owns action authority.

```text
                         L9 REASONING PLANE

        FORMAL               PROBABILISTIC              NUMERICAL
     admissibility               belief                  utility
          |                        |                        |
          +------------------------+------------------------+
                                   |
                    COMPOSED REASONING PATTERNS
                  dynamic / strategic / meta-decision
                                   |
                         consumer / AgentOS / DomainOS
```

The plane is **not** a super-node and does not own workflow orchestration, domain truth, agent authority, or operational mutation.

## Stable semantic owners

- **Formal Reasoning:** what is admissible, required, impossible, or contradictory?
- **Probabilistic Reasoning:** what should be believed given uncertainty and admitted evidence?
- **Numerical Reasoning:** what is preferable under a declared objective and quantitative state?
- **Consumer/runtime:** what question is being asked, what objective/policy applies, what actions are available/authorized, and what action is actually taken.

## Dynamic strategic extension

A decision state is time-indexed. Actions and observations change state, beliefs, incentives, and future action spaces. Strategic Interaction Reasoning is a **composed pattern**, not a fourth sibling:

```text
State(t)
  -> Formal pruning
  -> Probabilistic hidden-state / actor belief update
  -> Strategic response model / bounded lookahead
  -> Numerical Strategic Value
  -> Action(t)
  -> new observations
  -> State(t+1)
```

Game theory is a method family used inside this composition. `BoundedStrategicLookahead` is an algorithm family for exploring action/reaction trajectories under explicit horizon, belief-depth, and Value-of-Computation bounds.

## Strategic Value vocabulary

Machine-facing code does not use a vague `leverage_score`. Human shorthand may still say an intervention has leverage. Canonical machine vocabulary is:

```text
StrategicValue(a)
= ImmediateExpectedValue(a)
+ SystemicFutureValue(a)
- DirectCost(a)
- ExpectedRiskLoss(a)
- OpportunityCost(a)
```

`SystemicFutureValue` is the expected counterfactual improvement in future reachable utility caused by an intervention, excluding value already booked as its immediate effect. It captures capability unlock, recurring-cost reduction, future-work elimination, future-decision improvement, reusable asset value, dependency unlock, future-information improvement, and future action-space expansion without blindly summing overlapping categories.

## Signal bridge

Signal Leverage remains an external constitutional primitive that owns evidence-bearing signal propagation, meaning preservation, topology, eligibility, reconvergence, and evidence-bound write-back. The Reasoning Plane does **not** steal that concern. It consumes admitted evidence and reasons over what the signals imply.

```text
Observation
 -> Signal Leverage
 -> Evidence Admission
 -> Probabilistic hidden-state update
 -> Strategic Interaction
 -> Numerical valuation
 -> Action
 -> Outcome / new observations
```

## Graph Memory / Odoo boundary

- **Odoo:** authoritative commercial events/facts and a compressed human-facing projection such as `Negotiating Style`.
- **Graph Memory:** versioned, provenance-bound contextual/relational learning such as ActorObservations, ActorModels, strategy hypotheses, temporal interaction patterns, and higher-order beliefs.
- Dense inferred cognitive state is not duplicated into Odoo as hidden fields. Odoo may hold only a derived summary and opaque model reference/revision when useful.

## Core meta-action vocabulary

`ACT | LEARN | COMPUTE | WAIT | STOP`

The same substrate can answer:

- Should I act?
- Is it worth learning more?
- Is it worth computing more?
- Is it worth waiting?
- Should I commit or preserve optionality?
- How should scarce resources be allocated?
- What creates the greatest Systemic Future Value?
- What could change the current decision?
- How will another actor respond?
- What is my best response?
- Is the current policy exploitable?
- What information should be acquired, revealed, or withheld?
- Is a signal or threat credible under the actor's incentives?
- What present strategy has highest expected Strategic Value across a bounded action/reaction horizon?

## Folder map

- `docs/` canonical human-readable architecture
- `architecture/` machine-readable ADRs, invariants, authority and implementation blueprint
- `contracts/v2/` canonical v2 JSON Schemas
- `implementation/` build-ready component/filetree contracts
- `examples/` deterministic and synthetic acceptance fixtures
- `audit/` recursive extraction, alignment, completeness, and convergence evidence
- `source-lineage/` origin and supersession records
- `scripts/` deterministic validation
- `validation/` final observed validation report

## Explicit non-goals

- no merged super-reasoner;
- no fourth strategic sibling yet;
- no hidden plane orchestrator;
- no ML dependency;
- no model training requirement;
- no Odoo mutation by the plane;
- no Graph Memory truth authority;
- no autonomous policy activation;
- no direct peer routing outside Gate/Gate_SDK;
- no unbounded recursive beliefs or lookahead;
- no unproven scalar leverage score.
