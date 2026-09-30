from __future__ import annotations
from copy import deepcopy
from typing import Any, Mapping
from .canonical import semantic_digest
from .errors import ProjectionError
from .models import (
    CanonicalArtifact,
    ProjectionArtifact,
    ProjectionCompilation,
    ProjectionProfile,
    ProjectionSource,
)
from .receipts import build_projection_receipt
from .selectors import select
def compile_projection(
    *,
    profile: ProjectionProfile,
    sources: Mapping[
        str,
        CanonicalArtifact,
    ],
) -> ProjectionCompilation:
    payload: dict[str, Any] = {}
    source_refs: list[
        ProjectionSource
    ] = []
    for (
        source_class,
        source_spec,
    ) in profile.sources.items():
        if source_class not in sources:
            raise ProjectionError(
                f"profile {profile.profile_id} requires "
                f"missing source class {source_class}"
            )
        source = sources[source_class]
        selectors = source_spec.get(
            "selectors",
            [],
        )
        if not isinstance(selectors, list):
            raise ProjectionError(
                f"selectors for {source_class} must be an array"
            )
        projected_source = (
            _compile_source_projection(
                source.payload,
                selectors,
            )
        )
        payload[source_class] = (
            projected_source
        )
        source_refs.append(
            ProjectionSource(
                source_class=source.source_class,
                source_ref=source.source_ref,
                artifact_id=source.artifact_id,
                digest=source.digest,
            )
        )
    schema = str(
        profile.output.get(
            "schema",
            "l9.projection-artifact/v1",
        )
    )
    digest_payload = {
        "profile_ref": profile.profile_id,
        "profile_digest": profile.digest,
        "consumer": profile.consumer,
        "sources": [
            source.to_dict()
            for source in source_refs
        ],
        "payload": payload,
    }
    projection_digest = (
        semantic_digest(
            digest_payload
        )
    )
    artifact = ProjectionArtifact(
        schema=schema,
        authority_class="derived",
        profile_ref=profile.profile_id,
        profile_digest=profile.digest,
        consumer=profile.consumer,
        sources=tuple(source_refs),
        payload=payload,
        projection_digest=projection_digest,
    )
    receipt = build_projection_receipt(
        artifact=artifact,
    )
    return ProjectionCompilation(
        artifact=artifact,
        receipt=receipt,
    )
def _compile_source_projection(
    source: Mapping[str, Any],
    selectors: list[Any],
) -> Any:
    if selectors == ["$"]:
        return deepcopy(source)
    projected: dict[str, Any] = {}
    for raw_selector in selectors:
        selector = str(raw_selector)
        result = select(
            source,
            selector,
        )
        _insert_projection_result(
            projected,
            selector,
            result,
        )
    return projected
def _insert_projection_result(
    target: dict[str, Any],
    selector: str,
    value: Any,
) -> None:
    if selector == "$":
        if not isinstance(value, dict):
            raise ProjectionError(
                "root projection must produce object"
            )
        target.clear()
        target.update(
            deepcopy(value)
        )
        return
    path = selector.removeprefix("$.")
    if "[?" in path or "[*]" in path:
        collection = path.split("[", 1)[0]
        existing = target.get(
            collection
        )
        if existing is None:
            target[collection] = deepcopy(
                value
            )
            return
        if isinstance(
            existing,
            list,
        ) and isinstance(
            value,
            list,
        ):
            target[collection] = (
                _merge_projected_lists(
                    existing,
                    value,
                )
            )
            return
        raise ProjectionError(
            f"incompatible selector projection collision at {collection}"
        )
    parts = path.split(".")
    cursor = target
    for part in parts[:-1]:
        existing = cursor.get(part)
        if existing is None:
            cursor[part] = {}
        elif not isinstance(
            existing,
            dict,
        ):
            raise ProjectionError(
                f"projection collision at {part}"
            )
        cursor = cursor[part]
    leaf = parts[-1]
    if leaf in cursor:
        if cursor[leaf] != value:
            raise ProjectionError(
                f"projection collision at {path}"
            )
        return
    cursor[leaf] = deepcopy(value)
def _merge_projected_lists(
    existing: list[Any],
    incoming: list[Any],
) -> list[Any]:
    result = deepcopy(existing)
    for item in incoming:
        if item not in result:
            result.append(
                deepcopy(item)
            )
    return result
