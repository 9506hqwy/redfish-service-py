from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.redfish_error import RedfishError
from ..model.secure_boot import ResetKeysRequest, SecureBoot, SecureBootOnUpdate
from ..service import Service
from ..util import get_service, set_link_header

router = APIRouter()


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/SecureBoot", response_model_exclude_none=True
)
@router.head(
    "/redfish/v1/Systems/{computer_system_id}/SecureBoot", response_model_exclude_none=True
)
async def get1(computer_system_id: str, request: Request, response: Response) -> SecureBoot:
    s: Service = get_service(SecureBoot, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "request": request,
        "response": response,
    }
    m = cast(SecureBoot, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/Systems/{computer_system_id}/SecureBoot", response_model_exclude_none=True
)
@authenticate
async def patch1(
    computer_system_id: str, request: Request, response: Response, body: SecureBootOnUpdate
) -> SecureBoot:
    s: Service = get_service(SecureBoot, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(SecureBoot, s.patch(**b))


@router.post(
    "/redfish/v1/Systems/{computer_system_id}/SecureBoot/Actions/SecureBoot.ResetKeys",
    response_model_exclude_none=True,
)
@authenticate
async def reset_keys1(
    computer_system_id: str, request: Request, response: Response, body: ResetKeysRequest
) -> RedfishError:
    s: Service = get_service(SecureBoot, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "ResetKeys",
    }
    return s.action(**b)


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/SecureBoot",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/SecureBoot",
    response_model_exclude_none=True,
)
async def get2(
    resource_block_id: str, computer_system_id: str, request: Request, response: Response
) -> SecureBoot:
    s: Service = get_service(SecureBoot, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "request": request,
        "response": response,
    }
    m = cast(SecureBoot, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/SecureBoot",
    response_model_exclude_none=True,
)
@authenticate
async def patch2(
    resource_block_id: str,
    computer_system_id: str,
    request: Request,
    response: Response,
    body: SecureBootOnUpdate,
) -> SecureBoot:
    s: Service = get_service(SecureBoot, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(SecureBoot, s.patch(**b))


@router.post(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/SecureBoot/Actions/SecureBoot.ResetKeys",
    response_model_exclude_none=True,
)
@authenticate
async def reset_keys2(
    resource_block_id: str,
    computer_system_id: str,
    request: Request,
    response: Response,
    body: ResetKeysRequest,
) -> RedfishError:
    s: Service = get_service(SecureBoot, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "ResetKeys",
    }
    return s.action(**b)


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/SecureBoot",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/SecureBoot",
    response_model_exclude_none=True,
)
async def get3(
    resource_block_id: str, computer_system_id: str, request: Request, response: Response
) -> SecureBoot:
    s: Service = get_service(SecureBoot, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "request": request,
        "response": response,
    }
    m = cast(SecureBoot, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/SecureBoot",
    response_model_exclude_none=True,
)
@authenticate
async def patch3(
    resource_block_id: str,
    computer_system_id: str,
    request: Request,
    response: Response,
    body: SecureBootOnUpdate,
) -> SecureBoot:
    s: Service = get_service(SecureBoot, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(SecureBoot, s.patch(**b))


@router.post(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/SecureBoot/Actions/SecureBoot.ResetKeys",
    response_model_exclude_none=True,
)
@authenticate
async def reset_keys3(
    resource_block_id: str,
    computer_system_id: str,
    request: Request,
    response: Response,
    body: ResetKeysRequest,
) -> RedfishError:
    s: Service = get_service(SecureBoot, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "ResetKeys",
    }
    return s.action(**b)
