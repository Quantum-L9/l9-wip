from __future__ import annotations
from copy import deepcopy
from typing import Any
from .canonical import semantic_digest
from .errors import SemanticConflictError
from .models import (
    ComposedProjectionArtifact,
    CompositionCompilation,
    CompositionProfile,
    ProjectionArtifact,
)
from .receipts import build_composition_receipt
def compose_projections(
    *,
    profile: CompositionProfile,
    components: tuple[
        ProjectionArtifact,
        ...,
    ],
) -> CompositionCompilation:
    if not components:
        raise SemanticConflictError(
            "composition requires at least one projection"
        )
    merged: dict[str, Any] = {}
    for component in components:
        merged = _merge(
            merged,
            component.payload,
            path="$",
        )
    digest_payload = {
        "composition_profile_ref": (
            profile.profile_id
        ),
        "composition_profile_digest": (
            profile.digest
        ),
        "components": [
            {
                "profile_ref": component.profile_ref,
                "projection_digest": (
                    component.projection_digest
                ),
            }
            for component in components
        ],
        "payload": merged,
    }
    composition_digest = semantic_digest(
        digest_payload
    )
    artifact = ComposedProjectionArtifact(
        schema="l9.composed-projection/v1",
        authority_class="derived",
        composition_profile_ref=(
            profile.profile_id
        ),
        composition_profile_digest=(
            profile.digest
        ),
        components=components,
        payload=merged,
        composition_digest=composition_digest,
    )
    receipt = build_composition_receipt(
        artifact=artifact,
    )
    return CompositionCompilation(
        artifact=artifact,
        receipt=receipt,
    )
def _merge(
    left: Any,
    right: Any,
    *,
    path: str,
) -> Any:
    if left == {}:
        return deepcopy(right)
    if right == {}:
        return deepcopy(left)
    if isinstance(
        left,
        dict,
    ) and isinstance(
        right,
        dict,
    ):
        result = deepcopy(left)
        for key, right_value in right.items():
            child_path = f"{path}.{key}"
            if key not in result:
                result[key] = deepcopy(
                    right_value
                )
                continue
            result[key] = _merge(
                result[key],
                right_value,
                path=child_path,
            )
        return result
    if isinstance(
        left,
        list,
    ) and isinstance(
        right,
        list,
    ):
        result = deepcopy(left)
        for item in right:
            if item not in result:
                result.append(
                    deepcopy(item)
                )
        return result
    if left == right:
        return deepcopy(left)
    raise SemanticConflictError(
        f"semantic conflict at {path}: "
        f"{left!r} != {right!r}"
    )
