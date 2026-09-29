# Gate_SDK: observed/candidate seams

| Path | Disposition |
| --- | --- |
| src/constellation_node_sdk/gate/client.py | INSPECT current base, then MODIFY only where the scoped contract requires it. |
| src/constellation_node_sdk/gate/config.py | INSPECT current base, then MODIFY only where the scoped contract requires it. |
| src/constellation_node_sdk/transport/provenance.py | INSPECT current base, then MODIFY only where the scoped contract requires it. |
| src/constellation_node_sdk/security/validation.py | INSPECT current base, then MODIFY only where the scoped contract requires it. |
| src/constellation_node_sdk/runtime/ | INSPECT current base, then MODIFY only where the scoped contract requires it. |
| contracts/ROUTING_POLICY_SPEC.md | INSPECT current base, then MODIFY only where the scoped contract requires it. |
| tests/gate/test_application_execute.py | INSPECT current base, then MODIFY only where the scoped contract requires it. |
| tests/gate/test_error_taxonomy.py | INSPECT current base, then MODIFY only where the scoped contract requires it. |
| tests/packaging/test_installed_package.py | INSPECT current base, then MODIFY only where the scoped contract requires it. |

These paths are an evidence map, not proof they all exist unchanged at execution time. Current source inspection is mandatory. Preserve the owner's tests and do not hand-edit generated artifacts where a generator owns them.
