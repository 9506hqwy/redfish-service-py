from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..model.network_interface_collection import NetworkInterfaceCollection
from ..service import Service
from ..util import get_service, set_link_header

router = APIRouter()


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/NetworkInterfaces", response_model_exclude_none=True
)
@router.head(
    "/redfish/v1/Systems/{computer_system_id}/NetworkInterfaces", response_model_exclude_none=True
)
async def get1(
    computer_system_id: str, request: Request, response: Response
) -> NetworkInterfaceCollection:
    s: Service = get_service(NetworkInterfaceCollection, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "request": request,
        "response": response,
    }
    m = cast(NetworkInterfaceCollection, s.get(**b))
    set_link_header(m, response)
    return m


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/NetworkInterfaces",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/NetworkInterfaces",
    response_model_exclude_none=True,
)
async def get2(
    resource_block_id: str, computer_system_id: str, request: Request, response: Response
) -> NetworkInterfaceCollection:
    s: Service = get_service(NetworkInterfaceCollection, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "request": request,
        "response": response,
    }
    m = cast(NetworkInterfaceCollection, s.get(**b))
    set_link_header(m, response)
    return m


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/NetworkInterfaces",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/NetworkInterfaces",
    response_model_exclude_none=True,
)
async def get3(
    resource_block_id: str, computer_system_id: str, request: Request, response: Response
) -> NetworkInterfaceCollection:
    s: Service = get_service(NetworkInterfaceCollection, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "request": request,
        "response": response,
    }
    m = cast(NetworkInterfaceCollection, s.get(**b))
    set_link_header(m, response)
    return m
