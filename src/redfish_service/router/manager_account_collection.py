from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.manager_account import ManagerAccount, ManagerAccountOnCreate
from ..model.manager_account_collection import ManagerAccountCollection
from ..service import Service, ServiceCollection
from ..util import get_service, get_service_collection, set_link_header

router = APIRouter()


@router.get("/redfish/v1/AccountService/Accounts", response_model_exclude_none=True)
@router.head("/redfish/v1/AccountService/Accounts", response_model_exclude_none=True)
async def get1(request: Request, response: Response) -> ManagerAccountCollection:
    s: Service = get_service(ManagerAccountCollection, request)
    b: dict[str, Any] = {"request": request, "response": response}
    m = cast(ManagerAccountCollection, s.get(**b))
    set_link_header(m, response)
    return m


@router.post("/redfish/v1/AccountService/Accounts", response_model_exclude_none=True)
@router.post("/redfish/v1/AccountService/Accounts/Members", response_model_exclude_none=True)
@authenticate
async def post1(
    request: Request, response: Response, body: ManagerAccountOnCreate
) -> ManagerAccount:
    s: ServiceCollection = get_service_collection(ManagerAccountCollection, request)
    b: dict[str, Any] = {"request": request, "response": response, "body": body}
    return cast(ManagerAccount, s.post(**b))


@router.get(
    "/redfish/v1/Managers/{manager_id}/RemoteAccountService/Accounts",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Managers/{manager_id}/RemoteAccountService/Accounts",
    response_model_exclude_none=True,
)
async def get2(manager_id: str, request: Request, response: Response) -> ManagerAccountCollection:
    s: Service = get_service(ManagerAccountCollection, request)
    b: dict[str, Any] = {"manager_id": manager_id, "request": request, "response": response}
    m = cast(ManagerAccountCollection, s.get(**b))
    set_link_header(m, response)
    return m


@router.post(
    "/redfish/v1/Managers/{manager_id}/RemoteAccountService/Accounts",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/Managers/{manager_id}/RemoteAccountService/Accounts/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post2(
    manager_id: str, request: Request, response: Response, body: ManagerAccountOnCreate
) -> ManagerAccount:
    s: ServiceCollection = get_service_collection(ManagerAccountCollection, request)
    b: dict[str, Any] = {
        "manager_id": manager_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(ManagerAccount, s.post(**b))
