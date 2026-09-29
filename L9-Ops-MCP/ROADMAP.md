# Repository roadmap

Planned implementation only. PRs remain scoped to this repository; dependencies are evidence gates, not permission to edit another owner.

## OPS-01 - Reconcile source authority and generic machinery donor boundaries

Prerequisites: BASE-01, COG-01

1. Read source resolver/registry and distinguish owner-native authority from generic context/memory.
2. Keep Ops as optional source, not global context authority.
3. Map provider-specific local memory/client/transport code for retirement.
4. Freeze source revision references before any export.

**Acceptance:** Context can operate without Ops as mandatory dependency. No inferred graph content becomes normative source.

**Required negatives:** Missing source hash blocks authority projection. Ops transport-shaped dict cannot bypass SDK canonical envelope.

## OPS-02 - Cut over to shared owner APIs and retire duplicates

Prerequisites: OPS-01, CTX-02, MEM-02

1. Replace generic hydration/admission with owner capability calls.
2. Retain only proved source-specific deterministic authority behavior.
3. Remove direct Graphiti calls and alternate wire construction once replacement tests pass.
4. Run existing source resolver and packaging tests unchanged in intent.

**Acceptance:** No Ops-specific universal Context or memory authority remains. Exact source retrieval works over approved binding.

**Required negatives:** Graphiti credential absent from Ops consumer runtime. Source-specific rule cannot widen profile/node permissions.
