# Existing cognitive-runtime integration

Source: `l9-cognitive-runtime/docs/CONTEXT_PLANNING_BRIDGE.md` at the recorded baseline. It explicitly owns cognitive demand, not acquisition. Its public surfaces include CognitiveRuntimeService.plan_context, CLI --plan-context and MCP plan_context_requirements; final compilation can require expected_context_plan_id.

## Required protocol
Obtain the owner-issued ContextPlan bound to task scope, discovery snapshot, kernel/source/manifest/pipeline/compiler identities. Validate schema and provenance. Map each demand requirement to an already admitted source capability; mapping is fulfillment data, not a duplicate authority registry. Retrieve bounded source evidence through Gate. Construct the owner-native ContextSnapshot buckets without promoting memory to governed authority. Pass the final snapshot and expected context-plan identity back to the owner compilation path.

A changed requirement, kernel digest, discovery signal or governing input produces replan_required. Additional evidence that does not alter demand need not invalidate the plan. The context layer cannot suppress this check to reuse a stale result.

## Packaging and deployment
If the cognitive owner is consumed as a dependency package inside an admitted node, use its public contracts and facade only. If remote, the existing admitted capability wrapper is the transport target through Gate. This pack does not assume that an MCP endpoint is already a registered L9 node. Resolve the wrapper/registration at baseline; do not add a direct HTTP shortcut or a new standalone node casually.

## L9-Ops-MCP example
Ops is one possible authored artifact/authority source. Its profile/source-specific registry may supply exact artifacts and immutable references. Context does not import Ops' direct Graphiti hydrator or memory admission code. The source must remain replaceable by other repositories and domain capability sources.
