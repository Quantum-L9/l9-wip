# Bounded perception

Communication exposes perception as a bounded capability over an authorized input reference or negotiated media window. The media provider may produce transcripts, scene descriptions or structured observations, but those outputs are observations/inferences with provenance and limitations, not canonical facts or instructions.

## Request boundary
Bind modality, artifact/session reference, allowed observation classes, window/frame/byte limits, purpose, consent, privacy classification and budget. Any remote input reference is resolved by the authorized owner, not fetched from an arbitrary caller URL. No continuous capture is implied by a still-image request.

## Result boundary
Return an Observation reference, source coordinates, timestamp/window, confidence or an explicit confidence-unavailable state, transformation/provider identity, exclusions and processing limitations. Separate source-visible content from inferred interpretation. A scene label or transcript can be uncertain; never silently replace that uncertainty with a formal fact.

## Routing after perception
Communication -> Gate -> AgentOS supplies the observation. AgentOS may request Ingest to transform/retain permitted source material, Context to acquire relevant evidence, or Formal Reasoning to evaluate a separately admitted fact projection. Communication does not perform that downstream reasoning or write Memory.

## Privacy and scope
Recording, raw media retention, voice identity/clone, biometric inference and model-provider disclosure each require their own admitted capability and rights. Capability support does not grant consent. Exclude unsupported or disallowed classes before invoking the provider. Zero retained raw media is a valid successful outcome when a bounded transient observation is authorized.

V1 proves the boundary with bounded synthetic text/image/media-reference fixtures. Live video/avatar/biometric features remain separately admitted extensions, not prerequisites to basic text and voice communication.
