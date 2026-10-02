import pytest

from l9_state.errors import StateInfrastructureFailure
from l9_state.execution import ExecutionBudget, ExecutionBudgetPolicy


class MonotonicClock:
    def __init__(self) -> None:
        self.value = 100.0

    def __call__(self) -> float:
        return self.value

    def advance_ms(self, value: int) -> None:
        self.value += value / 1000.0


def test_execution_budget_preserves_reconciliation_and_return_reserves():
    clock = MonotonicClock()
    policy = ExecutionBudgetPolicy(
        reconciliation_reserve_ms=500,
        return_reserve_ms=100,
        min_mutation_start_ms=50,
        reconciliation_poll_ms=25,
    )
    budget = ExecutionBudget.start(2_000, policy=policy, clock=clock)
    assert budget.mutation_remaining_ms() == 1_400
    assert budget.reconciliation_remaining_ms() == 1_900
    clock.advance_ms(1_351)
    assert not budget.can_start_mutation()
    assert budget.reconciliation_remaining_ms() == 549


def test_exhausted_mutation_budget_is_definite_deadline_problem():
    clock = MonotonicClock()
    budget = ExecutionBudget.start(700, clock=clock)
    clock.advance_ms(60)
    with pytest.raises(StateInfrastructureFailure) as exc:
        budget.require_mutation_start(operation_id="op.1", scope_ref="scope.1")
    assert exc.value.code == "DEADLINE_EXCEEDED"
