from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.container import Container, ResetRequest
from ..model.redfish_error import RedfishError
from ..service import Service
from ..util import get_service

router = APIRouter()


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/OperatingSystem/Containers/{container_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Systems/{computer_system_id}/OperatingSystem/Containers/{container_id}",
    response_model_exclude_none=True,
)
async def get1(
    computer_system_id: str, container_id: str, request: Request, response: Response
) -> Container:
    s: Service = get_service(Container, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "container_id": container_id,
        "request": request,
        "response": response,
    }
    return cast(Container, s.get(**b))


@router.post(
    "/redfish/v1/Systems/{computer_system_id}/OperatingSystem/Containers/{container_id}/Actions/Container.Reset",
    response_model_exclude_none=True,
)
@authenticate
async def reset1(
    computer_system_id: str,
    container_id: str,
    request: Request,
    response: Response,
    body: ResetRequest,
) -> RedfishError:
    s: Service = get_service(Container, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "container_id": container_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Reset",
    }
    return s.action(**b)


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/OperatingSystem/Containers/{container_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/OperatingSystem/Containers/{container_id}",
    response_model_exclude_none=True,
)
async def get2(
    resource_block_id: str,
    computer_system_id: str,
    container_id: str,
    request: Request,
    response: Response,
) -> Container:
    s: Service = get_service(Container, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "container_id": container_id,
        "request": request,
        "response": response,
    }
    return cast(Container, s.get(**b))


@router.post(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/OperatingSystem/Containers/{container_id}/Actions/Container.Reset",
    response_model_exclude_none=True,
)
@authenticate
async def reset2(
    resource_block_id: str,
    computer_system_id: str,
    container_id: str,
    request: Request,
    response: Response,
    body: ResetRequest,
) -> RedfishError:
    s: Service = get_service(Container, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "container_id": container_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Reset",
    }
    return s.action(**b)


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/OperatingSystem/Containers/{container_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/OperatingSystem/Containers/{container_id}",
    response_model_exclude_none=True,
)
async def get3(
    resource_block_id: str,
    computer_system_id: str,
    container_id: str,
    request: Request,
    response: Response,
) -> Container:
    s: Service = get_service(Container, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "container_id": container_id,
        "request": request,
        "response": response,
    }
    return cast(Container, s.get(**b))


@router.post(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/OperatingSystem/Containers/{container_id}/Actions/Container.Reset",
    response_model_exclude_none=True,
)
@authenticate
async def reset3(
    resource_block_id: str,
    computer_system_id: str,
    container_id: str,
    request: Request,
    response: Response,
    body: ResetRequest,
) -> RedfishError:
    s: Service = get_service(Container, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "container_id": container_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Reset",
    }
    return s.action(**b)
