from typing import Any, cast

from fastapi import APIRouter

from ..model.manager_account import ManagerAccount
from ..service import Service, find_service
from . import authenticate

router = APIRouter()


@router.get(
    "/redfish/v1/AccountService/Accounts/{manager_account_id}", response_model_exclude_none=True
)
@authenticate
async def get1(manager_account_id: str) -> ManagerAccount:
    s: Service = find_service(ManagerAccount)
    b: dict[str, Any] = {"manager_account_id": manager_account_id}
    return cast(ManagerAccount, s.get(**b))


@router.get(
    "/redfish/v1/Managers/{manager_id}/RemoteAccountService/Accounts/{manager_account_id}",
    response_model_exclude_none=True,
)
@authenticate
async def get2(manager_id: str, manager_account_id: str) -> ManagerAccount:
    s: Service = find_service(ManagerAccount)
    b: dict[str, Any] = {"manager_id": manager_id, "manager_account_id": manager_account_id}
    return cast(ManagerAccount, s.get(**b))
