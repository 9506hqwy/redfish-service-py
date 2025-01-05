from typing import Any, cast

from fastapi import APIRouter

from ...model.swordfish.data_protection_los_capabilities import DataProtectionLosCapabilities
from ...service import Service, find_service
from .. import authenticate

router = APIRouter()


@router.get(
    "/redfish/v1/StorageServices/{storage_service_id}/DataProtectionLoSCapabilities",
    response_model_exclude_none=True,
)
@authenticate
async def get1(storage_service_id: str) -> DataProtectionLosCapabilities:
    s: Service = find_service(DataProtectionLosCapabilities)
    b: dict[str, Any] = {"storage_service_id": storage_service_id}
    return cast(DataProtectionLosCapabilities, s.get(**b))
