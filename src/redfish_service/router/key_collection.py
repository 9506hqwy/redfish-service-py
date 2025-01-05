from typing import Any, cast

from fastapi import APIRouter

from ..model.key_collection import KeyCollection
from ..service import Service, find_service
from . import authenticate

router = APIRouter()


@router.get("/redfish/v1/KeyService/NVMeoFSecrets", response_model_exclude_none=True)
@authenticate
async def get1() -> KeyCollection:
    s: Service = find_service(KeyCollection)
    b: dict[str, Any] = {}
    return cast(KeyCollection, s.get(**b))


@router.get("/redfish/v1/UpdateService/RemoteServerSSHKeys", response_model_exclude_none=True)
@authenticate
async def get2() -> KeyCollection:
    s: Service = find_service(KeyCollection)
    b: dict[str, Any] = {}
    return cast(KeyCollection, s.get(**b))


@router.get(
    "/redfish/v1/AccountService/Accounts/{manager_account_id}/Keys",
    response_model_exclude_none=True,
)
@authenticate
async def get3(manager_account_id: str) -> KeyCollection:
    s: Service = find_service(KeyCollection)
    b: dict[str, Any] = {"manager_account_id": manager_account_id}
    return cast(KeyCollection, s.get(**b))


@router.get(
    "/redfish/v1/Managers/{manager_id}/RemoteAccountService/Accounts/{manager_account_id}/Keys",
    response_model_exclude_none=True,
)
@authenticate
async def get4(manager_id: str, manager_account_id: str) -> KeyCollection:
    s: Service = find_service(KeyCollection)
    b: dict[str, Any] = {"manager_id": manager_id, "manager_account_id": manager_account_id}
    return cast(KeyCollection, s.get(**b))


@router.get(
    "/redfish/v1/AggregationService/AggregationSources/{aggregation_source_id}/TrustedPublicHostKeys",
    response_model_exclude_none=True,
)
@authenticate
async def get5(aggregation_source_id: str) -> KeyCollection:
    s: Service = find_service(KeyCollection)
    b: dict[str, Any] = {"aggregation_source_id": aggregation_source_id}
    return cast(KeyCollection, s.get(**b))
