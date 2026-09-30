from __future__ import annotations
from typing import Mapping
from .models import (
    CanonicalArtifact,
    ProjectionArtifact,
    ProjectionProfile,
)
def projection_is_stale(
    *,
    artifact: ProjectionArtifact,
    profile: ProjectionProfile,
    sources: Mapping[
        str,
        CanonicalArtifact,
    ],
) -> bool:
    if (
        artifact.profile_digest
        != profile.digest
    ):
        return True
    for source_ref in artifact.sources:
        current = sources.get(
            source_ref.source_class
        )
        if current is None:
            return True
        if current.digest != source_ref.digest:
            return True
    return False
