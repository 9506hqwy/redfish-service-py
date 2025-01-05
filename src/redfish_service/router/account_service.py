from typing import Any, cast

from fastapi import APIRouter

from ..authenticate import authenticate
from ..model.account_service import AccountService
from ..service import Service, find_service

router = APIRouter()


@router.get("/redfish/v1/AccountService", response_model_exclude_none=True)
@authenticate
async def get1() -> AccountService:
    s: Service = find_service(AccountService)
    b: dict[str, Any] = {}
    return cast(AccountService, s.get(**b))


@router.get(
    "/redfish/v1/Managers/{manager_id}/RemoteAccountService", response_model_exclude_none=True
)
@authenticate
async def get2(manager_id: str) -> AccountService:
    s: Service = find_service(AccountService)
    b: dict[str, Any] = {"manager_id": manager_id}
    return cast(AccountService, s.get(**b))
