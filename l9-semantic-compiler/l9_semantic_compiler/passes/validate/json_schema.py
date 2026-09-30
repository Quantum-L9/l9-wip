from __future__ import annotations
from dataclasses import dataclass
from typing import Iterable
from l9_semantic_compiler.engine.canonical import (
    semantic_digest,
)
from l9_semantic_compiler.ir.json_schema import (
    JsonSchemaDocumentIR,
)
@dataclass(frozen=True)
class JsonSchemaValidationResult:
    result: str
    document_digest: str
    diagnostics: tuple[str, ...]
def validate_json_schema_ir(
    document: JsonSchemaDocumentIR,
) -> JsonSchemaValidationResult:
    diagnostics: list[str] = []
    payload = document.to_dict()
    if payload.get("type") != "object":
        diagnostics.append(
            "root JSON Schema type must be object"
        )
    if "$schema" not in payload:
        diagnostics.append(
            "$schema is required"
        )
    if "$id" not in payload:
        diagnostics.append(
            "$id is required"
        )
    properties = payload.get(
        "properties"
    )
    if not isinstance(
        properties,
        dict,
    ):
        diagnostics.append(
            "properties must be an object"
        )
    required = payload.get(
        "required",
        [],
    )
    if not isinstance(
        required,
        list,
    ):
        diagnostics.append(
            "required must be an array"
        )
    elif isinstance(
        properties,
        dict,
    ):
        for field in required:
            if field not in properties:
                diagnostics.append(
                    f"required field {field!r} "
                    "has no property definition"
                )
    return JsonSchemaValidationResult(
        result=(
            "PASS"
            if not diagnostics
            else "FAIL"
        ),
        document_digest=(
            semantic_digest(payload)
        ),
        diagnostics=tuple(
            diagnostics
        ),
    )
def validate_all_json_schema_ir(
    documents: Iterable[
        JsonSchemaDocumentIR
    ],
) -> tuple[
    JsonSchemaValidationResult,
    ...,
]:
    return tuple(
        validate_json_schema_ir(
            document
        )
        for document in documents
    )
