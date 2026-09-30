from __future__ import annotations
from typing import Any, Mapping
from .dispatch import dispatch_validation
from .models import (
    SolverProjection,
    ValidationRequest,
    ValidationResult,
)
from .receipts import build_validation_receipt
from .registry import SolverRegistry
from .selector import select_solver_projection
class ValidationEngine:
    def __init__(
        self,
        *,
        registry: SolverRegistry,
    ) -> None:
        self.registry = registry
    def validate(
        self,
        *,
        candidate_ref: str,
        candidate_digest: str,
        candidate: Any,
        stage: str,
        compilation_profile: Mapping[str, Any],
        compilation_profile_ref: str,
        compilation_profile_digest: str,
        applicable_constraints: tuple[Any, ...],
        source_provenance: tuple[
            Mapping[str, Any],
            ...,
        ] = (),
    ) -> tuple[
        ValidationResult,
        dict[str, Any],
    ]:
        solver_projection = (
            select_solver_projection(
                stage=stage,
                compilation_profile=compilation_profile,
                compilation_profile_digest=(
                    compilation_profile_digest
                ),
            )
        )
        request = ValidationRequest(
            candidate_ref=candidate_ref,
            candidate_digest=candidate_digest,
            candidate=candidate,
            stage=stage,
            compilation_profile_ref=(
                compilation_profile_ref
            ),
            compilation_profile_digest=(
                compilation_profile_digest
            ),
            solver_projection=solver_projection,
            applicable_constraints=(
                applicable_constraints
            ),
            source_provenance=source_provenance,
        )
        result = dispatch_validation(
            request=request,
            registry=self.registry,
        )
        receipt = build_validation_receipt(
            request=request,
            result=result,
        )
        return result, receipt
