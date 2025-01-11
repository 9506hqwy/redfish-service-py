from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.account_service import AccountService, AccountServiceOnUpdate
from ..service import Service, find_service

router = APIRouter()


@router.get("/redfish/v1/AccountService", response_model_exclude_none=True)
@router.head("/redfish/v1/AccountService", response_model_exclude_none=True)
async def get1(request: Request, response: Response) -> AccountService:
    s: Service = find_service(AccountService)
    b: dict[str, Any] = {"request": request, "response": response}

    response.headers["OData-Version"] = "4.0"

    return cast(AccountService, s.get(**b))


@router.patch("/redfish/v1/AccountService", response_model_exclude_none=True)
@authenticate
async def patch1(
    request: Request, response: Response, body: AccountServiceOnUpdate
) -> AccountService:
    s: Service = find_service(AccountService)
    b: dict[str, Any] = {"request": request, "response": response, "body": body}

    response.headers["OData-Version"] = "4.0"

    return cast(AccountService, s.patch(**b))


@router.get(
    "/redfish/v1/Managers/{manager_id}/RemoteAccountService", response_model_exclude_none=True
)
@router.head(
    "/redfish/v1/Managers/{manager_id}/RemoteAccountService", response_model_exclude_none=True
)
async def get2(manager_id: str, request: Request, response: Response) -> AccountService:
    s: Service = find_service(AccountService)
    b: dict[str, Any] = {"manager_id": manager_id, "request": request, "response": response}

    response.headers["OData-Version"] = "4.0"

    return cast(AccountService, s.get(**b))


@router.patch(
    "/redfish/v1/Managers/{manager_id}/RemoteAccountService", response_model_exclude_none=True
)
@authenticate
async def patch2(
    manager_id: str, request: Request, response: Response, body: AccountServiceOnUpdate
) -> AccountService:
    s: Service = find_service(AccountService)
    b: dict[str, Any] = {
        "manager_id": manager_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(AccountService, s.patch(**b))
