# l9-evidence: repository-scoped development pack

**Intended repository:** `Quantum-L9/l9-evidence`. **Class:** new runnable constellation node. **Status:** architecture locked; detailed implementation proposal; code not built in this delivery.

## Purpose
Evidence retention, immutable provenance references, source projections, retrieval indexes and erasure of its own copies.

## Owns
- Evidence records, content-addressed artifact references and integrity checks.
- Exact source revision/locator provenance.
- Evidence retention, owned-copy erasure and legal-hold metadata supplied by authority.
- Source-derived text/vector retrieval projections and projection lifecycle.
- Source access filtering and retrieval receipts.
- Queryable operation proof without declaring domain outcomes itself.

## Must not own
- Mutable Work Item state or approvals authority.
- Memory admission, preference inference or Graphiti truth.
- Agent cognition or cross-source context compilation.
- A replacement for Git, ERP, mailbox or other source systems.
- Consumer arbitrary Mongo/search-pipeline access.
- Independent ontology or source inventory duplicating topology owners.

## First stack
MongoDB for evidence metadata and derived search documents; object storage behind an owned port for large content. One initial evaluated vector view; vector index/provider details remain private.

## Entry path
Authenticated client or node -> Constellation.Gate -> owner-registered `evidence.*` action -> SDK chassis validation -> typed capability handler -> owning service -> typed receipt. Outbound inter-node work returns to Gate. No handler takes a peer URL.

## Scope and dependency usage
- Gate_SDK: node chassis and transport.
- MongoDB metadata/projection adapter, first stack.
- Owner-controlled object storage for large binary/text artifacts.
- Optional Atlas vector/search adapter with deployment-specific capability probe.

## Start order
Read ARCHITECTURE.md, INVARIANTS.md, BOUNDARY.yaml, API_CONTRACT.md, IMPLEMENTATION_MAP.md, TEST_PLAN.md, SECURITY.md and execution_contract.yaml. Select only a dependency-ready unit from the coordinated roadmap. Source bytes in this pack are design artifacts; do not overwrite live files with proposed file maps.

## Done means
Contract shape, behavior, authorization, failure handling, installed-package boundaries, Gate integration, storage/recovery where relevant and owner-native CI all have current-revision receipts. A sample JSON that validates is not a node readiness receipt. Required live tests cannot be replaced with fixture assertions.


## v1.1 cross-repository integration
This scope participates in the Communication/Formal Reasoning extension. Its exact added work is in `execution_contract.yaml` and `ROADMAP.md`; generic ownership remains unchanged. Refer to `../../02_architecture/COMMUNICATION_REASONING_INTEGRATION.md`. A new upstream consumer does not authorize importing another node's implementation or moving its policy into l9-evidence.
