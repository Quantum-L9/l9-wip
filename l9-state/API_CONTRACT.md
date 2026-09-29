# Capability contract: l9-state

**Implementation proposal, not a live API inventory.** Gate action names below are canonical candidates. Payload specimens are intentionally separate from the SDK-owned transport. Authentication, tenant, correlation and transport lineage remain in the validated transport context. Per-action payload and result schemas are supplied as implementation proposals for owner review; memory request/receipt semantics continue to bind to the existing owner contract.

| Action | Request specimen | Core result specimen | Effect | Semantics |
| --- | --- | --- | --- | --- |
| state.create | StateCreateRequest | StateReceipt | write | Validate registered schema and scope; establish revision zero atomically with receipt and event. |
| state.get | StateReadRequest | StateReadResult | read | Read exact scoped current or named revision plus payload through the authorized service. |
| state.transition | StateTransitionRequest | StateReceipt | write | Compare expected revision/digest and required claim fence before atomic commit. |
| state.history | StateHistoryRequest | StateHistoryPage | read | Read ordered authorized journal using bounded pagination. |
| state.checkpoint | StateTransitionRequest | StateReceipt | write | Commit a schema-bound checkpoint using the same conditional-write unit of work. |
| state.claim | StateClaimRequest | StateClaimReceipt | write | Issue a policy-capped lease with monotonic fence under atomic ownership control. |
| state.renew | StateLeaseMutationRequest | StateClaimReceipt | write | Renew only the current nonexpired claim owned by authenticated caller. |
| state.release | StateLeaseMutationRequest | StateClaimReceipt | write | Release an exact active claim without resetting its fencing lineage. |
| state.events | StateEventReadRequest | StateEventPage | read | Read a bounded page of committed semantic events, not raw provider change records. |
| state.ack | StateAckRequest | StateAckReceipt | write | Durably advance a scoped consumer checkpoint after idempotent processing. |
| state.tombstone | StateTransitionRequest | StateReceipt | write | Commit retirement/deletion marker under conditional revision and retention policy. |
| state.list | StateListRequest | StateListPage | read | Enumerate authorized state references by admitted schema and generic lifecycle with bounded stable pagination. |
| state.operation.inspect | StateOperationInspectRequest | StateOperationInspectResult | read | Resolve the original operation receipt under exact scope without replaying a mutation. |

## Common boundary obligations

Every request validates authenticated role, effective scope, purpose, action grant, contract identity, size and deadline before effects. A payload scope is a request, never a grant. Domain write requests bind operation identity and request digest; exact replay returns the original authoritative result and mismatch conflicts. Read pagination has explicit limits/cursors and reports coverage. Service errors distinguish invalid request, forbidden, not found, conflict, unavailable, deadline, partial and outcome unknown. No generic success boolean is sufficient.

### state.create

Validate registered schema and scope; establish revision zero atomically with receipt and event. Same key/same request returns receipt; same key/different request conflicts.

**Receipt obligation:** bind action/operation, authenticated scope, owner contract, input digest and observed outcome. For reads report source coordinates, bounds and omissions. For mutations report committed revision or authoritative destination receipt. Transport acceptance alone never satisfies semantic completion.

**Negative proof:** l9state-api-1: refuse scope/contract mismatch and do not perform undeclared effects.

**Capability-specific completion:** see CAPABILITY_DETAILS.md and tests named in TEST_PLAN.md. Dependencies must fail visibly without bypass.

### state.get

Read exact scoped current or named revision plus payload through the authorized service. Absence, denial and service failure remain distinct.

**Receipt obligation:** bind action/operation, authenticated scope, owner contract, input digest and observed outcome. For reads report source coordinates, bounds and omissions. For mutations report committed revision or authoritative destination receipt. Transport acceptance alone never satisfies semantic completion.

**Negative proof:** l9state-api-2: refuse scope/contract mismatch and do not perform undeclared effects.

**Capability-specific completion:** see CAPABILITY_DETAILS.md and tests named in TEST_PLAN.md. Dependencies must fail visibly without bypass.

### state.transition

Compare expected revision/digest and required claim fence before atomic commit. Exactly one concurrent writer wins; stale writers cannot silently overwrite.

**Receipt obligation:** bind action/operation, authenticated scope, owner contract, input digest and observed outcome. For reads report source coordinates, bounds and omissions. For mutations report committed revision or authoritative destination receipt. Transport acceptance alone never satisfies semantic completion.

**Negative proof:** l9state-api-3: refuse scope/contract mismatch and do not perform undeclared effects.

**Capability-specific completion:** see CAPABILITY_DETAILS.md and tests named in TEST_PLAN.md. Dependencies must fail visibly without bypass.

### state.history

Read ordered authorized journal using bounded pagination. Truncation and missing history are explicit, not complete history.

**Receipt obligation:** bind action/operation, authenticated scope, owner contract, input digest and observed outcome. For reads report source coordinates, bounds and omissions. For mutations report committed revision or authoritative destination receipt. Transport acceptance alone never satisfies semantic completion.

**Negative proof:** l9state-api-4: refuse scope/contract mismatch and do not perform undeclared effects.

**Capability-specific completion:** see CAPABILITY_DETAILS.md and tests named in TEST_PLAN.md. Dependencies must fail visibly without bypass.

### state.checkpoint

Commit a schema-bound checkpoint using the same conditional-write unit of work. A checkpoint stores continuation data; it grants no execution authority.

**Receipt obligation:** bind action/operation, authenticated scope, owner contract, input digest and observed outcome. For reads report source coordinates, bounds and omissions. For mutations report committed revision or authoritative destination receipt. Transport acceptance alone never satisfies semantic completion.

**Negative proof:** l9state-api-5: refuse scope/contract mismatch and do not perform undeclared effects.

**Capability-specific completion:** see CAPABILITY_DETAILS.md and tests named in TEST_PLAN.md. Dependencies must fail visibly without bypass.

### state.claim

Issue a policy-capped lease with monotonic fence under atomic ownership control. Expired/reassigned holder cannot renew, release another claim or write.

**Receipt obligation:** bind action/operation, authenticated scope, owner contract, input digest and observed outcome. For reads report source coordinates, bounds and omissions. For mutations report committed revision or authoritative destination receipt. Transport acceptance alone never satisfies semantic completion.

**Negative proof:** l9state-api-6: refuse scope/contract mismatch and do not perform undeclared effects.

**Capability-specific completion:** see CAPABILITY_DETAILS.md and tests named in TEST_PLAN.md. Dependencies must fail visibly without bypass.

### state.renew

Renew only the current nonexpired claim owned by authenticated caller. Retry identity is stable; renewal cannot resurrect a superseded fence.

**Receipt obligation:** bind action/operation, authenticated scope, owner contract, input digest and observed outcome. For reads report source coordinates, bounds and omissions. For mutations report committed revision or authoritative destination receipt. Transport acceptance alone never satisfies semantic completion.

**Negative proof:** l9state-api-7: refuse scope/contract mismatch and do not perform undeclared effects.

**Capability-specific completion:** see CAPABILITY_DETAILS.md and tests named in TEST_PLAN.md. Dependencies must fail visibly without bypass.

### state.release

Release an exact active claim without resetting its fencing lineage. Repeated release is harmless and cannot release a new holder.

**Receipt obligation:** bind action/operation, authenticated scope, owner contract, input digest and observed outcome. For reads report source coordinates, bounds and omissions. For mutations report committed revision or authoritative destination receipt. Transport acceptance alone never satisfies semantic completion.

**Negative proof:** l9state-api-8: refuse scope/contract mismatch and do not perform undeclared effects.

**Capability-specific completion:** see CAPABILITY_DETAILS.md and tests named in TEST_PLAN.md. Dependencies must fail visibly without bypass.

### state.events

Read a bounded page of committed semantic events, not raw provider change records. Cursor is opaque and scoped; retained-journal exhaustion requires resync.

**Receipt obligation:** bind action/operation, authenticated scope, owner contract, input digest and observed outcome. For reads report source coordinates, bounds and omissions. For mutations report committed revision or authoritative destination receipt. Transport acceptance alone never satisfies semantic completion.

**Negative proof:** l9state-api-9: refuse scope/contract mismatch and do not perform undeclared effects.

**Capability-specific completion:** see CAPABILITY_DETAILS.md and tests named in TEST_PLAN.md. Dependencies must fail visibly without bypass.

### state.ack

Durably advance a scoped consumer checkpoint after idempotent processing. No cross-consumer or out-of-order acknowledgment beyond delivered eligibility.

**Receipt obligation:** bind action/operation, authenticated scope, owner contract, input digest and observed outcome. For reads report source coordinates, bounds and omissions. For mutations report committed revision or authoritative destination receipt. Transport acceptance alone never satisfies semantic completion.

**Negative proof:** l9state-api-10: refuse scope/contract mismatch and do not perform undeclared effects.

**Capability-specific completion:** see CAPABILITY_DETAILS.md and tests named in TEST_PLAN.md. Dependencies must fail visibly without bypass.

### state.tombstone

Commit retirement/deletion marker under conditional revision and retention policy. Never erase claim or operation history needed for unresolved effects.

**Receipt obligation:** bind action/operation, authenticated scope, owner contract, input digest and observed outcome. For reads report source coordinates, bounds and omissions. For mutations report committed revision or authoritative destination receipt. Transport acceptance alone never satisfies semantic completion.

**Negative proof:** l9state-api-11: refuse scope/contract mismatch and do not perform undeclared effects.

**Capability-specific completion:** see CAPABILITY_DETAILS.md and tests named in TEST_PLAN.md. Dependencies must fail visibly without bypass.

### state.list

Enumerate authorized state references by admitted schema and generic lifecycle with bounded stable pagination. Supports cold resume without a second AgentOS directory database; no arbitrary payload query or provider query syntax.

**Receipt obligation:** bind action/operation, authenticated scope, owner contract, input digest and observed outcome. For reads report source coordinates, bounds and omissions. For mutations report committed revision or authoritative destination receipt. Transport acceptance alone never satisfies semantic completion.

**Negative proof:** l9state-api-12: refuse scope/contract mismatch and do not perform undeclared effects.

**Capability-specific completion:** see CAPABILITY_DETAILS.md and tests named in TEST_PLAN.md. Dependencies must fail visibly without bypass.

### state.operation.inspect

Resolve the original operation receipt under exact scope without replaying a mutation. Only authoritative committed receipt proves effect; not_found or unknown cannot independently prove external no-effect.

**Receipt obligation:** bind action/operation, authenticated scope, owner contract, input digest and observed outcome. For reads report source coordinates, bounds and omissions. For mutations report committed revision or authoritative destination receipt. Transport acceptance alone never satisfies semantic completion.

**Negative proof:** l9state-api-13: refuse scope/contract mismatch and do not perform undeclared effects.

**Capability-specific completion:** see CAPABILITY_DETAILS.md and tests named in TEST_PLAN.md. Dependencies must fail visibly without bypass.

## Owner acceptance before implementation

This pack includes operation-specific read pages, inspect/status selectors, cancellation and lifecycle requests, claim and acknowledgment receipts, and exact-base context refresh requests. The owner contract PR must verify every shape against its behavioral contract, publish versioned schema/model parity and bind errors to the existing canonical transport. Memory remains deliberately mapped to its existing public request/receipt models; the wrapper shell never substitutes for owner validation. Proposed schemas do not certify runtime behavior.
