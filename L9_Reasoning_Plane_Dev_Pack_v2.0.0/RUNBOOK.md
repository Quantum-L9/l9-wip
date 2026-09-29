# Runbook

## Purpose

This is a pre-code architecture/contract pack. The runbook validates the pack itself and provides the implementation entry sequence; it does not deploy or create repositories.

## Validate

From the pack root:

```bash
./scripts/run_all_validation.sh
```

Expected output: six `PASS` lines.

For integrity after `SHA256SUMS` has been generated:

```bash
sha256sum -c SHA256SUMS
```

For ZIP verification from the parent directory:

```bash
unzip -t L9_Reasoning_Plane_Dev_Pack_v2.0.0.zip
```

## Rehydrate

Read in this order:

1. `00_REHYDRATION.md`
2. `README.md`
3. `docs/ARCHITECTURE.md`
4. `docs/INVARIANTS.md`
5. `architecture/AUTHORITY_MAP.yaml`
6. `architecture/IMPLEMENTATION_BLUEPRINT.yaml`
7. `docs/STRATEGIC_INTERACTION_REASONING.md`
8. `docs/STRATEGIC_VALUE_FRAMEWORK.md`
9. `docs/GRAPH_MEMORY_AND_ODOO_PROJECTION.md`
10. `audit/CONVERGENCE_REPORT.yaml`
11. implementation plans relevant to the selected slice.

## Implementation entry

The pack is PRE_CODE_SSOT. Before code mutation:
- reconcile live repository state;
- confirm current Gate/Gate_SDK contracts;
- confirm current repo-template / node chassis contracts;
- compile an implementation plan using current planning owner;
- bind plan to this exact pack revision/digest;
- do not reinterpret superseded v1 vocabulary as current law.

## Failure recovery

If a validation fails:
1. inspect the failing script/output;
2. repair the earliest invalid semantic layer;
3. rerun `run_all_validation.sh`;
4. regenerate manifest/SHA only after all semantic validation passes;
5. rebuild ZIP and run ZIP integrity.
