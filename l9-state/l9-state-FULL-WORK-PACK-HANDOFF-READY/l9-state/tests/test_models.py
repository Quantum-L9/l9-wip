import json
from pathlib import Path

import pytest
from pydantic import ValidationError

import l9_state.models as state_models
from l9_state.models import (
    StateAckReceipt,
    StateClaimReceipt,
    StateCreateRequest,
    StateEventPage,
    StateHistoryPage,
    StateListPage,
    StateProblem,
    StateReceipt,
    StateTransitionRequest,
)

ROOT = Path(__file__).parents[1]
FIXTURES = ROOT / "fixtures"


def _fixture(name: str):
    return json.loads((FIXTURES / name).read_text())


def test_pack_fixtures_parse():
    StateCreateRequest.model_validate(_fixture("create_valid.json"))
    StateReceipt.model_validate(_fixture("state_receipt_valid.json"))
    StateClaimReceipt.model_validate(_fixture("claim_receipt_valid.json"))


def test_authority_fields_rejected():
    base = _fixture("create_valid.json")
    base["tenant_org_id"] = "evil"
    try:
        StateCreateRequest.model_validate(base)
    except ValidationError:
        return
    raise AssertionError("provider/authority field accepted")


def test_claim_pair():
    data = _fixture("transition_valid.json")
    data["claim_id"] = "claim.1"
    try:
        StateTransitionRequest.model_validate(data)
    except ValidationError:
        return
    raise AssertionError("unpaired claim accepted")


def test_claim_receipt_requires_fence_metadata():
    try:
        StateClaimReceipt.model_validate(_fixture("claim_receipt_missing_fence_invalid.json"))
    except ValidationError:
        return
    raise AssertionError("claim receipt missing fence metadata was accepted")

def test_contract_version_is_required_at_runtime():
    base = _fixture("create_valid.json")
    base.pop("contract_version")
    with pytest.raises(ValidationError):
        StateCreateRequest.model_validate(base)


def test_payload_property_bound_matches_public_schema():
    base = _fixture("create_valid.json")
    base["payload"] = {f"k{i}": i for i in range(1001)}
    with pytest.raises(ValidationError):
        StateCreateRequest.model_validate(base)


def test_reason_code_bound_matches_public_schema():
    base = _fixture("state_receipt_valid.json")
    base["reason_codes"] = [f"R{i}" for i in range(33)]
    with pytest.raises(ValidationError):
        StateReceipt.model_validate(base)

def test_optional_nonnullable_field_rejects_explicit_null():
    data = _fixture("transition_valid.json")
    data["claim_id"] = None
    with pytest.raises(ValidationError):
        StateTransitionRequest.model_validate(data)



def test_all_public_schema_required_fields_match_runtime_models():
    schema_dir = ROOT / "contracts" / "schemas"
    compared = 0
    for schema_path in sorted(schema_dir.glob("*.schema.json")):
        model_name = schema_path.name.removesuffix(".schema.json")
        model = getattr(state_models, model_name)
        schema = json.loads(schema_path.read_text())
        schema_required = set(schema.get("required", ()))
        model_required = {
            name for name, field in model.model_fields.items() if field.is_required()
        }
        assert model_required == schema_required, model_name
        compared += 1
    assert compared == 24


def test_required_collection_fields_allow_explicit_empty_values():
    receipt_base = {
        "contract_version": "1.0",
        "receipt_id": "receipt.1",
        "operation_id": "op.1",
        "request_digest": "a" * 64,
        "scope_ref": "scope.1",
        "principal_ref": "agent-a",
        "authorization_ref": "state.authz.tenant-base:test",
        "issued_at": "2026-10-01T00:00:00Z",
        "reason_codes": [],
    }
    StateReceipt.model_validate(
        {**receipt_base, "action": "state.create", "status": "refused"}
    )
    StateClaimReceipt.model_validate(
        {
            **receipt_base,
            "action": "state.claim",
            "object_id": "object.1",
            "status": "refused",
        }
    )
    StateAckReceipt.model_validate(
        {
            **receipt_base,
            "consumer_ref": "agent-a",
            "status": "refused",
        }
    )
    StateProblem.model_validate(
        {
            "contract_version": "1.0",
            "status": "failed",
            "code": "INVALID_REQUEST",
            "retry_class": "no",
            "reason_codes": [],
        }
    )
    StateListPage.model_validate(
        {
            "contract_version": "1.0",
            "scope_ref": "scope.1",
            "consumer_ref": "agent-a",
            "states": [],
            "coverage": "complete",
            "resume_event_cursor": "cursor.1",
            "observed_at": "2026-10-01T00:00:00Z",
        }
    )
    StateEventPage.model_validate(
        {
            "contract_version": "1.0",
            "scope_ref": "scope.1",
            "consumer_ref": "agent-a",
            "events": [],
            "next_cursor": "cursor.1",
            "coverage": "complete",
            "high_water_seq": 0,
            "observed_at": "2026-10-01T00:00:00Z",
        }
    )
    StateHistoryPage.model_validate(
        {
            "contract_version": "1.0",
            "object_id": "object.1",
            "scope_ref": "scope.1",
            "events": [],
            "coverage": "complete",
            "oldest_available_revision": 0,
            "latest_revision": 0,
            "observed_at": "2026-10-01T00:00:00Z",
        }
    )
