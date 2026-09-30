from __future__ import annotations
import json
from pathlib import Path
from typing import Any, Mapping
import yaml
from .canonical import semantic_digest
from .errors import SourceResolutionError
from .models import CanonicalArtifact
def load_document(
    path: str | Path,
) -> dict[str, Any]:
    source_path = Path(path)
    if not source_path.exists():
        raise SourceResolutionError(
            f"source does not exist: {source_path}"
        )
    suffix = source_path.suffix.lower()
    try:
        raw = source_path.read_text(
            encoding="utf-8"
        )
        if suffix in {".yaml", ".yml"}:
            payload = yaml.safe_load(raw)
        elif suffix == ".json":
            payload = json.loads(raw)
        else:
            raise SourceResolutionError(
                f"unsupported source format: {suffix}"
            )
    except (
        OSError,
        json.JSONDecodeError,
        yaml.YAMLError,
    ) as exc:
        raise SourceResolutionError(
            f"failed loading {source_path}: {exc}"
        ) from exc
    if not isinstance(payload, Mapping):
        raise SourceResolutionError(
            f"canonical source must contain an object: {source_path}"
        )
    return dict(payload)
def load_canonical_artifact(
    *,
    path: str | Path,
    source_class: str,
) -> CanonicalArtifact:
    payload = load_document(path)
    artifact_id = payload.get("artifact_id")
    if artifact_id is not None:
        artifact_id = str(artifact_id)
    return CanonicalArtifact(
        source_class=source_class,
        source_ref=str(Path(path)),
        artifact_id=artifact_id,
        payload=payload,
        digest=semantic_digest(payload),
    )
