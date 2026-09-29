# ProviderComposition and selected stack

`ProviderComposition` is a deployment-owned choice of implementations for a semantic capability. It is not an AgentProfile. An AgentProfile may request a communication class and required features, but does not embed credentials, provider runtime objects or a right to switch implementations.

| Execution class | First-attempt composition | Admission obligation |
|---|---|---|
| Managed realtime | Agora + admitted STT + ElevenLabs TTS | Semantic turns go to AgentOS through Gate; no provider-owned memory or business tools |
| Telecom/outbound | Twilio capability / ConversationRelay where suitable | Proven call/session correlation, interruption, sender/recipient controls, timeout reconciliation |
| Messaging | Admitted Twilio channel adapter | Channel-specific deliverability and sender requirements; no hidden cross-channel fallback |
| Native email | Gmail or separately admitted mailbox adapter | Exact mailbox/thread identity, scoped access, duplicate-send reconciliation and minimal raw-body retention |
| Optional self-hosted realtime | Pipecat composition | Uses shared contracts and Gate bridge; no duplicated AgentOS or private semantic link |
| Bounded perception | Admitted perception provider | Modality/size/window/consent limits and uncertainty-bearing output |

The donor lists provider families, not proof of live compatibility. Current provider versions, account entitlement, region, API surface, feature status and allowed retention must be pinned and tested before release. Do not infer SDK versions from a blog or inherit provider-default agent behavior.

## Negotiation
Compute the intersection of requested capability, independent grant, region/privacy constraints and the adapter's verified capability descriptor. Required features cannot be dropped. Optional omissions appear in the receipt. An alternate composition is allowed only if explicitly authorized for this operation and semantically equivalent for the required features; record both the selection rule and resulting implementation identity.

## SDK-first does not mean authority delegation
Use the highest-level supported provider SDK that preserves the boundary. If a managed agent product cannot route semantic answer generation to the external L9 path without retaining an uncontrolled tool/memory brain, it fails admission for that execution class. Prefer an admitted lower media/turn surface to weakening the invariant.

Avoid building provider fallback frameworks, a general notification engine or another realtime framework. Selected provider tools remain replaceable; there is one communication capability contract, not one API per provider.
