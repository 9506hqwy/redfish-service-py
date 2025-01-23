from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ...authenticate import authenticate
from ...model.swordfish.class_of_service_collection import ClassOfServiceCollection
from ...model.swordfish.line_of_service import LineOfService, LineOfServiceOnCreate
from ...service import Service, ServiceCollection
from ...util import get_service, get_service_collection, set_link_header

router = APIRouter()


@router.get(
    "/redfish/v1/StorageServices/{storage_service_id}/ClassesOfService",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/StorageServices/{storage_service_id}/ClassesOfService",
    response_model_exclude_none=True,
)
async def get1(
    storage_service_id: str, request: Request, response: Response
) -> ClassOfServiceCollection:
    s: Service = get_service(ClassOfServiceCollection, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "request": request,
        "response": response,
    }
    m = cast(ClassOfServiceCollection, s.get(**b))
    set_link_header(m, response)
    return m


@router.post(
    "/redfish/v1/StorageServices/{storage_service_id}/ClassesOfService",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/StorageServices/{storage_service_id}/ClassesOfService/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post1(
    storage_service_id: str, request: Request, response: Response, body: LineOfServiceOnCreate
) -> LineOfService:
    s: ServiceCollection = get_service_collection(ClassOfServiceCollection, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(LineOfService, s.post(**b))


@router.get(
    "/redfish/v1/StorageServices/{storage_service_id}/StoragePools/{storage_pool_id}/ClassesOfService",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/StorageServices/{storage_service_id}/StoragePools/{storage_pool_id}/ClassesOfService",
    response_model_exclude_none=True,
)
async def get2(
    storage_service_id: str, storage_pool_id: str, request: Request, response: Response
) -> ClassOfServiceCollection:
    s: Service = get_service(ClassOfServiceCollection, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "storage_pool_id": storage_pool_id,
        "request": request,
        "response": response,
    }
    m = cast(ClassOfServiceCollection, s.get(**b))
    set_link_header(m, response)
    return m


@router.post(
    "/redfish/v1/StorageServices/{storage_service_id}/StoragePools/{storage_pool_id}/ClassesOfService",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/StorageServices/{storage_service_id}/StoragePools/{storage_pool_id}/ClassesOfService/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post2(
    storage_service_id: str,
    storage_pool_id: str,
    request: Request,
    response: Response,
    body: LineOfServiceOnCreate,
) -> LineOfService:
    s: ServiceCollection = get_service_collection(ClassOfServiceCollection, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "storage_pool_id": storage_pool_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(LineOfService, s.post(**b))
