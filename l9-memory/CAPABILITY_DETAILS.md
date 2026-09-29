# Memory node wrapper contract

## One domain owner
l9-memory is a separately deployable Gate node composing l9-graphiti-memory's public domain facade. The existing package distribution is spelled `l9-graphite-memory` and its Python package `l9_graphite_memory`; preserve real packaging names. Do not rename/import a fictional package while changing the node boundary.

## Canonical writes
The node receives a typed candidate/write payload, maps authenticated caller claims into the public MemoryPrincipal and invokes the existing public operation. MemoryService authorizes, normalizes/redacts, validates, admits and atomically commits canonical state/receipt/outbox or raises. The wrapper returns the actual owner status; it must not convert quarantined/rejected to remembered or queued projection to canonical success.

## Scope
Use generic tenant/namespace/subject/purpose references. No hardcoded manifestation names or repo slugs in core. Preserve exact identity encoding and server-derived producer/created_by stamps. Same profile is not shared memory authority. Purpose-bound consent for identity/preference material remains the memory owner's requirement; a caller cannot relabel sensitive personal data as an ordinary observation merely to bypass it.

## Reads
Preserve existing QueryClassifier, RetrievalPlanner, authorized canonical filtering, projection-hit UUID rehydration, distinct valid/transaction time, separated ranking factors, bounded hydration and per-strategy partial/failed receipts. Context consumes memory results but does not repeat its retrieval algorithm. A missing projection may degrade retrieval according to policy; a canonical store failure cannot be disguised as no hits.

## Lifecycle
Preserve supersession, retention, conflict records, governed promotion, consent, verified deletion, projection locator tracking and outbox recovery. Canonical memory is still not raw transcript storage, Work Item continuation or mutable operational state. A Work Item can produce one independently governed memory assertion with provenance, but the work record itself belongs in State.

## Existing SDK parity
Every node action maps to one existing public owner operation or a narrowly documented owner-side delta. Gate naming is an external binding; old internal CLI/MCP names remain until their owners approve deprecation. No direct Graphiti access is introduced to make the wrapper shorter. Configuration injects existing store/projection dependencies at deployment, not by importing their internals into AgentOS.
