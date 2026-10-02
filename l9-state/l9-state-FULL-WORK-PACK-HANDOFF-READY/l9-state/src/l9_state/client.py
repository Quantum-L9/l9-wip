from __future__ import annotations

from typing import Any

from constellation_node_sdk import GateClient

from .models import (
    StateAckReceipt,
    StateAckRequest,
    StateClaimReceipt,
    StateClaimRequest,
    StateCreateRequest,
    StateEventPage,
    StateEventReadRequest,
    StateHistoryPage,
    StateHistoryRequest,
    StateListPage,
    StateListRequest,
    StateOperationInspectRequest,
    StateOperationInspectResult,
    StateProblem,
    StateReadRequest,
    StateReadResult,
    StateReceipt,
    StateReleaseRequest,
    StateRenewRequest,
    StateRestoreRequest,
    StateTombstoneRequest,
    StateTransitionRequest,
)

StateMutationResult = StateReceipt | StateProblem
ClaimMutationResult = StateClaimReceipt | StateProblem
AckMutationResult = StateAckReceipt | StateProblem


class StateClient:
    def __init__(self, gate_client: GateClient) -> None:
        self._gate = gate_client

    async def _execute(
        self, *, action: str, request: Any, tenant: str | dict[str, Any], mutation: bool
    ) -> dict[str, Any]:
        packet = await self._gate.execute(
            action=action,
            payload=request.model_dump(mode="json", exclude_none=True),
            tenant=tenant,
            idempotency_key=request.operation_id if mutation else None,
        )
        return dict(packet.payload)

    @staticmethod
    def _state_mutation_result(payload: dict[str, Any]) -> StateMutationResult:
        if payload.get("status") == "failed":
            return StateProblem.model_validate(payload)
        return StateReceipt.model_validate(payload)

    @staticmethod
    def _claim_mutation_result(payload: dict[str, Any]) -> ClaimMutationResult:
        if payload.get("status") == "failed":
            return StateProblem.model_validate(payload)
        return StateClaimReceipt.model_validate(payload)

    async def create(
        self, request: StateCreateRequest, *, tenant: str | dict[str, Any]
    ) -> StateMutationResult:
        return self._state_mutation_result(
            await self._execute(action="state.create", request=request, tenant=tenant, mutation=True)
        )

    async def get(
        self, request: StateReadRequest, *, tenant: str | dict[str, Any]
    ) -> StateReadResult | StateProblem:
        payload = await self._execute(action="state.get", request=request, tenant=tenant, mutation=False)
        if payload.get("status") == "failed":
            return StateProblem.model_validate(payload)
        return StateReadResult.model_validate(payload)

    async def transition(
        self, request: StateTransitionRequest, *, tenant: str | dict[str, Any]
    ) -> StateMutationResult:
        return self._state_mutation_result(
            await self._execute(
                action="state.transition", request=request, tenant=tenant, mutation=True
            )
        )

    async def tombstone(
        self, request: StateTombstoneRequest, *, tenant: str | dict[str, Any]
    ) -> StateMutationResult:
        return self._state_mutation_result(
            await self._execute(
                action="state.tombstone", request=request, tenant=tenant, mutation=True
            )
        )

    async def restore(
        self, request: StateRestoreRequest, *, tenant: str | dict[str, Any]
    ) -> StateMutationResult:
        return self._state_mutation_result(
            await self._execute(
                action="state.restore", request=request, tenant=tenant, mutation=True
            )
        )

    async def claim(
        self, request: StateClaimRequest, *, tenant: str | dict[str, Any]
    ) -> ClaimMutationResult:
        return self._claim_mutation_result(
            await self._execute(action="state.claim", request=request, tenant=tenant, mutation=True)
        )

    async def renew(
        self, request: StateRenewRequest, *, tenant: str | dict[str, Any]
    ) -> ClaimMutationResult:
        return self._claim_mutation_result(
            await self._execute(action="state.renew", request=request, tenant=tenant, mutation=True)
        )

    async def release(
        self, request: StateReleaseRequest, *, tenant: str | dict[str, Any]
    ) -> ClaimMutationResult:
        return self._claim_mutation_result(
            await self._execute(action="state.release", request=request, tenant=tenant, mutation=True)
        )


    async def list_states(
        self, request: StateListRequest, *, tenant: str | dict[str, Any]
    ) -> StateListPage | StateProblem:
        payload = await self._execute(
            action="state.list", request=request, tenant=tenant, mutation=False
        )
        if payload.get("status") == "failed":
            return StateProblem.model_validate(payload)
        return StateListPage.model_validate(payload)

    async def events(
        self, request: StateEventReadRequest, *, tenant: str | dict[str, Any]
    ) -> StateEventPage | StateProblem:
        payload = await self._execute(
            action="state.events", request=request, tenant=tenant, mutation=False
        )
        if payload.get("status") == "failed":
            return StateProblem.model_validate(payload)
        return StateEventPage.model_validate(payload)

    async def acknowledge(
        self, request: StateAckRequest, *, tenant: str | dict[str, Any]
    ) -> AckMutationResult:
        payload = await self._execute(
            action="state.ack", request=request, tenant=tenant, mutation=True
        )
        if payload.get("status") == "failed":
            return StateProblem.model_validate(payload)
        return StateAckReceipt.model_validate(payload)

    async def history(
        self, request: StateHistoryRequest, *, tenant: str | dict[str, Any]
    ) -> StateHistoryPage | StateProblem:
        payload = await self._execute(
            action="state.history", request=request, tenant=tenant, mutation=False
        )
        if payload.get("status") == "failed":
            return StateProblem.model_validate(payload)
        return StateHistoryPage.model_validate(payload)

    async def inspect_operation(
        self, request: StateOperationInspectRequest, *, tenant: str | dict[str, Any]
    ) -> StateOperationInspectResult | StateProblem:
        payload = await self._execute(
            action="state.operation.inspect", request=request, tenant=tenant, mutation=False
        )
        if payload.get("status") == "failed":
            return StateProblem.model_validate(payload)
        return StateOperationInspectResult.model_validate(payload)
