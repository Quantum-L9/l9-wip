from __future__ import annotations
from .solvers.base import MechanicalSolver
class SolverRegistry:
    def __init__(self) -> None:
        self._solvers: dict[str, MechanicalSolver] = {}
    def register(
        self,
        solver: MechanicalSolver,
    ) -> None:
        ref = solver.identity.ref
        if ref in self._solvers:
            raise ValueError(
                f"solver already registered: {ref}"
            )
        self._solvers[ref] = solver
    def resolve(
        self,
        solver_ref: str,
    ) -> MechanicalSolver:
        try:
            return self._solvers[solver_ref]
        except KeyError as exc:
            raise KeyError(
                f"solver not registered: {solver_ref}"
            ) from exc
    def contains(
        self,
        solver_ref: str,
    ) -> bool:
        return solver_ref in self._solvers
