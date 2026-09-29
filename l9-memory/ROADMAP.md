# Repository roadmap

Planned implementation only. PRs remain scoped to this repository; dependencies are evidence gates, not permission to edit another owner.

## MEM-01 - Birth thin Gate node over existing MemoryService

Prerequisites: MEMCORE-02, SDK-02, GATE-01

1. Compose approved memory package in node-owned deployment.
2. Validate domain request against exact owner model, not this pack shell alone.
3. Map authenticated scope/purpose to owner principal without widening.
4. Route all inter-node calls through Gate; provider connections remain owner-local.

**Acceptance:** MemoryService is the sole memory authority. No new canonical MemoryRecord or lifecycle state machine.

**Required negatives:** Direct backing-table/provider access from wrapper forbidden. Forged source or principal refuses before canonical write.

## MEM-02 - Prove shared memory capabilities across manifestations

Prerequisites: MEM-01, GATE-02

1. Exercise ordinary and consent-sensitive records using same service.
2. Verify scope-specific retrieval and evidence-bearing failures.
3. Round-trip supersession, archival, conflict-sensitive writes and deletion.
4. Prove optional projection outages cannot falsify receipt or canonical record status.

**Acceptance:** All profiles use same APIs; policy restricts use without separate engines. Partial retrieval is never reported as empty complete memory.

**Required negatives:** Sibling manifestation memory denied without explicit grant. Forged memory-only policy cannot authorize an external action.
