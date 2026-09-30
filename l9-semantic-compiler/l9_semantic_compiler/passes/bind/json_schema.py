from __future__ import annotations
from dataclasses import dataclass
from typing import Mapping
@dataclass(frozen=True)
class JsonSchemaBinding:
    binding_id: str
    schema_uri: str
    semantic_type_map: Mapping[str, dict]
DEFAULT_JSON_SCHEMA_BINDING = JsonSchemaBinding(
    binding_id="l9.binding/json-schema-2020-12@1",
    schema_uri=(
        "https://json-schema.org/draft/2020-12/schema"
    ),
    semantic_type_map={
        "string": {
            "type": "string",
        },
        "integer": {
            "type": "integer",
        },
        "number": {
            "type": "number",
        },
        "boolean": {
            "type": "boolean",
        },
        "object": {
            "type": "object",
        },
        "array": {
            "type": "array",
        },
        "semantic_digest": {
            "type": "string",
            "pattern": "^sha256:[0-9a-f]{64}$",
        },
        "reference": {
            "type": "string",
            "minLength": 1,
        },
        "any": {},
    },
)
def resolve_json_schema_binding(
    binding_id: str,
) -> JsonSchemaBinding:
    if (
        binding_id
        != DEFAULT_JSON_SCHEMA_BINDING.binding_id
    ):
        raise ValueError(
            f"unknown JSON Schema binding: {binding_id}"
        )
    return DEFAULT_JSON_SCHEMA_BINDING
