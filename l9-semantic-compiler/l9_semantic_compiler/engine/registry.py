from __future__ import annotations
from pathlib import Path
from typing import Any, Mapping
from .canonical import semantic_digest
from .errors import (
    ProfileResolutionError,
    SourceResolutionError,
)
from .loader import load_document
from .models import (
    CompositionProfile,
    ProjectionProfile,
)
class CanonicalSourceRegistry:
    def __init__(
        self,
        registry_document: Mapping[str, Any],
        *,
        root: str | Path,
    ) -> None:
        self.root = Path(root)
        sources = registry_document.get(
            "sources",
            [],
        )
        if not isinstance(sources, list):
            raise SourceResolutionError(
                "canonical source registry sources must be an array"
            )
        self._sources: dict[
            str,
            dict[str, Any]
        ] = {}
        for source in sources:
            if not isinstance(source, Mapping):
                raise SourceResolutionError(
                    "canonical source registry entry must be an object"
                )
            source_id = str(source["id"])
            self._sources[source_id] = dict(source)
    def get(
        self,
        source_id: str,
    ) -> dict[str, Any]:
        try:
            return dict(
                self._sources[source_id]
            )
        except KeyError as exc:
            raise SourceResolutionError(
                f"unknown canonical source: {source_id}"
            ) from exc
    def resolve_path(
        self,
        source_id: str,
    ) -> Path:
        source = self.get(source_id)
        return (
            self.root
            / str(source["path"])
        )
class ProjectionProfileRegistry:
    def __init__(
        self,
        catalog: Mapping[str, Any],
    ) -> None:
        profiles = catalog.get(
            "projection_profiles",
            [],
        )
        if not isinstance(profiles, list):
            raise ProfileResolutionError(
                "projection_profiles must be an array"
            )
        self._profiles: dict[
            str,
            ProjectionProfile
        ] = {}
        for raw in profiles:
            if not isinstance(raw, Mapping):
                raise ProfileResolutionError(
                    "projection profile must be an object"
                )
            profile_id = str(raw["id"])
            self._profiles[profile_id] = (
                ProjectionProfile(
                    profile_id=profile_id,
                    profile_class=str(raw["class"]),
                    consumer=str(raw["consumer"]),
                    purpose=str(
                        raw.get(
                            "purpose",
                            "",
                        )
                    ),
                    sources=dict(
                        raw.get(
                            "sources",
                            {},
                        )
                    ),
                    output=dict(
                        raw.get(
                            "output",
                            {},
                        )
                    ),
                    forbidden=tuple(
                        str(item)
                        for item in raw.get(
                            "forbidden",
                            [],
                        )
                    ),
                    digest=semantic_digest(raw),
                    raw=dict(raw),
                )
            )
    def get(
        self,
        profile_id: str,
    ) -> ProjectionProfile:
        try:
            return self._profiles[
                profile_id
            ]
        except KeyError as exc:
            raise ProfileResolutionError(
                f"unknown projection profile: {profile_id}"
            ) from exc
class CompositionProfileRegistry:
    def __init__(
        self,
        catalog: Mapping[str, Any],
    ) -> None:
        profiles = catalog.get(
            "profiles",
            [],
        )
        if not isinstance(profiles, list):
            raise ProfileResolutionError(
                "composition profiles must be an array"
            )
        self._profiles: dict[
            str,
            CompositionProfile
        ] = {}
        for raw in profiles:
            if not isinstance(raw, Mapping):
                raise ProfileResolutionError(
                    "composition profile must be an object"
                )
            profile_id = str(raw["id"])
            self._profiles[profile_id] = (
                CompositionProfile(
                    profile_id=profile_id,
                    purpose=str(
                        raw.get(
                            "purpose",
                            "",
                        )
                    ),
                    merge_strategy=dict(
                        raw.get(
                            "merge_strategy",
                            {},
                        )
                    ),
                    conflict_result=str(
                        raw.get(
                            "conflict_result",
                            "invalid",
                        )
                    ),
                    digest=semantic_digest(raw),
                    raw=dict(raw),
                )
            )
    def get(
        self,
        profile_id: str,
    ) -> CompositionProfile:
        try:
            return self._profiles[
                profile_id
            ]
        except KeyError as exc:
            raise ProfileResolutionError(
                f"unknown composition profile: {profile_id}"
            ) from exc
def load_projection_profile_registry(
    path: str | Path,
) -> ProjectionProfileRegistry:
    return ProjectionProfileRegistry(
        load_document(path)
    )
def load_composition_profile_registry(
    path: str | Path,
) -> CompositionProfileRegistry:
    return CompositionProfileRegistry(
        load_document(path)
    )
