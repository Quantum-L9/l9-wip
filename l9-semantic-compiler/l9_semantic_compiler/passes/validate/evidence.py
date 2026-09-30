from __future__ import annotations
from typing import Any, Mapping
from .models import ValidationEvidence
def violated_constraints(
    refs: list[str] | tuple[str, ...],
    *,
    details: Mapping[str, Any] | None = None,
) -> ValidationEvidence:
    return ValidationEvidence(
        kind="violated_constraints",
        refs=tuple(refs),
        details=dict(details or {}),
    )
def unsat_core(
    refs: list[str] | tuple[str, ...],
    *,
    details: Mapping[str, Any] | None = None,
) -> ValidationEvidence:
    return ValidationEvidence(
        kind="unsat_core",
        refs=tuple(refs),
        details=dict(details or {}),
    )
def unresolved(
    refs: list[str] | tuple[str, ...],
    *,
    details: Mapping[str, Any] | None = None,
) -> ValidationEvidence:
    return ValidationEvidence(
        kind="unresolved",
        refs=tuple(refs),
        details=dict(details or {}),
    )
def invalidity(
    reason: str,
) -> ValidationEvidence:
    return ValidationEvidence(
        kind="invalidity",
        details={"reason": reason},
    )
