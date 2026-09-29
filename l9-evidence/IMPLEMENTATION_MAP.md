# Proposed target file map: l9-evidence

All entries below are **NEW/proposed** until the node-birth baseline proves an existing path. Use the current owner-native factory. Do not copy a historical chassis from an archive. The factory repository's current node product and admission contract are a Phase 0 proof obligation.

```text
l9-evidence/
  ARCHITECTURE.md
  INVARIANTS.md
  AGENTS.md
  RUNBOOK.md
  engine/spec.yaml
  contracts/                  # owner-native semantic and payload contracts
  src/l9_evidence/
    domain/evidence.py
    domain/source_refs.py
    domain/projections.py
    domain/deletion.py
    services/evidence_service.py
    services/projection_service.py
    services/search_service.py
    services/deletion_service.py
    ports/storage.py
    adapters/mongodb/metadata.py
    adapters/mongodb/search.py
    adapters/object_storage/artifacts.py
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
| src/l9_evidence/domain/evidence.py | NEW | Own only the named responsibility; no forbidden cross-node import/egress. |
| src/l9_evidence/domain/source_refs.py | NEW | Own only the named responsibility; no forbidden cross-node import/egress. |
| src/l9_evidence/domain/projections.py | NEW | Own only the named responsibility; no forbidden cross-node import/egress. |
| src/l9_evidence/domain/deletion.py | NEW | Own only the named responsibility; no forbidden cross-node import/egress. |
| src/l9_evidence/services/evidence_service.py | NEW | Own only the named responsibility; no forbidden cross-node import/egress. |
| src/l9_evidence/services/projection_service.py | NEW | Own only the named responsibility; no forbidden cross-node import/egress. |
| src/l9_evidence/services/search_service.py | NEW | Own only the named responsibility; no forbidden cross-node import/egress. |
| src/l9_evidence/services/deletion_service.py | NEW | Own only the named responsibility; no forbidden cross-node import/egress. |
| src/l9_evidence/ports/storage.py | NEW | Own only the named responsibility; no forbidden cross-node import/egress. |
| src/l9_evidence/adapters/mongodb/metadata.py | NEW | Own only the named responsibility; no forbidden cross-node import/egress. |
| src/l9_evidence/adapters/mongodb/search.py | NEW | Own only the named responsibility; no forbidden cross-node import/egress. |
| src/l9_evidence/adapters/object_storage/artifacts.py | NEW | Own only the named responsibility; no forbidden cross-node import/egress. |
| src/l9_evidence/bindings/gate_actions.py | NEW | Own only the named responsibility; no forbidden cross-node import/egress. |

## Change hygiene
Do not modify sibling repos from this worktree. Dependency deltas become their own units. Bind PR head, base SHA, schema digests, tested lock and validation receipts. Do not claim paths exist until the repo baseline confirms them.
