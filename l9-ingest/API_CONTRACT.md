# Capability contract: l9-ingest

**Implementation proposal, not a live API inventory.** Gate action names below are canonical candidates. Payload specimens are intentionally separate from the SDK-owned transport. Authentication, tenant, correlation and transport lineage remain in the validated transport context. Per-action payload and result schemas are supplied as implementation proposals for owner review; memory request/receipt semantics continue to bind to the existing owner contract.

| Action | Request specimen | Core result specimen | Effect | Semantics |
| --- | --- | --- | --- | --- |
| ingest.submit | IngestRequest | IngestReceipt | write | Capture one bounded source revision and transform under exact ingestion profile. |
| ingest.sync | IngestRequest | IngestReceipt | write | Compare immutable source/view/transform identities and process only changed eligible representations. |
| ingest.reconcile | IngestReconcileRequest | IngestReceipt | write | Read per-destination receipt state and reconcile uncertain deliveries with their owner. |
| ingest.replay | IngestReplayRequest | IngestReceipt | write | Rebuild eligible projections from retained evidence under current scope/retention constraints. |
| ingest.status | IngestStatusRequest | IngestReceipt | read | Return bounded stage and destination receipts without starting processing. |

## Common boundary obligations

Every request validates authenticated role, effective scope, purpose, action grant, contract identity, size and deadline before effects. A payload scope is a request, never a grant. Domain write requests bind operation identity and request digest; exact replay returns the original authoritative result and mismatch conflicts. Read pagination has explicit limits/cursors and reports coverage. Service errors distinguish invalid request, forbidden, not found, conflict, unavailable, deadline, partial and outcome unknown. No generic success boolean is sufficient.

### ingest.submit

Capture one bounded source revision and transform under exact ingestion profile. Accepted means durable source-processing responsibility, not downstream memory success.

**Receipt obligation:** bind action/operation, authenticated scope, owner contract, input digest and observed outcome. For reads report source coordinates, bounds and omissions. For mutations report committed revision or authoritative destination receipt. Transport acceptance alone never satisfies semantic completion.

**Negative proof:** l9ingest-api-1: refuse scope/contract mismatch and do not perform undeclared effects.

**Capability-specific completion:** see CAPABILITY_DETAILS.md and tests named in TEST_PLAN.md. Dependencies must fail visibly without bypass.

### ingest.sync

Compare immutable source/view/transform identities and process only changed eligible representations. No delete-and-recreate churn or re-embedding unchanged representations.

**Receipt obligation:** bind action/operation, authenticated scope, owner contract, input digest and observed outcome. For reads report source coordinates, bounds and omissions. For mutations report committed revision or authoritative destination receipt. Transport acceptance alone never satisfies semantic completion.

**Negative proof:** l9ingest-api-2: refuse scope/contract mismatch and do not perform undeclared effects.

**Capability-specific completion:** see CAPABILITY_DETAILS.md and tests named in TEST_PLAN.md. Dependencies must fail visibly without bypass.

### ingest.reconcile

Read per-destination receipt state and reconcile uncertain deliveries with their owner. Do not infer success from local queue disappearance.

**Receipt obligation:** bind action/operation, authenticated scope, owner contract, input digest and observed outcome. For reads report source coordinates, bounds and omissions. For mutations report committed revision or authoritative destination receipt. Transport acceptance alone never satisfies semantic completion.

**Negative proof:** l9ingest-api-3: refuse scope/contract mismatch and do not perform undeclared effects.

**Capability-specific completion:** see CAPABILITY_DETAILS.md and tests named in TEST_PLAN.md. Dependencies must fail visibly without bypass.

### ingest.replay

Rebuild eligible projections from retained evidence under current scope/retention constraints. Replay cannot resurrect erased content or repeat operational external effects.

**Receipt obligation:** bind action/operation, authenticated scope, owner contract, input digest and observed outcome. For reads report source coordinates, bounds and omissions. For mutations report committed revision or authoritative destination receipt. Transport acceptance alone never satisfies semantic completion.

**Negative proof:** l9ingest-api-4: refuse scope/contract mismatch and do not perform undeclared effects.

**Capability-specific completion:** see CAPABILITY_DETAILS.md and tests named in TEST_PLAN.md. Dependencies must fail visibly without bypass.

### ingest.status

Return bounded stage and destination receipts without starting processing. Terminal, pending, partial and unknown are not collapsed.

**Receipt obligation:** bind action/operation, authenticated scope, owner contract, input digest and observed outcome. For reads report source coordinates, bounds and omissions. For mutations report committed revision or authoritative destination receipt. Transport acceptance alone never satisfies semantic completion.

**Negative proof:** l9ingest-api-5: refuse scope/contract mismatch and do not perform undeclared effects.

**Capability-specific completion:** see CAPABILITY_DETAILS.md and tests named in TEST_PLAN.md. Dependencies must fail visibly without bypass.

## Owner acceptance before implementation

This pack includes operation-specific read pages, inspect/status selectors, cancellation and lifecycle requests, claim and acknowledgment receipts, and exact-base context refresh requests. The owner contract PR must verify every shape against its behavioral contract, publish versioned schema/model parity and bind errors to the existing canonical transport. Memory remains deliberately mapped to its existing public request/receipt models; the wrapper shell never substitutes for owner validation. Proposed schemas do not certify runtime behavior.
