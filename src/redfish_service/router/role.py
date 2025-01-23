from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.role import Role, RoleOnUpdate
from ..service import Service
from ..util import get_service, set_link_header

router = APIRouter()


@router.delete("/redfish/v1/AccountService/Roles/{role_id}", response_model_exclude_none=True)
@authenticate
async def delete1(role_id: str, request: Request, response: Response) -> None:
    s: Service = get_service(Role, request)
    b: dict[str, Any] = {"role_id": role_id, "request": request, "response": response}
    return s.delete(**b)


@router.get("/redfish/v1/AccountService/Roles/{role_id}", response_model_exclude_none=True)
@router.head("/redfish/v1/AccountService/Roles/{role_id}", response_model_exclude_none=True)
async def get1(role_id: str, request: Request, response: Response) -> Role:
    s: Service = get_service(Role, request)
    b: dict[str, Any] = {"role_id": role_id, "request": request, "response": response}
    m = cast(Role, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch("/redfish/v1/AccountService/Roles/{role_id}", response_model_exclude_none=True)
@authenticate
async def patch1(role_id: str, request: Request, response: Response, body: RoleOnUpdate) -> Role:
    s: Service = get_service(Role, request)
    b: dict[str, Any] = {
        "role_id": role_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Role, s.patch(**b))


@router.delete(
    "/redfish/v1/Managers/{manager_id}/RemoteAccountService/Roles/{role_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete2(manager_id: str, role_id: str, request: Request, response: Response) -> None:
    s: Service = get_service(Role, request)
    b: dict[str, Any] = {
        "manager_id": manager_id,
        "role_id": role_id,
        "request": request,
        "response": response,
    }
    return s.delete(**b)


@router.get(
    "/redfish/v1/Managers/{manager_id}/RemoteAccountService/Roles/{role_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Managers/{manager_id}/RemoteAccountService/Roles/{role_id}",
    response_model_exclude_none=True,
)
async def get2(manager_id: str, role_id: str, request: Request, response: Response) -> Role:
    s: Service = get_service(Role, request)
    b: dict[str, Any] = {
        "manager_id": manager_id,
        "role_id": role_id,
        "request": request,
        "response": response,
    }
    m = cast(Role, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/Managers/{manager_id}/RemoteAccountService/Roles/{role_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch2(
    manager_id: str, role_id: str, request: Request, response: Response, body: RoleOnUpdate
) -> Role:
    s: Service = get_service(Role, request)
    b: dict[str, Any] = {
        "manager_id": manager_id,
        "role_id": role_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Role, s.patch(**b))
