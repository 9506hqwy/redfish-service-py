from typing import Any, cast

from fastapi import APIRouter

from ...authenticate import authenticate
from ...model.swordfish.storage_system_collection import StorageSystemCollection
from ...service import Service, find_service

router = APIRouter()


@router.get("/redfish/v1/StorageSystems", response_model_exclude_none=True)
@authenticate
async def get1() -> StorageSystemCollection:
    s: Service = find_service(StorageSystemCollection)
    b: dict[str, Any] = {}
    return cast(StorageSystemCollection, s.get(**b))
