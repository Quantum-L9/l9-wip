# State lifecycle and retention mechanics

This document describes the STATE-04 implementation boundary. It does not define legal, business, or organizational retention policy.

## Public lifecycle

The public lifecycle is revisioned:

```text
active --state.tombstone--> tombstoned --state.restore--> active
                                      \
                                       \--internal hard erase--> erased
```

`erased` is terminal in v1.

### Tombstone

`state.tombstone` is a normal CAS/fence-protected State mutation. It creates `revision + 1`, lifecycle `tombstoned`, one canonical journal event, and one immutable OperationKey receipt. Tombstoning suppresses ordinary current reads but does not itself destroy retained payload bytes. Exact retained revisions remain readable while their payload is retained.

### Restore

`state.restore` is admitted only when the current lifecycle is `tombstoned`, the caller names a retained prior revision of the same object, the immutable schema binding matches, CAS succeeds, and any active claim/fence is satisfied. Restore copies the retained payload into a new active revision. It never rewinds or mutates an older revision.

## Internal hard erase

Hard erase is not a Gate action and is not exposed by `StateClient`. It is a private `StateStorePort.hard_erase` operation prepared from an already-authorized external retention decision.

The mechanical hard-erase commit:

1. verifies exact StateKey, revision/state digest, immutable retention binding, and claim/fence state; when an active claim exists the executor must present the exact current `claim_id` and `fencing_token`, but the retention executor is not required to equal the claim holder because the claim is coordination evidence rather than erase authority;
2. allocates a new revision with lifecycle `erased` and no payload;
3. scrubs payload bytes from all retained revisions of the object;
4. updates the current projection to the erased identity tombstone;
5. preserves object identity, highest revision, immutable schema binding, retention binding, and highest fence lineage;
6. deactivates any surviving claim without deleting its fence lineage;
7. appends the canonical `erased` event;
8. persists a private immutable hard-erase operation receipt in the same commit boundary.

The private receipt family exists because hard erase requires durable OperationKey finality but is intentionally absent from the public `StateReceipt` action enum.

The receipt `principal_ref` remains the retention executor and `authorization_ref` remains the external retention decision. Claim-holder identity is preserved in claim lineage but is not rewritten onto the erase receipt and is not used as retention authorization.

## External retention authority boundary

State does not own retention periods, legal holds, deletion schedules, or the decision that a particular object is eligible for hard erasure. The bound State v2 architecture requires a separately owned retention-policy decision interface before a `RetentionExecutor` can be activated.

That external decision interface is currently unresolved. Consequently:

- tombstone and restore are active State capabilities;
- hard-erase mechanics and conformance surfaces exist internally;
- no autonomous retention scheduler or policy interpreter exists;
- no `RetentionExecutor` is active;
- `prepare_hard_erase_plan(...)` requires an `authorization_ref` identifying the external decision/evidence and does not validate or invent that authority.

## Identity and replay safety after erase

Hard erase destroys payload bytes, not State identity. The erased StateKey remains reserved permanently in v1. Object ID reuse and restore from erased state are refused. Minimal revision, fence, journal, and OperationKey metadata remains so erasure cannot create ABA or replay ambiguity.

TTL indexes do not define tombstone, erase, operation-receipt validity, or claim expiry semantics.
