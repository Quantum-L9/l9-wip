# Donor migration and contract convergence

| Original pack element | Revised disposition |
|---|---|
| CommunicationIntent | CommunicationRequest payload carried by existing ActionIntent commitment |
| CommunicationEvent | CommunicationEvent payload bound to universal Observation/Evidence |
| CommunicationReceipt | Capability receipt with effect-strength and native correlation |
| Provider profile | ProviderComposition / CommunicationExecutionPlan, never AgentProfile |
| Voice bridge | Thin provider-edge turn adapter; semantic L9 traffic remains through Gate |
| Direct memory/context integration | Removed; AgentOS requests Context/Memory independently |
| Redis active session dependency borrowed from memory | Removed; transient buffers stay bounded, durable metadata uses State |
| Durable receipt owner unresolved | Bound to Evidence; operation settlement uses State |
| Agora / ElevenLabs / Twilio selection | Retained first-attempt options; explicit provider admission remains required |
| Pipecat | Optional implementation adapter, not new architecture |
| Novu and TEN | Deferred candidate/donor knowledge, no mandatory new runtime |
| Unified conversation authority | Still prohibited; preserve native channel identity |
| Video/perception | Preserve interface boundary; enable concrete features only when independently admitted |
| Python modular implementation | One scoped node implementation, not a constellation monolith |

The original source archive remains reference-only. Revised contracts supersede donor statements assigning memory ownership, bypassing Gate or treating named agent experiments as architectural types. Historical donor validation is not evidence of live integration.
