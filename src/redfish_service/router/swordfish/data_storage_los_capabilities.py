from typing import Any, cast

from fastapi import APIRouter

from ...model.swordfish.data_storage_los_capabilities import DataStorageLosCapabilities
from ...service import Service, find_service
from .. import authenticate

router = APIRouter()


@router.get(
    "/redfish/v1/StorageServices/{storage_service_id}/DataStorageLoSCapabilities",
    response_model_exclude_none=True,
)
@authenticate
async def get1(storage_service_id: str) -> DataStorageLosCapabilities:
    s: Service = find_service(DataStorageLosCapabilities)
    b: dict[str, Any] = {"storage_service_id": storage_service_id}
    return cast(DataStorageLosCapabilities, s.get(**b))
