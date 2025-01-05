from typing import Any, cast

from fastapi import APIRouter

from ..model.external_account_provider_collection import ExternalAccountProviderCollection
from ..service import Service, find_service
from . import authenticate

router = APIRouter()


@router.get(
    "/redfish/v1/AccountService/ExternalAccountProviders", response_model_exclude_none=True
)
@authenticate
async def get1() -> ExternalAccountProviderCollection:
    s: Service = find_service(ExternalAccountProviderCollection)
    b: dict[str, Any] = {}
    return cast(ExternalAccountProviderCollection, s.get(**b))


@router.get(
    "/redfish/v1/Managers/{manager_id}/RemoteAccountService/ExternalAccountProviders",
    response_model_exclude_none=True,
)
@authenticate
async def get2(manager_id: str) -> ExternalAccountProviderCollection:
    s: Service = find_service(ExternalAccountProviderCollection)
    b: dict[str, Any] = {"manager_id": manager_id}
    return cast(ExternalAccountProviderCollection, s.get(**b))
