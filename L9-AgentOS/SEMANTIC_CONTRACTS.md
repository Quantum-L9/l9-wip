# AgentOS semantic contract kernel

## S1. Agent Manifestation
A manifestation is one authenticated runtime identity bound to a resolved AgentProfile and authorized operating scope. Profile identity, manifestation identity, runtime replica identity and security principal are distinct. Two manifestations can share a profile without sharing permissions or data. A replica restart may resume the same manifestation only through deployment identity and fenced state ownership.

The manifestation does not own a private copy of the State, Context, Evidence or Memory service. It owns agent-semantic decisions and invokes those capabilities through Gate. Node deployment is admitted externally. A consumer deployment uses the same semantic core but never registers trusted actions or receives node dispatch.

## S2. AgentProfile
An AgentProfile is not one config file. It is the complete declarative manifestation of an agent. The canonical artifact is the resolved output of governed source fragments, not a directory name or prompt. It binds identity presentation, Objective policy, Work Item kinds, observation mapping, state semantics, context needs, memory policy, autonomy policy, capability requests, interaction policy, delegation and projections.

A profile can narrow behavior, never grant infrastructure trust or exceed authenticated permissions. Compilation requires closed references, deterministic merges, conflict rejection, schema checks, source digests and no ambient environment input. Profile content is data, not arbitrary code. Providers implement capabilities outside the profile.

## S3. Objective
An Objective describes an outcome, scope, success conditions, constraints, governing evidence and owner. It can be explicitly supplied by an authorized person/capability or derived from an observation only under the profile's declared rules. An observation from another person is not automatically an instruction from the operator. An Objective cannot silently expand after work starts; amendments produce a new revision and re-evaluation.

## S4. Work Item
A Work Item is the durable operational unit of agent work advancing an Objective. It has a stable identity, one active owner manifestation, a pinned profile digest, kind, bounded payload, references, universal lifecycle and optional profile-defined dimensions. The StateRecord/receipt supplies its authoritative persistence revision; the payload cannot forge that revision. A domain label never creates another shared primitive.

A Work Item may have parent/child/dependency relations to other Work Items. Delegation creates a bounded child or capability attempt, not another ownership system. A completed child does not automatically prove the parent Objective. No Work Item is itself memory, external business truth, authority or an approval.

## S5. Observation
An Observation names source kind, source identity/revision, observed time, subject scope, content/evidence reference, modality and integrity. It may be text, image, audio, video, a structured event or document. Large media remains at the Evidence/artifact owner. Normalization through Ingest does not change who said or observed something. An observation can create zero or several Work Items according to profile semantics.

## S6. ContextNeed
A ContextNeed names the Objective, Work Item revision, profile/context variant, required facts, scope, freshness, budget and expected authority classes. It contains demand, not retrieved facts or arbitrary backend queries. Context supplies a bounded bundle with source-specific coordinates. Missing required context cannot be hidden by retrieving more optional material.

## S7. Decision
A Decision records the question, selected outcome, compact rationale, evidence refs, unknowns, conflicts and relevant profile/context digests. It need not include private chain-of-thought. It may conclude no action, ask a person, request more context, delegate or construct one or more ActionIntents. Confidence is evidence-relative, never authority.

## S8. ActionIntent
An ActionIntent proposes one owner-advertised capability operation bound to the originating Work Item revision, current profile, actor, desired outcome, bounded payload, required evidence and stable logical effect identity. Destination nodes, credentials and database commands are not model-authored intent fields. The action name is checked against effective permitted capabilities. An intent is not execution.

## S9. AutonomyEvaluation
The generic evaluator considers the current authorized profile policy, Work Item state, fresh evidence, grants, budgets, revocations and action class. Results are allow_attempt, require_human, require_context, defer, deny or delegate. More confidence cannot override a deny or missing required input. An allowed attempt still crosses Gate and destination authorization. An approval must bind the exact intent/payload/profile/revision and expire or revoke according to its owner contract.

## S10. Receipt and State Transition
A receipt is accepted only when issuer, scope, logical operation, request digest, trace, action and result schema match the outstanding intent. A transport acknowledgment may prove acceptance, not completion. The resulting Work Item change is applied with expected revision/fence; an out-of-order receipt cannot overwrite newer state. The owner's original receipt is retained as evidence.

## S11. Interaction and delegation
Interaction can be with operator, employee, supplier, customer, contractor, another authorized person or system. Presentation identity is distinct from actor authority. Contact selection and credential access belong to capabilities, not arbitrary prompt fields. Delegation carries a strict subset of allowed scope/actions/budget and explicit expiry; downstream redelegation needs explicit permission. Human-services examples remain examples until an admitted capability owns execution.

## Contract composition
The contracts above remain meaningful without Mongo, Graphiti, LlamaIndex, OpenClaw or any particular model. Reverse conformance checks each infrastructure owner against these behaviors. No node is required to recognize a manifestation's name or domain vocabulary.
