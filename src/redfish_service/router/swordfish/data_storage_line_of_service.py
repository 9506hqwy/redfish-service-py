from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ...authenticate import authenticate
from ...model.swordfish.data_storage_line_of_service import (
    DataStorageLineOfService,
    DataStorageLineOfServiceOnUpdate,
)
from ...service import Service, find_service

router = APIRouter()


@router.delete(
    "/redfish/v1/StorageServices/{storage_service_id}/LinesOfService/DataStorageLinesOfService/{data_storage_line_of_service_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete1(
    storage_service_id: str,
    data_storage_line_of_service_id: str,
    request: Request,
    response: Response,
) -> None:
    s: Service = find_service(DataStorageLineOfService)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "data_storage_line_of_service_id": data_storage_line_of_service_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return s.delete(**b)


@router.get(
    "/redfish/v1/StorageServices/{storage_service_id}/LinesOfService/DataStorageLinesOfService/{data_storage_line_of_service_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/StorageServices/{storage_service_id}/LinesOfService/DataStorageLinesOfService/{data_storage_line_of_service_id}",
    response_model_exclude_none=True,
)
async def get1(
    storage_service_id: str,
    data_storage_line_of_service_id: str,
    request: Request,
    response: Response,
) -> DataStorageLineOfService:
    s: Service = find_service(DataStorageLineOfService)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "data_storage_line_of_service_id": data_storage_line_of_service_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(DataStorageLineOfService, s.get(**b))


@router.patch(
    "/redfish/v1/StorageServices/{storage_service_id}/LinesOfService/DataStorageLinesOfService/{data_storage_line_of_service_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch1(
    storage_service_id: str,
    data_storage_line_of_service_id: str,
    request: Request,
    response: Response,
    body: DataStorageLineOfServiceOnUpdate,
) -> DataStorageLineOfService:
    s: Service = find_service(DataStorageLineOfService)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "data_storage_line_of_service_id": data_storage_line_of_service_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(DataStorageLineOfService, s.patch(**b))


@router.delete(
    "/redfish/v1/StorageServices/{storage_service_id}/ClassesOfService/{class_of_service_id}/DataStorageLinesOfService/{data_storage_line_of_service_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete2(
    storage_service_id: str,
    class_of_service_id: str,
    data_storage_line_of_service_id: str,
    request: Request,
    response: Response,
) -> None:
    s: Service = find_service(DataStorageLineOfService)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "class_of_service_id": class_of_service_id,
        "data_storage_line_of_service_id": data_storage_line_of_service_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return s.delete(**b)


@router.get(
    "/redfish/v1/StorageServices/{storage_service_id}/ClassesOfService/{class_of_service_id}/DataStorageLinesOfService/{data_storage_line_of_service_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/StorageServices/{storage_service_id}/ClassesOfService/{class_of_service_id}/DataStorageLinesOfService/{data_storage_line_of_service_id}",
    response_model_exclude_none=True,
)
async def get2(
    storage_service_id: str,
    class_of_service_id: str,
    data_storage_line_of_service_id: str,
    request: Request,
    response: Response,
) -> DataStorageLineOfService:
    s: Service = find_service(DataStorageLineOfService)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "class_of_service_id": class_of_service_id,
        "data_storage_line_of_service_id": data_storage_line_of_service_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(DataStorageLineOfService, s.get(**b))


@router.patch(
    "/redfish/v1/StorageServices/{storage_service_id}/ClassesOfService/{class_of_service_id}/DataStorageLinesOfService/{data_storage_line_of_service_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch2(
    storage_service_id: str,
    class_of_service_id: str,
    data_storage_line_of_service_id: str,
    request: Request,
    response: Response,
    body: DataStorageLineOfServiceOnUpdate,
) -> DataStorageLineOfService:
    s: Service = find_service(DataStorageLineOfService)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "class_of_service_id": class_of_service_id,
        "data_storage_line_of_service_id": data_storage_line_of_service_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(DataStorageLineOfService, s.patch(**b))
