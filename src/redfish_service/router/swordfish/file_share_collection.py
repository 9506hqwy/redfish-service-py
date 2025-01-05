from typing import Any, cast

from fastapi import APIRouter

from ...model.swordfish.file_share_collection import FileShareCollection
from ...service import Service, find_service
from .. import authenticate

router = APIRouter()


@router.get(
    "/redfish/v1/Storage/{storage_id}/FileSystems/{file_systems_id}/ExportedFileShares",
    response_model_exclude_none=True,
)
@authenticate
async def get1(storage_id: str, file_systems_id: str) -> FileShareCollection:
    s: Service = find_service(FileShareCollection)
    b: dict[str, Any] = {"storage_id": storage_id, "file_systems_id": file_systems_id}
    return cast(FileShareCollection, s.get(**b))


@router.get(
    "/redfish/v1/StorageServices/{storage_service_id}/FileSystems/{file_systems_id}/ExportedFileShares",
    response_model_exclude_none=True,
)
@authenticate
async def get2(storage_service_id: str, file_systems_id: str) -> FileShareCollection:
    s: Service = find_service(FileShareCollection)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "file_systems_id": file_systems_id,
    }
    return cast(FileShareCollection, s.get(**b))
