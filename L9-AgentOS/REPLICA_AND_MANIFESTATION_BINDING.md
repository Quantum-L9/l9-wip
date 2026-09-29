# One action owner, many isolated manifestations

The canonical `agent.work.*` actions have one semantic owner: AgentOS. A manifestation ID is an authorized resource selector in the payload, not a new action name, node URL or trusted role. Gate owns dispatch and AgentOS verifies that the addressed manifestation is admitted in its deployment and that the caller has the requested access.

## First-attempt deployment
Use one admitted AgentOS service pool whose replicas can serve the same set of admitted manifestation bindings. Each request resolves an immutable profile release and a separately issued scoped execution identity. No replica relies on local session state for ownership: State's conditional revisions and fencing determine the active writer. The pool is one semantic owner but not one global unrestricted agent credential.

A node service principal and a delegated manifestation/subject principal are distinct. Downstream calls preserve the bounded delegation, tenant, purpose, scope and grant expiry. A trusted AgentOS node identity cannot replace that delegated authority with a wildcard memory or state principal. Keep per-request/worker isolation and never cache mutable credentials in profile artifacts.

## Registration conformance
Every replica registered behind a generic action must be able to serve the action's admitted resource scope, or Gate must have an explicit authenticated affinity/partition contract. The initial shared pool avoids requiring a new per-agent router. Do not register isolated single-manifestation workers into an undifferentiated load-balanced action pool and assume requests will land on the correct one.

If later deployment requires isolated tenant/manifestation pools, add a narrowly scoped Gate-owned placement/affinity contract and conformance proof before registering them. It must not use agent-name branches, consumer-selected destinations, per-profile action aliases or a client-maintained topology map. That deployment extension is not silently implied by the initial action registry.

Test two replicas racing one Work Item, two manifestations sharing one profile, different profiles on one pool and attempted cross-manifestation access. A restart preserves the admitted manifestation identity while rotating replica identity. Profile activation/rebinding is a controlled operation independent of node registration.
