from __future__ import annotations
from dataclasses import dataclass
from pathlib import Path
from l9_semantic_compiler.engine.canonical import (
    semantic_digest,
)
from l9_semantic_compiler.engine.loader import (
    load_document,
)
from l9_semantic_compiler.ir.contract import (
    ContractIR,
)
from l9_semantic_compiler.ir.json_schema import (
    JsonSchemaDocumentIR,
)
from l9_semantic_compiler.ir.structural import (
    StructuralRequirementsIR,
)
from l9_semantic_compiler.normalize.contract import (
    normalize_contract,
)
from l9_semantic_compiler.passes.bind.json_schema import (
    DEFAULT_JSON_SCHEMA_BINDING,
    JsonSchemaBinding,
)
from l9_semantic_compiler.passes.derive.structural import (
    derive_structural_requirements,
)
from l9_semantic_compiler.passes.lower.json_schema import (
    lower_structural_to_json_schema,
)
from l9_semantic_compiler.passes.render.json_schema import (
    render_json_schema_documents,
)
from l9_semantic_compiler.passes.validate.json_schema import (
    JsonSchemaValidationResult,
    validate_all_json_schema_ir,
)
@dataclass(frozen=True)
class ContractToJsonSchemaCompilation:
    contract_ir: ContractIR
    structural_ir: StructuralRequirementsIR
    json_schema_ir: tuple[
        JsonSchemaDocumentIR,
        ...,
    ]
    validation_results: tuple[
        JsonSchemaValidationResult,
        ...,
    ]
    emitted_files: tuple[Path, ...]
    compilation_digest: str
def compile_contract_to_json_schema(
    *,
    contract_path: str | Path,
    output_dir: str | Path,
    binding: JsonSchemaBinding = (
        DEFAULT_JSON_SCHEMA_BINDING
    ),
) -> ContractToJsonSchemaCompilation:
    document = load_document(
        contract_path
    )
    contract_ir = normalize_contract(
        document
    )
    structural_ir = (
        derive_structural_requirements(
            contract_ir
        )
    )
    schema_ir = (
        lower_structural_to_json_schema(
            structural=structural_ir,
            binding=binding,
        )
    )
    validation_results = (
        validate_all_json_schema_ir(
            schema_ir
        )
    )
    failures = tuple(
        result
        for result in validation_results
        if result.result != "PASS"
    )
    if failures:
        details = "; ".join(
            diagnostic
            for failure in failures
            for diagnostic in failure.diagnostics
        )
        raise ValueError(
            "JSON Schema IR validation failed: "
            + details
        )
    contract_name = (
        contract_ir.contract_id
        .split("/")[-1]
        .split("@")[0]
        .replace(".", "-")
        .replace("_", "-")
    )
    emitted = (
        render_json_schema_documents(
            documents=schema_ir,
            output_dir=output_dir,
            filename_prefix=contract_name,
        )
    )
    compilation_digest = (
        semantic_digest(
            {
                "contract_digest": (
                    contract_ir.source_digest
                ),
                "binding": (
                    binding.binding_id
                ),
                "schemas": [
                    result.document_digest
                    for result
                    in validation_results
                ],
            }
        )
    )
    return ContractToJsonSchemaCompilation(
        contract_ir=contract_ir,
        structural_ir=structural_ir,
        json_schema_ir=schema_ir,
        validation_results=(
            validation_results
        ),
        emitted_files=emitted,
        compilation_digest=(
            compilation_digest
        ),
    )
