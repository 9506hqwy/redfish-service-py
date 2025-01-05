from typing import Any, cast

from fastapi import APIRouter

from ...authenticate import authenticate
from ...model.swordfish.file_system import FileSystem
from ...service import Service, find_service

router = APIRouter()


@router.get(
    "/redfish/v1/StorageServices/{storage_service_id}/FileSystems/{file_system_id}",
    response_model_exclude_none=True,
)
@authenticate
async def get1(storage_service_id: str, file_system_id: str) -> FileSystem:
    s: Service = find_service(FileSystem)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "file_system_id": file_system_id,
    }
    return cast(FileSystem, s.get(**b))


@router.get(
    "/redfish/v1/Storage/{storage_id}/FileSystems/{file_system_id}",
    response_model_exclude_none=True,
)
@authenticate
async def get2(storage_id: str, file_system_id: str) -> FileSystem:
    s: Service = find_service(FileSystem)
    b: dict[str, Any] = {"storage_id": storage_id, "file_system_id": file_system_id}
    return cast(FileSystem, s.get(**b))
