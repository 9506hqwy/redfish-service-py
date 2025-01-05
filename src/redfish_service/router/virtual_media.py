from typing import Any, cast

from fastapi import APIRouter

from ..model.virtual_media import VirtualMedia
from ..service import Service, find_service
from . import authenticate

router = APIRouter()


@router.get(
    "/redfish/v1/Managers/{manager_id}/VirtualMedia/{virtual_media_id}",
    response_model_exclude_none=True,
)
@authenticate
async def get1(manager_id: str, virtual_media_id: str) -> VirtualMedia:
    s: Service = find_service(VirtualMedia)
    b: dict[str, Any] = {"manager_id": manager_id, "virtual_media_id": virtual_media_id}
    return cast(VirtualMedia, s.get(**b))


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/VirtualMedia/{virtual_media_id}",
    response_model_exclude_none=True,
)
@authenticate
async def get2(computer_system_id: str, virtual_media_id: str) -> VirtualMedia:
    s: Service = find_service(VirtualMedia)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "virtual_media_id": virtual_media_id,
    }
    return cast(VirtualMedia, s.get(**b))


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/VirtualMedia/{virtual_media_id}",
    response_model_exclude_none=True,
)
@authenticate
async def get3(
    resource_block_id: str, computer_system_id: str, virtual_media_id: str
) -> VirtualMedia:
    s: Service = find_service(VirtualMedia)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "virtual_media_id": virtual_media_id,
    }
    return cast(VirtualMedia, s.get(**b))


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/VirtualMedia/{virtual_media_id}",
    response_model_exclude_none=True,
)
@authenticate
async def get4(
    resource_block_id: str, computer_system_id: str, virtual_media_id: str
) -> VirtualMedia:
    s: Service = find_service(VirtualMedia)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "virtual_media_id": virtual_media_id,
    }
    return cast(VirtualMedia, s.get(**b))
