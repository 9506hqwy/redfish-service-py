from typing import Any, cast

from fastapi import APIRouter

from ...model.swordfish.class_of_service import ClassOfService
from ...service import Service, find_service
from .. import authenticate

router = APIRouter()


@router.get(
    "/redfish/v1/StorageServices/{storage_service_id}/ClassesOfService/{class_of_service_id}",
    response_model_exclude_none=True,
)
@authenticate
async def get1(storage_service_id: str, class_of_service_id: str) -> ClassOfService:
    s: Service = find_service(ClassOfService)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "class_of_service_id": class_of_service_id,
    }
    return cast(ClassOfService, s.get(**b))


@router.get(
    "/redfish/v1/StorageServices/{storage_service_id}/StoragePools/{storage_pool_id}/ClassesOfService/{class_of_service_id}",
    response_model_exclude_none=True,
)
@authenticate
async def get2(
    storage_service_id: str, storage_pool_id: str, class_of_service_id: str
) -> ClassOfService:
    s: Service = find_service(ClassOfService)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "storage_pool_id": storage_pool_id,
        "class_of_service_id": class_of_service_id,
    }
    return cast(ClassOfService, s.get(**b))
