# Repository roadmap

Planned implementation only. PRs remain scoped to this repository; dependencies are evidence gates, not permission to edit another owner.

## GATE-01 - Bind trusted roles and generic action ownership

Prerequisites: SDK-01, AG-01

1. Bind role and source identity to authenticated principal.
2. Register proposed action namespaces only after owner contract publication.
3. Enforce semantic owner collisions for all new actions and replicas.
4. Retain SDK dispatch transport and existing deadline clamping.

**Acceptance:** Client may invoke only allowed actions but cannot register/receive node dispatch. All six node families resolve by action, never client-supplied destination.

**Required negatives:** Owner collision rejects registration. Registered-looking client principal cannot become worker.

## GATE-02 - Validate async receipts, event re-entry and degraded routing

Prerequisites: GATE-01, SDK-02

1. Inspect which packet types ingress actually admits; define bounded State event relay using supported owner APIs.
2. Separate durable accepted-work receipts from completed-operation receipts.
3. Exercise no healthy owner, unknown action, expiry and cancellation without peer fallback.
4. Prove node-to-Gate-to-node scopes and parent causation.

**Acceptance:** Async acceptance cannot be interpreted as external execution completion. No capability work is dispatched to a consumer address.

**Required negatives:** Owner outage returns typed unavailable without direct-peer bypass. Long-running continuation cannot reset spent budget or impersonate a new objective.

## GATE-03 - Admit communication, formal and exact-context action owners

Prerequisites: GATE-02, COMM-01, FR-01, CTX-04, SDK-03

1. Register approved owner contracts without publishing roadmap adapters.
2. Verify authenticated consumer/node classes and observation delivery targets.
3. Check deadlines, payload bounds and health for added action families.
4. Prove callback input cannot impersonate a trusted node.

**Acceptance:** One semantic owner per action; replicas share that owner only. Inter-node events/requests cannot target ordinary consumers.

**Required negatives:** Client self-registration and declared role spoof are refused. Partial dependency outage does not create direct peer routing.
