from __future__ import annotations
from collections.abc import Mapping, Sequence
from ..evidence import violated_constraints
from ..models import ValidationRequest, ValidationResult
from ..result import ValidationStatus
from .base import MechanicalSolver, SolverIdentity
class StructuralSolver(MechanicalSolver):
    identity = SolverIdentity(
        ref="l9.solver/structural@1",
        version="1",
        solver_class="structural",
    )
    def validate(
        self,
        request: ValidationRequest,
    ) -> ValidationResult:
        violated: list[str] = []
        for constraint in request.applicable_constraints:
            if not isinstance(constraint, Mapping):
                continue
            ref = str(
                constraint.get(
                    "id",
                    "anonymous-constraint",
                )
            )
            required_fields = constraint.get(
                "required_fields",
                [],
            )
            if required_fields:
                if not isinstance(
                    request.candidate,
                    Mapping,
                ):
                    violated.append(ref)
                    continue
                missing = [
                    field
                    for field in required_fields
                    if field not in request.candidate
                ]
                if missing:
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
