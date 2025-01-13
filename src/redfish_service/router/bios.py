from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.bios import Bios, BiosOnUpdate, ChangePasswordRequest
from ..model.redfish_error import RedfishError
from ..service import Service
from ..util import get_service

router = APIRouter()


@router.get("/redfish/v1/Systems/{computer_system_id}/Bios", response_model_exclude_none=True)
@router.head("/redfish/v1/Systems/{computer_system_id}/Bios", response_model_exclude_none=True)
async def get1(computer_system_id: str, request: Request, response: Response) -> Bios:
    s: Service = get_service(Bios, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "request": request,
        "response": response,
    }
    return cast(Bios, s.get(**b))


@router.patch("/redfish/v1/Systems/{computer_system_id}/Bios", response_model_exclude_none=True)
@authenticate
async def patch1(
    computer_system_id: str, request: Request, response: Response, body: BiosOnUpdate
) -> Bios:
    s: Service = get_service(Bios, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Bios, s.patch(**b))


@router.post(
    "/redfish/v1/Systems/{computer_system_id}/Bios/Actions/Bios.ChangePassword",
    response_model_exclude_none=True,
)
@authenticate
async def change_password1(
    computer_system_id: str, request: Request, response: Response, body: ChangePasswordRequest
) -> RedfishError:
    s: Service = get_service(Bios, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "ChangePassword",
    }
    return s.action(**b)


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Bios",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Bios",
    response_model_exclude_none=True,
)
async def get2(
    resource_block_id: str, computer_system_id: str, request: Request, response: Response
) -> Bios:
    s: Service = get_service(Bios, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "request": request,
        "response": response,
    }
    return cast(Bios, s.get(**b))


@router.patch(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Bios",
    response_model_exclude_none=True,
)
@authenticate
async def patch2(
    resource_block_id: str,
    computer_system_id: str,
    request: Request,
    response: Response,
    body: BiosOnUpdate,
) -> Bios:
    s: Service = get_service(Bios, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Bios, s.patch(**b))


@router.post(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Bios/Actions/Bios.ChangePassword",
    response_model_exclude_none=True,
)
@authenticate
async def change_password2(
    resource_block_id: str,
    computer_system_id: str,
    request: Request,
    response: Response,
    body: ChangePasswordRequest,
) -> RedfishError:
    s: Service = get_service(Bios, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "ChangePassword",
    }
    return s.action(**b)


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Bios",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Bios",
    response_model_exclude_none=True,
)
async def get3(
    resource_block_id: str, computer_system_id: str, request: Request, response: Response
) -> Bios:
    s: Service = get_service(Bios, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "request": request,
        "response": response,
    }
    return cast(Bios, s.get(**b))


@router.patch(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Bios",
    response_model_exclude_none=True,
)
@authenticate
async def patch3(
    resource_block_id: str,
    computer_system_id: str,
    request: Request,
    response: Response,
    body: BiosOnUpdate,
) -> Bios:
    s: Service = get_service(Bios, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Bios, s.patch(**b))


@router.post(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Bios/Actions/Bios.ChangePassword",
    response_model_exclude_none=True,
)
@authenticate
async def change_password3(
    resource_block_id: str,
    computer_system_id: str,
    request: Request,
    response: Response,
    body: ChangePasswordRequest,
) -> RedfishError:
    s: Service = get_service(Bios, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "ChangePassword",
    }
    return s.action(**b)
