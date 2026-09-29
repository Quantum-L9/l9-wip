# Cold resume, wakeups and bounded execution discovery

AgentOS must not keep a second directory database just to discover its Work Items after restart. The proposed State `state.list` capability enumerates authorized references by scope, admitted schema and generic lifecycle with bounded pagination. It is not arbitrary domain-field search or a Mongo query interface. Load exact payloads by returned StateRef and recheck current revision/authorization before advancing.

At startup, enumerate only the manifestation's authorized schemas/scope, recover active Work Items and original intent receipts, and reconcile in-flight unknown effects. A page cursor records explicit snapshot/watermark semantics. Concurrent inserts/updates require event catch-up or a repeat bounded scan, not a claim of a globally atomic snapshot.

Profile timing rules may declare a wake condition, but do not imply that Gate is a durable timer service. The first implementation uses a bounded AgentOS readiness loop over its recovered authorized active Work Items and durable next-evaluation metadata, with State events waking it for new changes. Time eligibility is checked against current authority and server time; the loop never grants its own scope. A separate existing timer capability can replace wake delivery after its contract is verified, without moving policy into State or Mongo triggers.

After a downtime gap, wake delivery may be late or duplicated; event/condition evaluation is idempotent and bounded. Multiple replicas claim exact work with fences before effects. A timer expiry causes reconsideration, not automatic execution. Event-subscription readiness and consumer cursors are durable, scope-bound and recoverable; no unbounded all-tenant scan is permitted.

`state.operation.inspect` resolves original mechanical mutation receipts. It does not prove whether a different domain provider executed an effect; AgentOS must consult that capability's authoritative operation receipt. Cold resume and scoped enumeration are STATE-03/AG-03 acceptance obligations.
