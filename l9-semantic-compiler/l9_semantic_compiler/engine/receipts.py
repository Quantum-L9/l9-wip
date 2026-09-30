from __future__ import annotations
from .models import (
    ComposedProjectionArtifact,
    CompilerReceipt,
    ProjectionArtifact,
)
def build_projection_receipt(
    *,
    artifact: ProjectionArtifact,
) -> CompilerReceipt:
    return CompilerReceipt(
        schema="l9.compiler-receipt/v1",
        operation="projection",
        inputs=tuple(
            {
                "ref": source.source_ref,
                "digest": source.digest,
            }
            for source in artifact.sources
        ),
        profile_ref=artifact.profile_ref,
        profile_digest=artifact.profile_digest,
        output_ref=(
            f"projection:{artifact.profile_ref}"
        ),
        output_digest=(
            artifact.projection_digest
        ),
        result="pass",
        diagnostics=(),
    )
def build_composition_receipt(
    *,
    artifact: ComposedProjectionArtifact,
) -> CompilerReceipt:
    return CompilerReceipt(
        schema="l9.compiler-receipt/v1",
        operation="composition",
        inputs=tuple(
            {
                "ref": (
                    component.profile_ref
                ),
                "digest": (
                    component.projection_digest
                ),
            }
            for component in artifact.components
        ),
        profile_ref=(
            artifact.composition_profile_ref
        ),
        profile_digest=(
            artifact.composition_profile_digest
        ),
        output_ref=(
            "composed-projection:"
            + artifact.composition_profile_ref
        ),
        output_digest=(
            artifact.composition_digest
        ),
        result="pass",
        diagnostics=(),
    )
