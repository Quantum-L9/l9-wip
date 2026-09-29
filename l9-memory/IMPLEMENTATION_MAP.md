# Proposed target file map: l9-memory

All entries below are **NEW/proposed** until the node-birth baseline proves an existing path. Use the current owner-native factory. Do not copy a historical chassis from an archive. The factory repository's current node product and admission contract are a Phase 0 proof obligation.

```text
l9-memory/
  ARCHITECTURE.md
  INVARIANTS.md
  AGENTS.md
  RUNBOOK.md
  engine/spec.yaml
  contracts/                  # owner-native semantic and payload contracts
  src/l9_memory_node/
    bindings/actions.py
    bindings/principals.py
    bindings/receipts.py
    application/composition.py
    application/readiness.py
    configuration/settings.py
    contracts/capability_map.py
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
| src/l9_memory_node/bindings/actions.py | NEW | Own only the named responsibility; no forbidden cross-node import/egress. |
| src/l9_memory_node/bindings/principals.py | NEW | Own only the named responsibility; no forbidden cross-node import/egress. |
| src/l9_memory_node/bindings/receipts.py | NEW | Own only the named responsibility; no forbidden cross-node import/egress. |
| src/l9_memory_node/application/composition.py | NEW | Own only the named responsibility; no forbidden cross-node import/egress. |
| src/l9_memory_node/application/readiness.py | NEW | Own only the named responsibility; no forbidden cross-node import/egress. |
| src/l9_memory_node/configuration/settings.py | NEW | Own only the named responsibility; no forbidden cross-node import/egress. |
| src/l9_memory_node/contracts/capability_map.py | NEW | Own only the named responsibility; no forbidden cross-node import/egress. |

## Change hygiene
Do not modify sibling repos from this worktree. Dependency deltas become their own units. Bind PR head, base SHA, schema digests, tested lock and validation receipts. Do not claim paths exist until the repo baseline confirms them.
