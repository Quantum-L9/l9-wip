from __future__ import annotations
from typing import Any, Mapping
from l9_semantic_compiler.engine.canonical import semantic_digest
from l9_semantic_compiler.ir.contract import (
    ContractFieldIR,
    ContractIR,
    ContractMessageIR,
)
def normalize_contract(
    document: Mapping[str, Any],
) -> ContractIR:
    contract_id = str(
        document["contract_id"]
    )
    schema = str(
        document["schema"]
    )
    inputs = _normalize_message(
        "request",
        document.get("inputs"),
    )
    outputs = _normalize_message(
        "result",
        document.get("outputs"),
    )
    receipt = _normalize_receipt(
        document.get("receipt"),
    )
    failure_states = _normalize_failure_states(
        document.get("failure_states"),
    )
    return ContractIR(
        contract_id=contract_id,
        schema=schema,
        inputs=inputs,
        outputs=outputs,
        receipt=receipt,
        failure_states=failure_states,
        raw=dict(document),
        source_digest=semantic_digest(document),
    )
def _normalize_message(
    name: str,
    raw: Any,
) -> ContractMessageIR | None:
    if raw is None:
        return None
    if not isinstance(raw, Mapping):
        raise ValueError(
            f"{name} contract section must be an object"
        )
    required_names = tuple(
        str(value)
        for value in raw.get(
            "required",
            [],
        )
    )
    field_defs = raw.get(
        "fields",
        {},
    )
    fields: list[ContractFieldIR] = []
    if isinstance(field_defs, Mapping):
        for field_name, definition in field_defs.items():
            fields.append(
                _normalize_field(
                    name=str(field_name),
                    definition=definition,
                    required=(
                        str(field_name)
                        in required_names
                    ),
                )
            )
    for required_name in required_names:
        if not any(
            field.name == required_name
            for field in fields
        ):
            fields.append(
                ContractFieldIR(
                    name=required_name,
                    required=True,
                )
            )
    return ContractMessageIR(
        name=name,
        fields=tuple(fields),
    )
def _normalize_receipt(
    raw: Any,
) -> ContractMessageIR | None:
    if raw is None:
        return None
    if not isinstance(raw, Mapping):
        raise ValueError(
            "receipt contract section must be an object"
        )
    required_names = tuple(
        str(value)
        for value in raw.get(
            "required",
            [],
        )
    )
    fields = tuple(
        ContractFieldIR(
            name=name,
            required=True,
        )
        for name in required_names
    )
    return ContractMessageIR(
        name="receipt",
        fields=fields,
    )
def _normalize_field(
    *,
    name: str,
    definition: Any,
    required: bool,
) -> ContractFieldIR:
    if definition is None:
        return ContractFieldIR(
            name=name,
            required=required,
        )
    if isinstance(definition, str):
        return ContractFieldIR(
            name=name,
            type_ref=definition,
            required=required,
        )
    if not isinstance(definition, Mapping):
        raise ValueError(
            f"invalid field definition for {name}"
        )
    enum_raw = definition.get(
        "enum",
        [],
    )
    enum = (
        tuple(enum_raw)
        if isinstance(enum_raw, list)
        else ()
    )
    additional = {
        key: value
        for key, value in definition.items()
        if key not in {
            "type",
            "description",
            "enum",
            "items_type",
        }
    }
    return ContractFieldIR(
        name=name,
        type_ref=(
            str(definition["type"])
            if definition.get("type")
            else None
        ),
        required=required,
        description=(
            str(definition["description"])
            if definition.get("description")
            else None
        ),
        enum=enum,
        items_type_ref=(
            str(definition["items_type"])
            if definition.get("items_type")
            else None
        ),
        additional=additional,
    )
def _normalize_failure_states(
    raw: Any,
) -> tuple[str, ...]:
    if raw is None:
        return ()
    if isinstance(raw, list):
        return tuple(
            str(value)
            for value in raw
        )
    if isinstance(raw, Mapping):
        return tuple(
            str(key)
            for key in raw.keys()
        )
    raise ValueError(
        "failure_states must be an array or object"
    )
