# Repository roadmap

Planned implementation only. PRs remain scoped to this repository; dependencies are evidence gates, not permission to edit another owner.

## COMM-01 - Birth communication payloads and provider-composition boundary

Prerequisites: EXT-01, SDK-02, GATE-01

1. Use the current canonical node birth path.
2. Implement strict payload validation and generic capability descriptors.
3. Keep AgentOS cognition and provider composition distinct.
4. Implement authenticated external input boundary and native channel correlation contracts.

**Acceptance:** All proposed communication payloads have strict positive/negative tests. No provider-specific field or peer URL enters canonical requests.

**Required negatives:** Provider tool/memory defaults are refused by composition admission. Webhook body cannot choose tenant or node role.

## COMM-02 - Persist effect operations and reconcile uncertain outcomes

Prerequisites: COMM-01, STATE-03, EVID-03

1. Bind State generic operation schemas with revision and fencing.
2. Commit prepared intent before network action.
3. Normalize acceptance/delivery/cancellation strength and preserve native IDs.
4. Implement inspect/reconcile against original operation identity.
5. Retain redacted effect receipts via Evidence with explicit failure behavior.

**Acceptance:** Crash after provider effect cannot silently resend. Receipt strength and State/Evidence ownership remain separate.

**Required negatives:** Same key/different recipient conflicts. Unknown outcome cannot be retried with a new key.

## COMM-03 - Admit messaging and email provider adapters

Prerequisites: COMM-02

1. Pin reviewed provider SDK/API/account capability evidence.
2. Implement thin native messaging/email adapters and scoped recipient resolution.
3. Verify webhook signatures, replay protection, thread correlation and body minimization.
4. Run synthetic and explicitly authorized sandbox recipient cases.

**Acceptance:** One common request contract operates across admitted channels. A provider lacking required receipt/privacy features is not advertised ready.

**Required negatives:** Two channel display names cannot merge person identity. A callback replay does not duplicate an Observation or external reply.

## COMM-04 - Admit realtime composition and interruption-safe output

Prerequisites: COMM-02, SDK-03

1. Prove Agora/ElevenLabs and Twilio execution composition behavior from exact selected versions.
2. Implement provider-edge turn translation only.
3. Bind session/turn/generation/sequence and drop stale response chunks.
4. Use Gate-owned transport support or explicitly limited final-turn mode.
5. Measure end-to-end latency, stop/reconnect behavior and cleanup.

**Acceptance:** No semantic response bypass or provider brain. Interruption fences prevent post-cancel stale playback requests.

**Required negatives:** Late chunk from prior generation is dropped. Missing Gate streaming support cannot create a direct peer connection.

## COMM-05 - Qualify bounded perception, privacy and operator recovery

Prerequisites: COMM-03, COMM-04, GATE-03

1. Implement bounded perception request/result capability with admitted provider or honest unavailable status.
2. Test input reference authorization and source coordinates.
3. Demonstrate privacy controls, redaction, retention and revoked consent.
4. Run live channel tests only under explicit current authorization.
5. Publish per-feature readiness rather than pass-all status.

**Acceptance:** Basic messaging/voice readiness is distinct from optional video/avatar capabilities. Every requested perception feature is either demonstrated or explicitly unavailable.

**Required negatives:** A still-image request cannot turn on continuous recording. Perception content cannot change law/grants or write memory.
