from __future__ import annotations
from collections.abc import Mapping
from ..evidence import invalidity, violated_constraints
from ..models import ValidationRequest, ValidationResult
from ..result import ValidationStatus
from .base import MechanicalSolver, SolverIdentity
class SetCompatibilitySolver(MechanicalSolver):
    identity = SolverIdentity(
        ref="l9.solver/set-compatibility@1",
        version="1",
        solver_class="set_compatibility",
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
                        "set compatibility candidate must be mapping"
                    ),
                ),
            )
        required = set(
            candidate.get(
                "required_capabilities",
                [],
            )
        )
        provided = set(
            candidate.get(
                "provided_capabilities",
                [],
            )
        )
        missing = required - provided
        if missing:
            return ValidationResult(
                status=ValidationStatus.FAIL,
                evidence=(
                    violated_constraints(
                        tuple(
                            sorted(missing)
                        ),
                        details={
                            "missing_capabilities": sorted(
                                missing
                            )
                        },
                    ),
                ),
            )
        return ValidationResult(
            status=ValidationStatus.PASS
        )
