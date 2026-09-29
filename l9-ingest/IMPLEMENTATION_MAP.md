# Proposed target file map: l9-ingest

All entries below are **NEW/proposed** until the node-birth baseline proves an existing path. Use the current owner-native factory. Do not copy a historical chassis from an archive. The factory repository's current node product and admission contract are a Phase 0 proof obligation.

```text
l9-ingest/
  ARCHITECTURE.md
  INVARIANTS.md
  AGENTS.md
  RUNBOOK.md
  engine/spec.yaml
  contracts/                  # owner-native semantic and payload contracts
  src/l9_ingest/
    domain/sources.py
    domain/jobs.py
    domain/candidates.py
    domain/receipts.py
    profiles/ingestion.py
    pipeline/runner.py
    pipeline/stages.py
    pipeline/delivery.py
    pipeline/reconcile.py
    adapters/llamaindex/transforms.py
    adapters/parsers/markdown.py
    adapters/parsers/structured.py
    adapters/parsers/code.py
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
| src/l9_ingest/domain/sources.py | NEW | Own only the named responsibility; no forbidden cross-node import/egress. |
| src/l9_ingest/domain/jobs.py | NEW | Own only the named responsibility; no forbidden cross-node import/egress. |
| src/l9_ingest/domain/candidates.py | NEW | Own only the named responsibility; no forbidden cross-node import/egress. |
| src/l9_ingest/domain/receipts.py | NEW | Own only the named responsibility; no forbidden cross-node import/egress. |
| src/l9_ingest/profiles/ingestion.py | NEW | Own only the named responsibility; no forbidden cross-node import/egress. |
| src/l9_ingest/pipeline/runner.py | NEW | Own only the named responsibility; no forbidden cross-node import/egress. |
| src/l9_ingest/pipeline/stages.py | NEW | Own only the named responsibility; no forbidden cross-node import/egress. |
| src/l9_ingest/pipeline/delivery.py | NEW | Own only the named responsibility; no forbidden cross-node import/egress. |
| src/l9_ingest/pipeline/reconcile.py | NEW | Own only the named responsibility; no forbidden cross-node import/egress. |
| src/l9_ingest/adapters/llamaindex/transforms.py | NEW | Own only the named responsibility; no forbidden cross-node import/egress. |
| src/l9_ingest/adapters/parsers/markdown.py | NEW | Own only the named responsibility; no forbidden cross-node import/egress. |
| src/l9_ingest/adapters/parsers/structured.py | NEW | Own only the named responsibility; no forbidden cross-node import/egress. |
| src/l9_ingest/adapters/parsers/code.py | NEW | Own only the named responsibility; no forbidden cross-node import/egress. |
| src/l9_ingest/bindings/gate_actions.py | NEW | Own only the named responsibility; no forbidden cross-node import/egress. |

## Change hygiene
Do not modify sibling repos from this worktree. Dependency deltas become their own units. Bind PR head, base SHA, schema digests, tested lock and validation receipts. Do not claim paths exist until the repo baseline confirms them.
