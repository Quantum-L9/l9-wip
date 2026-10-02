from pathlib import Path

from l9_state.adapters.mongodb_contract import (
    COLLECTIONS,
    REQUIRED_INDEXES,
    acquire_claim_filter,
    acquire_claim_pipeline,
    claimless_transition_guard_filter,
    exact_claim_filter,
    exact_claim_fence_filter,
    renew_claim_pipeline,
    transition_guard_pipeline,
)


def test_required_mongodb_collections_and_unique_indexes_are_explicit():
    assert set(COLLECTIONS.values()) == {
        "state_objects",
        "state_revisions",
        "state_operations",
        "state_events",
        "state_claims",
        "state_consumer_cursors",
        "state_scope_counters",
    }
    names = {entry[3] for entry in REQUIRED_INDEXES}
    assert names == {
        "uq_state_key",
        "uq_state_revision",
        "uq_state_operation",
        "uq_scope_journal_seq",
        "uq_event_id",
        "uq_state_claim_lineage",
        "uq_consumer_cursor",
        "uq_scope_counter",
    }
    assert all(unique for _collection, _fields, unique, _name in REQUIRED_INDEXES)


def test_claim_predicates_use_server_authoritative_now():
    acquire = acquire_claim_filter("tenant", "scope", "object")
    claimless = claimless_transition_guard_filter("tenant", "scope", "object")
    exact = exact_claim_filter(
        "tenant", "scope", "object", claim_id="claim.1", fencing_token=4, holder_ref="agent"
    )
    assert "$$NOW" in repr(acquire)
    assert "$$NOW" in repr(claimless)
    assert "$$NOW" in repr(exact)

    acquire_update = acquire_claim_pipeline(claim_id="claim.1", holder_ref="agent", ttl_seconds=5)
    renew_update = renew_claim_pipeline(5)
    guard_update = transition_guard_pipeline()
    assert "$$NOW" in repr(acquire_update)
    assert "$$NOW" in repr(renew_update)
    assert "$$NOW" in repr(guard_update)


def test_mongo_adapter_uses_explicit_budgeted_transactions_and_reconciliation():
    path = Path(__file__).parents[1] / "src/l9_state/adapters/mongodb.py"
    source = path.read_text()
    assert "AsyncMongoClient" in source
    assert 'ReadConcern("snapshot")' in source
    assert 'WriteConcern("majority")' in source
    assert "ReadPreference.PRIMARY" in source
    assert "with_transaction" not in source
    assert "start_transaction" in source
    assert "commit_transaction" in source
    assert "max_commit_time_ms" in source
    assert "ExecutionBudget" in source
    assert "_reconcile_after_commit" in source
    assert "motor" not in source.lower()
    assert "watch(" not in source
    assert "change_stream" not in source.lower()


def test_transition_claim_guard_is_a_write_to_claim_lineage():
    path = Path(__file__).parents[1] / "src/l9_state/adapters/mongodb.py"
    source = path.read_text()
    assert "_guard_transition_claim" in source
    assert "self._claims.find_one_and_update" in source
    assert "transition_guard_pipeline()" in source


def test_state_dependent_negative_outcomes_are_transaction_receipts():
    path = Path(__file__).parents[1] / "src/l9_state/adapters/mongodb.py"
    source = path.read_text()
    assert "logical_receipt_factory" in source
    assert "state_terminal_receipt" in source
    assert "claim_terminal_receipt" in source
    assert "terminal_operation" in source


def test_commit_error_labels_distinguish_retry_from_ambiguity_reconciliation():
    path = Path(__file__).parents[1] / "src/l9_state/adapters/mongodb.py"
    source = path.read_text()
    assert '"UnknownTransactionCommitResult"' in source
    assert '"TransientTransactionError"' in source
    assert "if self._is_ambiguous_commit(exc):" in source
    assert "if self._is_transient_transaction(exc) and budget.can_start_mutation():" in source
    assert "semantic execution is forbidden; reconcile only" in source


def test_hard_erase_exact_claim_fence_filter_excludes_holder_identity():
    guarded = exact_claim_fence_filter(
        "tenant", "scope", "object", claim_id="claim.1", fencing_token=4
    )
    assert guarded["claim_id"] == "claim.1"
    assert guarded["fencing_token"] == 4
    assert "holder_ref" not in guarded
    assert "$expr" in guarded
