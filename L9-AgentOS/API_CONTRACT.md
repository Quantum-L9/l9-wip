# Capability contract: L9-AgentOS

**Implementation proposal, not a live API inventory.** Gate action names below are canonical candidates. Payload specimens are intentionally separate from the SDK-owned transport. Authentication, tenant, correlation and transport lineage remain in the validated transport context. Per-action payload and result schemas are supplied as implementation proposals for owner review; memory request/receipt semantics continue to bind to the existing owner contract.

| Action | Request specimen | Core result specimen | Effect | Semantics |
| --- | --- | --- | --- | --- |
| agent.work.submit | AgentSubmitRequest | AgentOperationReceipt | write | Bind an authorized objective/observation to one universal Work Item; persist before acknowledging. |
| agent.work.advance | AgentAdvanceRequest | AgentOperationReceipt | write | Acquire the current Work Item revision and fence, satisfy context requirements, produce a bounded next disposition. |
| agent.work.inspect | AgentInspectRequest | AgentInspectResult | read | Read authorized Work Item and linked receipts without advancing it. |
| agent.work.reconcile | AgentReconcileRequest | AgentOperationReceipt | write | Resolve uncertain prior effects using authoritative operation receipts before any subsequent action. |
| agent.work.cancel | AgentCancelRequest | AgentOperationReceipt | write | Persist cancellation request and propagate only capability-supported cancellation with narrowed authority. |

## Common boundary obligations

Every request validates authenticated role, effective scope, purpose, action grant, contract identity, size and deadline before effects. A payload scope is a request, never a grant. Domain write requests bind operation identity and request digest; exact replay returns the original authoritative result and mismatch conflicts. Read pagination has explicit limits/cursors and reports coverage. Service errors distinguish invalid request, forbidden, not found, conflict, unavailable, deadline, partial and outcome unknown. No generic success boolean is sufficient.

### agent.work.submit

Bind an authorized objective/observation to one universal Work Item; persist before acknowledging. Duplicate operation returns the original Work Item reference, never a second object.

**Receipt obligation:** bind action/operation, authenticated scope, owner contract, input digest and observed outcome. For reads report source coordinates, bounds and omissions. For mutations report committed revision or authoritative destination receipt. Transport acceptance alone never satisfies semantic completion.

**Negative proof:** l9agentos-api-1: refuse scope/contract mismatch and do not perform undeclared effects.

**Capability-specific completion:** see CAPABILITY_DETAILS.md and tests named in TEST_PLAN.md. Dependencies must fail visibly without bypass.

### agent.work.advance

Acquire the current Work Item revision and fence, satisfy context requirements, produce a bounded next disposition. One eligible attempt per exact intent identity; no-op, waiting and blocked are valid outcomes.

**Receipt obligation:** bind action/operation, authenticated scope, owner contract, input digest and observed outcome. For reads report source coordinates, bounds and omissions. For mutations report committed revision or authoritative destination receipt. Transport acceptance alone never satisfies semantic completion.

**Negative proof:** l9agentos-api-2: refuse scope/contract mismatch and do not perform undeclared effects.

**Capability-specific completion:** see CAPABILITY_DETAILS.md and tests named in TEST_PLAN.md. Dependencies must fail visibly without bypass.

### agent.work.inspect

Read authorized Work Item and linked receipts without advancing it. No hidden retry, cognition, activation or external effect.

**Receipt obligation:** bind action/operation, authenticated scope, owner contract, input digest and observed outcome. For reads report source coordinates, bounds and omissions. For mutations report committed revision or authoritative destination receipt. Transport acceptance alone never satisfies semantic completion.

**Negative proof:** l9agentos-api-3: refuse scope/contract mismatch and do not perform undeclared effects.

**Capability-specific completion:** see CAPABILITY_DETAILS.md and tests named in TEST_PLAN.md. Dependencies must fail visibly without bypass.

### agent.work.reconcile

Resolve uncertain prior effects using authoritative operation receipts before any subsequent action. Unknown remains unknown; this is not a retry endpoint.

**Receipt obligation:** bind action/operation, authenticated scope, owner contract, input digest and observed outcome. For reads report source coordinates, bounds and omissions. For mutations report committed revision or authoritative destination receipt. Transport acceptance alone never satisfies semantic completion.

**Negative proof:** l9agentos-api-4: refuse scope/contract mismatch and do not perform undeclared effects.

**Capability-specific completion:** see CAPABILITY_DETAILS.md and tests named in TEST_PLAN.md. Dependencies must fail visibly without bypass.

### agent.work.cancel

Persist cancellation request and propagate only capability-supported cancellation with narrowed authority. Cancellation request differs from confirmed cancellation and compensation.

**Receipt obligation:** bind action/operation, authenticated scope, owner contract, input digest and observed outcome. For reads report source coordinates, bounds and omissions. For mutations report committed revision or authoritative destination receipt. Transport acceptance alone never satisfies semantic completion.

**Negative proof:** l9agentos-api-5: refuse scope/contract mismatch and do not perform undeclared effects.

**Capability-specific completion:** see CAPABILITY_DETAILS.md and tests named in TEST_PLAN.md. Dependencies must fail visibly without bypass.

## Owner acceptance before implementation

This pack includes operation-specific read pages, inspect/status selectors, cancellation and lifecycle requests, claim and acknowledgment receipts, and exact-base context refresh requests. The owner contract PR must verify every shape against its behavioral contract, publish versioned schema/model parity and bind errors to the existing canonical transport. Memory remains deliberately mapped to its existing public request/receipt models; the wrapper shell never substitutes for owner validation. Proposed schemas do not certify runtime behavior.
