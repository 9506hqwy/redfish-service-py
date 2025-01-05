from typing import Any, cast

from fastapi import APIRouter

from ..model.boot_option_collection import BootOptionCollection
from ..service import Service, find_service
from . import authenticate

router = APIRouter()


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/BootOptions", response_model_exclude_none=True
)
@authenticate
async def get1(computer_system_id: str) -> BootOptionCollection:
    s: Service = find_service(BootOptionCollection)
    b: dict[str, Any] = {"computer_system_id": computer_system_id}
    return cast(BootOptionCollection, s.get(**b))


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/BootOptions",
    response_model_exclude_none=True,
)
@authenticate
async def get2(resource_block_id: str, computer_system_id: str) -> BootOptionCollection:
    s: Service = find_service(BootOptionCollection)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
    }
    return cast(BootOptionCollection, s.get(**b))


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/BootOptions",
    response_model_exclude_none=True,
)
@authenticate
async def get3(resource_block_id: str, computer_system_id: str) -> BootOptionCollection:
    s: Service = find_service(BootOptionCollection)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
    }
    return cast(BootOptionCollection, s.get(**b))
