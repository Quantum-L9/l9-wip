# External effects and reconciliation

## Commit boundary
Before an external send/origination, persist operation identity, exact authorized request digest, current scope, target/content commitment, admission and prepared attempt using State's conditional write. An Evidence copy is supporting evidence, not a second operation-status writer. Network I/O occurs only after the prepared operation is durable.

A crash after provider acceptance but before settlement creates uncertainty. The authoritative recovery sequence is: inspect the State operation, query provider status/dedupe receipt with the same identity where supported, preserve correlation, and settle conditionally. If the provider cannot prove execution or non-execution, return `outcome_unknown` and require reconciliation. Never label a transport error as definitive no-effect.

## Idempotency
The logical operation identity is explicit and stable. Same key plus same semantic request returns the original result; same key plus different content or recipient is a conflict. Content hash alone is not an operation ID because identical messages can be intentionally distinct operations. Provider idempotency behavior is feature-probed and recorded, never assumed from SDK availability.

## Receipt strength
`accepted` means the provider accepted a request. `effect_confirmed` names a demonstrated specific effect. `delivered`, `played` and `read` require their respective provider evidence; unsupported receipt levels remain unavailable. An observed message delivery never establishes the user's Objective complete. Effect truth and downstream Work Item state belong to different owners.

## Retry and cancellation
Gate_SDK does not perform hidden execution retry. Communication may retry only after policy permits and non-execution/idempotent repetition is proven for the exact request. A cancellation request does not itself prove cancellation. Sending a compensating message or initiating a refund is a new governed ActionIntent, not an automatic storage rollback.
