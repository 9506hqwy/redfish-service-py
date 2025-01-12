from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ...authenticate import authenticate
from ...model.swordfish.storage_service import StorageService, StorageServiceOnCreate
from ...model.swordfish.storage_service_collection import StorageServiceCollection
from ...service import Service, ServiceCollection
from ...util import get_service, get_service_collection

router = APIRouter()


@router.get("/redfish/v1/StorageServices", response_model_exclude_none=True)
@router.head("/redfish/v1/StorageServices", response_model_exclude_none=True)
async def get1(request: Request, response: Response) -> StorageServiceCollection:
    s: Service = get_service(StorageServiceCollection, request)
    b: dict[str, Any] = {"request": request, "response": response}

    response.headers["OData-Version"] = "4.0"

    return cast(StorageServiceCollection, s.get(**b))


@router.post("/redfish/v1/StorageServices", response_model_exclude_none=True)
@router.post("/redfish/v1/StorageServices/Members", response_model_exclude_none=True)
@authenticate
async def post1(
    request: Request, response: Response, body: StorageServiceOnCreate
) -> StorageService:
    s: ServiceCollection = get_service_collection(StorageServiceCollection, request)
    b: dict[str, Any] = {"request": request, "response": response, "body": body}

    response.headers["OData-Version"] = "4.0"

    return cast(StorageService, s.post(**b))


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/StorageServices", response_model_exclude_none=True
)
@router.head(
    "/redfish/v1/Systems/{computer_system_id}/StorageServices", response_model_exclude_none=True
)
async def get2(
    computer_system_id: str, request: Request, response: Response
) -> StorageServiceCollection:
    s: Service = get_service(StorageServiceCollection, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(StorageServiceCollection, s.get(**b))


@router.post(
    "/redfish/v1/Systems/{computer_system_id}/StorageServices", response_model_exclude_none=True
)
@router.post(
    "/redfish/v1/Systems/{computer_system_id}/StorageServices/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post2(
    computer_system_id: str, request: Request, response: Response, body: StorageServiceOnCreate
) -> StorageService:
    s: ServiceCollection = get_service_collection(StorageServiceCollection, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(StorageService, s.post(**b))
