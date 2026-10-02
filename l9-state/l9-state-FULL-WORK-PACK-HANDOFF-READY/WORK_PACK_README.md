# L9 State Full Work Pack — Handoff Ready

This is the complete L9 State work pack through local closure of `VALIDATE-F-001` and preparation for the remaining Cursor-only validation gates.

## Current state

`VALIDATE-F-001` is repaired. There are **zero known code failures** in the locally executable validation surface.

Local evidence:

- source pytest: **73/73 PASS**
- installed repaired wheel pytest: **73/73 PASS**
- signed released Gate_SDK round trip from source: **13/13 PASS**
- signed released Gate_SDK round trip from installed wheel: **13/13 PASS**
- VALIDATE-F001 static: **19/19 PASS**
- Mongo handoff static audit: **20/20 PASS**
- REMED-01 static: **43/43 PASS**
- STATE-03 static: **125/125 PASS**
- STATE-04 static: **153/153 PASS**
- public JSON schema bytes changed: **0**
- repaired State wheel SHA-256: `25d2bd7e0bffaeddd95ba4952001188a643cce879c3c82648a630219e20a951b`

The hard-erase repair preserves the architecture boundary: an active claim supplies coordination/fencing evidence through the exact current `claim_id` and `fencing_token`; the externally authorized retention executor is not required to impersonate the claim holder. Receipt authorship and external retention authorization remain distinct and preserved.

## Exact handoff

Start with:

- `handoff/HANDOFF_READINESS.yaml`
- `handoff/CURSOR/CURSOR_HANDOFF_CONTRACT.yaml`
- `handoff/CURSOR/MONGO_VALIDATION_MATRIX.yaml`
- `handoff/CURSOR/run_remaining_validation.sh`
- `handoff/CURSOR/validate_mongo_live.py`

Cursor is authorized only to close the remaining environment-dependent validation gates: Ruff, mypy, live transaction-capable MongoDB behavior, fault injection, failover/restart, and replay evidence. It must not redesign State, change public schemas, modify Gate_SDK or sibling repositories, invent retention policy, begin ProductTopology/admission work, merge, publish, or deploy.

## Authority coordinates at handoff

- Semantic authority: `Quantum-L9/.github@43600db3ee43f17fd30d2df589ff6bc0eb8b19d2`
- Gate compatibility contract: `v1`
- Gate `v1` / `v1.2.0` tag commit: `7ec6cdf5e26c837057ca35b7324a88de4d499ea3`
- Released Gate wheel SHA-256: `543d95ba4270f64bf885770fd296340a59c762c21e4d73748dec8da0775a2107`

The handoff contract fails closed if either upstream coordinate moves before validation begins.

## Contents

The pack retains the complete State source/contracts/tests/build-state lineage, original v2 Dev Pack input, REVIEW-01, REMED-01, delta review, original VALIDATE-01 failure evidence, historical pre-fix State wheel, repaired State wheel, VALIDATE-F001 closure evidence, and the Cursor handoff package.

No merge, publish, deployment, admission, or external retention-policy activation is represented by this pack.
