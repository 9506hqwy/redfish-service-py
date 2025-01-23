from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.external_account_provider import (
    ExternalAccountProvider,
    ExternalAccountProviderOnUpdate,
)
from ..service import Service
from ..util import get_service, set_link_header

router = APIRouter()


@router.delete(
    "/redfish/v1/AccountService/ExternalAccountProviders/{external_account_provider_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete1(external_account_provider_id: str, request: Request, response: Response) -> None:
    s: Service = get_service(ExternalAccountProvider, request)
    b: dict[str, Any] = {
        "external_account_provider_id": external_account_provider_id,
        "request": request,
        "response": response,
    }
    return s.delete(**b)


@router.get(
    "/redfish/v1/AccountService/ExternalAccountProviders/{external_account_provider_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/AccountService/ExternalAccountProviders/{external_account_provider_id}",
    response_model_exclude_none=True,
)
async def get1(
    external_account_provider_id: str, request: Request, response: Response
) -> ExternalAccountProvider:
    s: Service = get_service(ExternalAccountProvider, request)
    b: dict[str, Any] = {
        "external_account_provider_id": external_account_provider_id,
        "request": request,
        "response": response,
    }
    m = cast(ExternalAccountProvider, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/AccountService/ExternalAccountProviders/{external_account_provider_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch1(
    external_account_provider_id: str,
    request: Request,
    response: Response,
    body: ExternalAccountProviderOnUpdate,
) -> ExternalAccountProvider:
    s: Service = get_service(ExternalAccountProvider, request)
    b: dict[str, Any] = {
        "external_account_provider_id": external_account_provider_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(ExternalAccountProvider, s.patch(**b))


@router.delete(
    "/redfish/v1/Managers/{manager_id}/RemoteAccountService/ExternalAccountProviders/{external_account_provider_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete2(
    manager_id: str, external_account_provider_id: str, request: Request, response: Response
) -> None:
    s: Service = get_service(ExternalAccountProvider, request)
    b: dict[str, Any] = {
        "manager_id": manager_id,
        "external_account_provider_id": external_account_provider_id,
        "request": request,
        "response": response,
    }
    return s.delete(**b)


@router.get(
    "/redfish/v1/Managers/{manager_id}/RemoteAccountService/ExternalAccountProviders/{external_account_provider_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Managers/{manager_id}/RemoteAccountService/ExternalAccountProviders/{external_account_provider_id}",
    response_model_exclude_none=True,
)
async def get2(
    manager_id: str, external_account_provider_id: str, request: Request, response: Response
) -> ExternalAccountProvider:
    s: Service = get_service(ExternalAccountProvider, request)
    b: dict[str, Any] = {
        "manager_id": manager_id,
        "external_account_provider_id": external_account_provider_id,
        "request": request,
        "response": response,
    }
    m = cast(ExternalAccountProvider, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/Managers/{manager_id}/RemoteAccountService/ExternalAccountProviders/{external_account_provider_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch2(
    manager_id: str,
    external_account_provider_id: str,
    request: Request,
    response: Response,
    body: ExternalAccountProviderOnUpdate,
) -> ExternalAccountProvider:
    s: Service = get_service(ExternalAccountProvider, request)
    b: dict[str, Any] = {
        "manager_id": manager_id,
        "external_account_provider_id": external_account_provider_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(ExternalAccountProvider, s.patch(**b))
