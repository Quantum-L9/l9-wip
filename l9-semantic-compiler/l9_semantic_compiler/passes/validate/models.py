from __future__ import annotations
from dataclasses import dataclass, field
from typing import Any, Mapping
from .result import ValidationStatus
@dataclass(frozen=True)
class SolverProjection:
    solver_ref: str
    solver_version: str
    solver_profile_digest: str
    parameters: Mapping[str, Any] = field(default_factory=dict)
@dataclass(frozen=True)
class ValidationRequest:
    candidate_ref: str
    candidate_digest: str
    candidate: Any
    stage: str
    compilation_profile_ref: str
    compilation_profile_digest: str
    solver_projection: SolverProjection
    applicable_constraints: tuple[Any, ...]
    source_provenance: tuple[Mapping[str, Any], ...] = ()
@dataclass(frozen=True)
class ValidationEvidence:
    kind: str
    refs: tuple[str, ...] = ()
    details: Mapping[str, Any] = field(default_factory=dict)
@dataclass(frozen=True)
class ValidationResult:
    status: ValidationStatus
    evidence: tuple[ValidationEvidence, ...] = ()
    diagnostics: tuple[str, ...] = ()
    @property
    def passed(self) -> bool:
        return self.status is ValidationStatus.PASS
