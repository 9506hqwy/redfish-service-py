from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.role import Role, RoleOnCreate
from ..model.role_collection import RoleCollection
from ..service import Service, ServiceCollection
from ..util import get_service, get_service_collection

router = APIRouter()


@router.get("/redfish/v1/AccountService/Roles", response_model_exclude_none=True)
@router.head("/redfish/v1/AccountService/Roles", response_model_exclude_none=True)
async def get1(request: Request, response: Response) -> RoleCollection:
    s: Service = get_service(RoleCollection, request)
    b: dict[str, Any] = {"request": request, "response": response}
    return cast(RoleCollection, s.get(**b))


@router.post("/redfish/v1/AccountService/Roles", response_model_exclude_none=True)
@router.post("/redfish/v1/AccountService/Roles/Members", response_model_exclude_none=True)
@authenticate
async def post1(request: Request, response: Response, body: RoleOnCreate) -> Role:
    s: ServiceCollection = get_service_collection(RoleCollection, request)
    b: dict[str, Any] = {"request": request, "response": response, "body": body}
    return cast(Role, s.post(**b))


@router.get(
    "/redfish/v1/Managers/{manager_id}/RemoteAccountService/Roles",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Managers/{manager_id}/RemoteAccountService/Roles",
    response_model_exclude_none=True,
)
async def get2(manager_id: str, request: Request, response: Response) -> RoleCollection:
    s: Service = get_service(RoleCollection, request)
    b: dict[str, Any] = {"manager_id": manager_id, "request": request, "response": response}
    return cast(RoleCollection, s.get(**b))


@router.post(
    "/redfish/v1/Managers/{manager_id}/RemoteAccountService/Roles",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/Managers/{manager_id}/RemoteAccountService/Roles/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post2(manager_id: str, request: Request, response: Response, body: RoleOnCreate) -> Role:
    s: ServiceCollection = get_service_collection(RoleCollection, request)
    b: dict[str, Any] = {
        "manager_id": manager_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Role, s.post(**b))
