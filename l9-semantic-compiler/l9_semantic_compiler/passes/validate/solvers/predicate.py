from __future__ import annotations
from typing import Any, Mapping
from ..evidence import invalidity, violated_constraints
from ..models import ValidationRequest, ValidationResult
from ..result import ValidationStatus
from .base import MechanicalSolver, SolverIdentity
class PredicateSolver(MechanicalSolver):
    identity = SolverIdentity(
        ref="l9.solver/predicate@1",
        version="1",
        solver_class="predicate",
    )
    def validate(
        self,
        request: ValidationRequest,
    ) -> ValidationResult:
        if not isinstance(
            request.candidate,
            Mapping,
        ):
            return ValidationResult(
                status=ValidationStatus.INVALID,
                evidence=(
                    invalidity(
                        "predicate solver requires mapping candidate"
                    ),
                ),
            )
        violated: list[str] = []
        for constraint in request.applicable_constraints:
            if not isinstance(
                constraint,
                Mapping,
            ):
                continue
            ref = str(
                constraint.get(
                    "id",
                    "anonymous",
                )
            )
            when = constraint.get(
                "when",
                {},
            )
            must = constraint.get(
                "must",
                {},
            )
            if _matches(
                request.candidate,
                when,
            ):
                if not _matches(
                    request.candidate,
                    must,
                ):
                    violated.append(ref)
        if violated:
            return ValidationResult(
                status=ValidationStatus.FAIL,
                evidence=(
                    violated_constraints(violated),
                ),
            )
        return ValidationResult(
            status=ValidationStatus.PASS
        )
def _matches(
    candidate: Mapping[str, Any],
    expected: Mapping[str, Any],
) -> bool:
    return all(
        candidate.get(key) == value
        for key, value in expected.items()
    )
