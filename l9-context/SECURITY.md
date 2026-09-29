# l9-context security boundary

## Inputs treated as untrusted
Request payloads, profile source fragments, retrieved text, provider callbacks, archive paths, attachment references and declared actor names. An authenticated transport still requires destination resource authorization.

## Policy
Accept only admitted schema versions and action names; reject unknown fields outside explicitly bounded extension payloads. Bind requested scope to authenticated principal claims. Require purpose and consent when the owner contract demands them. Prohibit profiles and context text from issuing credentials, registry entries or security roles.

## Controls
Bound request bytes, object depth, array counts, per-principal concurrency, evaluation rounds, deadline, external model calls and adapter read sizes. Use encrypted secret injection; no secret values in profile artifacts, evidence samples, error messages or generated config. Source URLs must pass scheme/host restrictions and authorization to prevent server-side request forgery. Schema references resolve from an admitted catalog/package, not arbitrary network URLs supplied by a caller.

## Execution and replay
Use one logical operation identity, explicit expected revision and a fenced claim when needed. A hash is integrity evidence, not actor authentication. An outbox delivery identity is not a permission grant. Replays recheck revocation/retention rules and cannot resurrect deleted source material or reproduce settled external effects.

## Audit and privacy
Log event IDs, operation IDs, scope references and safe reason codes. Redact payloads by default. Store private data only at the owning evidence/memory/state service under explicit retention. Any local metadata store is restricted to this node's own mechanical recovery, never a shadow canonical store for another node.
