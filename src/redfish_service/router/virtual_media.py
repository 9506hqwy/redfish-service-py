from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.virtual_media import VirtualMedia, VirtualMediaOnUpdate
from ..service import Service
from ..util import get_service

router = APIRouter()


@router.get(
    "/redfish/v1/Managers/{manager_id}/VirtualMedia/{virtual_media_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Managers/{manager_id}/VirtualMedia/{virtual_media_id}",
    response_model_exclude_none=True,
)
async def get1(
    manager_id: str, virtual_media_id: str, request: Request, response: Response
) -> VirtualMedia:
    s: Service = get_service(VirtualMedia, request)
    b: dict[str, Any] = {
        "manager_id": manager_id,
        "virtual_media_id": virtual_media_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(VirtualMedia, s.get(**b))


@router.patch(
    "/redfish/v1/Managers/{manager_id}/VirtualMedia/{virtual_media_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch1(
    manager_id: str,
    virtual_media_id: str,
    request: Request,
    response: Response,
    body: VirtualMediaOnUpdate,
) -> VirtualMedia:
    s: Service = get_service(VirtualMedia, request)
    b: dict[str, Any] = {
        "manager_id": manager_id,
        "virtual_media_id": virtual_media_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(VirtualMedia, s.patch(**b))


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/VirtualMedia/{virtual_media_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Systems/{computer_system_id}/VirtualMedia/{virtual_media_id}",
    response_model_exclude_none=True,
)
async def get2(
    computer_system_id: str, virtual_media_id: str, request: Request, response: Response
) -> VirtualMedia:
    s: Service = get_service(VirtualMedia, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "virtual_media_id": virtual_media_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(VirtualMedia, s.get(**b))


@router.patch(
    "/redfish/v1/Systems/{computer_system_id}/VirtualMedia/{virtual_media_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch2(
    computer_system_id: str,
    virtual_media_id: str,
    request: Request,
    response: Response,
    body: VirtualMediaOnUpdate,
) -> VirtualMedia:
    s: Service = get_service(VirtualMedia, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "virtual_media_id": virtual_media_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(VirtualMedia, s.patch(**b))


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/VirtualMedia/{virtual_media_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/VirtualMedia/{virtual_media_id}",
    response_model_exclude_none=True,
)
async def get3(
    resource_block_id: str,
    computer_system_id: str,
    virtual_media_id: str,
    request: Request,
    response: Response,
) -> VirtualMedia:
    s: Service = get_service(VirtualMedia, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "virtual_media_id": virtual_media_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(VirtualMedia, s.get(**b))


@router.patch(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/VirtualMedia/{virtual_media_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch3(
    resource_block_id: str,
    computer_system_id: str,
    virtual_media_id: str,
    request: Request,
    response: Response,
    body: VirtualMediaOnUpdate,
) -> VirtualMedia:
    s: Service = get_service(VirtualMedia, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "virtual_media_id": virtual_media_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(VirtualMedia, s.patch(**b))


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/VirtualMedia/{virtual_media_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/VirtualMedia/{virtual_media_id}",
    response_model_exclude_none=True,
)
async def get4(
    resource_block_id: str,
    computer_system_id: str,
    virtual_media_id: str,
    request: Request,
    response: Response,
) -> VirtualMedia:
    s: Service = get_service(VirtualMedia, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "virtual_media_id": virtual_media_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(VirtualMedia, s.get(**b))


@router.patch(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/VirtualMedia/{virtual_media_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch4(
    resource_block_id: str,
    computer_system_id: str,
    virtual_media_id: str,
    request: Request,
    response: Response,
    body: VirtualMediaOnUpdate,
) -> VirtualMedia:
    s: Service = get_service(VirtualMedia, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "virtual_media_id": virtual_media_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(VirtualMedia, s.patch(**b))
