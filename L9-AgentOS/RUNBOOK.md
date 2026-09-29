# L9-AgentOS operator and implementer runbook

## Before code
Read the assigned execution unit and verify current repo/ref, outstanding PRs, authority, SDK version and required predecessor receipts. Confirm the node-birth contract and preserve all organization CI ownership. Run the pack validator first; then create the target's real tests before claiming implementation behavior.

## Build-time sequence
1. Publish/review semantic contracts and candidate schemas without runtime side effects.
2. Implement pure domain behavior and conformance tests.
3. Add private first-stack adapters and fault injection.
4. Wire the existing Gate SDK/chassis and prove signed role/scope round trips.
5. Run independent installed-artifact and recovery proofs; request release admission only with receipts.

## Planned target commands
`uv sync --frozen --extra dev` after the target lock exists; `uv run python -m pytest tests/contracts tests/unit`; `uv run python -m pytest tests/architecture`; `uv run python -m pytest tests/integration`; owner-native lint/type/package/release commands discovered at baseline. These are planned commands for the implementation, not claims they ran here. Do not invent a fallback installation path when the target's CI contract differs.

## Recovery
Preserve evidence and exact operation IDs before restarting. Inspect operation status at the owner. Do not replay an unknown effect blindly. If a provider is unavailable, retain recovery state and wait for authorized reconciliation rather than switching to a second truth store. Restore from a tested snapshot only after proving source journal and tombstone consistency.

## Release admission
Requires locked images/packages, supported deployment topology, authenticated identity, scoped credentials, active health probes, rollback plan, backups/restore test, and no required skipped tests. A registry entry alone does not prove readiness. Deployment or migration needs separate operator authorization.
