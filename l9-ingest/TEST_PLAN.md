# l9-ingest: implementation test plan

The test filenames below are **planned implementation evidence**, not tests executed in this packet. Pack-local schema/semantic-fixture checks are separate and reported in ../../VALIDATION.md.

| Planned file | Minimum proof |
| --- | --- |
| test_source_integrity.py | Positive path plus adversarial failure, identity/scope binding, explicit receipt and current-revision evidence. |
| test_profile_eligibility.py | Positive path plus adversarial failure, identity/scope binding, explicit receipt and current-revision evidence. |
| test_transform_idempotency.py | Positive path plus adversarial failure, identity/scope binding, explicit receipt and current-revision evidence. |
| test_delivery_partial.py | Positive path plus adversarial failure, identity/scope binding, explicit receipt and current-revision evidence. |
| test_no_direct_destination_store.py | Positive path plus adversarial failure, identity/scope binding, explicit receipt and current-revision evidence. |
| test_replay_revocation.py | Positive path plus adversarial failure, identity/scope binding, explicit receipt and current-revision evidence. |
| test_projection_view_identity.py | Positive path plus adversarial failure, identity/scope binding, explicit receipt and current-revision evidence. |
| test_untrusted_source_handling.py | Positive path plus adversarial failure, identity/scope binding, explicit receipt and current-revision evidence. |

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
