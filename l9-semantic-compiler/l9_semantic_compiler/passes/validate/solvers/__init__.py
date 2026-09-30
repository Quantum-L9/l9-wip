from .conformance import ConformanceSolver
from .fixture_derivation import FixtureDerivationSolver
from .graph import GraphSolver
from .predicate import PredicateSolver
from .satisfiability import SatisfiabilitySolver
from .schema import SchemaSolver
from .semantic_preservation import SemanticPreservationSolver
from .set_compatibility import SetCompatibilitySolver
from .structural import StructuralSolver
__all__ = [
    "ConformanceSolver",
    "FixtureDerivationSolver",
    "GraphSolver",
    "PredicateSolver",
    "SatisfiabilitySolver",
    "SchemaSolver",
    "SemanticPreservationSolver",
    "SetCompatibilitySolver",
    "StructuralSolver",
]
def register_builtin_solvers(registry) -> None:
    for solver in (
        StructuralSolver(),
        SchemaSolver(),
        PredicateSolver(),
        SetCompatibilitySolver(),
        GraphSolver(),
        SatisfiabilitySolver(),
        FixtureDerivationSolver(),
        ConformanceSolver(),
        SemanticPreservationSolver(),
    ):
        registry.register(solver)
