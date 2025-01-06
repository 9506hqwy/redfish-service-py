from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ...authenticate import authenticate
from ...model.swordfish.io_performance_los_capabilities import IoPerformanceLosCapabilities
from ...service import Service, find_service

router = APIRouter()


@router.get(
    "/redfish/v1/StorageServices/{storage_service_id}/IOPerformanceLoSCapabilities",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/StorageServices/{storage_service_id}/IOPerformanceLoSCapabilities",
    response_model_exclude_none=True,
)
@authenticate
async def get1(
    storage_service_id: str, request: Request, response: Response
) -> IoPerformanceLosCapabilities:
    s: Service = find_service(IoPerformanceLosCapabilities)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(IoPerformanceLosCapabilities, s.get(**b))
