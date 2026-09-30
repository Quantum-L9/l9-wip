class SemanticCompilerError(Exception):
    """Base error for the generic semantic compiler."""
class CanonicalizationError(SemanticCompilerError):
    pass
class SourceResolutionError(SemanticCompilerError):
    pass
class ProfileResolutionError(SemanticCompilerError):
    pass
class SelectorError(SemanticCompilerError):
    pass
class ProjectionError(SemanticCompilerError):
    pass
class CompositionError(SemanticCompilerError):
    pass
class SemanticConflictError(CompositionError):
    pass
class ValidationError(SemanticCompilerError):
    pass
class StaleArtifactError(SemanticCompilerError):
    pass
