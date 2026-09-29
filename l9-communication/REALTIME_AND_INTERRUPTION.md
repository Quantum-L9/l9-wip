# Realtime sessions, turns and interruption

## Session lifecycle
`requested -> connecting -> active -> ending -> ended`, with explicit `degraded`, `failed` and `outcome_unknown` outcomes. These are Communication operation states, not alternate AgentOS Work Item types. Native provider state is mapped without silently dropping distinctions relevant to effect recovery.

## Turn contract
Every semantic turn and response chunk binds scope, session reference, turn reference, a turn generation fence, sequence number, content digest and final/partial status. A finalized user turn may supersede partial transcripts. It is not valid to act on a partial transcript unless the profile and capability explicitly permit that bounded action.

A new interruption advances the turn generation, marks prior generation output invalid and sends cancellation/stop to the provider through the owned adapter. Late tokens from a cancelled generation are discarded. Cancellation acknowledgment and already-played media are recorded separately. Do not claim that stopping future playback erased speech already heard.

## Rendering
AgentOS supplies semantic output. Communication performs approved rendering/TTS and delivery. Fixed non-semantic acknowledgements or earcons may be allowed by a composition policy; generated substantive answers, negotiation, authority decisions and business tool calls are not. Any provider-generated filler must be disabled or separately bounded so it cannot speak unapproved substantive content.

## Recovery
Reconnect only within the same authorized participant/session binding. Expired media grants require renewed independent authority, not automatic extension. On process restart read the State operation and query the provider's status only through its approved adapter. An uncertain call origination is not repeated with a fresh operation ID.

## Quality evidence
Measure onset-to-final-turn, Gate round-trip, answer-ready-to-playback, interruption-to-stop, late-token drop count and reconnect outcomes separately. Report observed percentiles and test environment; do not promote target latency to measured SLO. Test high latency, reordering, duplicate chunks and provider disconnect during playback.
