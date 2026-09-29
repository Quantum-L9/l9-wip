# l9-state: repository-scoped development pack

**Intended repository:** `Quantum-L9/l9-state`. **Class:** new runnable constellation node. **Status:** architecture locked; detailed implementation proposal; code not built in this delivery.

## Purpose
Durable state mechanics, revisions, conditional commits, checkpoints, fenced claims, journal and committed transition delivery.

## Owns
- StateRecord, revision and operation identity.
- Atomic conditional commit of state, receipt and journal/outbox event.
- Checkpoints and bounded object history.
- Fenced claim acquisition, renewal, release and expiry.
- Committed transition journal, delivery cursor and deduplicated acknowledgement.
- Owned retention, tombstones, restore and schema-binding verification.

## Must not own
- Work Item meaning, business lifecycle or next-action selection.
- Source system business truth.
- Memory, context ranking or semantic extraction.
- Node/client trust grants.
- A global scheduler or authoritative Program Execution state machine.
- Generic public database queries, SQL or Mongo operators.

## First stack
MongoDB replica-set adapter with transactions, explicit write/read concern and unique indexes; Change Streams may wake journal publication but do not define canonical events. PyMongo remains adapter-private.

## Entry path
Authenticated client or node -> Constellation.Gate -> owner-registered `state.*` action -> SDK chassis validation -> typed capability handler -> owning service -> typed receipt. Outbound inter-node work returns to Gate. No handler takes a peer URL.

## Scope and dependency usage
- Gate_SDK: node chassis and transport.
- MongoDB replica set through private StateStore adapter, first stack.
- Optional Evidence archival via Gate after local commit, never required for atomic State commit.

## Start order
Read ARCHITECTURE.md, INVARIANTS.md, BOUNDARY.yaml, API_CONTRACT.md, IMPLEMENTATION_MAP.md, TEST_PLAN.md, SECURITY.md and execution_contract.yaml. Select only a dependency-ready unit from the coordinated roadmap. Source bytes in this pack are design artifacts; do not overwrite live files with proposed file maps.

## Done means
Contract shape, behavior, authorization, failure handling, installed-package boundaries, Gate integration, storage/recovery where relevant and owner-native CI all have current-revision receipts. A sample JSON that validates is not a node readiness receipt. Required live tests cannot be replaced with fixture assertions.


## v1.1 cross-repository integration
This scope participates in the Communication/Formal Reasoning extension. Its exact added work is in `execution_contract.yaml` and `ROADMAP.md`; generic ownership remains unchanged. Refer to `../../02_architecture/COMMUNICATION_REASONING_INTEGRATION.md`. A new upstream consumer does not authorize importing another node's implementation or moving its policy into l9-state.
