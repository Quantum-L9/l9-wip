# l9-context: repository-scoped development pack

**Intended repository:** `Quantum-L9/l9-context`. **Class:** new runnable constellation node. **Status:** architecture locked; detailed implementation proposal; code not built in this delivery.

## Purpose
Objective-scoped multi-source context fulfillment, typed evidence fusion, bounded bundles and deltas.

## Owns
- Scoped ContextNeed handling and provider-neutral fulfillment planning.
- Deterministic required/optional reads and bound source precedence.
- Multi-source retrieval through Gate and evidence normalization.
- Coverage, freshness, conflict and omission accounting.
- Budgeted ContextBundle/ContextDelta issuance and cache invalidation.
- Scoped reverse-ingestion requests when already authorized.

## Must not own
- Memory retrieval planner or canonical lifecycle duplicated locally.
- Normative cognitive compiler or kernel registry duplicated locally.
- Action authorization, routing or domain source truth.
- Database/Graphiti calls bypassing source owners.
- Automatic policy promotion from retrieved material.
- A custom broker for each named agent.

## First stack
Deterministic fulfillment/ranking baseline, existing cognitive demand contract reuse, optional LlamaIndex reranker adapters. No direct Atlas/Graphiti client and no context-owned canonical memory database.

## Entry path
Authenticated client or node -> Constellation.Gate -> owner-registered `context.*` action -> SDK chassis validation -> typed capability handler -> owning service -> typed receipt. Outbound inter-node work returns to Gate. No handler takes a peer URL.

## Scope and dependency usage
- Gate_SDK: node transport.
- State/Evidence/Memory and source capability owners through Gate.
- l9-cognitive-runtime typed demand and snapshot contracts via supported binding.
- Optional LlamaIndex reranker/selector adapter only for non-mandatory retrieval choices.

## Start order
Read ARCHITECTURE.md, INVARIANTS.md, BOUNDARY.yaml, API_CONTRACT.md, IMPLEMENTATION_MAP.md, TEST_PLAN.md, SECURITY.md and execution_contract.yaml. Select only a dependency-ready unit from the coordinated roadmap. Source bytes in this pack are design artifacts; do not overwrite live files with proposed file maps.

## Done means
Contract shape, behavior, authorization, failure handling, installed-package boundaries, Gate integration, storage/recovery where relevant and owner-native CI all have current-revision receipts. A sample JSON that validates is not a node readiness receipt. Required live tests cannot be replaced with fixture assertions.


## v1.1 cross-repository integration
This scope participates in the Communication/Formal Reasoning extension. Its exact added work is in `execution_contract.yaml` and `ROADMAP.md`; generic ownership remains unchanged. Refer to `../../02_architecture/COMMUNICATION_REASONING_INTEGRATION.md`. A new upstream consumer does not authorize importing another node's implementation or moving its policy into l9-context.
