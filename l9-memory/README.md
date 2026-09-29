# l9-memory: repository-scoped development pack

**Intended repository:** `Quantum-L9/l9-memory`. **Class:** new runnable constellation node. **Status:** architecture locked; detailed implementation proposal; code not built in this delivery.

## Purpose
Gate-facing governed memory service; composes the existing memory domain core without duplicating it.

## Owns
- Gate-facing memory capability adapters.
- Authenticated transport principal mapping into existing memory contracts.
- Node lifecycle, configuration and readiness for the embedded memory domain.
- Public request/response compatibility and explicit per-operation receipts.
- Deployment composition of existing canonical store and projection backend.

## Must not own
- A second MemoryService, canonical store or lifecycle engine.
- Agent-specific memory taxonomy or namespace hardcoding.
- New generic source-ingestion framework.
- Direct remote node URLs.
- Requiring graph projection to admit canonical memory.
- A mandatory new global database migration.

## First stack
Existing Python memory domain. Preserve configured SQLite diagnostic or PostgreSQL shared authority, with Graphiti/Zep/none as optional rebuildable projections. No Mongo move for canonical memory in this campaign.

## Entry path
Authenticated client or node -> Constellation.Gate -> owner-registered `memory.*` action -> SDK chassis validation -> typed capability handler -> owning service -> typed receipt. Outbound inter-node work returns to Gate. No handler takes a peer URL.

## Scope and dependency usage
- Gate_SDK: trusted node runtime and transport.
- l9-graphiti-memory (distribution l9-graphite-memory): canonical memory domain.
- Existing RecordStore adapters and configured Graphiti/Zep/none projection via the domain package.

## Start order
Read ARCHITECTURE.md, INVARIANTS.md, BOUNDARY.yaml, API_CONTRACT.md, IMPLEMENTATION_MAP.md, TEST_PLAN.md, SECURITY.md and execution_contract.yaml. Select only a dependency-ready unit from the coordinated roadmap. Source bytes in this pack are design artifacts; do not overwrite live files with proposed file maps.

## Done means
Contract shape, behavior, authorization, failure handling, installed-package boundaries, Gate integration, storage/recovery where relevant and owner-native CI all have current-revision receipts. A sample JSON that validates is not a node readiness receipt. Required live tests cannot be replaced with fixture assertions.
