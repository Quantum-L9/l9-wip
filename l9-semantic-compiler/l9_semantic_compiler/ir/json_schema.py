from __future__ import annotations
from dataclasses import dataclass, field
from typing import Any, Mapping
@dataclass(frozen=True)
class JsonSchemaPropertyIR:
    name: str
    schema: Mapping[str, Any]
@dataclass(frozen=True)
class JsonSchemaDocumentIR:
    schema_uri: str
    schema_id: str
    title: str
    type: str
    properties: tuple[JsonSchemaPropertyIR, ...]
    required: tuple[str, ...]
    additional_properties: bool = False
    metadata: Mapping[str, Any] = field(default_factory=dict)
    def to_dict(self) -> dict[str, Any]:
        result = {
            "$schema": self.schema_uri,
            "$id": self.schema_id,
            "title": self.title,
            "type": self.type,
            "properties": {
                prop.name: dict(prop.schema)
                for prop in self.properties
            },
            "additionalProperties": self.additional_properties,
        }
        if self.required:
            result["required"] = list(self.required)
        if self.metadata:
            result["x-l9"] = dict(self.metadata)
        return result
