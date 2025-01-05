from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.key_collection import KeyCollection
from ..service import Service, find_service

router = APIRouter()


@router.get("/redfish/v1/KeyService/NVMeoFSecrets", response_model_exclude_none=True)
@authenticate
async def get1(request: Request, response: Response) -> KeyCollection:
    s: Service = find_service(KeyCollection)
    b: dict[str, Any] = {"request": request, "response": response}

    response.headers["OData-Version"] = "4.0"

    return cast(KeyCollection, s.get(**b))


@router.get("/redfish/v1/UpdateService/RemoteServerSSHKeys", response_model_exclude_none=True)
@authenticate
async def get2(request: Request, response: Response) -> KeyCollection:
    s: Service = find_service(KeyCollection)
    b: dict[str, Any] = {"request": request, "response": response}

    response.headers["OData-Version"] = "4.0"

    return cast(KeyCollection, s.get(**b))


@router.get(
    "/redfish/v1/AccountService/Accounts/{manager_account_id}/Keys",
    response_model_exclude_none=True,
)
@authenticate
async def get3(manager_account_id: str, request: Request, response: Response) -> KeyCollection:
    s: Service = find_service(KeyCollection)
    b: dict[str, Any] = {
        "manager_account_id": manager_account_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(KeyCollection, s.get(**b))


@router.get(
    "/redfish/v1/Managers/{manager_id}/RemoteAccountService/Accounts/{manager_account_id}/Keys",
    response_model_exclude_none=True,
)
@authenticate
async def get4(
    manager_id: str, manager_account_id: str, request: Request, response: Response
) -> KeyCollection:
    s: Service = find_service(KeyCollection)
    b: dict[str, Any] = {
        "manager_id": manager_id,
        "manager_account_id": manager_account_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(KeyCollection, s.get(**b))


@router.get(
    "/redfish/v1/AggregationService/AggregationSources/{aggregation_source_id}/TrustedPublicHostKeys",
    response_model_exclude_none=True,
)
@authenticate
async def get5(aggregation_source_id: str, request: Request, response: Response) -> KeyCollection:
    s: Service = find_service(KeyCollection)
    b: dict[str, Any] = {
        "aggregation_source_id": aggregation_source_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(KeyCollection, s.get(**b))
