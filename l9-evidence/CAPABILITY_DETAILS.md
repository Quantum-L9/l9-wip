# Evidence and projection contract

## Evidence admission
EvidenceRecord retains issuer/source identity, source revision/locator, scope, classification, permitted use, content digest/ref, observed/recorded coordinates and retention/deletion rules. `evidence.append` proves the submitted artifact was accepted under that scope; it does not prove the underlying claim is true or an external business action occurred. Source signatures/issuer trust are separate evidence fields.

## Large artifacts
Store binaries and large source documents behind ArtifactStorePort. First reserve or upload immutable digest-bound content, then commit evidence metadata only when size/hash/authorization are verified. An incomplete upload cannot appear as retrievable evidence. Garbage collection removes unreferenced temporary objects after a bounded safe period. A signed URL is short-lived access, not source identity.

## Exact reads and search
`evidence.get` returns one authorized canonical evidence ref. `evidence.resolve` resolves source/revision identity from admitted source metadata. `evidence.search` retrieves eligible representations with scope/freshness/classification prefilters and a second canonical access/visibility check before returning content. Provider scores never confer authority. A backend fault remains explicit, and a projection hit that cannot be tied to its source record is not served as evidence.

## Representation lifecycle
A ProjectionRecord binds source identity, normalized representation digest, transform version, view ID, model/embedding-space identity where used, provenance and lifecycle. Evidence owns the persisted search representation and its deletion lifecycle. Ingest owns how a candidate representation was produced. Current aliases change only under a versioned promotion/verification operation; old projections can remain for authorized audit, never silently enter current context.

## Canonical source distinction
Git authored files remain Git authority. ERP/mailbox/calendar records remain at their providers. Evidence holds immutable copies/receipts or projections for citation and retrieval. A stale copy is not a live approval or capability grant. Context and AgentOS must request current source-owner evidence for consequential actions.

## Erasure
Owned raw content, text chunks, vector indexes, summary caches and artifact links are tracked through explicit derivation references. A deletion request is authorized, reason-bound and receipt-producing. Visibility is denied immediately; physical deletion can remain in progress. Completion requires all required owned targets to attest erasure. Pending replay checks tombstones and cannot recreate a removed projection. No cross-node deletion is falsely presented as one atomic database operation.
