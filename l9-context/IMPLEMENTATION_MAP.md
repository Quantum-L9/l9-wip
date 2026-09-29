# Proposed target file map: l9-context

All entries below are **NEW/proposed** until the node-birth baseline proves an existing path. Use the current owner-native factory. Do not copy a historical chassis from an archive. The factory repository's current node product and admission contract are a Phase 0 proof obligation.

```text
l9-context/
  ARCHITECTURE.md
  INVARIANTS.md
  AGENTS.md
  RUNBOOK.md
  engine/spec.yaml
  contracts/                  # owner-native semantic and payload contracts
  src/l9_context/
    domain/needs.py
    domain/plans.py
    domain/bundles.py
    domain/deltas.py
    profiles/requirements.py
    planning/fulfillment.py
    planning/budget.py
    services/compile.py
    services/refresh.py
    services/explain.py
    adapters/cognitive_runtime/demand_binding.py
    adapters/llamaindex/reranker.py
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
| src/l9_context/domain/needs.py | NEW | Own only the named responsibility; no forbidden cross-node import/egress. |
| src/l9_context/domain/plans.py | NEW | Own only the named responsibility; no forbidden cross-node import/egress. |
| src/l9_context/domain/bundles.py | NEW | Own only the named responsibility; no forbidden cross-node import/egress. |
| src/l9_context/domain/deltas.py | NEW | Own only the named responsibility; no forbidden cross-node import/egress. |
| src/l9_context/profiles/requirements.py | NEW | Own only the named responsibility; no forbidden cross-node import/egress. |
| src/l9_context/planning/fulfillment.py | NEW | Own only the named responsibility; no forbidden cross-node import/egress. |
| src/l9_context/planning/budget.py | NEW | Own only the named responsibility; no forbidden cross-node import/egress. |
| src/l9_context/services/compile.py | NEW | Own only the named responsibility; no forbidden cross-node import/egress. |
| src/l9_context/services/refresh.py | NEW | Own only the named responsibility; no forbidden cross-node import/egress. |
| src/l9_context/services/explain.py | NEW | Own only the named responsibility; no forbidden cross-node import/egress. |
| src/l9_context/adapters/cognitive_runtime/demand_binding.py | NEW | Own only the named responsibility; no forbidden cross-node import/egress. |
| src/l9_context/adapters/llamaindex/reranker.py | NEW | Own only the named responsibility; no forbidden cross-node import/egress. |
| src/l9_context/bindings/gate_actions.py | NEW | Own only the named responsibility; no forbidden cross-node import/egress. |

## Change hygiene
Do not modify sibling repos from this worktree. Dependency deltas become their own units. Bind PR head, base SHA, schema digests, tested lock and validation receipts. Do not claim paths exist until the repo baseline confirms them.
