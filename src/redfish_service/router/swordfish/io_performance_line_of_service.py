from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ...authenticate import authenticate
from ...model.swordfish.io_performance_line_of_service import (
    IoPerformanceLineOfService,
    IoPerformanceLineOfServiceOnUpdate,
)
from ...service import Service
from ...util import get_service, set_link_header

router = APIRouter()


@router.delete(
    "/redfish/v1/StorageServices/{storage_service_id}/LinesOfService/IOPerformanceLinesOfService/{io_performance_line_of_service_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete1(
    storage_service_id: str,
    io_performance_line_of_service_id: str,
    request: Request,
    response: Response,
) -> None:
    s: Service = get_service(IoPerformanceLineOfService, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "io_performance_line_of_service_id": io_performance_line_of_service_id,
        "request": request,
        "response": response,
    }
    return s.delete(**b)


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
    s: Service = get_service(IoPerformanceLineOfService, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "io_performance_line_of_service_id": io_performance_line_of_service_id,
        "request": request,
        "response": response,
    }
    m = cast(IoPerformanceLineOfService, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/StorageServices/{storage_service_id}/LinesOfService/IOPerformanceLinesOfService/{io_performance_line_of_service_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch1(
    storage_service_id: str,
    io_performance_line_of_service_id: str,
    request: Request,
    response: Response,
    body: IoPerformanceLineOfServiceOnUpdate,
) -> IoPerformanceLineOfService:
    s: Service = get_service(IoPerformanceLineOfService, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "io_performance_line_of_service_id": io_performance_line_of_service_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(IoPerformanceLineOfService, s.patch(**b))


@router.delete(
    "/redfish/v1/StorageServices/{storage_service_id}/ClassesOfService/{class_of_service_id}/IOPerformanceLinesOfService/{io_performance_line_of_service_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete2(
    storage_service_id: str,
    class_of_service_id: str,
    io_performance_line_of_service_id: str,
    request: Request,
    response: Response,
) -> None:
    s: Service = get_service(IoPerformanceLineOfService, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "class_of_service_id": class_of_service_id,
        "io_performance_line_of_service_id": io_performance_line_of_service_id,
        "request": request,
        "response": response,
    }
    return s.delete(**b)


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
    s: Service = get_service(IoPerformanceLineOfService, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "class_of_service_id": class_of_service_id,
        "io_performance_line_of_service_id": io_performance_line_of_service_id,
        "request": request,
        "response": response,
    }
    m = cast(IoPerformanceLineOfService, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/StorageServices/{storage_service_id}/ClassesOfService/{class_of_service_id}/IOPerformanceLinesOfService/{io_performance_line_of_service_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch2(
    storage_service_id: str,
    class_of_service_id: str,
    io_performance_line_of_service_id: str,
    request: Request,
    response: Response,
    body: IoPerformanceLineOfServiceOnUpdate,
) -> IoPerformanceLineOfService:
    s: Service = get_service(IoPerformanceLineOfService, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "class_of_service_id": class_of_service_id,
        "io_performance_line_of_service_id": io_performance_line_of_service_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(IoPerformanceLineOfService, s.patch(**b))
