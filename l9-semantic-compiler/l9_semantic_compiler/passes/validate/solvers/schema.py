from __future__ import annotations
from typing import Any, Mapping
from ..evidence import invalidity, violated_constraints
from ..models import ValidationRequest, ValidationResult
from ..result import ValidationStatus
from .base import MechanicalSolver, SolverIdentity
class SchemaSolver(MechanicalSolver):
    identity = SolverIdentity(
        ref="l9.solver/schema@1",
        version="1",
        solver_class="schema",
    )
    def validate(
        self,
        request: ValidationRequest,
    ) -> ValidationResult:
        schema = (
            request.solver_projection.parameters.get(
                "schema"
            )
        )
        if schema is None:
            return ValidationResult(
                status=ValidationStatus.INVALID,
                evidence=(
                    invalidity(
                        "schema solver requires schema parameter"
                    ),
                ),
            )
        violations = _validate(
            request.candidate,
            schema,
            path="$",
        )
        if violations:
            return ValidationResult(
                status=ValidationStatus.FAIL,
                evidence=(
                    violated_constraints(
                        tuple(violations)
                    ),
                ),
                diagnostics=tuple(violations),
            )
        return ValidationResult(
            status=ValidationStatus.PASS
        )
def _validate(
    value: Any,
    schema: Mapping[str, Any],
    *,
    path: str,
) -> list[str]:
    violations: list[str] = []
    expected = schema.get("type")
    if expected == "object":
        if not isinstance(value, Mapping):
            return [f"{path}: expected object"]
        for field in schema.get(
            "required",
            [],
        ):
            if field not in value:
                violations.append(
                    f"{path}.{field}: required"
                )
        properties = schema.get(
            "properties",
            {},
        )
        for field, child_schema in properties.items():
            if field not in value:
                continue
            violations.extend(
                _validate(
                    value[field],
                    child_schema,
                    path=f"{path}.{field}",
                )
            )
    elif expected == "array":
        if not isinstance(value, list):
            violations.append(
                f"{path}: expected array"
            )
    elif expected == "string":
        if not isinstance(value, str):
            violations.append(
                f"{path}: expected string"
            )
    elif expected == "integer":
        if (
            not isinstance(value, int)
            or isinstance(value, bool)
        ):
            violations.append(
                f"{path}: expected integer"
            )
    elif expected == "number":
        if (
            not isinstance(value, (int, float))
            or isinstance(value, bool)
        ):
            violations.append(
                f"{path}: expected number"
            )
    elif expected == "boolean":
        if not isinstance(value, bool):
            violations.append(
                f"{path}: expected boolean"
            )
    if "enum" in schema:
        if value not in schema["enum"]:
            violations.append(
                f"{path}: value not in enum"
            )
    return violations
