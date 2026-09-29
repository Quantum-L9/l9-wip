# Capability contract: l9-memory

**Implementation proposal, not a live API inventory.** Gate action names below are canonical candidates. Payload specimens are intentionally separate from the SDK-owned transport. Authentication, tenant, correlation and transport lineage remain in the validated transport context. Per-action payload and result schemas are supplied as implementation proposals for owner review; memory request/receipt semantics continue to bind to the existing owner contract.

| Action | Request specimen | Core result specimen | Effect | Semantics |
| --- | --- | --- | --- | --- |
| memory.write | MemoryBindingRequest | Existing memory owner receipt | write | Map to existing owner write contract and MemoryService, preserving explicit operation identity. |
| memory.ingest | MemoryBindingRequest | Existing memory owner receipt | write | Map governed candidate to existing GeneratedDataService/MemoryService public path. |
| memory.search | MemoryBindingRequest | Existing memory owner receipt | read | Preserve owner query selectors, authorized namespaces and canonical-hit resolution. |
| memory.hydrate | MemoryBindingRequest | Existing memory owner receipt | read | Use owner bounded hydration, not a second cross-source Context compiler. |
| memory.close | MemoryBindingRequest | Existing memory owner receipt | write | Use owner-supported close semantics only for permitted lifecycle classes. |
| memory.phase-lock | MemoryBindingRequest | Existing memory owner receipt | write | Request owner conflict-sensitive snapshot consistency evidence. |
| memory.delete | MemoryBindingRequest | Existing memory owner receipt | write | Delegate verified deletion/consent/lifecycle obligations to memory owner. |
| memory.rebuild-projection | MemoryBindingRequest | Existing memory owner receipt | write | Use existing owner maintenance authority to rebuild optional projections. |

## Common boundary obligations

Every request validates authenticated role, effective scope, purpose, action grant, contract identity, size and deadline before effects. A payload scope is a request, never a grant. Domain write requests bind operation identity and request digest; exact replay returns the original authoritative result and mismatch conflicts. Read pagination has explicit limits/cursors and reports coverage. Service errors distinguish invalid request, forbidden, not found, conflict, unavailable, deadline, partial and outcome unknown. No generic success boolean is sufficient.

### memory.write

Map to existing owner write contract and MemoryService, preserving explicit operation identity. Only owner admission/duplicate receipt permits a remembered claim.

**Receipt obligation:** bind action/operation, authenticated scope, owner contract, input digest and observed outcome. For reads report source coordinates, bounds and omissions. For mutations report committed revision or authoritative destination receipt. Transport acceptance alone never satisfies semantic completion.

**Negative proof:** l9memory-api-1: refuse scope/contract mismatch and do not perform undeclared effects.

**Capability-specific completion:** see CAPABILITY_DETAILS.md and tests named in TEST_PLAN.md. Dependencies must fail visibly without bypass.

### memory.ingest

Map governed candidate to existing GeneratedDataService/MemoryService public path. Source-processing eligibility does not replace memory admission.

**Receipt obligation:** bind action/operation, authenticated scope, owner contract, input digest and observed outcome. For reads report source coordinates, bounds and omissions. For mutations report committed revision or authoritative destination receipt. Transport acceptance alone never satisfies semantic completion.

**Negative proof:** l9memory-api-2: refuse scope/contract mismatch and do not perform undeclared effects.

**Capability-specific completion:** see CAPABILITY_DETAILS.md and tests named in TEST_PLAN.md. Dependencies must fail visibly without bypass.

### memory.search

Preserve owner query selectors, authorized namespaces and canonical-hit resolution. Empty is not denied/unavailable; no projection-only truth.

**Receipt obligation:** bind action/operation, authenticated scope, owner contract, input digest and observed outcome. For reads report source coordinates, bounds and omissions. For mutations report committed revision or authoritative destination receipt. Transport acceptance alone never satisfies semantic completion.

**Negative proof:** l9memory-api-3: refuse scope/contract mismatch and do not perform undeclared effects.

**Capability-specific completion:** see CAPABILITY_DETAILS.md and tests named in TEST_PLAN.md. Dependencies must fail visibly without bypass.

### memory.hydrate

Use owner bounded hydration, not a second cross-source Context compiler. Return selector, coverage and failure evidence without widening scope.

**Receipt obligation:** bind action/operation, authenticated scope, owner contract, input digest and observed outcome. For reads report source coordinates, bounds and omissions. For mutations report committed revision or authoritative destination receipt. Transport acceptance alone never satisfies semantic completion.

**Negative proof:** l9memory-api-4: refuse scope/contract mismatch and do not perform undeclared effects.

**Capability-specific completion:** see CAPABILITY_DETAILS.md and tests named in TEST_PLAN.md. Dependencies must fail visibly without bypass.

### memory.close

Use owner-supported close semantics only for permitted lifecycle classes. Not a substitute for AgentOS Work Item state.

**Receipt obligation:** bind action/operation, authenticated scope, owner contract, input digest and observed outcome. For reads report source coordinates, bounds and omissions. For mutations report committed revision or authoritative destination receipt. Transport acceptance alone never satisfies semantic completion.

**Negative proof:** l9memory-api-5: refuse scope/contract mismatch and do not perform undeclared effects.

**Capability-specific completion:** see CAPABILITY_DETAILS.md and tests named in TEST_PLAN.md. Dependencies must fail visibly without bypass.

### memory.phase-lock

Request owner conflict-sensitive snapshot consistency evidence. Lock never grants repository, node or commercial authority.

**Receipt obligation:** bind action/operation, authenticated scope, owner contract, input digest and observed outcome. For reads report source coordinates, bounds and omissions. For mutations report committed revision or authoritative destination receipt. Transport acceptance alone never satisfies semantic completion.

**Negative proof:** l9memory-api-6: refuse scope/contract mismatch and do not perform undeclared effects.

**Capability-specific completion:** see CAPABILITY_DETAILS.md and tests named in TEST_PLAN.md. Dependencies must fail visibly without bypass.

### memory.delete

Delegate verified deletion/consent/lifecycle obligations to memory owner. Canonical redaction and projection erasure statuses stay distinct.

**Receipt obligation:** bind action/operation, authenticated scope, owner contract, input digest and observed outcome. For reads report source coordinates, bounds and omissions. For mutations report committed revision or authoritative destination receipt. Transport acceptance alone never satisfies semantic completion.

**Negative proof:** l9memory-api-7: refuse scope/contract mismatch and do not perform undeclared effects.

**Capability-specific completion:** see CAPABILITY_DETAILS.md and tests named in TEST_PLAN.md. Dependencies must fail visibly without bypass.

### memory.rebuild-projection

Use existing owner maintenance authority to rebuild optional projections. Does not admit new canonical memory or replay external actions.

**Receipt obligation:** bind action/operation, authenticated scope, owner contract, input digest and observed outcome. For reads report source coordinates, bounds and omissions. For mutations report committed revision or authoritative destination receipt. Transport acceptance alone never satisfies semantic completion.

**Negative proof:** l9memory-api-8: refuse scope/contract mismatch and do not perform undeclared effects.

**Capability-specific completion:** see CAPABILITY_DETAILS.md and tests named in TEST_PLAN.md. Dependencies must fail visibly without bypass.

## Owner acceptance before implementation

This pack includes operation-specific read pages, inspect/status selectors, cancellation and lifecycle requests, claim and acknowledgment receipts, and exact-base context refresh requests. The owner contract PR must verify every shape against its behavioral contract, publish versioned schema/model parity and bind errors to the existing canonical transport. Memory remains deliberately mapped to its existing public request/receipt models; the wrapper shell never substitutes for owner validation. Proposed schemas do not certify runtime behavior.
