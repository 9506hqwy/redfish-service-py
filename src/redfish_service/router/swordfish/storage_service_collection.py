from typing import Any, cast

from fastapi import APIRouter

from ...authenticate import authenticate
from ...model.swordfish.storage_service_collection import StorageServiceCollection
from ...service import Service, find_service

router = APIRouter()


@router.get("/redfish/v1/StorageServices", response_model_exclude_none=True)
@authenticate
async def get1() -> StorageServiceCollection:
    s: Service = find_service(StorageServiceCollection)
    b: dict[str, Any] = {}
    return cast(StorageServiceCollection, s.get(**b))


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/StorageServices", response_model_exclude_none=True
)
@authenticate
async def get2(computer_system_id: str) -> StorageServiceCollection:
    s: Service = find_service(StorageServiceCollection)
    b: dict[str, Any] = {"computer_system_id": computer_system_id}
    return cast(StorageServiceCollection, s.get(**b))
