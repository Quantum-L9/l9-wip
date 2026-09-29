# L9-AgentOS architecture

## Layering
`bindings` owns Gate action-to-domain translation. `services` or `application` owns the single capability operation. `domain` owns its typed invariants. `ports` describe required behavior without provider types. `adapters` implement those ports. The node chassis comes from the admitted L9 SDK/factory; no locally invented HTTP/auth/transport framework.

## Owned implementation surfaces
- `l9_agentos/domain/objectives.py`.
- `l9_agentos/domain/work_items.py`.
- `l9_agentos/domain/observations.py`.
- `l9_agentos/domain/decisions.py`.
- `l9_agentos/domain/action_intents.py`.
- `l9_agentos/domain/delegation.py`.
- `l9_agentos/profiles/compiler.py`.
- `l9_agentos/profiles/resolver.py`.
- `l9_agentos/profiles/lifecycle.py`.
- `l9_agentos/autonomy/evaluator.py`.
- `l9_agentos/application/observation_loop.py`.
- `l9_agentos/application/intent_loop.py`.
- `l9_agentos/application/resume.py`.
- `l9_agentos/bindings/gate_actions.py`.
- `l9_agentos/ports/capabilities.py`.

## Resource and transaction boundary
The owning service validates scope and semantic request before any I/O. Domain objects and persisted metadata carry schema/profile/source identity where applicable. Large content is referenced by immutable digest-bound evidence rather than copied into control-plane packets. A cross-node call cannot participate in a local database transaction; settle it through durable operation identities and receipts.

## Security placement
SDK/Gate authenticate the transport and route only admitted actions. The node reauthorizes the exact requested resources and purpose. A user-supplied namespace, capability name, schema reference, profile digest or source URL is an input to validation, never proof. Errors redact secrets and reveal no unauthorized existence information.

## Failure design
Canonical writes fail closed; optional enrichment can be degraded only when the capability's declared policy allows it. Transport timeout does not prove no mutation. All consequential retries carry the original operation key and use the owner's receipt lookup/reconciliation surface. Per-repo details are in CAPABILITY_DETAILS.md.

## Deployment independence
Publish a separate runtime artifact and maintain a separate lockfile. The server image owns only this node's adapters. Consumer contracts/client extras must not install server database drivers. Tests prove replacement of an adapter does not change public payloads, source identities or failure semantics.

## Donor use
- Mack domain ports, context authority ordering and source-binding negative tests.
- Emma approval-version/evidence/tenant isolation behavior and multimodal interaction semantics.
- LCTO revision/digest-bound work coordination and ambiguous-dispatch recovery.
- Cursor-Governance generic autonomy policy/evaluator concepts, after removing coding assumptions.

Donor code is not copied merely because it passes its old tests. Map behavior, inspect required invariants, reject duplicate owners, and rewrite bindings to canonical vocabulary. Preserve old identities only in explicit migration records.
