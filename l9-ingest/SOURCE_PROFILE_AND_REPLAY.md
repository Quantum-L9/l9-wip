# Ingestion profiles, source coordinates and replay

## Declarative source profile
A profile names accepted media/source kinds, authorized use purposes, size/depth limits, normalization, redaction, parser, chunk/view contract, extraction policy, eligible destinations, retry bounds and output requirements. It contains no database collection, provider credentials or peer endpoint. Optional transforms are explicit and cannot silently become mandatory just because a plugin is installed.

## Source coordinates
Git: repository identity, immutable commit, blob, path and content digest. Documents: artifact digest plus page/section/table/cell/byte locator when available. Audio/video: artifact digest plus time range and extraction model identity. Structured events: issuer occurrence ID, schema version and immutable event digest. Source coordinates are not fabricated from another locator form; a PDF page number is not a source line number.

## Representation
Structure-aware Markdown sections, structured-record units and code-symbol chunks can share one generic representation contract. Tree-sitter is a parsing adapter for code artifacts only. It does not determine whether Git bytes changed, grant source authority or replace content hashing. Human-meaningful metadata can enter embedding input; opaque tokens, approval states, credentials and dynamic operational fields must not be embedded as permission evidence.

## LlamaIndex adapter
Use bounded transformation APIs and return output units. Do not configure a vector-store sink that writes directly into Evidence's Mongo database. Where embedding generation is assigned to this pipeline, emit a representation artifact and Gate-routed destination request. Preserve transformation caching under explicit scope/model/view identities. Do not expose LlamaIndex nodes or index handles in public payloads.

## Replay modes
Inspection compares stored source/transform/delivery identities without writes. Safe replay reconstructs representations and unsettled destination delivery only. Rebuild targets derived projections and is blocked by current deletion/consent status. Reconciliation of an unknown destination write queries its operation receipt before attempting a retry. No replay mode reproduces a business effect or circumvents a quarantined candidate.
