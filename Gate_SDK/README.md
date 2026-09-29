# Gate_SDK: scoped convergence workstream

**Intended repository:** `Quantum-L9/Gate_SDK`. This is not authorization for unrestricted repository changes. The exact current base, open PRs and path inventory must be revalidated before mutation.

## Goal
Represent consumer and admitted-node invocation distinctly while preserving one canonical transport and opaque capability payloads.

## Included changes
- Keep GateClient.execute as the single application entry point; no mandatory node registration for clients.
- Represent authenticated client versus node role without caller-controlled elevation; coordinate server binding with Gate.
- Preserve one deadline, one send attempt, canonical response validation, correlation and lineage.
- Offer optional owner-published typed capability clients over execute, not domain models in SDK production code.
- Expose a safe node follow-up binding preserving parent lineage; do not use application root calls to erase ancestry.

## Excluded
- Second packet envelope or second HTTP stack
- AgentProfile parser, State/Memory/Context domain models in SDK core
- Peer URL APIs
- Automatic retry of domain effects
- Trust based only on a declared origin_kind

## Build relation
This repo retains its existing semantic ownership. It is not cloned into AgentOS. Each required delta is a separate PR unit in execution_contract.yaml. If the required seam already conforms at the current head, record a no-change proof rather than editing it to match an old plan.


## v1.1 cross-repository integration
This scope participates in the Communication/Formal Reasoning extension. Its exact added work is in `execution_contract.yaml` and `ROADMAP.md`; generic ownership remains unchanged. Refer to `../../02_architecture/COMMUNICATION_REASONING_INTEGRATION.md`. A new upstream consumer does not authorize importing another node's implementation or moving its policy into Gate_SDK.
