# Proposed target file map: l9-state

All entries below are **NEW/proposed** until the node-birth baseline proves an existing path. Use the current owner-native factory. Do not copy a historical chassis from an archive. The factory repository's current node product and admission contract are a Phase 0 proof obligation.

```text
l9-state/
  ARCHITECTURE.md
  INVARIANTS.md
  AGENTS.md
  RUNBOOK.md
  engine/spec.yaml
  contracts/                  # owner-native semantic and payload contracts
  src/l9_state/
    domain/records.py
    domain/operations.py
    domain/claims.py
    domain/events.py
    services/state_service.py
    services/checkpoint_service.py
    services/transition_delivery.py
    ports/store.py
    adapters/mongodb/store.py
    adapters/mongodb/transactions.py
    adapters/mongodb/indexes.py
    adapters/mongodb/change_wakeup.py
    bindings/gate_actions.py
  tests/unit/
  tests/contracts/
  tests/integration/
  tests/architecture/
  pyproject.toml
  uv.lock
  .github/workflows/          # organization-owned callers, not copied CI semantics
```

## File responsibilities and constraints
| Surface | Change | Acceptance |
| --- | --- | --- |
| src/l9_state/domain/records.py | NEW | Own only the named responsibility; no forbidden cross-node import/egress. |
| src/l9_state/domain/operations.py | NEW | Own only the named responsibility; no forbidden cross-node import/egress. |
| src/l9_state/domain/claims.py | NEW | Own only the named responsibility; no forbidden cross-node import/egress. |
| src/l9_state/domain/events.py | NEW | Own only the named responsibility; no forbidden cross-node import/egress. |
| src/l9_state/services/state_service.py | NEW | Own only the named responsibility; no forbidden cross-node import/egress. |
| src/l9_state/services/checkpoint_service.py | NEW | Own only the named responsibility; no forbidden cross-node import/egress. |
| src/l9_state/services/transition_delivery.py | NEW | Own only the named responsibility; no forbidden cross-node import/egress. |
| src/l9_state/ports/store.py | NEW | Own only the named responsibility; no forbidden cross-node import/egress. |
| src/l9_state/adapters/mongodb/store.py | NEW | Own only the named responsibility; no forbidden cross-node import/egress. |
| src/l9_state/adapters/mongodb/transactions.py | NEW | Own only the named responsibility; no forbidden cross-node import/egress. |
| src/l9_state/adapters/mongodb/indexes.py | NEW | Own only the named responsibility; no forbidden cross-node import/egress. |
| src/l9_state/adapters/mongodb/change_wakeup.py | NEW | Own only the named responsibility; no forbidden cross-node import/egress. |
| src/l9_state/bindings/gate_actions.py | NEW | Own only the named responsibility; no forbidden cross-node import/egress. |

## Change hygiene
Do not modify sibling repos from this worktree. Dependency deltas become their own units. Bind PR head, base SHA, schema digests, tested lock and validation receipts. Do not claim paths exist until the repo baseline confirms them.
