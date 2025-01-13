from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.manager_account import (
    ChangePasswordRequest,
    ManagerAccount,
    ManagerAccountOnUpdate,
    VerifyTimeBasedOneTimePasswordRequest,
)
from ..model.redfish_error import RedfishError
from ..service import Service
from ..util import get_service

router = APIRouter()


@router.delete(
    "/redfish/v1/AccountService/Accounts/{manager_account_id}", response_model_exclude_none=True
)
@authenticate
async def delete1(manager_account_id: str, request: Request, response: Response) -> None:
    s: Service = get_service(ManagerAccount, request)
    b: dict[str, Any] = {
        "manager_account_id": manager_account_id,
        "request": request,
        "response": response,
    }
    return s.delete(**b)


@router.get(
    "/redfish/v1/AccountService/Accounts/{manager_account_id}", response_model_exclude_none=True
)
@router.head(
    "/redfish/v1/AccountService/Accounts/{manager_account_id}", response_model_exclude_none=True
)
async def get1(manager_account_id: str, request: Request, response: Response) -> ManagerAccount:
    s: Service = get_service(ManagerAccount, request)
    b: dict[str, Any] = {
        "manager_account_id": manager_account_id,
        "request": request,
        "response": response,
    }
    return cast(ManagerAccount, s.get(**b))


@router.patch(
    "/redfish/v1/AccountService/Accounts/{manager_account_id}", response_model_exclude_none=True
)
@authenticate
async def patch1(
    manager_account_id: str, request: Request, response: Response, body: ManagerAccountOnUpdate
) -> ManagerAccount:
    s: Service = get_service(ManagerAccount, request)
    b: dict[str, Any] = {
        "manager_account_id": manager_account_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(ManagerAccount, s.patch(**b))


@router.post(
    "/redfish/v1/AccountService/Accounts/{manager_account_id}/Actions/ManagerAccount.ChangePassword",
    response_model_exclude_none=True,
)
@authenticate
async def change_password1(
    manager_account_id: str, request: Request, response: Response, body: ChangePasswordRequest
) -> RedfishError:
    s: Service = get_service(ManagerAccount, request)
    b: dict[str, Any] = {
        "manager_account_id": manager_account_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "ChangePassword",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/AccountService/Accounts/{manager_account_id}/Actions/ManagerAccount.VerifyTimeBasedOneTimePassword",
    response_model_exclude_none=True,
)
@authenticate
async def verify_time_based_one_time_password1(
    manager_account_id: str,
    request: Request,
    response: Response,
    body: VerifyTimeBasedOneTimePasswordRequest,
) -> RedfishError:
    s: Service = get_service(ManagerAccount, request)
    b: dict[str, Any] = {
        "manager_account_id": manager_account_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "VerifyTimeBasedOneTimePassword",
    }
    return s.action(**b)


@router.delete(
    "/redfish/v1/Managers/{manager_id}/RemoteAccountService/Accounts/{manager_account_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete2(
    manager_id: str, manager_account_id: str, request: Request, response: Response
) -> None:
    s: Service = get_service(ManagerAccount, request)
    b: dict[str, Any] = {
        "manager_id": manager_id,
        "manager_account_id": manager_account_id,
        "request": request,
        "response": response,
    }
    return s.delete(**b)


@router.get(
    "/redfish/v1/Managers/{manager_id}/RemoteAccountService/Accounts/{manager_account_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Managers/{manager_id}/RemoteAccountService/Accounts/{manager_account_id}",
    response_model_exclude_none=True,
)
async def get2(
    manager_id: str, manager_account_id: str, request: Request, response: Response
) -> ManagerAccount:
    s: Service = get_service(ManagerAccount, request)
    b: dict[str, Any] = {
        "manager_id": manager_id,
        "manager_account_id": manager_account_id,
        "request": request,
        "response": response,
    }
    return cast(ManagerAccount, s.get(**b))


@router.patch(
    "/redfish/v1/Managers/{manager_id}/RemoteAccountService/Accounts/{manager_account_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch2(
    manager_id: str,
    manager_account_id: str,
    request: Request,
    response: Response,
    body: ManagerAccountOnUpdate,
) -> ManagerAccount:
    s: Service = get_service(ManagerAccount, request)
    b: dict[str, Any] = {
        "manager_id": manager_id,
        "manager_account_id": manager_account_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(ManagerAccount, s.patch(**b))


@router.post(
    "/redfish/v1/Managers/{manager_id}/RemoteAccountService/Accounts/{manager_account_id}/Actions/ManagerAccount.ChangePassword",
    response_model_exclude_none=True,
)
@authenticate
async def change_password2(
    manager_id: str,
    manager_account_id: str,
    request: Request,
    response: Response,
    body: ChangePasswordRequest,
) -> RedfishError:
    s: Service = get_service(ManagerAccount, request)
    b: dict[str, Any] = {
        "manager_id": manager_id,
        "manager_account_id": manager_account_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "ChangePassword",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Managers/{manager_id}/RemoteAccountService/Accounts/{manager_account_id}/Actions/ManagerAccount.VerifyTimeBasedOneTimePassword",
    response_model_exclude_none=True,
)
@authenticate
async def verify_time_based_one_time_password2(
    manager_id: str,
    manager_account_id: str,
    request: Request,
    response: Response,
    body: VerifyTimeBasedOneTimePasswordRequest,
) -> RedfishError:
    s: Service = get_service(ManagerAccount, request)
    b: dict[str, Any] = {
        "manager_id": manager_id,
        "manager_account_id": manager_account_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "VerifyTimeBasedOneTimePassword",
    }
    return s.action(**b)
