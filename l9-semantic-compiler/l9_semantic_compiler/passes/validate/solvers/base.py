from __future__ import annotations
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any, Mapping
from ..models import ValidationRequest, ValidationResult
@dataclass(frozen=True)
class SolverIdentity:
    ref: str
    version: str
    solver_class: str
class MechanicalSolver(ABC):
    identity: SolverIdentity
    @abstractmethod
    def validate(
        self,
        request: ValidationRequest,
    ) -> ValidationResult:
        raise NotImplementedError
    def supports(
        self,
        *,
        parameters: Mapping[str, Any],
    ) -> bool:
        return True
