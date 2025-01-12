from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ...authenticate import authenticate
from ...model.swordfish.storage_service import StorageService, StorageServiceOnUpdate
from ...service import Service
from ...util import get_service

router = APIRouter()


@router.delete(
    "/redfish/v1/StorageServices/{storage_service_id}", response_model_exclude_none=True
)
@authenticate
async def delete1(storage_service_id: str, request: Request, response: Response) -> None:
    s: Service = get_service(StorageService, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return s.delete(**b)


@router.get("/redfish/v1/StorageServices/{storage_service_id}", response_model_exclude_none=True)
@router.head("/redfish/v1/StorageServices/{storage_service_id}", response_model_exclude_none=True)
async def get1(storage_service_id: str, request: Request, response: Response) -> StorageService:
    s: Service = get_service(StorageService, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(StorageService, s.get(**b))


@router.patch("/redfish/v1/StorageServices/{storage_service_id}", response_model_exclude_none=True)
@authenticate
async def patch1(
    storage_service_id: str, request: Request, response: Response, body: StorageServiceOnUpdate
) -> StorageService:
    s: Service = get_service(StorageService, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(StorageService, s.patch(**b))


@router.delete(
    "/redfish/v1/Systems/{computer_system_id}/StorageServices/{storage_service_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete2(
    computer_system_id: str, storage_service_id: str, request: Request, response: Response
) -> None:
    s: Service = get_service(StorageService, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_service_id": storage_service_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return s.delete(**b)


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/StorageServices/{storage_service_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Systems/{computer_system_id}/StorageServices/{storage_service_id}",
    response_model_exclude_none=True,
)
async def get2(
    computer_system_id: str, storage_service_id: str, request: Request, response: Response
) -> StorageService:
    s: Service = get_service(StorageService, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_service_id": storage_service_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(StorageService, s.get(**b))


@router.patch(
    "/redfish/v1/Systems/{computer_system_id}/StorageServices/{storage_service_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch2(
    computer_system_id: str,
    storage_service_id: str,
    request: Request,
    response: Response,
    body: StorageServiceOnUpdate,
) -> StorageService:
    s: Service = get_service(StorageService, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_service_id": storage_service_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(StorageService, s.patch(**b))
