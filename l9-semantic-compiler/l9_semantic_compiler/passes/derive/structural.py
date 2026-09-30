from __future__ import annotations
from l9_semantic_compiler.ir.contract import (
    ContractFieldIR,
    ContractIR,
    ContractMessageIR,
)
from l9_semantic_compiler.ir.structural import (
    StructuralFieldIR,
    StructuralMessageIR,
    StructuralRequirementsIR,
)
DEFAULT_TYPE = "any"
def derive_structural_requirements(
    contract: ContractIR,
) -> StructuralRequirementsIR:
    messages: list[
        StructuralMessageIR
    ] = []
    if contract.inputs is not None:
        messages.append(
            _derive_message(
                contract.inputs
            )
        )
    if contract.outputs is not None:
        messages.append(
            _derive_message(
                contract.outputs
            )
        )
    if contract.receipt is not None:
        messages.append(
            _derive_message(
                contract.receipt
            )
        )
    return StructuralRequirementsIR(
        source_contract_id=(
            contract.contract_id
        ),
        source_digest=(
            contract.source_digest
        ),
        messages=tuple(messages),
    )
def _derive_message(
    message: ContractMessageIR,
) -> StructuralMessageIR:
    return StructuralMessageIR(
        name=message.name,
        fields=tuple(
            _derive_field(field)
            for field in message.fields
        ),
    )
def _derive_field(
    field: ContractFieldIR,
) -> StructuralFieldIR:
    semantic_type = (
        field.type_ref
        or DEFAULT_TYPE
    )
    return StructuralFieldIR(
        name=field.name,
        semantic_type=semantic_type,
        required=field.required,
        description=field.description,
        enum=field.enum,
        item_semantic_type=(
            field.items_type_ref
        ),
    )
