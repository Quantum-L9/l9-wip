# l9-evidence dependencies

| Dependency | Binding rule |
| --- | --- |
| Gate_SDK: node chassis and transport | Owner-native contract; immutable release/ref before implementation integration. |
| MongoDB metadata/projection adapter, first stack | Owner-native contract; immutable release/ref before implementation integration. |
| Owner-controlled object storage for large binary/text artifacts | Owner-native contract; immutable release/ref before implementation integration. |
| Optional Atlas vector/search adapter with deployment-specific capability probe | Owner-native contract; immutable release/ref before implementation integration. |

## Packaging
Publish contract/schema resources from this repository's owner-controlled distribution. An optional thin typed client may call `GateClient.execute` but may not create a second transport, route map, authentication logic or retry policy. Gate_SDK transports opaque domain payloads and must not import this node's domain models. Public contracts must not leak provider credentials, database IDs, framework objects or private store handles.

## Compatibility
Observed source SHAs are not automatically release pins. Record the installed version/commit, schema version, package hash and compatibility probe in the baseline receipt. Avoid wide untested ranges. A contracts-only dependency may be shared; runnable node implementations are not imported by peer nodes.
