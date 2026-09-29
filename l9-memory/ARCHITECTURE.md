# l9-memory architecture

## Layering
`bindings` owns Gate action-to-domain translation. `services` or `application` owns the single capability operation. `domain` owns its typed invariants. `ports` describe required behavior without provider types. `adapters` implement those ports. The node chassis comes from the admitted L9 SDK/factory; no locally invented HTTP/auth/transport framework.

## Owned implementation surfaces
- `l9_memory_node/bindings/actions.py`.
- `l9_memory_node/bindings/principals.py`.
- `l9_memory_node/bindings/receipts.py`.
- `l9_memory_node/application/composition.py`.
- `l9_memory_node/application/readiness.py`.
- `l9_memory_node/configuration/settings.py`.
- `l9_memory_node/contracts/capability_map.py`.

## Resource and transaction boundary
The owning service validates scope and semantic request before any I/O. Domain objects and persisted metadata carry schema/profile/source identity where applicable. Large content is referenced by immutable digest-bound evidence rather than copied into control-plane packets. A cross-node call cannot participate in a local database transaction; settle it through durable operation identities and receipts.

## Security placement
SDK/Gate authenticate the transport and route only admitted actions. The node reauthorizes the exact requested resources and purpose. A user-supplied namespace, capability name, schema reference, profile digest or source URL is an input to validation, never proof. Errors redact secrets and reveal no unauthorized existence information.

## Failure design
Canonical writes fail closed; optional enrichment can be degraded only when the capability's declared policy allows it. Transport timeout does not prove no mutation. All consequential retries carry the original operation key and use the owner's receipt lookup/reconciliation surface. Per-repo details are in CAPABILITY_DETAILS.md.

## Deployment independence
Publish a separate runtime artifact and maintain a separate lockfile. The server image owns only this node's adapters. Consumer contracts/client extras must not install server database drivers. Tests prove replacement of an adapter does not change public payloads, source identities or failure semantics.

## Donor use
- l9-graphiti-memory public facade, contracts, typed errors and tests.
- Mack authenticity/scope tests.
- Emma consent/retention/isolation tests.

Donor code is not copied merely because it passes its old tests. Map behavior, inspect required invariants, reject duplicate owners, and rewrite bindings to canonical vocabulary. Preserve old identities only in explicit migration records.
