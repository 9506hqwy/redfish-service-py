from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ...model.swordfish.file_system_metrics import FileSystemMetrics
from ...service import Service
from ...util import get_service

router = APIRouter()


@router.get(
    "/redfish/v1/StorageServices/{storage_service_id}/FileSystems/{file_system_id}/Metrics",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/StorageServices/{storage_service_id}/FileSystems/{file_system_id}/Metrics",
    response_model_exclude_none=True,
)
async def get1(
    storage_service_id: str, file_system_id: str, request: Request, response: Response
) -> FileSystemMetrics:
    s: Service = get_service(FileSystemMetrics, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "file_system_id": file_system_id,
        "request": request,
        "response": response,
    }
    return cast(FileSystemMetrics, s.get(**b))


@router.get(
    "/redfish/v1/Storage/{storage_id}/FileSystems/{file_system_id}/Metrics",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Storage/{storage_id}/FileSystems/{file_system_id}/Metrics",
    response_model_exclude_none=True,
)
async def get2(
    storage_id: str, file_system_id: str, request: Request, response: Response
) -> FileSystemMetrics:
    s: Service = get_service(FileSystemMetrics, request)
    b: dict[str, Any] = {
        "storage_id": storage_id,
        "file_system_id": file_system_id,
        "request": request,
        "response": response,
    }
    return cast(FileSystemMetrics, s.get(**b))
