from __future__ import annotations
from .models import (
    ValidationEvidence,
    ValidationRequest,
    ValidationResult,
)
from .registry import SolverRegistry
from .result import ValidationStatus
def dispatch_validation(
    *,
    request: ValidationRequest,
    registry: SolverRegistry,
) -> ValidationResult:
    try:
        solver = registry.resolve(
            request.solver_projection.solver_ref
        )
    except KeyError as exc:
        return ValidationResult(
            status=ValidationStatus.INVALID,
            diagnostics=(str(exc),),
        )
    if (
        solver.identity.version
        != request.solver_projection.solver_version
    ):
        return ValidationResult(
            status=ValidationStatus.INVALID,
            diagnostics=(
                "solver version does not match "
                "selected solver projection",
            ),
        )
    try:
        return solver.validate(request)
    except Exception as exc:
        return ValidationResult(
            status=ValidationStatus.INVALID,
            evidence=(
                ValidationEvidence(
                    kind="solver_exception",
                    details={
                        "solver_ref": solver.identity.ref,
                        "exception_type": type(exc).__name__,
                    },
                ),
            ),
            diagnostics=(str(exc),),
        )
