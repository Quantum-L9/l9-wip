# L9 Agent Communication Plane

## Mission
`l9-communication` is the intended separately deployable L9 node for controlled access to external communication and perception. AgentOS manifestations plug into shared channel, realtime and bounded perception capabilities. The node transports, transcribes, renders and normalizes. It does not become the agent's brain.

External world <-> provider adapters <-> Communication <-> Gate <-> AgentOS.

Provider-specific APIs are implementation details. Communication does not read Memory, invoke a local agent runtime, merge identities across channels, decide what a message means to an Objective or mutate a Work Item. It returns Observations and capability Receipts. AgentOS decides what those observations mean and which governed next ActionIntent to issue.

## V1 stack direction
Retain the donor's selected composition direction: Agora managed realtime, ElevenLabs premium voice rendering, Twilio telecom/messaging and a native email adapter where admitted. Pipecat is optional and requirement-gated. TEN remains donor inspiration; Novu is a deferred candidate, not an extra mandatory control plane. Every composition must prove that agent cognition and tools remain outside the media provider.

## Read order
`BOUNDARY.yaml`, `ARCHITECTURE.md`, `PROVIDER_COMPOSITION.md`, `API_CONTRACT.md`, `MEDIA_VS_CONTROL.md`, `EFFECTS_AND_RECONCILIATION.md`, `TEST_PLAN.md`, then `execution_contract.yaml`.

This is an implementation specification with offline contract fixtures. No phone call, message, recording, payment or provider deployment is performed by this pack.
