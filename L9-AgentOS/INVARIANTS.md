# L9-AgentOS invariant enforcement

Local machine-readable owner: `invariants.yaml`. Global index points here and does not replace this owner. Imported routing/security invariants keep their original owners.

| ID | Invariant | Required negative proof |
| --- | --- | --- |
| L9-001 | One runtime manifests agents only through a resolved AgentProfile; no agent-name branches in shared core. | Add a sixth synthetic profile without changing runtime source. |
| L9-002 | Work Item is the canonical unit of agent work across schemas, APIs, examples and documentation. | Canonical schemas contain no legacy work primitive; migration records may quote source names. |
| L9-003 | AgentProfile is a compiled, versioned, provenance-bound declarative aggregate, not one config file. | Compile multi-file inputs deterministically; reject missing refs, cycles and policy conflicts. |
| L9-015 | Autonomy permits a bounded attempt only; Gate and destination recheck authorization at execution. | Expired approval between evaluation and invocation yields zero external effect. |
| L9-016 | Unknown external outcome requires reconciliation, not blind retry or a new idempotency key. | Crash after provider execution and before receipt does not duplicate the effect. |
| L9-017 | Domain logic is declarative profile content or owned domain capability behavior, not generic node code. | Profile loading rejects executable code, dynamic imports and provider credentials. |
| L9-020 | Scope is server-derived and binding-preserving across delegations; sharing is explicit and revocable. | Sibling manifestations cannot read each other by matching a profile name or user label. |
| L9-021 | Profile identity, manifestation identity, replica identity and security principal are distinct. | Restart preserves manifestation state without changing producer identity; replica has no extra authority. |
| L9-024 | Persist compact decision outputs and source references, not private chain-of-thought as mandatory evidence. | Evidence schema has no required private reasoning trace. |
| L9-027 | One repository does not mean one privileged process or one globally writable agent. | Concurrent manifestations enforce separate principals, budgets, capabilities and state scopes. |
| L9-030 | Implementation may not weaken locked architecture to make a proof green. | Evidence gap creates a blocking receipt and narrowly scoped upstream work, never a local fallback brain. |

## Always preserve
One canonical transport; Gate-only inter-node requests; authenticated scope; no provider leakage; no claim of persistence, projection or execution without an owner receipt. Profile data is untrusted until compiled and admitted, and its authorization requests never outrank runtime grants.

## CI enforcement
Add architecture import/egress guards, payload schema tests, failed-path tests and explicit owner references. Test adapters use the same conformance surface as production. A test that only checks doc strings or fixture counts is not proof of runtime enforcement.
