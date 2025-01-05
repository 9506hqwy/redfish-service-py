from typing import Any, cast

from fastapi import APIRouter

from ...model.swordfish.io_connectivity_los_capabilities import IoConnectivityLosCapabilities
from ...service import Service, find_service
from .. import authenticate

router = APIRouter()


@router.get(
    "/redfish/v1/StorageServices/{storage_service_id}/IOConnectivityLoSCapabilities",
    response_model_exclude_none=True,
)
@authenticate
async def get1(storage_service_id: str) -> IoConnectivityLosCapabilities:
    s: Service = find_service(IoConnectivityLosCapabilities)
    b: dict[str, Any] = {"storage_service_id": storage_service_id}
    return cast(IoConnectivityLosCapabilities, s.get(**b))
