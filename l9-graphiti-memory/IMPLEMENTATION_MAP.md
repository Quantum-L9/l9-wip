# l9-graphiti-memory: observed/candidate seams

| Path | Disposition |
| --- | --- |
| src/l9_graphite_memory/sdk.py | INSPECT current base, then MODIFY only where the scoped contract requires it. |
| src/l9_graphite_memory/services/memory_service.py | INSPECT current base, then MODIFY only where the scoped contract requires it. |
| src/l9_graphite_memory/services/generated_data.py | INSPECT current base, then MODIFY only where the scoped contract requires it. |
| src/l9_graphite_memory/contracts/ | INSPECT current base, then MODIFY only where the scoped contract requires it. |
| src/l9_graphite_memory/retrieval/ | INSPECT current base, then MODIFY only where the scoped contract requires it. |
| src/l9_graphite_memory/projections/ | INSPECT current base, then MODIFY only where the scoped contract requires it. |
| src/l9_graphite_memory/integrations/constellation.py | INSPECT current base, then MODIFY only where the scoped contract requires it. |
| tests/unit/test_control_plane_transport_parity.py | INSPECT current base, then MODIFY only where the scoped contract requires it. |

These paths are an evidence map, not proof they all exist unchanged at execution time. Current source inspection is mandatory. Preserve the owner's tests and do not hand-edit generated artifacts where a generator owns them.
