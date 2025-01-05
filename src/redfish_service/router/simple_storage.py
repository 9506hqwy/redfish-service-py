from typing import Any, cast

from fastapi import APIRouter

from ..authenticate import authenticate
from ..model.simple_storage import SimpleStorage
from ..service import Service, find_service

router = APIRouter()


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/SimpleStorage/{simple_storage_id}",
    response_model_exclude_none=True,
)
@authenticate
async def get1(computer_system_id: str, simple_storage_id: str) -> SimpleStorage:
    s: Service = find_service(SimpleStorage)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "simple_storage_id": simple_storage_id,
    }
    return cast(SimpleStorage, s.get(**b))


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/SimpleStorage/{simple_storage_id}",
    response_model_exclude_none=True,
)
@authenticate
async def get2(resource_block_id: str, simple_storage_id: str) -> SimpleStorage:
    s: Service = find_service(SimpleStorage)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "simple_storage_id": simple_storage_id,
    }
    return cast(SimpleStorage, s.get(**b))


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/SimpleStorage/{simple_storage_id}",
    response_model_exclude_none=True,
)
@authenticate
async def get3(
    resource_block_id: str, computer_system_id: str, simple_storage_id: str
) -> SimpleStorage:
    s: Service = find_service(SimpleStorage)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "simple_storage_id": simple_storage_id,
    }
    return cast(SimpleStorage, s.get(**b))


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/SimpleStorage/{simple_storage_id}",
    response_model_exclude_none=True,
)
@authenticate
async def get4(resource_block_id: str, simple_storage_id: str) -> SimpleStorage:
    s: Service = find_service(SimpleStorage)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "simple_storage_id": simple_storage_id,
    }
    return cast(SimpleStorage, s.get(**b))


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/SimpleStorage/{simple_storage_id}",
    response_model_exclude_none=True,
)
@authenticate
async def get5(
    resource_block_id: str, computer_system_id: str, simple_storage_id: str
) -> SimpleStorage:
    s: Service = find_service(SimpleStorage)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "simple_storage_id": simple_storage_id,
    }
    return cast(SimpleStorage, s.get(**b))
