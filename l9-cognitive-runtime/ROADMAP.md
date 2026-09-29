# Repository roadmap

Planned implementation only. PRs remain scoped to this repository; dependencies are evidence gates, not permission to edit another owner.

## COG-01 - Bind existing demand/compile contracts without acquisition

Prerequisites: BASE-01, AG-01

1. Inspect ContextPlan, ContextSnapshot and final compile interfaces.
2. Bind exact required/optional coverage and compiler identity.
3. Keep all source acquisition out of this repo.
4. Publish deterministic demand changes and stale-plan rejection tests.

**Acceptance:** Context fulfills existing demand instead of copying planner. Compiler identity and source digests survive installed artifact packaging.

**Required negatives:** Changed requirement forces replan. Adding irrelevant facts does not spuriously change semantic demand.
