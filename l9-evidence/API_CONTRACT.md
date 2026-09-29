# Capability contract: l9-evidence

**Implementation proposal, not a live API inventory.** Gate action names below are canonical candidates. Payload specimens are intentionally separate from the SDK-owned transport. Authentication, tenant, correlation and transport lineage remain in the validated transport context. Per-action payload and result schemas are supplied as implementation proposals for owner review; memory request/receipt semantics continue to bind to the existing owner contract.

| Action | Request specimen | Core result specimen | Effect | Semantics |
| --- | --- | --- | --- | --- |
| evidence.append | EvidenceAppendRequest | EvidenceOperationReceipt | write | Verify source identity, digest, scope and permitted retention; return stable accepted evidence reference. |
| evidence.get | EvidenceGetRequest | EvidenceReadResult | read | Resolve an exact authorized immutable evidence reference. |
| evidence.resolve | EvidenceResolveRequest | EvidenceReadResult | read | Resolve source identity/revision without semantic guessing. |
| evidence.search | EvidenceSearchRequest | EvidenceSearchPage | read | Search only authorized views with explicit query/space compatibility and bounded results. |
| evidence.project | ProjectionCandidate | EvidenceOperationReceipt | write | Accept deterministic representation/view provenance and maintain a disposable retrieval view. |
| evidence.invalidate | EvidenceLifecycleRequest | EvidenceOperationReceipt | write | Record source-revision invalidation and retire dependent searchable views. |
| evidence.erase | EvidenceLifecycleRequest | EvidenceOperationReceipt | write | Erase owned source copies/derivatives according to authorized policy and track completion. |

## Common boundary obligations

Every request validates authenticated role, effective scope, purpose, action grant, contract identity, size and deadline before effects. A payload scope is a request, never a grant. Domain write requests bind operation identity and request digest; exact replay returns the original authoritative result and mismatch conflicts. Read pagination has explicit limits/cursors and reports coverage. Service errors distinguish invalid request, forbidden, not found, conflict, unavailable, deadline, partial and outcome unknown. No generic success boolean is sufficient.

### evidence.append

Verify source identity, digest, scope and permitted retention; return stable accepted evidence reference. Metadata and bytes must be durably linked; orphan bytes are quarantined, never served.

**Receipt obligation:** bind action/operation, authenticated scope, owner contract, input digest and observed outcome. For reads report source coordinates, bounds and omissions. For mutations report committed revision or authoritative destination receipt. Transport acceptance alone never satisfies semantic completion.

**Negative proof:** l9evidence-api-1: refuse scope/contract mismatch and do not perform undeclared effects.

**Capability-specific completion:** see CAPABILITY_DETAILS.md and tests named in TEST_PLAN.md. Dependencies must fail visibly without bypass.

### evidence.get

Resolve an exact authorized immutable evidence reference. Reference possession alone is not read permission.

**Receipt obligation:** bind action/operation, authenticated scope, owner contract, input digest and observed outcome. For reads report source coordinates, bounds and omissions. For mutations report committed revision or authoritative destination receipt. Transport acceptance alone never satisfies semantic completion.

**Negative proof:** l9evidence-api-2: refuse scope/contract mismatch and do not perform undeclared effects.

**Capability-specific completion:** see CAPABILITY_DETAILS.md and tests named in TEST_PLAN.md. Dependencies must fail visibly without bypass.

### evidence.resolve

Resolve source identity/revision without semantic guessing. An outdated materialized projection cannot be represented as live source authority.

**Receipt obligation:** bind action/operation, authenticated scope, owner contract, input digest and observed outcome. For reads report source coordinates, bounds and omissions. For mutations report committed revision or authoritative destination receipt. Transport acceptance alone never satisfies semantic completion.

**Negative proof:** l9evidence-api-3: refuse scope/contract mismatch and do not perform undeclared effects.

**Capability-specific completion:** see CAPABILITY_DETAILS.md and tests named in TEST_PLAN.md. Dependencies must fail visibly without bypass.

### evidence.search

Search only authorized views with explicit query/space compatibility and bounded results. Filter before ranking; candidates are reverified against evidence scope and lifecycle.

**Receipt obligation:** bind action/operation, authenticated scope, owner contract, input digest and observed outcome. For reads report source coordinates, bounds and omissions. For mutations report committed revision or authoritative destination receipt. Transport acceptance alone never satisfies semantic completion.

**Negative proof:** l9evidence-api-4: refuse scope/contract mismatch and do not perform undeclared effects.

**Capability-specific completion:** see CAPABILITY_DETAILS.md and tests named in TEST_PLAN.md. Dependencies must fail visibly without bypass.

### evidence.project

Accept deterministic representation/view provenance and maintain a disposable retrieval view. One executor per embedding view; no in-place mutation of immutable source evidence.

**Receipt obligation:** bind action/operation, authenticated scope, owner contract, input digest and observed outcome. For reads report source coordinates, bounds and omissions. For mutations report committed revision or authoritative destination receipt. Transport acceptance alone never satisfies semantic completion.

**Negative proof:** l9evidence-api-5: refuse scope/contract mismatch and do not perform undeclared effects.

**Capability-specific completion:** see CAPABILITY_DETAILS.md and tests named in TEST_PLAN.md. Dependencies must fail visibly without bypass.

### evidence.invalidate

Record source-revision invalidation and retire dependent searchable views. Invalidation is not proof that an upstream source has been deleted.

**Receipt obligation:** bind action/operation, authenticated scope, owner contract, input digest and observed outcome. For reads report source coordinates, bounds and omissions. For mutations report committed revision or authoritative destination receipt. Transport acceptance alone never satisfies semantic completion.

**Negative proof:** l9evidence-api-6: refuse scope/contract mismatch and do not perform undeclared effects.

**Capability-specific completion:** see CAPABILITY_DETAILS.md and tests named in TEST_PLAN.md. Dependencies must fail visibly without bypass.

### evidence.erase

Erase owned source copies/derivatives according to authorized policy and track completion. Do not claim complete until all owned targets settle or explicit holds are recorded.

**Receipt obligation:** bind action/operation, authenticated scope, owner contract, input digest and observed outcome. For reads report source coordinates, bounds and omissions. For mutations report committed revision or authoritative destination receipt. Transport acceptance alone never satisfies semantic completion.

**Negative proof:** l9evidence-api-7: refuse scope/contract mismatch and do not perform undeclared effects.

**Capability-specific completion:** see CAPABILITY_DETAILS.md and tests named in TEST_PLAN.md. Dependencies must fail visibly without bypass.

## Owner acceptance before implementation

This pack includes operation-specific read pages, inspect/status selectors, cancellation and lifecycle requests, claim and acknowledgment receipts, and exact-base context refresh requests. The owner contract PR must verify every shape against its behavioral contract, publish versioned schema/model parity and bind errors to the existing canonical transport. Memory remains deliberately mapped to its existing public request/receipt models; the wrapper shell never substitutes for owner validation. Proposed schemas do not certify runtime behavior.
