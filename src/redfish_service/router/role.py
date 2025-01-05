from typing import Any, cast

from fastapi import APIRouter

from ..model.role import Role
from ..service import Service, find_service
from . import authenticate

router = APIRouter()


@router.get("/redfish/v1/AccountService/Roles/{role_id}", response_model_exclude_none=True)
@authenticate
async def get1(role_id: str) -> Role:
    s: Service = find_service(Role)
    b: dict[str, Any] = {"role_id": role_id}
    return cast(Role, s.get(**b))


@router.get(
    "/redfish/v1/Managers/{manager_id}/RemoteAccountService/Roles/{role_id}",
    response_model_exclude_none=True,
)
@authenticate
async def get2(manager_id: str, role_id: str) -> Role:
    s: Service = find_service(Role)
    b: dict[str, Any] = {"manager_id": manager_id, "role_id": role_id}
    return cast(Role, s.get(**b))
