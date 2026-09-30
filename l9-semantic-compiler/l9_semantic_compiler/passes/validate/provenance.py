from __future__ import annotations
from dataclasses import dataclass
from typing import Mapping, Sequence
from .models import ValidationEvidence
@dataclass(frozen=True)
class ProvenanceHit:
    semantic_ref: str
    source_ref: str
    source_digest: str | None
    revision: str | None
def resolve_failure_provenance(
    *,
    evidence: Sequence[ValidationEvidence],
    provenance_index: Mapping[
        str,
        Mapping[str, str],
    ],
) -> tuple[ProvenanceHit, ...]:
    refs: list[str] = []
    for item in evidence:
        refs.extend(item.refs)
    hits: list[ProvenanceHit] = []
    for ref in refs:
        source = provenance_index.get(ref)
        if source is None:
            continue
        hits.append(
            ProvenanceHit(
                semantic_ref=ref,
                source_ref=source["source_ref"],
                source_digest=source.get("source_digest"),
                revision=source.get("revision"),
            )
        )
    return tuple(hits)
