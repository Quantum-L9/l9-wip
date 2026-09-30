from __future__ import annotations
from dataclasses import dataclass
from typing import Any
@dataclass(frozen=True)
class StructuralFieldIR:
    name: str
    semantic_type: str
    required: bool
    description: str | None = None
    enum: tuple[Any, ...] = ()
    item_semantic_type: str | None = None
@dataclass(frozen=True)
class StructuralMessageIR:
    name: str
    fields: tuple[StructuralFieldIR, ...]
@dataclass(frozen=True)
class StructuralRequirementsIR:
    source_contract_id: str
    source_digest: str
    messages: tuple[StructuralMessageIR, ...]
