from __future__ import annotations
from typing import Any, Mapping
from .models import SolverProjection
def select_solver_projection(
    *,
    stage: str,
    compilation_profile: Mapping[str, Any],
    compilation_profile_digest: str,
) -> SolverProjection:
    stages = compilation_profile.get("stages", [])
    for stage_spec in stages:
        if stage_spec.get("id") != stage:
            continue
        validation = stage_spec.get("validation", {})
        solver_ref = validation.get("solver_ref")
        if not solver_ref:
            raise ValueError(
                f"stage {stage!r} does not declare solver_ref"
            )
        solver_version = _version_from_ref(
            str(solver_ref)
        )
        return SolverProjection(
            solver_ref=str(solver_ref),
            solver_version=solver_version,
            solver_profile_digest=compilation_profile_digest,
            parameters=dict(
                validation.get("parameters", {})
            ),
        )
    raise ValueError(
        f"stage not found in compilation profile: {stage}"
    )
def _version_from_ref(ref: str) -> str:
    if "@" not in ref:
        raise ValueError(
            f"solver ref must be versioned: {ref}"
        )
    return ref.rsplit("@", 1)[1]
