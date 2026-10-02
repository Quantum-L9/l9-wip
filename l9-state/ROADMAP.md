# Repository roadmap

Planned implementation only. PRs remain scoped to this repository; dependencies are evidence gates, not permission to edit another owner.

## STATE-01 - Birth State contract and atomic persistence port

Prerequisites: AG-01, SDK-02, GATE-01

1. Birth only this node using verified chassis.
2. Finalize state/reference/operation identity contracts and generic schema registry binding.
3. Specify atomic commit of state, receipt, journal and outbox.
4. Build in-process contract double with the same semantics for tests only.

**Acceptance:** No Work Item kind or agent identity branch in State core. Same operation/different payload rejected.

**Required negatives:** Payload attempts to supply actor/principal are not honored. Partial multi-store commit cannot produce committed receipt.

## STATE-02 - Implement Mongo adapter with revision and fenced claim conformance

Prerequisites: STATE-01

1. Pin approved Mongo/PyMongo versions and replica-set deployment.
2. Create private state, operation, journal/outbox and consumer-checkpoint collections with scoped uniqueness.
3. Implement expected-revision conditional mutation and monotonic fencing in transactional unit of work.
4. Test concurrent writers, lease expiry, paused old holder, transaction retries and network ambiguity.

**Acceptance:** Only one concurrent mutation wins and receipt/event commit is atomic. No expired/reassigned holder can mutate under stale fence.

**Required negatives:** Kill worker at each transaction boundary and verify all-or-none. Reusing operation id with new payload fails even after restart.

## STATE-03 - Deliver committed events and exact recovery without provider leakage

Prerequisites: STATE-02, GATE-02

1. Use Mongo Change Streams only as wakeup, or bounded polling over durable journal.
2. Persist scoped consumer checkpoint/ack separately from provider resume token.
3. Define cursor expiry/resync and cancellation/tombstone behavior.
4. Validate publication replay idempotency through Gate and isolated multi-manifestation access.

**Acceptance:** Lost provider cursor can rebuild notification progress from canonical retained journal. Event stream never confuses later updateLookup with exact committed transition.

**Required negatives:** Duplicate event does not duplicate downstream intent. Cross-consumer ack and out-of-scope cursor fail.
