from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.manager_account_collection import ManagerAccountCollection
from ..service import Service, find_service

router = APIRouter()


@router.get("/redfish/v1/AccountService/Accounts", response_model_exclude_none=True)
@router.head("/redfish/v1/AccountService/Accounts", response_model_exclude_none=True)
@authenticate
async def get1(request: Request, response: Response) -> ManagerAccountCollection:
    s: Service = find_service(ManagerAccountCollection)
    b: dict[str, Any] = {"request": request, "response": response}

    response.headers["OData-Version"] = "4.0"

    return cast(ManagerAccountCollection, s.get(**b))


@router.get(
    "/redfish/v1/Managers/{manager_id}/RemoteAccountService/Accounts",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Managers/{manager_id}/RemoteAccountService/Accounts",
    response_model_exclude_none=True,
)
@authenticate
async def get2(manager_id: str, request: Request, response: Response) -> ManagerAccountCollection:
    s: Service = find_service(ManagerAccountCollection)
    b: dict[str, Any] = {"manager_id": manager_id, "request": request, "response": response}

    response.headers["OData-Version"] = "4.0"

    return cast(ManagerAccountCollection, s.get(**b))
