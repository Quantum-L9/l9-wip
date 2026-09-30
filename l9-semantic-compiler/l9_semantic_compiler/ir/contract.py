from __future__ import annotations
from dataclasses import dataclass, field
from typing import Any, Mapping
@dataclass(frozen=True)
class ContractFieldIR:
    name: str
    type_ref: str | None = None
    required: bool = False
    description: str | None = None
    enum: tuple[Any, ...] = ()
    items_type_ref: str | None = None
    additional: Mapping[str, Any] = field(default_factory=dict)
@dataclass(frozen=True)
class ContractMessageIR:
    name: str
    fields: tuple[ContractFieldIR, ...]
@dataclass(frozen=True)
class ContractIR:
    contract_id: str
    schema: str
    inputs: ContractMessageIR | None
    outputs: ContractMessageIR | None
    receipt: ContractMessageIR | None
    failure_states: tuple[str, ...]
    raw: Mapping[str, Any]
    source_digest: str
