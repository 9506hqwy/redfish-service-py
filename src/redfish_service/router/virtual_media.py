from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.redfish_error import RedfishError
from ..model.virtual_media import InsertMediaRequest, VirtualMedia, VirtualMediaOnUpdate
from ..service import Service
from ..util import get_service, set_link_header

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
    m = cast(VirtualMedia, s.get(**b))
    set_link_header(m, response)
    return m


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
    return cast(VirtualMedia, s.patch(**b))


@router.post(
    "/redfish/v1/Managers/{manager_id}/VirtualMedia/{virtual_media_id}/Actions/VirtualMedia.InsertMedia",
    response_model_exclude_none=True,
)
@authenticate
async def insert_media1(
    manager_id: str,
    virtual_media_id: str,
    request: Request,
    response: Response,
    body: InsertMediaRequest,
) -> RedfishError:
    s: Service = get_service(VirtualMedia, request)
    b: dict[str, Any] = {
        "manager_id": manager_id,
        "virtual_media_id": virtual_media_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "InsertMedia",
    }
    return s.action(**b)


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
    m = cast(VirtualMedia, s.get(**b))
    set_link_header(m, response)
    return m


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
    return cast(VirtualMedia, s.patch(**b))


@router.post(
    "/redfish/v1/Systems/{computer_system_id}/VirtualMedia/{virtual_media_id}/Actions/VirtualMedia.InsertMedia",
    response_model_exclude_none=True,
)
@authenticate
async def insert_media2(
    computer_system_id: str,
    virtual_media_id: str,
    request: Request,
    response: Response,
    body: InsertMediaRequest,
) -> RedfishError:
    s: Service = get_service(VirtualMedia, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "virtual_media_id": virtual_media_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "InsertMedia",
    }
    return s.action(**b)


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
    m = cast(VirtualMedia, s.get(**b))
    set_link_header(m, response)
    return m


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
    return cast(VirtualMedia, s.patch(**b))


@router.post(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/VirtualMedia/{virtual_media_id}/Actions/VirtualMedia.InsertMedia",
    response_model_exclude_none=True,
)
@authenticate
async def insert_media3(
    resource_block_id: str,
    computer_system_id: str,
    virtual_media_id: str,
    request: Request,
    response: Response,
    body: InsertMediaRequest,
) -> RedfishError:
    s: Service = get_service(VirtualMedia, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "virtual_media_id": virtual_media_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "InsertMedia",
    }
    return s.action(**b)


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
    m = cast(VirtualMedia, s.get(**b))
    set_link_header(m, response)
    return m


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
    return cast(VirtualMedia, s.patch(**b))


@router.post(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/VirtualMedia/{virtual_media_id}/Actions/VirtualMedia.InsertMedia",
    response_model_exclude_none=True,
)
@authenticate
async def insert_media4(
    resource_block_id: str,
    computer_system_id: str,
    virtual_media_id: str,
    request: Request,
    response: Response,
    body: InsertMediaRequest,
) -> RedfishError:
    s: Service = get_service(VirtualMedia, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "virtual_media_id": virtual_media_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "InsertMedia",
    }
    return s.action(**b)
