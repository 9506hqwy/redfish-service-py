from typing import Any, cast

from fastapi import APIRouter

from ...model.swordfish.storage_group import StorageGroup
from ...service import Service, find_service
from .. import authenticate

router = APIRouter()


@router.get(
    "/redfish/v1/StorageServices/{storage_service_id}/StorageGroups/{storage_group_id}",
    response_model_exclude_none=True,
)
@authenticate
async def get1(storage_service_id: str, storage_group_id: str) -> StorageGroup:
    s: Service = find_service(StorageGroup)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "storage_group_id": storage_group_id,
    }
    return cast(StorageGroup, s.get(**b))


@router.get(
    "/redfish/v1/StorageServices/{storage_service_id}/Volumes/{volume_id}/StorageGroups/{storage_group_id}",
    response_model_exclude_none=True,
)
@authenticate
async def get2(storage_service_id: str, volume_id: str, storage_group_id: str) -> StorageGroup:
    s: Service = find_service(StorageGroup)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "volume_id": volume_id,
        "storage_group_id": storage_group_id,
    }
    return cast(StorageGroup, s.get(**b))


@router.get(
    "/redfish/v1/Storage/{storage_id}/StorageGroups/{storage_group_id}",
    response_model_exclude_none=True,
)
@authenticate
async def get3(storage_id: str, storage_group_id: str) -> StorageGroup:
    s: Service = find_service(StorageGroup)
    b: dict[str, Any] = {"storage_id": storage_id, "storage_group_id": storage_group_id}
    return cast(StorageGroup, s.get(**b))


@router.get(
    "/redfish/v1/Storage/{storage_id}/Volumes/{volume_id}/StorageGroups/{storage_group_id}",
    response_model_exclude_none=True,
)
@authenticate
async def get4(storage_id: str, volume_id: str, storage_group_id: str) -> StorageGroup:
    s: Service = find_service(StorageGroup)
    b: dict[str, Any] = {
        "storage_id": storage_id,
        "volume_id": volume_id,
        "storage_group_id": storage_group_id,
    }
    return cast(StorageGroup, s.get(**b))
