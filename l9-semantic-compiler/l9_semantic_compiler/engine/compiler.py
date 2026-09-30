from __future__ import annotations
from pathlib import Path
from typing import Mapping
from .composition import compose_projections
from .loader import (
    load_canonical_artifact,
    load_document,
)
from .models import (
    CanonicalArtifact,
    CompositionCompilation,
    ProjectionCompilation,
)
from .projection import compile_projection
from .registry import (
    CompositionProfileRegistry,
    ProjectionProfileRegistry,
)
from .staleness import projection_is_stale
from .validation import (
    validate_composed_projection,
    validate_projection_artifact,
)
class GenericSemanticCompiler:
    def __init__(
        self,
        *,
        projection_profiles: ProjectionProfileRegistry,
        composition_profiles: CompositionProfileRegistry,
    ) -> None:
        self.projection_profiles = (
            projection_profiles
        )
        self.composition_profiles = (
            composition_profiles
        )
    def project(
        self,
        *,
        profile_id: str,
        sources: Mapping[
            str,
            CanonicalArtifact,
        ],
    ) -> ProjectionCompilation:
        profile = (
            self.projection_profiles.get(
                profile_id
            )
        )
        compilation = compile_projection(
            profile=profile,
            sources=sources,
        )
        validate_projection_artifact(
            compilation.artifact
        )
        return compilation
    def compose(
        self,
        *,
        profile_id: str,
        projections: tuple[
            ProjectionCompilation,
            ...,
        ],
    ) -> CompositionCompilation:
        profile = (
            self.composition_profiles.get(
                profile_id
            )
        )
        components = tuple(
            projection.artifact
            for projection in projections
        )
        compilation = compose_projections(
            profile=profile,
            components=components,
        )
        validate_composed_projection(
            compilation.artifact
        )
        return compilation
    def is_stale(
        self,
        *,
        projection: ProjectionCompilation,
        profile_id: str,
        sources: Mapping[
            str,
            CanonicalArtifact,
        ],
    ) -> bool:
        profile = (
            self.projection_profiles.get(
                profile_id
            )
        )
        return projection_is_stale(
            artifact=projection.artifact,
            profile=profile,
            sources=sources,
        )
def load_sources(
    *,
    semantic_root: str | Path,
    source_classes: Mapping[
        str,
        str,
    ],
) -> dict[
    str,
    CanonicalArtifact,
]:
    root = Path(semantic_root)
    return {
        source_class: (
            load_canonical_artifact(
                path=root / relative_path,
                source_class=source_class,
            )
        )
        for (
            source_class,
            relative_path,
        ) in source_classes.items()
    }
