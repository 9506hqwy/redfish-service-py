from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ...authenticate import authenticate
from ...model.swordfish.file_system import FileSystem, FileSystemOnCreate
from ...model.swordfish.file_system_collection import FileSystemCollection
from ...service import Service, ServiceCollection
from ...util import get_service, get_service_collection

router = APIRouter()


@router.get(
    "/redfish/v1/StorageServices/{storage_service_id}/FileSystems",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/StorageServices/{storage_service_id}/FileSystems",
    response_model_exclude_none=True,
)
async def get1(
    storage_service_id: str, request: Request, response: Response
) -> FileSystemCollection:
    s: Service = get_service(FileSystemCollection, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "request": request,
        "response": response,
    }
    return cast(FileSystemCollection, s.get(**b))


@router.post(
    "/redfish/v1/StorageServices/{storage_service_id}/FileSystems",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/StorageServices/{storage_service_id}/FileSystems/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post1(
    storage_service_id: str, request: Request, response: Response, body: FileSystemOnCreate
) -> FileSystem:
    s: ServiceCollection = get_service_collection(FileSystemCollection, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(FileSystem, s.post(**b))


@router.get("/redfish/v1/Storage/{storage_id}/FileSystems", response_model_exclude_none=True)
@router.head("/redfish/v1/Storage/{storage_id}/FileSystems", response_model_exclude_none=True)
async def get2(storage_id: str, request: Request, response: Response) -> FileSystemCollection:
    s: Service = get_service(FileSystemCollection, request)
    b: dict[str, Any] = {"storage_id": storage_id, "request": request, "response": response}
    return cast(FileSystemCollection, s.get(**b))


@router.post("/redfish/v1/Storage/{storage_id}/FileSystems", response_model_exclude_none=True)
@router.post(
    "/redfish/v1/Storage/{storage_id}/FileSystems/Members", response_model_exclude_none=True
)
@authenticate
async def post2(
    storage_id: str, request: Request, response: Response, body: FileSystemOnCreate
) -> FileSystem:
    s: ServiceCollection = get_service_collection(FileSystemCollection, request)
    b: dict[str, Any] = {
        "storage_id": storage_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(FileSystem, s.post(**b))
