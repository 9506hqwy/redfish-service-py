from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ...authenticate import authenticate
from ...model.swordfish.class_of_service import ClassOfService, ClassOfServiceOnUpdate
from ...service import Service
from ...util import get_service

router = APIRouter()


@router.delete(
    "/redfish/v1/StorageServices/{storage_service_id}/ClassesOfService/{class_of_service_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete1(
    storage_service_id: str, class_of_service_id: str, request: Request, response: Response
) -> None:
    s: Service = get_service(ClassOfService, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "class_of_service_id": class_of_service_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return s.delete(**b)


@router.get(
    "/redfish/v1/StorageServices/{storage_service_id}/ClassesOfService/{class_of_service_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/StorageServices/{storage_service_id}/ClassesOfService/{class_of_service_id}",
    response_model_exclude_none=True,
)
async def get1(
    storage_service_id: str, class_of_service_id: str, request: Request, response: Response
) -> ClassOfService:
    s: Service = get_service(ClassOfService, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "class_of_service_id": class_of_service_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(ClassOfService, s.get(**b))


@router.patch(
    "/redfish/v1/StorageServices/{storage_service_id}/ClassesOfService/{class_of_service_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch1(
    storage_service_id: str,
    class_of_service_id: str,
    request: Request,
    response: Response,
    body: ClassOfServiceOnUpdate,
) -> ClassOfService:
    s: Service = get_service(ClassOfService, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "class_of_service_id": class_of_service_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(ClassOfService, s.patch(**b))


@router.delete(
    "/redfish/v1/StorageServices/{storage_service_id}/StoragePools/{storage_pool_id}/ClassesOfService/{class_of_service_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete2(
    storage_service_id: str,
    storage_pool_id: str,
    class_of_service_id: str,
    request: Request,
    response: Response,
) -> None:
    s: Service = get_service(ClassOfService, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "storage_pool_id": storage_pool_id,
        "class_of_service_id": class_of_service_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return s.delete(**b)


@router.get(
    "/redfish/v1/StorageServices/{storage_service_id}/StoragePools/{storage_pool_id}/ClassesOfService/{class_of_service_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/StorageServices/{storage_service_id}/StoragePools/{storage_pool_id}/ClassesOfService/{class_of_service_id}",
    response_model_exclude_none=True,
)
async def get2(
    storage_service_id: str,
    storage_pool_id: str,
    class_of_service_id: str,
    request: Request,
    response: Response,
) -> ClassOfService:
    s: Service = get_service(ClassOfService, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "storage_pool_id": storage_pool_id,
        "class_of_service_id": class_of_service_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(ClassOfService, s.get(**b))


@router.patch(
    "/redfish/v1/StorageServices/{storage_service_id}/StoragePools/{storage_pool_id}/ClassesOfService/{class_of_service_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch2(
    storage_service_id: str,
    storage_pool_id: str,
    class_of_service_id: str,
    request: Request,
    response: Response,
    body: ClassOfServiceOnUpdate,
) -> ClassOfService:
    s: Service = get_service(ClassOfService, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "storage_pool_id": storage_pool_id,
        "class_of_service_id": class_of_service_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(ClassOfService, s.patch(**b))
