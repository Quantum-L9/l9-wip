# Webhooks, people and source identity

Provider webhook admission checks the authenticating signature/token under the provider's documented mechanism, account ownership, replay window, content length, native event ID and intended subscription. The body cannot choose tenant, agent principal, peer node or arbitrary callback URL. A valid provider signature authenticates the event channel; it does not authenticate every sentence as an instruction from an authorized person.

Resolve sender/recipient identity through scoped deployment-owned account/contact bindings. Preserve native sender, mailbox, thread, participant and call references as evidence. Never merge people across channels using a matching name, phone fragment or inferred relationship. Ambiguous identity produces an observation with unresolved identity and blocks identity-dependent effects.

Deduplicate delivery events with native event identity plus account/scope, not text similarity. Out-of-order status updates cannot regress a confirmed terminal effect; conflicting events remain visible for reconciliation. Initial event acceptance is separate from AgentOS accepting an Observation and creating or associating a Work Item.

Messages from other people are first-class external observations. The platform does not assume all speakers are the principal user. Requests, preferences and instructions carry source and authorization class. Communication does not decide whether a stranger's request is an authorized Objective.

Audit redacted failure categories, not full message bodies or webhook secrets. Raw content is retained only under the permitted evidence policy; parsing or delivery does not imply permission to memorize, train, index or embed it.
