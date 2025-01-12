from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ...authenticate import authenticate
from ...model.swordfish.file_share import FileShare, FileShareOnUpdate
from ...service import Service
from ...util import get_service

router = APIRouter()


@router.delete(
    "/redfish/v1/Storage/{storage_id}/FileSystems/{file_systems_id}/ExportedFileShares/{exported_file_shares_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete1(
    storage_id: str,
    file_systems_id: str,
    exported_file_shares_id: str,
    request: Request,
    response: Response,
) -> None:
    s: Service = get_service(FileShare, request)
    b: dict[str, Any] = {
        "storage_id": storage_id,
        "file_systems_id": file_systems_id,
        "exported_file_shares_id": exported_file_shares_id,
        "request": request,
        "response": response,
    }
    return s.delete(**b)


@router.get(
    "/redfish/v1/Storage/{storage_id}/FileSystems/{file_systems_id}/ExportedFileShares/{exported_file_shares_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Storage/{storage_id}/FileSystems/{file_systems_id}/ExportedFileShares/{exported_file_shares_id}",
    response_model_exclude_none=True,
)
async def get1(
    storage_id: str,
    file_systems_id: str,
    exported_file_shares_id: str,
    request: Request,
    response: Response,
) -> FileShare:
    s: Service = get_service(FileShare, request)
    b: dict[str, Any] = {
        "storage_id": storage_id,
        "file_systems_id": file_systems_id,
        "exported_file_shares_id": exported_file_shares_id,
        "request": request,
        "response": response,
    }
    return cast(FileShare, s.get(**b))


@router.patch(
    "/redfish/v1/Storage/{storage_id}/FileSystems/{file_systems_id}/ExportedFileShares/{exported_file_shares_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch1(
    storage_id: str,
    file_systems_id: str,
    exported_file_shares_id: str,
    request: Request,
    response: Response,
    body: FileShareOnUpdate,
) -> FileShare:
    s: Service = get_service(FileShare, request)
    b: dict[str, Any] = {
        "storage_id": storage_id,
        "file_systems_id": file_systems_id,
        "exported_file_shares_id": exported_file_shares_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(FileShare, s.patch(**b))


@router.delete(
    "/redfish/v1/Systems/{computer_systems_id}/Storage/{storage_id}/FileSystems/{file_systems_id}/ExportedFileShares/{exported_file_shares_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete2(
    computer_systems_id: str,
    storage_id: str,
    file_systems_id: str,
    exported_file_shares_id: str,
    request: Request,
    response: Response,
) -> None:
    s: Service = get_service(FileShare, request)
    b: dict[str, Any] = {
        "computer_systems_id": computer_systems_id,
        "storage_id": storage_id,
        "file_systems_id": file_systems_id,
        "exported_file_shares_id": exported_file_shares_id,
        "request": request,
        "response": response,
    }
    return s.delete(**b)


@router.get(
    "/redfish/v1/Systems/{computer_systems_id}/Storage/{storage_id}/FileSystems/{file_systems_id}/ExportedFileShares/{exported_file_shares_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Systems/{computer_systems_id}/Storage/{storage_id}/FileSystems/{file_systems_id}/ExportedFileShares/{exported_file_shares_id}",
    response_model_exclude_none=True,
)
async def get2(
    computer_systems_id: str,
    storage_id: str,
    file_systems_id: str,
    exported_file_shares_id: str,
    request: Request,
    response: Response,
) -> FileShare:
    s: Service = get_service(FileShare, request)
    b: dict[str, Any] = {
        "computer_systems_id": computer_systems_id,
        "storage_id": storage_id,
        "file_systems_id": file_systems_id,
        "exported_file_shares_id": exported_file_shares_id,
        "request": request,
        "response": response,
    }
    return cast(FileShare, s.get(**b))


@router.patch(
    "/redfish/v1/Systems/{computer_systems_id}/Storage/{storage_id}/FileSystems/{file_systems_id}/ExportedFileShares/{exported_file_shares_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch2(
    computer_systems_id: str,
    storage_id: str,
    file_systems_id: str,
    exported_file_shares_id: str,
    request: Request,
    response: Response,
    body: FileShareOnUpdate,
) -> FileShare:
    s: Service = get_service(FileShare, request)
    b: dict[str, Any] = {
        "computer_systems_id": computer_systems_id,
        "storage_id": storage_id,
        "file_systems_id": file_systems_id,
        "exported_file_shares_id": exported_file_shares_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(FileShare, s.patch(**b))


@router.delete(
    "/redfish/v1/StorageServices/{storage_service_id}/FileSystems/{file_systems_id}/ExportedFileShares/{exported_file_shares_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete3(
    storage_service_id: str,
    file_systems_id: str,
    exported_file_shares_id: str,
    request: Request,
    response: Response,
) -> None:
    s: Service = get_service(FileShare, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "file_systems_id": file_systems_id,
        "exported_file_shares_id": exported_file_shares_id,
        "request": request,
        "response": response,
    }
    return s.delete(**b)


@router.get(
    "/redfish/v1/StorageServices/{storage_service_id}/FileSystems/{file_systems_id}/ExportedFileShares/{exported_file_shares_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/StorageServices/{storage_service_id}/FileSystems/{file_systems_id}/ExportedFileShares/{exported_file_shares_id}",
    response_model_exclude_none=True,
)
async def get3(
    storage_service_id: str,
    file_systems_id: str,
    exported_file_shares_id: str,
    request: Request,
    response: Response,
) -> FileShare:
    s: Service = get_service(FileShare, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "file_systems_id": file_systems_id,
        "exported_file_shares_id": exported_file_shares_id,
        "request": request,
        "response": response,
    }
    return cast(FileShare, s.get(**b))


@router.patch(
    "/redfish/v1/StorageServices/{storage_service_id}/FileSystems/{file_systems_id}/ExportedFileShares/{exported_file_shares_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch3(
    storage_service_id: str,
    file_systems_id: str,
    exported_file_shares_id: str,
    request: Request,
    response: Response,
    body: FileShareOnUpdate,
) -> FileShare:
    s: Service = get_service(FileShare, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "file_systems_id": file_systems_id,
        "exported_file_shares_id": exported_file_shares_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(FileShare, s.patch(**b))
