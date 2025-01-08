from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ...model.swordfish.io_performance_line_of_service import IoPerformanceLineOfService
from ...service import Service, find_service

router = APIRouter()


@router.get(
    "/redfish/v1/StorageServices/{storage_service_id}/LinesOfService/IOPerformanceLinesOfService/{io_performance_line_of_service_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/StorageServices/{storage_service_id}/LinesOfService/IOPerformanceLinesOfService/{io_performance_line_of_service_id}",
    response_model_exclude_none=True,
)
async def get1(
    storage_service_id: str,
    io_performance_line_of_service_id: str,
    request: Request,
    response: Response,
) -> IoPerformanceLineOfService:
    s: Service = find_service(IoPerformanceLineOfService)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "io_performance_line_of_service_id": io_performance_line_of_service_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(IoPerformanceLineOfService, s.get(**b))


@router.get(
    "/redfish/v1/StorageServices/{storage_service_id}/ClassesOfService/{class_of_service_id}/IOPerformanceLinesOfService/{io_performance_line_of_service_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/StorageServices/{storage_service_id}/ClassesOfService/{class_of_service_id}/IOPerformanceLinesOfService/{io_performance_line_of_service_id}",
    response_model_exclude_none=True,
)
async def get2(
    storage_service_id: str,
    class_of_service_id: str,
    io_performance_line_of_service_id: str,
    request: Request,
    response: Response,
) -> IoPerformanceLineOfService:
    s: Service = find_service(IoPerformanceLineOfService)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "class_of_service_id": class_of_service_id,
        "io_performance_line_of_service_id": io_performance_line_of_service_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(IoPerformanceLineOfService, s.get(**b))
