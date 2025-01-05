from typing import Any, cast

from fastapi import APIRouter

from ...model.swordfish.storage_service import StorageService
from ...service import Service, find_service
from .. import authenticate

router = APIRouter()


@router.get("/redfish/v1/StorageServices/{storage_service_id}", response_model_exclude_none=True)
@authenticate
async def get1(storage_service_id: str) -> StorageService:
    s: Service = find_service(StorageService)
    b: dict[str, Any] = {"storage_service_id": storage_service_id}
    return cast(StorageService, s.get(**b))


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/StorageServices/{storage_service_id}",
    response_model_exclude_none=True,
)
@authenticate
async def get2(computer_system_id: str, storage_service_id: str) -> StorageService:
    s: Service = find_service(StorageService)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_service_id": storage_service_id,
    }
    return cast(StorageService, s.get(**b))
