from __future__ import annotations
import json
from pathlib import Path
from typing import Iterable
from l9_semantic_compiler.ir.json_schema import (
    JsonSchemaDocumentIR,
)
def render_json_schema(
    schema_ir: JsonSchemaDocumentIR,
) -> str:
    return (
        json.dumps(
            schema_ir.to_dict(),
            ensure_ascii=False,
            indent=2,
            sort_keys=True,
        )
        + "\n"
    )
def render_json_schema_documents(
    *,
    documents: Iterable[
        JsonSchemaDocumentIR
    ],
    output_dir: str | Path,
    filename_prefix: str,
) -> tuple[Path, ...]:
    root = Path(output_dir)
    root.mkdir(
        parents=True,
        exist_ok=True,
    )
    emitted: list[Path] = []
    for document in documents:
        message = str(
            document.metadata["message"]
        )
        path = root / (
            f"{filename_prefix}-"
            f"{message}.schema.json"
        )
        path.write_text(
            render_json_schema(
                document
            ),
            encoding="utf-8",
        )
        emitted.append(path)
    return tuple(emitted)
