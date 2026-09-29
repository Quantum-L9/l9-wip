# Context fulfillment contract

## Demand and fulfillment
ContextNeed comes from the shared agent semantic contract. ContextProfile specifies required/optional evidence, source classes, coverage, freshness, source precedence and budgets. The node resolves source capabilities and compiles a provider-neutral fulfillment plan. It never exposes database queries, Graphiti calls or provider endpoints to the agent.

Existing cognitive-runtime owns its cognitive ContextPlan. When bound, Context fulfills that exact demand and emits a ContextSnapshot-compatible result; the cognitive owner recomputes and checks expected_context_plan_id before final compilation. Do not copy its KernelResolver or execution-contract compiler. A generic ContextNeed not using that compiler can still use the same fulfillment operations.

## Exact versus semantic
Exact state/authority requests use source-owner exact retrieval. Semantic Evidence search and Memory retrieval are separate optional/required sources according to the profile. Reranking affects relevance only inside the eligible evidence set. It cannot invent source authority, omit required coverage or make expired evidence valid.

## Coverage
Requirements can use minimum count, all-eligible within a bounded exact scope, or required semantic keys. Each requirement declares source scope, minimal authority/freshness, byte/item budget and missing-data policy. Truncation that removes a required key fails coverage. A complete empty result is different from unavailable, refused, stale or not evaluated.

## Bundle
ContextBundle binds Work Item/profile/need/plan identity, scope, issued/expiry coordinates, item provenance, authority labels, required-coverage result, conflicts, omissions, retrieval receipts and content digest. It records source-specific state versions. It is not a globally atomic snapshot, universal truth or authorization token. Evidence text is treated as untrusted input, not executable instructions.

## Delta
ContextDelta names exact base_bundle_id and digest, adds/removes/changes items, updates source coordinates and records invalidation/reason. A receiver applies it only to that base and matching scope/profile/requirement plan. Otherwise recompile. Deltas can remove previously available facts after revocation or deletion; retaining a prior prompt does not preserve permission to reuse it.

## Reverse ingestion
An unindexed allowed source may produce an IngestNeed. Context can submit it only under an existing grant/profile bound and within the operation budget. It receives acceptance, not proof of immediate indexing. End the attempt or return incomplete/pending according to policy, then refresh when a new source result arrives. Never recursively wait on itself or emit infinite unchanged sync requests.

## Operations
the owner-native context-demand planning step, `context.compile`, `context.refresh` and `context.explain` use generic payloads. `context.explain` exposes selected sources, exclusions, budgets and evidence labels, not private chain-of-thought. No endpoint grants a capability, changes canonical memory or claims source-owner records were created.
