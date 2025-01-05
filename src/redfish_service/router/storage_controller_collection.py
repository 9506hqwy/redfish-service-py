from typing import Any, cast

from fastapi import APIRouter

from ..model.storage_controller_collection import StorageControllerCollection
from ..service import Service, find_service
from . import authenticate

router = APIRouter()


@router.get("/redfish/v1/Storage/{storage_id}/Controllers", response_model_exclude_none=True)
@authenticate
async def get1(storage_id: str) -> StorageControllerCollection:
    s: Service = find_service(StorageControllerCollection)
    b: dict[str, Any] = {"storage_id": storage_id}
    return cast(StorageControllerCollection, s.get(**b))


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/Controllers",
    response_model_exclude_none=True,
)
@authenticate
async def get2(computer_system_id: str, storage_id: str) -> StorageControllerCollection:
    s: Service = find_service(StorageControllerCollection)
    b: dict[str, Any] = {"computer_system_id": computer_system_id, "storage_id": storage_id}
    return cast(StorageControllerCollection, s.get(**b))


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Storage/{storage_id}/Controllers",
    response_model_exclude_none=True,
)
@authenticate
async def get3(resource_block_id: str, storage_id: str) -> StorageControllerCollection:
    s: Service = find_service(StorageControllerCollection)
    b: dict[str, Any] = {"resource_block_id": resource_block_id, "storage_id": storage_id}
    return cast(StorageControllerCollection, s.get(**b))


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Storage/{storage_id}/Controllers",
    response_model_exclude_none=True,
)
@authenticate
async def get4(
    resource_block_id: str, computer_system_id: str, storage_id: str
) -> StorageControllerCollection:
    s: Service = find_service(StorageControllerCollection)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
    }
    return cast(StorageControllerCollection, s.get(**b))


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Storage/{storage_id}/Controllers",
    response_model_exclude_none=True,
)
@authenticate
async def get5(resource_block_id: str, storage_id: str) -> StorageControllerCollection:
    s: Service = find_service(StorageControllerCollection)
    b: dict[str, Any] = {"resource_block_id": resource_block_id, "storage_id": storage_id}
    return cast(StorageControllerCollection, s.get(**b))


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Storage/{storage_id}/Controllers",
    response_model_exclude_none=True,
)
@authenticate
async def get6(
    resource_block_id: str, computer_system_id: str, storage_id: str
) -> StorageControllerCollection:
    s: Service = find_service(StorageControllerCollection)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
    }
    return cast(StorageControllerCollection, s.get(**b))
