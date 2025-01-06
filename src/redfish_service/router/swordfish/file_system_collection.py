from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ...authenticate import authenticate
from ...model.swordfish.file_system_collection import FileSystemCollection
from ...service import Service, find_service

router = APIRouter()


@router.get(
    "/redfish/v1/StorageServices/{storage_service_id}/FileSystems",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/StorageServices/{storage_service_id}/FileSystems",
    response_model_exclude_none=True,
)
@authenticate
async def get1(
    storage_service_id: str, request: Request, response: Response
) -> FileSystemCollection:
    s: Service = find_service(FileSystemCollection)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(FileSystemCollection, s.get(**b))


@router.get("/redfish/v1/Storage/{storage_id}/FileSystems", response_model_exclude_none=True)
@router.head("/redfish/v1/Storage/{storage_id}/FileSystems", response_model_exclude_none=True)
@authenticate
async def get2(storage_id: str, request: Request, response: Response) -> FileSystemCollection:
    s: Service = find_service(FileSystemCollection)
    b: dict[str, Any] = {"storage_id": storage_id, "request": request, "response": response}

    response.headers["OData-Version"] = "4.0"

    return cast(FileSystemCollection, s.get(**b))
