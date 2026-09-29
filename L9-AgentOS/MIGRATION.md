# L9-AgentOS: adoption and migration

## Source status
The target is a separate node. It is not created in this delivery. Donor inventory and current implementation seams are in ../../sources and the donor repo packs.

## Sequence
Extract behavior and invariants first. Introduce canonical payload contracts without moving live writes. Build the owner implementation and fixtures. Compare it against donor semantics using synthetic and read-only sampled evidence. Establish a cutover cursor/profile/schema binding. Switch one authorized scope at a time to one writer. Verify exact receipts and recovery. Retain donor read-only until rollback and history obligations close.

## Must preserve
Source identifiers and digests, tenant/subject scope, operation identity, original evidence provenance, revocation/deletion semantics and unresolved outcome state. Vocabulary changes do not manufacture new source authority. Every translated record carries an explicit legacy-to-canonical mapping in migration evidence; canonical APIs do not keep old aliases indefinitely.

## Do not do
No dual canonical write for convenience. No direct copying of another node's backing tables. No replay of external effects during data migration. No automatic promotion of raw transcripts into memory. No destructive cleanup before destination receipts and source retention obligations are reconciled.

## Rollback
Rollback routing/configuration to the last proved safe owner only when that does not restore a known security defect. Preserve newly committed records and replay mappings. If the previous writer cannot understand new schema versions, freeze writes and perform forward repair instead of losing state.
