from __future__ import annotations
from collections.abc import Mapping
from ..evidence import invalidity, violated_constraints
from ..models import ValidationRequest, ValidationResult
from ..result import ValidationStatus
from .base import MechanicalSolver, SolverIdentity
class FixtureDerivationSolver(MechanicalSolver):
    identity = SolverIdentity(
        ref="l9.solver/fixture-derivation@1",
        version="1",
        solver_class="fixture_derivation",
    )
    def validate(
        self,
        request: ValidationRequest,
    ) -> ValidationResult:
        candidate = request.candidate
        if not isinstance(candidate, Mapping):
            return ValidationResult(
                status=ValidationStatus.INVALID,
                evidence=(
                    invalidity(
                        "fixture candidate must be mapping"
                    ),
                ),
            )
        required = {
            "derived_from",
            "given",
            "expect",
        }
        missing = required - set(
            candidate.keys()
        )
        if missing:
            return ValidationResult(
                status=ValidationStatus.FAIL,
                evidence=(
                    violated_constraints(
                        tuple(sorted(missing)),
                        details={
                            "missing_fixture_fields": sorted(
                                missing
                            )
                        },
                    ),
                ),
            )
        if not candidate["derived_from"]:
            return ValidationResult(
                status=ValidationStatus.FAIL,
                evidence=(
                    violated_constraints(
                        ("fixture_requires_source_law",)
                    ),
                ),
            )
        return ValidationResult(
            status=ValidationStatus.PASS
        )
