from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..model.account_service import AccountService
from ..service import Service, find_service

router = APIRouter()


@router.get("/redfish/v1/AccountService", response_model_exclude_none=True)
@router.head("/redfish/v1/AccountService", response_model_exclude_none=True)
async def get1(request: Request, response: Response) -> AccountService:
    s: Service = find_service(AccountService)
    b: dict[str, Any] = {"request": request, "response": response}

    response.headers["OData-Version"] = "4.0"

    return cast(AccountService, s.get(**b))


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
