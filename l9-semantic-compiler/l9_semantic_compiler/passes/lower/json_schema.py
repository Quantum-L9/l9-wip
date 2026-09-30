from __future__ import annotations
from copy import deepcopy
from l9_semantic_compiler.ir.json_schema import (
    JsonSchemaDocumentIR,
    JsonSchemaPropertyIR,
)
from l9_semantic_compiler.ir.structural import (
    StructuralFieldIR,
    StructuralMessageIR,
    StructuralRequirementsIR,
)
from l9_semantic_compiler.passes.bind.json_schema import (
    JsonSchemaBinding,
)
def lower_structural_to_json_schema(
    *,
    structural: StructuralRequirementsIR,
    binding: JsonSchemaBinding,
) -> tuple[JsonSchemaDocumentIR, ...]:
    return tuple(
        _lower_message(
            structural=structural,
            message=message,
            binding=binding,
        )
        for message in structural.messages
    )
def _lower_message(
    *,
    structural: StructuralRequirementsIR,
    message: StructuralMessageIR,
    binding: JsonSchemaBinding,
) -> JsonSchemaDocumentIR:
    properties = tuple(
        JsonSchemaPropertyIR(
            name=field.name,
            schema=_lower_field(
                field,
                binding=binding,
            ),
        )
        for field in message.fields
    )
    required = tuple(
        field.name
        for field in message.fields
        if field.required
    )
    safe_contract_id = (
        structural.source_contract_id
        .replace("/", ".")
        .replace("@", ".")
    )
    schema_id = (
        f"urn:l9:schema:"
        f"{safe_contract_id}:"
        f"{message.name}:v1"
    )
    title = (
        f"{structural.source_contract_id} "
        f"{message.name}"
    )
    return JsonSchemaDocumentIR(
        schema_uri=binding.schema_uri,
        schema_id=schema_id,
        title=title,
        type="object",
        properties=properties,
        required=required,
        additional_properties=False,
        metadata={
            "source_contract": (
                structural.source_contract_id
            ),
            "source_digest": (
                structural.source_digest
            ),
            "binding": binding.binding_id,
            "message": message.name,
        },
    )
def _lower_field(
    field: StructuralFieldIR,
    *,
    binding: JsonSchemaBinding,
) -> dict:
    try:
        schema = deepcopy(
            binding.semantic_type_map[
                field.semantic_type
            ]
        )
    except KeyError as exc:
        raise ValueError(
            "no JSON Schema mapping for semantic type "
            f"{field.semantic_type!r}"
        ) from exc
    if field.description:
        schema["description"] = (
            field.description
        )
    if field.enum:
        schema["enum"] = list(
            field.enum
        )
    if field.semantic_type == "array":
        if field.item_semantic_type:
            try:
                item_schema = deepcopy(
                    binding.semantic_type_map[
                        field.item_semantic_type
                    ]
                )
            except KeyError as exc:
                raise ValueError(
                    "no JSON Schema mapping for item type "
                    f"{field.item_semantic_type!r}"
                ) from exc
            schema["items"] = item_schema
    return schema
