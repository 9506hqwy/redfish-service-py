from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.boot_option import BootOption, BootOptionOnCreate
from ..model.boot_option_collection import BootOptionCollection
from ..service import Service, ServiceCollection
from ..util import get_service, get_service_collection, set_link_header

router = APIRouter()


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/BootOptions", response_model_exclude_none=True
)
@router.head(
    "/redfish/v1/Systems/{computer_system_id}/BootOptions", response_model_exclude_none=True
)
async def get1(
    computer_system_id: str, request: Request, response: Response
) -> BootOptionCollection:
    s: Service = get_service(BootOptionCollection, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "request": request,
        "response": response,
    }
    m = cast(BootOptionCollection, s.get(**b))
    set_link_header(m, response)
    return m


@router.post(
    "/redfish/v1/Systems/{computer_system_id}/BootOptions", response_model_exclude_none=True
)
@router.post(
    "/redfish/v1/Systems/{computer_system_id}/BootOptions/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post1(
    computer_system_id: str, request: Request, response: Response, body: BootOptionOnCreate
) -> BootOption:
    s: ServiceCollection = get_service_collection(BootOptionCollection, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(BootOption, s.post(**b))


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/BootOptions",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/BootOptions",
    response_model_exclude_none=True,
)
async def get2(
    resource_block_id: str, computer_system_id: str, request: Request, response: Response
) -> BootOptionCollection:
    s: Service = get_service(BootOptionCollection, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "request": request,
        "response": response,
    }
    m = cast(BootOptionCollection, s.get(**b))
    set_link_header(m, response)
    return m


@router.post(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/BootOptions",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/BootOptions/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post2(
    resource_block_id: str,
    computer_system_id: str,
    request: Request,
    response: Response,
    body: BootOptionOnCreate,
) -> BootOption:
    s: ServiceCollection = get_service_collection(BootOptionCollection, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(BootOption, s.post(**b))


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/BootOptions",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/BootOptions",
    response_model_exclude_none=True,
)
async def get3(
    resource_block_id: str, computer_system_id: str, request: Request, response: Response
) -> BootOptionCollection:
    s: Service = get_service(BootOptionCollection, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "request": request,
        "response": response,
    }
    m = cast(BootOptionCollection, s.get(**b))
    set_link_header(m, response)
    return m


@router.post(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/BootOptions",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/BootOptions/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post3(
    resource_block_id: str,
    computer_system_id: str,
    request: Request,
    response: Response,
    body: BootOptionOnCreate,
) -> BootOption:
    s: ServiceCollection = get_service_collection(BootOptionCollection, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(BootOption, s.post(**b))
