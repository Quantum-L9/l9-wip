# Manifestation lifecycle and recovery

## Startup
Resolve deployment principal, trust role, admitted runtime build and authorized scope. Resolve the admitted AgentProfile digest and required contract versions. Verify owner capability readiness through Gate. Recover outstanding state claims and unfinished attempts before consuming new observations. Required State unavailability blocks consequential work; optional Memory/Context sources follow explicit profile degradation rules.

## Observation loop
Authenticate source and scope -> deduplicate source occurrence -> create/attach Observation -> evaluate profile mapping -> create/update Work Item through State -> request required context -> issue Decision/ActionIntent or no-op. An already structured source need not go through Ingest; raw content does. An inbox's many messages may map to one Work Item, multiple Work Items or none.

## Consequential attempt protocol
1. Read exact Work Item revision and effective profile binding.
2. Acquire a fenced bounded claim; record intent, request digest and stable operation key durably.
3. Evaluate current autonomy policy and required external approval/grants. Persist the outcome and evidence refs.
4. Immediately before dispatch, recheck revocation, intent identity, budget and lease; call Gate once through the SDK.
5. Validate the returned owner receipt and classify accepted/in_progress/completed/refused/unknown.
6. Commit receipt-linked Work Item state with expected revision. Persist event consumption and budget counters so restart cannot reset them.

## Crash cases
Before intent commit: no external action. After intent commit but before dispatch: safe to resume only after confirming not dispatched and rechecking authority. After dispatch but before response: effect_unknown, reconcile through destination operation identity. After receipt but before state update: reapply receipt idempotently; do not dispatch again. After State commit but before event acknowledgment: replay the event as a no-op under its consumption identity.

## Claims versus authority
A State lease proves exclusive mechanical ownership of a resource revision window. It does not authorize an external action. The destination must enforce grant/approval and operation idempotency. A fencing token becomes useful only where stale writers are rejected; merely attaching a token to a log is not enforcement.

## Delegation and concurrency
Multiple Work Items may execute concurrently if profile and grants allow it and state/resource claims do not conflict. Concurrency is a generic runtime mechanism, not a fixed number baked into the product. Parent Work Item waits on stable child/capability receipts. One node's successful transport response cannot substitute for the downstream capability's semantic result.

## Completion
WorkItem.completed requires profile-defined success evidence and settlement of outstanding effect-unknown conditions. Objective completion is separately evaluated; one completed Work Item may not fulfill the whole Objective. Explicit no-op or rejected action remains an auditable outcome. A human-facing summary never becomes a completion receipt.

## Rehydration
Resume bundle binds manifestation identity, profile digest/compiler identity, Work Item records/revisions, outstanding operation keys, claims/fences, source/event cursors, context bundle refs, unresolved facts and pending owner receipts. Secrets are re-resolved, never serialized into checkpoints. Context is refreshed if its source/revocation/expiry binding is stale. Do not replay model reasoning as a substitute for reading exact durable state.
