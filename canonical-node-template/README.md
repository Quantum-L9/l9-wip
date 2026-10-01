# L9 Canonical Contract Templates

These templates define the reusable structural starting point for designing an L9 product:

- `product-topology.yaml` — what the product is
- `repository-spec.yaml` — how the product's source repository is organized and projected
- `workflow-spec.yaml` — how a governed process executes

## Required Upstream Alignment

Before specializing or admitting any of these templates for a real L9 product, the implementing agent MUST align the resulting contracts with the canonical semantics owned by:

`Quantum-L9/.github/semantics`

Repository:

https://github.com/Quantum-L9/.github

The `.github/semantics` folder is the upstream semantic authority for shared L9 concepts, vocabulary, invariants, contracts, authority boundaries, product kinds, archetypes, lifecycle semantics, projection semantics, identity semantics, and other globally governed definitions.

## Agent Rules

An agent designing an L9 product from these templates MUST:

1. Resolve the current canonical semantics from `Quantum-L9/.github/semantics` before assigning product-specific meaning.
2. Use admitted canonical terms, contract references, archetypes, patterns, lifecycle states, authority classes, and identity semantics where they exist.
3. Preserve the ownership boundary between global L9 semantics and product-owned semantics.
4. Never redefine, fork, weaken, or silently reinterpret canonical `.github/semantics` definitions inside a product repository.
5. Treat unresolved or conflicting upstream semantics as `Unknown` and fail closed rather than inventing a local substitute.
6. Bind the specialized ProductTopology, RepositorySpec, and WorkflowSpec to the exact upstream semantic coordinates required by the governing contracts.
7. Re-evaluate affected derived contracts whenever a material upstream semantic dependency changes.
8. Keep generated or projected artifacts derived. They do not become independent semantic authority.

## Specialization Order

Use the templates in this order:

```text
Quantum-L9/.github/semantics
            ↓
    product-topology.yaml
            ↓
    repository-spec.yaml
            ↓
      workflow-spec.yaml
            ↓
   derived projections
```

`ProductTopology` defines product meaning.

`RepositorySpec` organizes and projects that product meaning into repository-scoped source structure without redefining it.

`WorkflowSpec` defines governed process execution under the already-resolved semantic and authority boundaries.

## Non-Negotiable Rule

If a template field conflicts with current canonical semantics in `Quantum-L9/.github/semantics`, the canonical upstream semantics win.

Do not "make the template fit" by inventing local semantics. Resolve the authority conflict first.
