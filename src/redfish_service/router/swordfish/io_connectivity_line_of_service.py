from typing import Any, cast

from fastapi import APIRouter

from ...authenticate import authenticate
from ...model.swordfish.io_connectivity_line_of_service import IoConnectivityLineOfService
from ...service import Service, find_service

router = APIRouter()


@router.get(
    "/redfish/v1/StorageServices/{storage_service_id}/LinesOfService/IOConnectivityLinesOfService/{io_connectivity_line_of_service_id}",
    response_model_exclude_none=True,
)
@authenticate
async def get1(
    storage_service_id: str, io_connectivity_line_of_service_id: str
) -> IoConnectivityLineOfService:
    s: Service = find_service(IoConnectivityLineOfService)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "io_connectivity_line_of_service_id": io_connectivity_line_of_service_id,
    }
    return cast(IoConnectivityLineOfService, s.get(**b))


@router.get(
    "/redfish/v1/StorageServices/{storage_service_id}/ClassesOfService/{class_of_service_id}/IOConnectivityLinesOfService/{io_connectivity_line_of_service_id}",
    response_model_exclude_none=True,
)
@authenticate
async def get2(
    storage_service_id: str, class_of_service_id: str, io_connectivity_line_of_service_id: str
) -> IoConnectivityLineOfService:
    s: Service = find_service(IoConnectivityLineOfService)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "class_of_service_id": class_of_service_id,
        "io_connectivity_line_of_service_id": io_connectivity_line_of_service_id,
    }
    return cast(IoConnectivityLineOfService, s.get(**b))
