# L9-AgentOS: repository-scoped development pack

**Intended repository:** `Quantum-L9/L9-AgentOS`. **Class:** new runnable constellation node. **Status:** architecture locked; detailed implementation proposal; code not built in this delivery.

## Purpose
Agent semantics, AgentProfile compilation, manifestation lifecycle, Work Item semantics, cognition and bounded-autonomy evaluation.

## Owns
- AgentProfile source grammar, resolution, digest and lifecycle.
- Manifestation identity and profile binding.
- Objective and Work Item semantics.
- Observation handling, context needs, decisions and ActionIntents.
- Generic declarative autonomy evaluation and delegation semantics.
- Durable execution-intent coordination through State and Gate.

## Must not own
- Direct provider/database/Graphiti calls.
- Gate routing, transport models or node admission.
- Canonical memory admission or storage.
- Domain-specific commercial, calendar, coding or procurement branches.
- Generic multi-source retrieval implementation.
- A new downstream validator agent.

## First stack
Python 3.12-compatible L9 node chassis, typed contracts, deterministic profile compiler and rule evaluator; all shared services invoked through Gate. No OpenClaw/LangGraph runtime dependency.

## Entry path
Authenticated client or node -> Constellation.Gate -> owner-registered `agent.*` action -> SDK chassis validation -> typed capability handler -> owning service -> typed receipt. Outbound inter-node work returns to Gate. No handler takes a peer URL.

## Scope and dependency usage
- Gate_SDK: node chassis and outbound protocol.
- l9-state: durable Work Item and execution state.
- l9-context: required context fulfillment.
- l9-memory: governed durable knowledge.
- l9-evidence: evidence and receipt retention.
- l9-ingest: optional transformation of raw observations.
- l9-cognitive-runtime: owner-native compilation through an admitted binding when required.

## Start order
Read ARCHITECTURE.md, INVARIANTS.md, BOUNDARY.yaml, API_CONTRACT.md, IMPLEMENTATION_MAP.md, TEST_PLAN.md, SECURITY.md and execution_contract.yaml. Select only a dependency-ready unit from the coordinated roadmap. Source bytes in this pack are design artifacts; do not overwrite live files with proposed file maps.

## Done means
Contract shape, behavior, authorization, failure handling, installed-package boundaries, Gate integration, storage/recovery where relevant and owner-native CI all have current-revision receipts. A sample JSON that validates is not a node readiness receipt. Required live tests cannot be replaced with fixture assertions.


## v1.1 cross-repository integration
This scope participates in the Communication/Formal Reasoning extension. Its exact added work is in `execution_contract.yaml` and `ROADMAP.md`; generic ownership remains unchanged. Refer to `../../02_architecture/COMMUNICATION_REASONING_INTEGRATION.md`. A new upstream consumer does not authorize importing another node's implementation or moving its policy into L9-AgentOS.
