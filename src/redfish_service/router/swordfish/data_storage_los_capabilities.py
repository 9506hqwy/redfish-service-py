from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ...authenticate import authenticate
from ...model.swordfish.data_storage_los_capabilities import (
    DataStorageLosCapabilities,
    DataStorageLosCapabilitiesOnUpdate,
)
from ...service import Service
from ...util import get_service

router = APIRouter()


@router.get(
    "/redfish/v1/StorageServices/{storage_service_id}/DataStorageLoSCapabilities",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/StorageServices/{storage_service_id}/DataStorageLoSCapabilities",
    response_model_exclude_none=True,
)
async def get1(
    storage_service_id: str, request: Request, response: Response
) -> DataStorageLosCapabilities:
    s: Service = get_service(DataStorageLosCapabilities, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(DataStorageLosCapabilities, s.get(**b))


@router.patch(
    "/redfish/v1/StorageServices/{storage_service_id}/DataStorageLoSCapabilities",
    response_model_exclude_none=True,
)
@authenticate
async def patch1(
    storage_service_id: str,
    request: Request,
    response: Response,
    body: DataStorageLosCapabilitiesOnUpdate,
) -> DataStorageLosCapabilities:
    s: Service = get_service(DataStorageLosCapabilities, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(DataStorageLosCapabilities, s.patch(**b))
