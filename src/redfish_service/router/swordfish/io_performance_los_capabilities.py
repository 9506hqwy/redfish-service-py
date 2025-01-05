from typing import Any, cast

from fastapi import APIRouter

from ...authenticate import authenticate
from ...model.swordfish.io_performance_los_capabilities import IoPerformanceLosCapabilities
from ...service import Service, find_service

router = APIRouter()


@router.get(
    "/redfish/v1/StorageServices/{storage_service_id}/IOPerformanceLoSCapabilities",
    response_model_exclude_none=True,
)
@authenticate
async def get1(storage_service_id: str) -> IoPerformanceLosCapabilities:
    s: Service = find_service(IoPerformanceLosCapabilities)
    b: dict[str, Any] = {"storage_service_id": storage_service_id}
    return cast(IoPerformanceLosCapabilities, s.get(**b))
