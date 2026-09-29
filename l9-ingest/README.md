# l9-ingest: repository-scoped development pack

**Intended repository:** `Quantum-L9/l9-ingest`. **Class:** new runnable constellation node. **Status:** architecture locked; detailed implementation proposal; code not built in this delivery.

## Purpose
Bounded source acquisition/normalization/transformation and destination-specific candidate delivery.

## Owns
- Source-operation identity and bounded processing lifecycle.
- Authorized source capture, normalization and provenance.
- Profile-selected parsing, representation generation and candidate extraction.
- Deterministic transformation/view/cache identity.
- Destination-specific candidate compilation and per-destination delivery settlement.
- Replay and reconciliation of source processing, never domain effects.

## Must not own
- Canonical memory admission/lifecycle.
- Mutable agent Work Item semantics.
- Evidence/vector persistence behind another node.
- Cross-source context compilation.
- A global crawler, duplicate topology scanner or domain scheduler.
- Direct provider writes into Graphiti or Evidence database.

## First stack
Deterministic native parsers plus bounded LlamaIndex transformations. Framework vector-store sinks disabled; outputs are typed intents delivered through Gate. Tree-sitter is optional profile-specific parsing, not a mandatory agent dependency.

## Entry path
Authenticated client or node -> Constellation.Gate -> owner-registered `ingest.*` action -> SDK chassis validation -> typed capability handler -> owning service -> typed receipt. Outbound inter-node work returns to Gate. No handler takes a peer URL.

## Scope and dependency usage
- Gate_SDK: node runtime and transport.
- l9-evidence: source and projection destination.
- l9-memory: canonical memory-candidate destination.
- LlamaIndex transformation adapter, selected first stack.
- Tree-sitter parser adapter only for justified code/source profiles.
- Existing topology publication contracts as input where available.

## Start order
Read ARCHITECTURE.md, INVARIANTS.md, BOUNDARY.yaml, API_CONTRACT.md, IMPLEMENTATION_MAP.md, TEST_PLAN.md, SECURITY.md and execution_contract.yaml. Select only a dependency-ready unit from the coordinated roadmap. Source bytes in this pack are design artifacts; do not overwrite live files with proposed file maps.

## Done means
Contract shape, behavior, authorization, failure handling, installed-package boundaries, Gate integration, storage/recovery where relevant and owner-native CI all have current-revision receipts. A sample JSON that validates is not a node readiness receipt. Required live tests cannot be replaced with fixture assertions.


## v1.1 cross-repository integration
This scope participates in the Communication/Formal Reasoning extension. Its exact added work is in `execution_contract.yaml` and `ROADMAP.md`; generic ownership remains unchanged. Refer to `../../02_architecture/COMMUNICATION_REASONING_INTEGRATION.md`. A new upstream consumer does not authorize importing another node's implementation or moving its policy into l9-ingest.
