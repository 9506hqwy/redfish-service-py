from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ...model.swordfish.storage_service_metrics import StorageServiceMetrics
from ...service import Service
from ...util import get_service, set_link_header

router = APIRouter()


@router.get(
    "/redfish/v1/StorageServices/{storage_service_id}/Metrics", response_model_exclude_none=True
)
@router.head(
    "/redfish/v1/StorageServices/{storage_service_id}/Metrics", response_model_exclude_none=True
)
async def get1(
    storage_service_id: str, request: Request, response: Response
) -> StorageServiceMetrics:
    s: Service = get_service(StorageServiceMetrics, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "request": request,
        "response": response,
    }
    m = cast(StorageServiceMetrics, s.get(**b))
    set_link_header(m, response)
    return m


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/StorageServices/{storage_service_id}/Metrics",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Systems/{computer_system_id}/StorageServices/{storage_service_id}/Metrics",
    response_model_exclude_none=True,
)
async def get2(
    computer_system_id: str, storage_service_id: str, request: Request, response: Response
) -> StorageServiceMetrics:
    s: Service = get_service(StorageServiceMetrics, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_service_id": storage_service_id,
        "request": request,
        "response": response,
    }
    m = cast(StorageServiceMetrics, s.get(**b))
    set_link_header(m, response)
    return m
