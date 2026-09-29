# Media transport versus constellation control

## Hard routing rule
All semantic inter-node calls, turn delivery, response decisions, State/Evidence operations and capability requests cross Gate using Gate_SDK. A latency target cannot justify an AgentOS-to-Communication peer WebSocket, direct callback URL or duplicated transport envelope.

## External media is different
A caller microphone/video stream and the media provider are outside the L9 node mesh. Audio/video packets can use the provider's negotiated media plane after authorization. That stream is private adapter I/O; it carries no L9 node delegation authority. The canonical control path still admits the session, constrains participants/features and receives bounded events/receipts through Gate.

## Streamed semantic output
Prefer the existing Gate/SDK-supported streaming or bounded chunk/session contract when available. If that transport is not admitted, use bounded final-turn request/response and mark interactive token streaming unavailable. Do not invent a bypass. `SDK-03` is a compatibility proof and gap-only change, not permission to build a second streaming stack.

## Backpressure and deadlines
Bound queued turns, chunk bytes, frame sampling, per-session duration and per-tenant concurrency. Preserve interruption priority without letting untrusted event rate starve other tenants. Carry the remaining budget into each semantic hop. For a long-lived session, each authorized operation has its own bounded budget linked to the session; do not refresh a root timeout repeatedly or claim one HTTP request lasts indefinitely.

## Directionality
Ordinary consumers may request permitted communication operations and receive correlated responses or poll owned operation results. They are not registered node targets. Only admitted node manifestations receive Gate-dispatched semantic observations. External provider callbacks enter through authenticated boundary code and cannot masquerade as node-origin packets.
