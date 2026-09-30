# L9 `.github` Product-Compilation Architecture ADR Pack

Status: **REPLACEMENT CANDIDATE / RELEASE-READY**

This ADR pack formalizes how `Quantum-L9/.github` acts as the organization-level semantic authority for product topology, product compilation, and shared architecture semantics. It governs canonical meaning and compiler inputs, not product runtime implementation.

## North-star equation

```text
ProductTopology
    -> ProductKind + Archetype Resolution
    -> Requirement Closure
    -> Semantic Resolution
    -> Contracts / Laws / Conformance
    -> Architecture / Ports / Adapters / Relationships
    -> Technology / Provider Bindings
    -> ProductManifest
    -> Implementation IR
    -> Target Artifacts
```

## ADRs

- ADR-001: `.github` as the L9 global semantic authority
- ADR-002: One flat canonical semantic surface and one global contract catalog
- ADR-003: ProductTopology as the first-class product contract
- ADR-004: Requirement and resolution algebra
- ADR-005: Capability -> architecture -> port semantic resolution
- ADR-006: Technology binding after semantic resolution
- ADR-007: Conformance requirements and independent correctness
- ADR-008: ProductManifest as proof-carrying resolved realization
- ADR-009: Contract wiring, projections, compilation profiles, and invalidation
- ADR-010: Ownership boundaries and anti-recipe constraint
- ADR-011: ProductKind from canonical consumption and deployment

- `ADR-012-identity-topology-first-class-primitive.md` — identity dimensions, canonical resolution, typed assertions, and governance-profile separation.
