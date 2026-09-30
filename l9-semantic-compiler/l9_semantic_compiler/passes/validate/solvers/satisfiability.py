from __future__ import annotations
from itertools import product
from typing import Mapping
from ..evidence import unsat_core
from ..models import ValidationRequest, ValidationResult
from ..result import ValidationStatus
from .base import MechanicalSolver, SolverIdentity
class SatisfiabilitySolver(MechanicalSolver):
    identity = SolverIdentity(
        ref="l9.solver/satisfiability@1",
        version="1",
        solver_class="satisfiability",
    )
    def validate(
        self,
        request: ValidationRequest,
    ) -> ValidationResult:
        constraints = [
            constraint
            for constraint in request.applicable_constraints
            if isinstance(constraint, Mapping)
        ]
        variables = sorted(
            {
                str(variable)
                for constraint in constraints
                for variable in constraint.get(
                    "variables",
                    [],
                )
            }
        )
        if not variables:
            return ValidationResult(
                status=ValidationStatus.PASS
            )
        for values in product(
            [False, True],
            repeat=len(variables),
        ):
            assignment = dict(
                zip(variables, values)
            )
            if all(
                _constraint_holds(
                    constraint,
                    assignment,
                )
                for constraint in constraints
            ):
                return ValidationResult(
                    status=ValidationStatus.PASS
                )
        refs = tuple(
            str(
                constraint.get(
                    "id",
                    "anonymous",
                )
            )
            for constraint in constraints
        )
        return ValidationResult(
            status=ValidationStatus.UNSAT,
            evidence=(
                unsat_core(refs),
            ),
        )
def _constraint_holds(
    constraint: Mapping,
    assignment: Mapping[str, bool],
) -> bool:
    kind = constraint.get("kind")
    if kind == "require":
        variable = str(
            constraint["variable"]
        )
        return bool(
            assignment.get(variable)
        )
    if kind == "forbid":
        variable = str(
            constraint["variable"]
        )
        return not bool(
            assignment.get(variable)
        )
    if kind == "imply":
        left = str(constraint["if"])
        right = str(constraint["then"])
        return (
            not assignment.get(left, False)
            or assignment.get(right, False)
        )
    return True
