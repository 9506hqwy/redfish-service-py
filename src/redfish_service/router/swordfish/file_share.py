from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ...model.swordfish.file_share import FileShare
from ...service import Service, find_service

router = APIRouter()


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
    s: Service = find_service(FileShare)
    b: dict[str, Any] = {
        "storage_id": storage_id,
        "file_systems_id": file_systems_id,
        "exported_file_shares_id": exported_file_shares_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(FileShare, s.get(**b))


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
    s: Service = find_service(FileShare)
    b: dict[str, Any] = {
        "computer_systems_id": computer_systems_id,
        "storage_id": storage_id,
        "file_systems_id": file_systems_id,
        "exported_file_shares_id": exported_file_shares_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(FileShare, s.get(**b))


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
    s: Service = find_service(FileShare)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "file_systems_id": file_systems_id,
        "exported_file_shares_id": exported_file_shares_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(FileShare, s.get(**b))
