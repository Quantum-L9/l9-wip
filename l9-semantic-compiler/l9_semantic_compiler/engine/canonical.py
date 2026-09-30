from __future__ import annotations
import hashlib
import json
from dataclasses import asdict, is_dataclass
from enum import Enum
from typing import Any, Mapping
from .errors import CanonicalizationError
def to_primitive(value: Any) -> Any:
    if isinstance(value, Enum):
        return value.value
    if is_dataclass(value):
        return {
            key: to_primitive(item)
            for key, item in asdict(value).items()
        }
    if isinstance(value, Mapping):
        return {
            str(key): to_primitive(item)
            for key, item in value.items()
        }
    if isinstance(value, tuple):
        return [
            to_primitive(item)
            for item in value
        ]
    if isinstance(value, list):
        return [
            to_primitive(item)
            for item in value
        ]
    if value is None or isinstance(
        value,
        (str, int, float, bool),
    ):
        return value
    raise CanonicalizationError(
        f"unsupported canonical value type: {type(value).__name__}"
    )
def canonical_json(value: Any) -> str:
    primitive = to_primitive(value)
    return json.dumps(
        primitive,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
        allow_nan=False,
    )
def semantic_digest(value: Any) -> str:
    encoded = canonical_json(value).encode("utf-8")
    return (
        "sha256:"
        + hashlib.sha256(encoded).hexdigest()
    )
