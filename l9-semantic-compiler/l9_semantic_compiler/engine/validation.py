from __future__ import annotations
from typing import Any, Mapping
from .canonical import semantic_digest
from .errors import ValidationError
from .models import (
    ComposedProjectionArtifact,
    ProjectionArtifact,
)
def validate_projection_artifact(
    artifact: ProjectionArtifact,
) -> None:
    if artifact.authority_class != "derived":
        raise ValidationError(
            "projection artifact authority must be derived"
        )
    if not artifact.sources:
        raise ValidationError(
            "projection must preserve at least one source"
        )
    if not artifact.profile_ref:
        raise ValidationError(
            "projection profile ref is required"
        )
    if not artifact.profile_digest:
        raise ValidationError(
            "projection profile digest is required"
        )
    expected = semantic_digest(
        {
            "profile_ref": artifact.profile_ref,
            "profile_digest": artifact.profile_digest,
            "consumer": artifact.consumer,
            "sources": [
                source.to_dict()
                for source in artifact.sources
            ],
            "payload": artifact.payload,
        }
    )
    if expected != artifact.projection_digest:
        raise ValidationError(
            "projection digest mismatch"
        )
def validate_composed_projection(
    artifact: ComposedProjectionArtifact,
) -> None:
    if artifact.authority_class != "derived":
        raise ValidationError(
            "composed projection authority must be derived"
        )
    if not artifact.components:
        raise ValidationError(
            "composed projection requires components"
        )
    expected = semantic_digest(
        {
            "composition_profile_ref": (
                artifact.composition_profile_ref
            ),
            "composition_profile_digest": (
                artifact.composition_profile_digest
            ),
            "components": [
                {
                    "profile_ref": (
                        component.profile_ref
                    ),
                    "projection_digest": (
                        component.projection_digest
                    ),
                }
                for component in artifact.components
            ],
            "payload": artifact.payload,
        }
    )
    if expected != artifact.composition_digest:
        raise ValidationError(
            "composition digest mismatch"
        )
def require_fields(
    value: Mapping[str, Any],
    *fields: str,
) -> None:
    missing = [
        field
        for field in fields
        if field not in value
    ]
    if missing:
        raise ValidationError(
            "missing required fields: "
            + ", ".join(missing)
        )
