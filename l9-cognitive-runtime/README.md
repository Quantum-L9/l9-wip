# l9-cognitive-runtime: scoped convergence workstream

**Intended repository:** `Quantum-L9/l9-cognitive-runtime`. This is not authorization for unrestricted repository changes. The exact current base, open PRs and path inventory must be revalidated before mutation.

## Goal
Provide owner-native demand/compilation seams to Context without growing acquisition, provider or agent identity responsibilities.

## Included changes
- Freeze/test ContextPlan and ContextSnapshot semantics needed by generic fulfillment.
- Preserve expected_context_plan_id recomputation at final compile.
- Add small published contracts/package parity only where the wrapper genuinely needs it.
- Document that actual source fetching is outside the cognitive compiler.

## Excluded
- Git/Graphiti/State/Mongo clients inside the compiler
- A second kernel registry or copied semantic compiler in Context
- Source acquisition inferred from repository presence
- Memory promoted into authority facts

## Build relation
This repo retains its existing semantic ownership. It is not cloned into AgentOS. Each required delta is a separate PR unit in execution_contract.yaml. If the required seam already conforms at the current head, record a no-change proof rather than editing it to match an old plan.


## v1.1 cross-repository integration
This scope participates in the Communication/Formal Reasoning extension. Its exact added work is in `execution_contract.yaml` and `ROADMAP.md`; generic ownership remains unchanged. Refer to `../../02_architecture/COMMUNICATION_REASONING_INTEGRATION.md`. A new upstream consumer does not authorize importing another node's implementation or moving its policy into l9-cognitive-runtime.
