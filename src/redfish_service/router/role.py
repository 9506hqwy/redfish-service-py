from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..model.role import Role
from ..service import Service, find_service

router = APIRouter()


@router.get("/redfish/v1/AccountService/Roles/{role_id}", response_model_exclude_none=True)
@router.head("/redfish/v1/AccountService/Roles/{role_id}", response_model_exclude_none=True)
async def get1(role_id: str, request: Request, response: Response) -> Role:
    s: Service = find_service(Role)
    b: dict[str, Any] = {"role_id": role_id, "request": request, "response": response}

    response.headers["OData-Version"] = "4.0"

    return cast(Role, s.get(**b))


@router.get(
    "/redfish/v1/Managers/{manager_id}/RemoteAccountService/Roles/{role_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Managers/{manager_id}/RemoteAccountService/Roles/{role_id}",
    response_model_exclude_none=True,
)
async def get2(manager_id: str, role_id: str, request: Request, response: Response) -> Role:
    s: Service = find_service(Role)
    b: dict[str, Any] = {
        "manager_id": manager_id,
        "role_id": role_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(Role, s.get(**b))
