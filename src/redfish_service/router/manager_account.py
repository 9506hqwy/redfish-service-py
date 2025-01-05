from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.manager_account import ManagerAccount
from ..service import Service, find_service

router = APIRouter()


@router.get(
    "/redfish/v1/AccountService/Accounts/{manager_account_id}", response_model_exclude_none=True
)
@authenticate
async def get1(manager_account_id: str, request: Request, response: Response) -> ManagerAccount:
    s: Service = find_service(ManagerAccount)
    b: dict[str, Any] = {
        "manager_account_id": manager_account_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(ManagerAccount, s.get(**b))


@router.get(
    "/redfish/v1/Managers/{manager_id}/RemoteAccountService/Accounts/{manager_account_id}",
    response_model_exclude_none=True,
)
@authenticate
async def get2(
    manager_id: str, manager_account_id: str, request: Request, response: Response
) -> ManagerAccount:
    s: Service = find_service(ManagerAccount)
    b: dict[str, Any] = {
        "manager_id": manager_id,
        "manager_account_id": manager_account_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(ManagerAccount, s.get(**b))
