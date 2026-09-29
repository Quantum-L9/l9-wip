# Architecture

## Outbound path
```text
AgentOS ActionIntent + current autonomy/effect authorization
  -> Gate -> Communication
  exact scope/recipient/content/operation validation
  deployment-owned ProviderComposition admission
  -> Gate -> State: commit prepared operation with revision/fence
  private provider adapter: render/send/connect
  -> Gate -> Evidence: retained redacted receipt
  -> Gate -> State: conditional operation settlement
  response through Gate to original caller
```
Communication owns the meaning of its provider effect receipt. State owns durable mechanics only. A provider acknowledgement is not a delivered message and does not mean the Objective succeeded.

## Inbound path
```text
provider webhook/session stream
  authenticate external source + timestamp/replay window
  bounded parse + account/channel binding + deduplication
  construct provenance-bound Observation payload
  retain only permitted evidence through Gate -> Evidence
  -> Gate -> AgentOS observation admission
```
No inbound speech, message content or provider metadata can nominate a trusted L9 role, choose a peer URL, install law or expand capability rights. Communication binds the intended manifestation using deployment-owned subscription/account configuration. Ambiguity is explicit, not guessed from display name.

## Processing layers
The outer chassis owns inbound L9 authentication, packet and transport behavior. Domain handlers validate communication capability semantics. A provider-composition selector checks exact required features and privacy constraints against deployed adapters. Each adapter owns its provider translation, SDK calls and normalization; it never owns general memory, prompting, source ranking or Work Item advancement.

Small session buffers are permitted for transport/turn mechanics and bounded by TTL/size. Durable resumption, effect identity and fences live in generic State records accessed through Gate. Recordings/transcripts/media bytes, if explicitly permitted, use Evidence retention. There is no Communication memory plane or borrowed Redis from the memory package.

## Three identities stay separate
A native email thread or call session is channel identity. A Work Item is AgentOS operational identity. A person's cross-channel identity is established by an authorized identity/source owner. Correlation links can reference all three, but one does not automatically imply another.
