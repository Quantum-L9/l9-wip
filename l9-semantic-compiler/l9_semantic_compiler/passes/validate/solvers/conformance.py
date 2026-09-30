from __future__ import annotations
from collections.abc import Mapping
from ..evidence import invalidity, violated_constraints
from ..models import ValidationRequest, ValidationResult
from ..result import ValidationStatus
from .base import MechanicalSolver, SolverIdentity
class ConformanceSolver(MechanicalSolver):
    identity = SolverIdentity(
        ref="l9.solver/conformance@1",
        version="1",
        solver_class="conformance",
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
                        "conformance candidate must be mapping"
                    ),
                ),
            )
        cases = candidate.get(
            "cases",
            []
        )
        failed = [
            str(case.get("id", "anonymous"))
            for case in cases
            if isinstance(case, Mapping)
            and case.get("result") != "PASS"
        ]
        if failed:
            return ValidationResult(
                status=ValidationStatus.FAIL,
                evidence=(
                    violated_constraints(
                        tuple(failed),
                        details={
                            "failed_cases": failed,
                        },
                    ),
                ),
            )
        return ValidationResult(
            status=ValidationStatus.PASS
        )
