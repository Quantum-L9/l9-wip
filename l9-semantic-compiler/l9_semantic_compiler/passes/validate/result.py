from enum import StrEnum
class ValidationStatus(StrEnum):
    PASS = "PASS"
    FAIL = "FAIL"
    UNSAT = "UNSAT"
    INVALID = "INVALID"
    UNKNOWN = "UNKNOWN"
