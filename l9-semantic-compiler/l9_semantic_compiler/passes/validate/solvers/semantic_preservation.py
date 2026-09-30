from __future__ import annotations
from collections.abc import Mapping
from ..evidence import invalidity, violated_constraints
from ..models import ValidationRequest, ValidationResult
from ..result import ValidationStatus
from .base import MechanicalSolver, SolverIdentity
class SemanticPreservationSolver(MechanicalSolver):
    identity = SolverIdentity(
        ref="l9.solver/semantic-preservation@1",
        version="1",
        solver_class="semantic_preservation",
    )
    def validate(
        self,
        request: ValidationRequest,
    ) -> ValidationResult:
        candidate = request.candidate
        if not isinstance(candidate, Mapping):
            return ValidationResult(
                status=ValidationStatus.INVALID,
                evidence=(
                    invalidity(
                        "semantic preservation candidate must be mapping"
                    ),
                ),
            )
        required = set(
            candidate.get(
                "required_semantics",
                [],
            )
        )
        preserved = set(
            candidate.get(
                "preserved_semantics",
                [],
            )
        )
        lost = required - preserved
        if lost:
            return ValidationResult(
                status=ValidationStatus.FAIL,
                evidence=(
                    violated_constraints(
                        tuple(sorted(lost)),
                        details={
                            "lost_semantics": sorted(lost)
                        },
                    ),
                ),
            )
        return ValidationResult(
            status=ValidationStatus.PASS
        )
