from typing import Any, cast

from fastapi import APIRouter

from ...authenticate import authenticate
from ...model.swordfish.class_of_service_collection import ClassOfServiceCollection
from ...service import Service, find_service

router = APIRouter()


@router.get(
    "/redfish/v1/StorageServices/{storage_service_id}/ClassesOfService",
    response_model_exclude_none=True,
)
@authenticate
async def get1(storage_service_id: str) -> ClassOfServiceCollection:
    s: Service = find_service(ClassOfServiceCollection)
    b: dict[str, Any] = {"storage_service_id": storage_service_id}
    return cast(ClassOfServiceCollection, s.get(**b))


@router.get(
    "/redfish/v1/StorageServices/{storage_service_id}/StoragePools/{storage_pool_id}/ClassesOfService",
    response_model_exclude_none=True,
)
@authenticate
async def get2(storage_service_id: str, storage_pool_id: str) -> ClassOfServiceCollection:
    s: Service = find_service(ClassOfServiceCollection)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "storage_pool_id": storage_pool_id,
    }
    return cast(ClassOfServiceCollection, s.get(**b))
