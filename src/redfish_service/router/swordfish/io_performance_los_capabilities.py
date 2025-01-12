from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ...authenticate import authenticate
from ...model.swordfish.io_performance_los_capabilities import (
    IoPerformanceLosCapabilities,
    IoPerformanceLosCapabilitiesOnUpdate,
)
from ...service import Service
from ...util import get_service

router = APIRouter()


@router.get(
    "/redfish/v1/StorageServices/{storage_service_id}/IOPerformanceLoSCapabilities",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/StorageServices/{storage_service_id}/IOPerformanceLoSCapabilities",
    response_model_exclude_none=True,
)
async def get1(
    storage_service_id: str, request: Request, response: Response
) -> IoPerformanceLosCapabilities:
    s: Service = get_service(IoPerformanceLosCapabilities, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "request": request,
        "response": response,
    }
    return cast(IoPerformanceLosCapabilities, s.get(**b))


@router.patch(
    "/redfish/v1/StorageServices/{storage_service_id}/IOPerformanceLoSCapabilities",
    response_model_exclude_none=True,
)
@authenticate
async def patch1(
    storage_service_id: str,
    request: Request,
    response: Response,
    body: IoPerformanceLosCapabilitiesOnUpdate,
) -> IoPerformanceLosCapabilities:
    s: Service = get_service(IoPerformanceLosCapabilities, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(IoPerformanceLosCapabilities, s.patch(**b))
