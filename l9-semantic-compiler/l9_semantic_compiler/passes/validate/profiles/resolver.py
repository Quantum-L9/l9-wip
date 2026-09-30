from __future__ import annotations
from typing import Any, Mapping
def resolve_validation_profile(
    *,
    stage: str,
    compilation_profile: Mapping[str, Any],
) -> Mapping[str, Any]:
    for stage_spec in compilation_profile.get(
        "stages",
        [],
    ):
        if stage_spec.get("id") == stage:
            return dict(
                stage_spec.get(
                    "validation",
                    {},
                )
            )
    raise KeyError(
        f"validation profile not found for stage: {stage}"
    )
