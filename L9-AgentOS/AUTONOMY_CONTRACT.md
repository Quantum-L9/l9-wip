# AutonomyProfile and generic evaluator

## Ownership
AgentProfile declares bounded policy. AgentOS implements the universal evaluator once. Gate and capability owners enforce authorization independently. State stores policy inputs, grants/approval references and evaluations without interpreting the domain.

## Input binding
An evaluation binds profile digest, policy revision, Work Item state revision, ActionIntent digest, actor/principal, current authority references, context-plan/bundle identity, required evidence and budget window. Absent inputs remain unknown. Payload or target edits invalidate approval/evaluation; one character change cannot reuse authority for a different action.

## Decision procedure
Apply platform and deployment denials first. Confirm scope, profile compatibility and action allowlist. Resolve all required current authorization/approval/evidence. Check temporal constraints and budget. Check claim, concurrency and delegation limits. Apply deterministic profile rules; use model judgment only where a rule explicitly accepts a proposal that still passes mechanical checks. Emit one of deny, require_human, require_context, defer, delegate or allow_attempt with safe reason codes and evidence refs.

## Trigger semantics
Only committed StateTransition events, authenticated observations, authorized timer expirations or explicit requests trigger reevaluation. A raw database change notification is not a canonical event. The trigger can request refresh or reconsideration, not grant permission. Dedupe `(manifestation,event_id,profile_digest,policy_revision)` and prohibit unchanged context refresh from re-triggering itself.

## Bounded persistence
Budget reservations and claims must be conditional, durable and released/settled explicitly. Counters cannot reset on restart or profile alias change. Cost estimates are not actual spend; record both separately. With uncertain external spend/effect, reserve the liability until reconciliation rather than refunding it optimistically.

## Eviction mapping
Extract generic rules, evaluator mechanics, error/receipt discipline and lease-related constraints from Cursor-Governance. Leave coding-specific resource/path policies as a coding profile. Leave Program Execution's existing task readiness, program-state machine and controller authority at its owner. Do not reproduce those in AgentOS merely because LCTO uses the capability.

## Non-goals
This is not a new node-level security service, a global scheduler, a financial authority or a separate validator agent. It is the generic agent policy gate for requesting the next bounded capability attempt.
