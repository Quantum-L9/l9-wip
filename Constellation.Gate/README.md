# Constellation.Gate: scoped convergence workstream

**Intended repository:** `Quantum-L9/Constellation.Gate`. This is not authorization for unrestricted repository changes. The exact current base, open PRs and path inventory must be revalidated before mutation.

## Goal
Admit and route the six node action families while enforcing distinct authenticated consumer/node roles and unique semantic ownership.

## Included changes
- Bind role/source/tenant claims to authenticated identity and reject claimed role mismatches.
- Register generic action families with one semantic owner; replicas share that owner but not arbitrary credentials.
- Reject clients as worker destinations and deny client action-owner registration.
- Keep dispatch deadline clamping and SDK-owned worker transport.
- Validate event/request binding actually supported by ingress; do not assume event type support from SDK enumeration.

## Excluded
- AgentProfile evaluation in Gate
- Database-specific payload handling
- Node-specific business workflows built into routing
- Silent peer fallback during a node outage
- Authorization based solely on graph presence or profile capability list

## Build relation
This repo retains its existing semantic ownership. It is not cloned into AgentOS. Each required delta is a separate PR unit in execution_contract.yaml. If the required seam already conforms at the current head, record a no-change proof rather than editing it to match an old plan.


## v1.1 cross-repository integration
This scope participates in the Communication/Formal Reasoning extension. Its exact added work is in `execution_contract.yaml` and `ROADMAP.md`; generic ownership remains unchanged. Refer to `../../02_architecture/COMMUNICATION_REASONING_INTEGRATION.md`. A new upstream consumer does not authorize importing another node's implementation or moving its policy into Constellation.Gate.
