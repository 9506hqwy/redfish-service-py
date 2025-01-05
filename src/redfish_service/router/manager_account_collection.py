from typing import Any, cast

from fastapi import APIRouter

from ..authenticate import authenticate
from ..model.manager_account_collection import ManagerAccountCollection
from ..service import Service, find_service

router = APIRouter()


@router.get("/redfish/v1/AccountService/Accounts", response_model_exclude_none=True)
@authenticate
async def get1() -> ManagerAccountCollection:
    s: Service = find_service(ManagerAccountCollection)
    b: dict[str, Any] = {}
    return cast(ManagerAccountCollection, s.get(**b))


@router.get(
    "/redfish/v1/Managers/{manager_id}/RemoteAccountService/Accounts",
    response_model_exclude_none=True,
)
@authenticate
async def get2(manager_id: str) -> ManagerAccountCollection:
    s: Service = find_service(ManagerAccountCollection)
    b: dict[str, Any] = {"manager_id": manager_id}
    return cast(ManagerAccountCollection, s.get(**b))
