# Proposed target file map: L9-AgentOS

All entries below are **NEW/proposed** until the node-birth baseline proves an existing path. Use the current owner-native factory. Do not copy a historical chassis from an archive. The factory repository's current node product and admission contract are a Phase 0 proof obligation.

```text
L9-AgentOS/
  ARCHITECTURE.md
  INVARIANTS.md
  AGENTS.md
  RUNBOOK.md
  engine/spec.yaml
  contracts/                  # owner-native semantic and payload contracts
  src/l9_agentos/
    domain/objectives.py
    domain/work_items.py
    domain/observations.py
    domain/decisions.py
    domain/action_intents.py
    domain/delegation.py
    profiles/compiler.py
    profiles/resolver.py
    profiles/lifecycle.py
    autonomy/evaluator.py
    application/observation_loop.py
    application/intent_loop.py
    application/resume.py
    bindings/gate_actions.py
    ports/capabilities.py
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
| src/l9_agentos/domain/objectives.py | NEW | Own only the named responsibility; no forbidden cross-node import/egress. |
| src/l9_agentos/domain/work_items.py | NEW | Own only the named responsibility; no forbidden cross-node import/egress. |
| src/l9_agentos/domain/observations.py | NEW | Own only the named responsibility; no forbidden cross-node import/egress. |
| src/l9_agentos/domain/decisions.py | NEW | Own only the named responsibility; no forbidden cross-node import/egress. |
| src/l9_agentos/domain/action_intents.py | NEW | Own only the named responsibility; no forbidden cross-node import/egress. |
| src/l9_agentos/domain/delegation.py | NEW | Own only the named responsibility; no forbidden cross-node import/egress. |
| src/l9_agentos/profiles/compiler.py | NEW | Own only the named responsibility; no forbidden cross-node import/egress. |
| src/l9_agentos/profiles/resolver.py | NEW | Own only the named responsibility; no forbidden cross-node import/egress. |
| src/l9_agentos/profiles/lifecycle.py | NEW | Own only the named responsibility; no forbidden cross-node import/egress. |
| src/l9_agentos/autonomy/evaluator.py | NEW | Own only the named responsibility; no forbidden cross-node import/egress. |
| src/l9_agentos/application/observation_loop.py | NEW | Own only the named responsibility; no forbidden cross-node import/egress. |
| src/l9_agentos/application/intent_loop.py | NEW | Own only the named responsibility; no forbidden cross-node import/egress. |
| src/l9_agentos/application/resume.py | NEW | Own only the named responsibility; no forbidden cross-node import/egress. |
| src/l9_agentos/bindings/gate_actions.py | NEW | Own only the named responsibility; no forbidden cross-node import/egress. |
| src/l9_agentos/ports/capabilities.py | NEW | Own only the named responsibility; no forbidden cross-node import/egress. |

## Change hygiene
Do not modify sibling repos from this worktree. Dependency deltas become their own units. Bind PR head, base SHA, schema digests, tested lock and validation receipts. Do not claim paths exist until the repo baseline confirms them.
