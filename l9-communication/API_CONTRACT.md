# API and payload contracts

All schemas are proposed owner payload contracts, not new TransportPacket definitions. Gate action bindings are indexed in `../../02_architecture/ACTION_OWNERSHIP_PROPOSAL.yaml`. Authentication, scope, digest equality, authority, cross-field semantics and runtime limits require service validation beyond JSON Schema.

## Schema inventory
- `ChannelTarget.schema.json`: `urn:l9:devpack:l9-communication:ChannelTarget:0.1`.
- `SendContent.schema.json`: `urn:l9:devpack:l9-communication:SendContent:0.1`.
- `CommunicationRequest.schema.json`: `urn:l9:devpack:l9-communication:CommunicationRequest:0.1`.
- `CommunicationCapabilitiesRequest.schema.json`: `urn:l9:devpack:l9-communication:CommunicationCapabilitiesRequest:0.1`.
- `ProviderCapability.schema.json`: `urn:l9:devpack:l9-communication:ProviderCapability:0.1`.
- `CommunicationCapabilitiesReceipt.schema.json`: `urn:l9:devpack:l9-communication:CommunicationCapabilitiesReceipt:0.1`.
- `ProviderComposition.schema.json`: `urn:l9:devpack:l9-communication:ProviderComposition:0.1`.
- `CommunicationExecutionPlan.schema.json`: `urn:l9:devpack:l9-communication:CommunicationExecutionPlan:0.1`.
- `CommunicationEvent.schema.json`: `urn:l9:devpack:l9-communication:CommunicationEvent:0.1`.
- `CommunicationReceipt.schema.json`: `urn:l9:devpack:l9-communication:CommunicationReceipt:0.1`.
- `SessionOpenRequest.schema.json`: `urn:l9:devpack:l9-communication:SessionOpenRequest:0.1`.
- `SessionRespondRequest.schema.json`: `urn:l9:devpack:l9-communication:SessionRespondRequest:0.1`.
- `SessionCloseRequest.schema.json`: `urn:l9:devpack:l9-communication:SessionCloseRequest:0.1`.
- `CommunicationInspectRequest.schema.json`: `urn:l9:devpack:l9-communication:CommunicationInspectRequest:0.1`.
- `CommunicationInspectResult.schema.json`: `urn:l9:devpack:l9-communication:CommunicationInspectResult:0.1`.
- `PerceptionRequest.schema.json`: `urn:l9:devpack:l9-communication:PerceptionRequest:0.1`.
- `PerceptionResult.schema.json`: `urn:l9:devpack:l9-communication:PerceptionResult:0.1`.

## Behavioral validation
Unknown fields fail closed. A nonempty string naming a law, scope or evidence is not proof that it exists or is authorized. Resolve these references against owner services and independent admission evidence. Verify original operation/payload identity and current rights on every effect or solve. Caps in schemas are absolute proposed ceilings, not production SLOs or rights. Effective deployment limits may be narrower.

## Compatibility
The v0.1 payloads have not been registered live. Freeze public owner versions during implementation before routing. Publish a new incompatible version for breaking semantics; do not redefine a deployed family or silently translate old requests. Fixtures test shape and selected proof invariants, not provider readiness.
