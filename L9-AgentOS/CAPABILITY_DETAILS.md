# AgentOS capability behavior

The public candidate action family is `agent.work.submit`, `agent.work.advance`, `agent.work.inspect`, `agent.work.reconcile` and `agent.work.cancel`. API_CONTRACT.md owns the binding index and request/result schema references; no synonymous route families are introduced.

`agent.work.submit` validates Objective/profile/observation/owner binding and persists a universal Work Item before acknowledging it. `agent.work.advance` performs a bounded turn under the current revision/fence/context, producing an explicit no-op, waiting, blocked or next-intent outcome. It persists exact ActionIntent and operation identity before any approved capability call. `agent.work.inspect` returns authorized current state and receipt projections without advancing work. `agent.work.reconcile` consults authoritative prior-effect receipts; it cannot blindly retry uncertain effects. `agent.work.cancel` requests bounded cancellation and distinguishes requested, confirmed and compensating outcomes.

Profile compilation is a deterministic local build operation over admitted source artifacts, not a new Gate action in this slice. Manifestation binding/activation belongs to the externally authorized deployment control plane. Observation interpretation, Decision production, resume and delegation are internal shared AgentOS mechanics composed within the universal Work Item lifecycle, not extra public route synonyms.

All public actions address generic manifestation and Work Item IDs. A profile supplies semantics and independently granted capability requests; no action name encodes an agent name. Domain capability absence can block one request without requiring an AgentOS fork.

Reconciliation can remain pending or unknown. Similar memory, cached narrative, process exit zero or a profile-provided success string cannot manufacture completion.
