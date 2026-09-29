# Operator runbook

## Prepare
Validate the consolidated archive and read the repo contract. Refresh Gate/SDK admission and streaming capabilities. Admit provider versions, account scope, feature inventory, webhook authentication, sender/recipient identities, retention policy and exact effects. Provision only this node's external provider credentials and required L9 action grants.

## Synthetic and sandbox proof
Run a dry routing test with synthetic messages and test accounts. Verify no messages reach real people. Exercise duplicate operation keys, accepted-but-not-delivered receipts, webhook replay, cross-tenant target tampering, recipient ambiguity, late tokens after interruption, current grant revocation and unconfirmed cancellation.

## Live canary
A later explicitly authorized session may enable a single scoped channel and test recipient. Record native IDs, actual receipt strength and recovery behavior. Prove State settlement and Evidence retention. Do not enable public outbound or recording because a schema test passed.

## Incident handling
On unknown send/call outcome inspect the original operation and provider evidence; do not retry from scratch. On webhook abuse reject at ingress before AgentOS processing. On turn-generation drift stop playback for stale output. On revoked consent stop capture and trigger retention-owner procedures for permitted copies. On Evidence outage keep the operation's outcome truth visible and do not falsify durable audit completion.

## Rollback
Disable new session/send admission, drain/cancel provider sessions where supported, reconcile outstanding effects and retain original receipts. Roll back adapter code only after compatibility review; never replay uncertain sends under the prior version. Do not roll back domain Work Items or erase provider receipts as a substitute for compensation.
