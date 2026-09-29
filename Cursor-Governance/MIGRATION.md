# Cursor-Governance: migration and rollback

## Preconditions
Current base/head census; predecessor contract artifacts; exact scope authorization; source and destination identity mapping; negative-case fixtures; rollback eligibility. Read the actual current code, not only docs or this archived plan.

## Cutover discipline
Introduce the new contract alongside the old interface only when compatibility is explicit. Route one scope to one writer. Shadow reads compare behavior without mutating either canonical system. Persist migration receipts, operation maps and unresolved outcomes. Retire old paths only after end-to-end proof and source retention obligations close.

## Rollback
Before writer switch, revert bindings only. After switch, preserve canonical records and replay identities; use read-only donor fallback for inspection, never dual writers or old unsafe provider paths.

## Definition of done
All listed proof obligations have current-revision evidence. No generic duplicate owner remains. Docs and generated projections point to the actual new owner. Deferred unrelated issues are recorded, not opportunistically fixed.
