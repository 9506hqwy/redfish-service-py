from typing import Any, cast

from fastapi import APIRouter

from ..model.container_image import ContainerImage
from ..service import Service, find_service
from . import authenticate

router = APIRouter()


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/OperatingSystem/ContainerImages/{container_image_id}",
    response_model_exclude_none=True,
)
@authenticate
async def get1(computer_system_id: str, container_image_id: str) -> ContainerImage:
    s: Service = find_service(ContainerImage)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "container_image_id": container_image_id,
    }
    return cast(ContainerImage, s.get(**b))


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/OperatingSystem/ContainerImages/{container_image_id}",
    response_model_exclude_none=True,
)
@authenticate
async def get2(
    resource_block_id: str, computer_system_id: str, container_image_id: str
) -> ContainerImage:
    s: Service = find_service(ContainerImage)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "container_image_id": container_image_id,
    }
    return cast(ContainerImage, s.get(**b))


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/OperatingSystem/ContainerImages/{container_image_id}",
    response_model_exclude_none=True,
)
@authenticate
async def get3(
    resource_block_id: str, computer_system_id: str, container_image_id: str
) -> ContainerImage:
    s: Service = find_service(ContainerImage)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "container_image_id": container_image_id,
    }
    return cast(ContainerImage, s.get(**b))
