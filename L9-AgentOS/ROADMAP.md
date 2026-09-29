# Repository roadmap

Planned implementation only. PRs remain scoped to this repository; dependencies are evidence gates, not permission to edit another owner.

## BASE-01 - Rehydrate authority and inspect current owners

Prerequisites: 

1. Read locked intent, decision register, repository maps, source baselines and relevant owner invariants.
2. Resolve all current default-branch heads and existing open work affecting these seams; do not assume pinned snapshots remain current.
3. Verify whether target repos already exist and identify the current canonical runnable-node birth front door without invoking publication.
4. Probe installed/public dependencies and node action inventories. Separate observed, absent and inaccessible resources.
5. Record changes from this pack and route material conflicts to the architecture owner without re-deciding explicit user locks.

**Acceptance:** Every named repository/dependency has observed identity or a typed blocking absence for its dependent unit. No existing owner is silently replaced and no fabricated factory command is used.

**Required negatives:** Stale source SHA must cause refresh/review, not silently pass. Unavailable provider cannot be recorded as validated.

## AG-01 - Freeze universal semantic contracts and owner bindings

Prerequisites: BASE-01

1. Reconcile this pack semantic contracts against current owner models.
2. Define universal primitive identity, lifecycle, state/reference boundaries and first-class profile compilation.
3. Replace legacy vocabulary only through explicit migration maps; do not rename external source APIs blindly.
4. Publish behavioral positive/negative fixtures before using machine schemas as API authority.

**Acceptance:** Work Item and AgentProfile definitions are complete and provider neutral. Schema references have one owner and no copied TransportPacket/MemoryRecord.

**Required negatives:** Reject competing work primitive keys in canonical payloads. State revision cannot be forged inside WorkItem payload.

## AG-02 - Implement multi-artifact AgentProfile compiler

Prerequisites: AG-01

1. Resolve only bounded local/approved immutable refs with content hashes.
2. Validate all first-class sections and cross-profile restrictions.
3. Normalize/digest semantics; keep deployment secrets and node grants external.
4. Reject cycles, ambiguous overrides, executable code and capability escalation.

**Acceptance:** All five specimen manifestations compile through identical code. No profile name branches or domain logic in compiler.

**Required negatives:** Missing section/hash mismatch/traversal rejected. Profile change cannot silently upgrade active Work Item authority.

## AG-03 - Implement universal Work Item and observation lifecycle

Prerequisites: AG-02, STATE-03, EVID-01

1. Instantiate manifestation identity separately from profile/replica/principal.
2. Persist universal Work Item through State and source evidence references through Evidence.
3. Model multiple actors/modalities with authenticated attribution, not implicit operator equivalence.
4. Implement interrupt/resume/cancel and dependency references without external capability effects.

**Acceptance:** Exactly same lifecycle handles each profile specimen. Cold restart recovers exact Work Item without a parallel local ledger.

**Required negatives:** Duplicate observation cannot duplicate Work Item creation. Contact/actor identity is not an authority grant.

## AG-04 - Implement generic autonomy and exact intent commitments

Prerequisites: AG-03, CTX-02, MEM-02

1. Extract generic evaluation mechanics from donor without coding-specific role constants.
2. Evaluate immutable profile, current state, context, grants and budget; default deny/require context as defined.
3. Persist exact ActionIntent digest/key before any external dispatch.
4. Bind approval/revocation/evaluation expiry and capability receipt to exact request.

**Acceptance:** Autonomy allows only an attempt, never overrides Gate/destination. Unknown external effect transitions to reconciliation without blind retry.

**Required negatives:** Grant expires between evaluation and execution: no effect. Proposal/profile/payload changes invalidate prior approval.

## AG-05 - Wire Gate-only capability and delegation execution

Prerequisites: AG-04, GATE-02, CTX-03, ING-03

1. Use SDK node follow-up path preserving ancestry for trusted node execution.
2. Constrain each delegation to intersect parent grants, budget and scope.
3. Reference communication/inference/domain capabilities by approved action contract, not provider URLs.
4. Persist attempts and receipts; feed selected observed outcomes to Ingest/Memory without self-reinforcement.

**Acceptance:** No node calls another node directly or imports its service internals. Delegation/cancellation completion distinguished from request acceptance.

**Required negatives:** Delegate refuses scope expansion and expired parent grant. Lost response reconciles original key before new execution.

## AG-06 - Prove profile-only manifestations and unseen use case

Prerequisites: AG-05

1. Run commercial, assistance, technical and human-service synthetic cases against same immutable AgentOS image.
2. Add unseen profile without code changes and run modality/third-party interaction cases.
3. Check privacy, interruption, uncertain-effect and provider outage behavior.
4. Do not enable real external messages/payments/hiring during this proof.

**Acceptance:** Five manifestations run with identical binary and owner APIs. Capabilities equal in mechanism while policy limits differ declaratively.

**Required negatives:** Per-agent runtime patch fails acceptance. Forbidden raw content cannot enter memory merely via another profile.

## AG-07 - Prove operator readiness, cold recovery and release boundaries

Prerequisites: AG-06, OPS-02

1. Pin all runtime images/packages/provider models by tested version/digest.
2. Exercise replica failure, database failover, missing node, provider delay, privacy erasure and profile rollback.
3. Observe metrics and alert paths against workload assumptions.
4. Request separate deployment/data-cutover authorization only after evidence is complete.

**Acceptance:** No production-ready claim without all runtime gates. Hydration handoff independently reconstructs exact state and outstanding obligations.

**Required negatives:** Empty required environment/provider proof blocks release. Artifact-validator pass cannot mark staging/runtime gates complete.

## EXT-01 - Reconcile two-plane contracts and donor supersession

Prerequisites: BASE-01, AG-01

1. Read v1.1 decision register, both donor inventories and revised node boundaries.
2. Refresh intended repo existence, current action owners and exact Gate/SDK capability contracts.
3. Classify every donor contract as retained, generalized, moved or superseded without copying old authority.
4. Record native provider/family verification gates separately from offline spec checks.

**Acceptance:** One canonical ReasoningAdapter name; two separately scoped node owners. No user lock re-decided and no source archive treated as deployment authority.

**Required negatives:** A stale donor memory dependency cannot survive as a direct Communication/Reasoning import. An unavailable runtime capability remains unverified.

## AG-08 - Compile capability behavior bindings and admit observations

Prerequisites: AG-05, EXT-01, COMM-01, FR-01

1. Add optional declarative behavior bindings within the existing AgentProfile composition.
2. Verify referenced behavior contracts/digests and independent deployment permissions.
3. Implement generic Observation admission without new Work Item types.
4. Keep Communication/Reasoning requests as universal ActionIntent payloads.

**Acceptance:** Same profile/compiler structure for all manifestations. No native solver/media SDK appears in AgentOS domain code.

**Required negatives:** Behavior reference cannot grant node trust or effect authorization. External source text cannot become profile/law.

## AG-09 - Prove cross-plane perception, reasoning and effect loops

Prerequisites: AG-08, COMM-05, FR-05, CTX-04

1. Run communication observation -> Work Item -> Context -> reasoning evidence -> autonomy -> communication effect with all L9 hops via Gate.
2. Prove exact commitment and original operation recovery.
3. Run the identical runtime against five profile specimens and one unseen profile in conformance.
4. Verify source revocation, budgets, loop limits and non-node restrictions.

**Acceptance:** Communication never becomes brain and reasoning never becomes permission. Single runtime handles all profile fixtures.

**Required negatives:** Reasoning SAT with revoked effect grant yields no send. Duplicate provider event plus source changes cannot generate infinite feedback.
