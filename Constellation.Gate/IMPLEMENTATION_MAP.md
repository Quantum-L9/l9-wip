# Constellation.Gate: observed/candidate seams

| Path | Disposition |
| --- | --- |
| constellation-gate/src/constellation_gate/boundary/ingress_validator.py | INSPECT current base, then MODIFY only where the scoped contract requires it. |
| constellation-gate/src/constellation_gate/boundary/routing_policy.py | INSPECT current base, then MODIFY only where the scoped contract requires it. |
| constellation-gate/src/constellation_gate/routing/action_ownership.py | INSPECT current base, then MODIFY only where the scoped contract requires it. |
| constellation-gate/src/constellation_gate/routing/node_registry.py | INSPECT current base, then MODIFY only where the scoped contract requires it. |
| constellation-gate/src/constellation_gate/routing/dispatch.py | INSPECT current base, then MODIFY only where the scoped contract requires it. |
| constellation-gate/src/constellation_gate/orchestration/workflow_engine.py | INSPECT current base, then MODIFY only where the scoped contract requires it. |
| constellation-gate/src/constellation_gate/runtime/ | INSPECT current base, then MODIFY only where the scoped contract requires it. |

These paths are an evidence map, not proof they all exist unchanged at execution time. Current source inspection is mandatory. Preserve the owner's tests and do not hand-edit generated artifacts where a generator owns them.
