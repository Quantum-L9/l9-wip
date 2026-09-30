from __future__ import annotations
from collections import defaultdict
from typing import Mapping
from ..evidence import invalidity, violated_constraints
from ..models import ValidationRequest, ValidationResult
from ..result import ValidationStatus
from .base import MechanicalSolver, SolverIdentity
class GraphSolver(MechanicalSolver):
    identity = SolverIdentity(
        ref="l9.solver/graph@1",
        version="1",
        solver_class="graph",
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
                        "graph solver requires mapping candidate"
                    ),
                ),
            )
        edges = candidate.get("edges", [])
        graph: dict[str, list[str]] = defaultdict(list)
        for edge in edges:
            if not isinstance(edge, Mapping):
                continue
            source = edge.get("from")
            target = edge.get("to")
            if isinstance(source, str) and isinstance(target, str):
                graph[source].append(target)
        if _has_cycle(graph):
            return ValidationResult(
                status=ValidationStatus.FAIL,
                evidence=(
                    violated_constraints(
                        ("graph_must_be_acyclic",)
                    ),
                ),
            )
        return ValidationResult(
            status=ValidationStatus.PASS
        )
def _has_cycle(
    graph: Mapping[str, list[str]],
) -> bool:
    visiting: set[str] = set()
    visited: set[str] = set()
    def visit(node: str) -> bool:
        if node in visiting:
            return True
        if node in visited:
            return False
        visiting.add(node)
        for child in graph.get(node, []):
            if visit(child):
                return True
        visiting.remove(node)
        visited.add(node)
        return False
    return any(
        visit(node)
        for node in graph
        if node not in visited
    )
