from __future__ import annotations

from dataclasses import dataclass
from datetime import UTC, datetime
from uuid import uuid4

from .digests import request_digest, state_digest
from .execution import ExecutionBudget
from .internal_models import HardEraseReceipt
from .models import StateRef, StateTransitionEvent
from .ports import HARD_ERASE_RECEIPT_SCHEMA_REF, PendingRevision, StoredOperation, StoredRevision

_INTERNAL_HARD_ERASE_ACTION = "state.internal.hard_erase"


@dataclass(frozen=True)
class HardErasePlan:
    """State-owned mechanical projection of an already-authorized retention decision.

    The external retention-policy decision contract is intentionally not defined here.
    A future bound RetentionExecutor may create this plan only after that external
    authority has produced an admissible decision.
    """

    revision: PendingRevision
    expected_revision: int
    expected_state_digest: str
    expected_retention_policy_ref: str
    expected_retention_policy_digest: str
    claim_id: str | None
    fencing_token: int | None
    operation: StoredOperation
    event: StateTransitionEvent
    budget: ExecutionBudget


def prepare_hard_erase_plan(
    *,
    current: StoredRevision,
    operation_id: str,
    principal_ref: str,
    authorization_ref: str,
    budget: ExecutionBudget,
    claim_id: str | None = None,
    fencing_token: int | None = None,
    causation_ref: str | None = None,
    issued_at: datetime | None = None,
) -> HardErasePlan:
    """Prepare provider-neutral hard-erasure mechanics from an authorized decision.

    ``authorization_ref`` must identify the external retention-policy decision/evidence.
    This helper does not validate or invent that external authority.
    """

    if (claim_id is None) != (fencing_token is None):
        raise ValueError("claim_id and fencing_token must be supplied together")
    now = issued_at or datetime.now(UTC)
    action = _INTERNAL_HARD_ERASE_ACTION
    domain_request = {
        "contract_version": "1.0",
        "object_id": current.state_ref.object_id,
        "scope_ref": current.state_ref.scope_ref,
        "expected_revision": current.state_ref.revision,
        "expected_state_digest": current.state_ref.state_digest,
        "retention_policy_ref": current.retention_policy_ref,
        "retention_policy_digest": current.retention_policy_digest,
        "authorization_ref": authorization_ref,
        **({"claim_id": claim_id, "fencing_token": fencing_token} if claim_id is not None else {}),
    }
    rd = request_digest(action, domain_request)
    new_ref = StateRef(
        contract_version="1.0",
        object_id=current.state_ref.object_id,
        scope_ref=current.state_ref.scope_ref,
        revision=current.state_ref.revision + 1,
        state_digest=state_digest(
            schema_ref=current.state_ref.schema_ref,
            schema_digest=current.state_ref.schema_digest,
            lifecycle="erased",
            payload=None,
        ),
        schema_ref=current.state_ref.schema_ref,
        schema_digest=current.state_ref.schema_digest,
        lifecycle="erased",
    )
    event_id = f"event.{uuid4().hex}"
    receipt = HardEraseReceipt(
        contract_version="1.0",
        receipt_id=f"receipt.{uuid4().hex}",
        action=action,
        operation_id=operation_id,
        request_digest=rd,
        scope_ref=current.state_ref.scope_ref,
        principal_ref=principal_ref,
        authorization_ref=authorization_ref,
        status="committed",
        state_ref=new_ref,
        event_ref=event_id,
        issued_at=now,
        reason_codes=(),
    )
    event = StateTransitionEvent(
        contract_version="1.0",
        event_id=event_id,
        journal_seq=1,
        event_kind="erased",
        state_ref=new_ref,
        prior_revision=current.state_ref.revision,
        operation_id=operation_id,
        principal_ref=principal_ref,
        committed_at=now,
        **({"causation_ref": causation_ref} if causation_ref is not None else {}),
    )
    return HardErasePlan(
        revision=PendingRevision(current.tenant_org_id, new_ref, None, now),
        expected_revision=current.state_ref.revision,
        expected_state_digest=current.state_ref.state_digest,
        expected_retention_policy_ref=current.retention_policy_ref,
        expected_retention_policy_digest=current.retention_policy_digest,
        claim_id=claim_id,
        fencing_token=fencing_token,
        operation=StoredOperation(action, rd, HARD_ERASE_RECEIPT_SCHEMA_REF, receipt),
        event=event,
        budget=budget,
    )
