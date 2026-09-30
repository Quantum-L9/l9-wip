from __future__ import annotations
from typing import Any, Mapping
def validate_validation_profile(
    profile: Mapping[str, Any],
) -> tuple[str, ...]:
    errors: list[str] = []
    if profile.get("required") is not True:
        errors.append(
            "validation profile must declare required: true"
        )
    solver_ref = profile.get("solver_ref")
    if not solver_ref:
        errors.append(
            "validation profile requires solver_ref"
        )
    elif "@" not in str(solver_ref):
        errors.append(
            "solver_ref must be versioned"
        )
    return tuple(errors)
