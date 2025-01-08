from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ...model.swordfish.class_of_service import ClassOfService
from ...service import Service, find_service

router = APIRouter()


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
    s: Service = find_service(ClassOfService)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "class_of_service_id": class_of_service_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(ClassOfService, s.get(**b))


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
    s: Service = find_service(ClassOfService)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "storage_pool_id": storage_pool_id,
        "class_of_service_id": class_of_service_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(ClassOfService, s.get(**b))
