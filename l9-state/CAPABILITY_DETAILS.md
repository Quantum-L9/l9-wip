# State capability contract

## StateRecord
A StateRecord contains an opaque owner-schema-bound payload, stable object identity, requested resource scope verified against the caller, authoritative revision, payload/schema digests, lifecycle metadata, ownership principal and references to its commit receipt. State assigns revisions. Payloads cannot select Mongo collection names, operators, credential refs or routing destinations.

## Conditional mutation
A mutation carries object ref, expected revision, stable operation ID, expected schema/profile binding, proposed replacement/typed patch and optional required fence. State validates request shape, scope, admitted schema, content limits and current revision. It commits exactly one next revision or returns a conflict/current-ref response with no partial effect. The public patch language must be small and provider-neutral; arbitrary JSONPath evaluation, Mongo update documents or code execution are not allowed.

## Operation identity
Scope + operation ID is unique. Same key and same canonical request yields the original receipt. Same key and different canonical request produces IDEMPOTENCY_COLLISION. Caller business identity is not replaced with payload similarity. A lost acknowledgment is resolved via the same operation lookup; retry cannot silently create another revision.

## Claim
Claim identity is separate from work ownership. Acquire with resource scope, owner identity, TTL and expected binding; return lease ID, expiry, fencing token and receipt. Renew/release require the exact owner and current fence. Reassignment increases the fence. Expiry is checked against server time in every protected write. Database TTL cleanup never defines the instant at which authority expires.

## Events
Each successful semantic mutation produces one canonical StateTransitionEvent identity in the same transaction as the revision and receipt. Event order is per object/journal partition, not globally total. `state.events` returns a scope-filtered ordered batch and opaque provider-independent cursor. `state.ack` records consumer progress without letting one consumer suppress another's events. Delivery is at least once; receivers deduplicate. Canonical events carry safe change metadata and refs, not unrestricted full private payloads.

## Checkpoints
`state.checkpoint` stores a typed provider-neutral continuation snapshot or content reference under the same revision/idempotency law. It is not a LangGraph serialization endpoint. A framework checkpointer can be an optional adapter translating to this contract. Never pickle arbitrary objects or persist credentials. A checkpoint is a convenience view over owned state, not another revision authority.

## Tombstone and retrieval
Deleting/tombstoning prevents future ordinary reads and references according to retention policy, but keeps required audit metadata and erasure receipts. Legal-hold instructions are authorized inputs, not locally invented law. History reads are separately authorized. A schema evolution cannot make an old protected payload public.
