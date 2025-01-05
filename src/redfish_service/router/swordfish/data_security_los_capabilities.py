from typing import Any, cast

from fastapi import APIRouter

from ...model.swordfish.data_security_los_capabilities import DataSecurityLosCapabilities
from ...service import Service, find_service
from .. import authenticate

router = APIRouter()


@router.get(
    "/redfish/v1/StorageServices/{storage_service_id}/DataSecurityLoSCapabilities",
    response_model_exclude_none=True,
)
@authenticate
async def get1(storage_service_id: str) -> DataSecurityLosCapabilities:
    s: Service = find_service(DataSecurityLosCapabilities)
    b: dict[str, Any] = {"storage_service_id": storage_service_id}
    return cast(DataSecurityLosCapabilities, s.get(**b))
