# Evidence retrieval representations

## Initial scope
Start with one source corpus and one evaluated embedding view. Exact lookup and structured scope filters work without embeddings. Add lexical/vector fusion and optional reranking only after a gold retrieval set demonstrates value. Additional code or domain-specific views require measured failure evidence, not aesthetic taxonomy expansion.

## Identity
Source identity answers which immutable source was used. Representation identity answers what normalized view/chunk was derived and by which transform. Embedding-space identity answers model/version, dimension, normalization, distance and view. Index binding answers which admitted projection version is currently queried. These are separate identities; swapping one cannot silently reuse another's cache.

Ingest can produce embeddings through a bounded adapter as part of a declared representation pipeline, but only Evidence's destination action writes them into its index. Alternatively Evidence can own an embedding worker for its own representations. Choose one executor per view in its manifest; never generate the same view in both services. Memory's Graphiti embeddings remain completely separate under Memory's owner.

## Public schema
References expose provider-neutral `view_ref`, `space_ref`, `source_ref`, `representation_digest` and `transform_ref`. Dimensions/metric live in an admitted space contract, not in arbitrary consumer search arguments. Large vector arrays are transferred as bounded artifact references or controlled internal payloads, never added to every context bundle.

## Cache and privacy
Cache identity includes representation text hash, transform contract, embedding model/revision and scope/classification boundary. Identical text from two private subjects is not a permission to share a cache entry with visible metadata. Deletion invalidates affected caches and aliases. Re-embedding unchanged content under an unchanged contract is avoided; model/view changes create new versioned projections.

## Tool boundary
Atlas Vector Search is a first-adapter option, not the domain contract. Native Atlas reranking is still Preview at the checked date and is not required for production. LlamaIndex integration may rerank optional results behind a bounded adapter; it cannot reorder mandatory authority facts out of a context bundle.
