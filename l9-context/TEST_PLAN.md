# l9-context: implementation test plan

The test filenames below are **planned implementation evidence**, not tests executed in this packet. Pack-local schema/semantic-fixture checks are separate and reported in ../../VALIDATION.md.

| Planned file | Minimum proof |
| --- | --- |
| test_required_coverage.py | Positive path plus adversarial failure, identity/scope binding, explicit receipt and current-revision evidence. |
| test_authority_separation.py | Positive path plus adversarial failure, identity/scope binding, explicit receipt and current-revision evidence. |
| test_plan_identity.py | Positive path plus adversarial failure, identity/scope binding, explicit receipt and current-revision evidence. |
| test_multisource_temporal.py | Positive path plus adversarial failure, identity/scope binding, explicit receipt and current-revision evidence. |
| test_delta_binding.py | Positive path plus adversarial failure, identity/scope binding, explicit receipt and current-revision evidence. |
| test_scope_cache_keys.py | Positive path plus adversarial failure, identity/scope binding, explicit receipt and current-revision evidence. |
| test_reverse_ingest_budget.py | Positive path plus adversarial failure, identity/scope binding, explicit receipt and current-revision evidence. |
| test_partial_failure.py | Positive path plus adversarial failure, identity/scope binding, explicit receipt and current-revision evidence. |

## Mandatory cross-cutting cases
- Wrong tenant, wrong subject, wrong manifestation, stale profile and expired authorization are refused before protected I/O.
- A forged client/node role and self-issued capability grant do not change authorization.
- Same operation key plus same payload returns the recorded result; same key plus different request rejects a collision.
- Provider/transport outage remains an explicit typed failure, not empty results or successful queuing.
- Installation of contracts/client-only artifact has no runtime imports of Mongo, Graphiti or sibling services.
- All external capability invocations are visible through Gate in a signed round-trip test.
- Process kill/restart at consequential boundaries yields durable recovery or a typed reconciliation state.
- Two manifestations using the same profile cannot access one another's scoped state without a separate explicit grant.

## Evidence receipt
Record source revision, lock hash, command argv, start/end, environment class, exit code, assertion counts, skipped/blocked cases and log digests. Preserve original failures. A suite that skips a required live dependency is BLOCKED for that release gate, not PASS.
