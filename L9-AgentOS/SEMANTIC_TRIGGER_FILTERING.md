# Transition filtering without self-trigger loops

State emits committed mechanical transitions. AgentOS decides which transitions matter using bounded declarative AutonomyProfile trigger rules. The State node never decides that a particular payload field means a business event.

Each rule identifies allowed event labels/source classes and a bounded subscribed projection of the Work Item/context inputs. The generic evaluator computes an input fingerprint over that projection, profile/rule identity and relevant authoritative source revisions. Bookkeeping-only changes such as acknowledgment cursors, read times, telemetry and last-evaluated markers must not count as fresh decision evidence.

Persist causal dedupe and the last processed fingerprint under the same protected Work Item processing discipline. A new storage revision caused solely by recording a decision is not itself permission for another full reasoning round. A timeout retry cannot mint a new fingerprint by changing timestamps. A relevant changed observation, source revision or granted explicit wake condition can make work eligible again, subject to the remaining work-epoch budget.

Trigger filtering is deterministic where fields are known; a model-generated assertion cannot certify its own novelty or promote its output into independent corroboration. Record explicit no-op reasons. Re-evaluation, context refresh and capability attempt have separate budget and receipt accounting. This closes the feedback loop without converting useful circular leverage into perpetual self-observation.
