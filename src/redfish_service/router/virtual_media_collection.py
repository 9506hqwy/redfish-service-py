from typing import Any, cast

from fastapi import APIRouter

from ..authenticate import authenticate
from ..model.virtual_media_collection import VirtualMediaCollection
from ..service import Service, find_service

router = APIRouter()


@router.get("/redfish/v1/Managers/{manager_id}/VirtualMedia", response_model_exclude_none=True)
@authenticate
async def get1(manager_id: str) -> VirtualMediaCollection:
    s: Service = find_service(VirtualMediaCollection)
    b: dict[str, Any] = {"manager_id": manager_id}
    return cast(VirtualMediaCollection, s.get(**b))


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/VirtualMedia", response_model_exclude_none=True
)
@authenticate
async def get2(computer_system_id: str) -> VirtualMediaCollection:
    s: Service = find_service(VirtualMediaCollection)
    b: dict[str, Any] = {"computer_system_id": computer_system_id}
    return cast(VirtualMediaCollection, s.get(**b))


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/VirtualMedia",
    response_model_exclude_none=True,
)
@authenticate
async def get3(resource_block_id: str, computer_system_id: str) -> VirtualMediaCollection:
    s: Service = find_service(VirtualMediaCollection)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
    }
    return cast(VirtualMediaCollection, s.get(**b))


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/VirtualMedia",
    response_model_exclude_none=True,
)
@authenticate
async def get4(resource_block_id: str, computer_system_id: str) -> VirtualMediaCollection:
    s: Service = find_service(VirtualMediaCollection)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
    }
    return cast(VirtualMediaCollection, s.get(**b))
