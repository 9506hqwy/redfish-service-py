from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.external_account_provider import ExternalAccountProvider
from ..service import Service, find_service

router = APIRouter()


@router.get(
    "/redfish/v1/AccountService/ExternalAccountProviders/{external_account_provider_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/AccountService/ExternalAccountProviders/{external_account_provider_id}",
    response_model_exclude_none=True,
)
@authenticate
async def get1(
    external_account_provider_id: str, request: Request, response: Response
) -> ExternalAccountProvider:
    s: Service = find_service(ExternalAccountProvider)
    b: dict[str, Any] = {
        "external_account_provider_id": external_account_provider_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(ExternalAccountProvider, s.get(**b))


@router.get(
    "/redfish/v1/Managers/{manager_id}/RemoteAccountService/ExternalAccountProviders/{external_account_provider_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Managers/{manager_id}/RemoteAccountService/ExternalAccountProviders/{external_account_provider_id}",
    response_model_exclude_none=True,
)
@authenticate
async def get2(
    manager_id: str, external_account_provider_id: str, request: Request, response: Response
) -> ExternalAccountProvider:
    s: Service = find_service(ExternalAccountProvider)
    b: dict[str, Any] = {
        "manager_id": manager_id,
        "external_account_provider_id": external_account_provider_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(ExternalAccountProvider, s.get(**b))
