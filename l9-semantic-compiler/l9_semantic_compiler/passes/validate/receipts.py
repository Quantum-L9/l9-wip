from __future__ import annotations
from dataclasses import asdict
from typing import Any
from l9_semantic_compiler.engine.canonical import (
    semantic_digest,
)
from .models import ValidationRequest, ValidationResult
def build_validation_receipt(
    *,
    request: ValidationRequest,
    result: ValidationResult,
) -> dict[str, Any]:
    payload = {
        "schema": "l9.validation-receipt/v1",
        "candidate": {
            "ref": request.candidate_ref,
            "digest": request.candidate_digest,
        },
        "stage": request.stage,
        "compilation_profile": {
            "ref": request.compilation_profile_ref,
            "digest": request.compilation_profile_digest,
        },
        "solver": {
            "ref": request.solver_projection.solver_ref,
            "version": request.solver_projection.solver_version,
            "profile_digest": (
                request.solver_projection.solver_profile_digest
            ),
        },
        "constraints": list(
            request.applicable_constraints
        ),
        "result": result.status.value,
        "evidence": [
            asdict(item)
            for item in result.evidence
        ],
        "diagnostics": list(result.diagnostics),
    }
    return {
        **payload,
        "receipt_digest": semantic_digest(payload),
    }
