from __future__ import annotations
from dataclasses import dataclass
from typing import Any, Mapping, Sequence
JsonObject = Mapping[str, Any]
@dataclass(frozen=True)
class CanonicalArtifact:
    source_class: str
    source_ref: str
    artifact_id: str | None
    payload: JsonObject
    digest: str
    def to_dict(self) -> dict[str, Any]:
        return {
            "source_class": self.source_class,
            "source_ref": self.source_ref,
            "artifact_id": self.artifact_id,
            "digest": self.digest,
            "payload": dict(self.payload),
        }
@dataclass(frozen=True)
class ProjectionSource:
    source_class: str
    source_ref: str
    artifact_id: str | None
    digest: str
    def to_dict(self) -> dict[str, Any]:
        return {
            "source_class": self.source_class,
            "source_ref": self.source_ref,
            "artifact_id": self.artifact_id,
            "digest": self.digest,
        }
@dataclass(frozen=True)
class ProjectionProfile:
    profile_id: str
    profile_class: str
    consumer: str
    purpose: str
    sources: Mapping[str, Mapping[str, Any]]
    output: Mapping[str, Any]
    forbidden: tuple[str, ...]
    digest: str
    raw: JsonObject
    def to_dict(self) -> dict[str, Any]:
        return dict(self.raw)
@dataclass(frozen=True)
class ProjectionArtifact:
    schema: str
    authority_class: str
    profile_ref: str
    profile_digest: str
    consumer: str
    sources: tuple[ProjectionSource, ...]
    payload: JsonObject
    projection_digest: str
    def to_dict(self) -> dict[str, Any]:
        return {
            "schema": self.schema,
            "authority_class": self.authority_class,
            "projection_profile": {
                "ref": self.profile_ref,
                "digest": self.profile_digest,
            },
            "consumer": self.consumer,
            "sources": [
                source.to_dict()
                for source in self.sources
            ],
            "payload": dict(self.payload),
            "projection_digest": self.projection_digest,
        }
@dataclass(frozen=True)
class CompositionProfile:
    profile_id: str
    purpose: str
    merge_strategy: Mapping[str, str]
    conflict_result: str
    digest: str
    raw: JsonObject
@dataclass(frozen=True)
class ComposedProjectionArtifact:
    schema: str
    authority_class: str
    composition_profile_ref: str
    composition_profile_digest: str
    components: tuple[ProjectionArtifact, ...]
    payload: JsonObject
    composition_digest: str
    def to_dict(self) -> dict[str, Any]:
        return {
            "schema": self.schema,
            "authority_class": self.authority_class,
            "composition_profile": {
                "ref": self.composition_profile_ref,
                "digest": self.composition_profile_digest,
            },
            "components": [
                {
                    "projection_ref": component.profile_ref,
                    "projection_digest": component.projection_digest,
                }
                for component in self.components
            ],
            "payload": dict(self.payload),
            "composition_digest": self.composition_digest,
        }
@dataclass(frozen=True)
class CompilerReceipt:
    schema: str
    operation: str
    inputs: tuple[Mapping[str, str], ...]
    profile_ref: str
    profile_digest: str
    output_ref: str
    output_digest: str
    result: str
    diagnostics: tuple[str, ...]
    def to_dict(self) -> dict[str, Any]:
        return {
            "schema": self.schema,
            "operation": self.operation,
            "inputs": [
                dict(value)
                for value in self.inputs
            ],
            "profile": {
                "ref": self.profile_ref,
                "digest": self.profile_digest,
            },
            "output": {
                "ref": self.output_ref,
                "digest": self.output_digest,
            },
            "result": self.result,
            "diagnostics": list(self.diagnostics),
        }
@dataclass(frozen=True)
class ProjectionCompilation:
    artifact: ProjectionArtifact
    receipt: CompilerReceipt
@dataclass(frozen=True)
class CompositionCompilation:
    artifact: ComposedProjectionArtifact
    receipt: CompilerReceipt
