from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ...authenticate import authenticate
from ...model.swordfish.data_security_los_capabilities import (
    DataSecurityLosCapabilities,
    DataSecurityLosCapabilitiesOnUpdate,
)
from ...service import Service
from ...util import get_service

router = APIRouter()


@router.get(
    "/redfish/v1/StorageServices/{storage_service_id}/DataSecurityLoSCapabilities",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/StorageServices/{storage_service_id}/DataSecurityLoSCapabilities",
    response_model_exclude_none=True,
)
async def get1(
    storage_service_id: str, request: Request, response: Response
) -> DataSecurityLosCapabilities:
    s: Service = get_service(DataSecurityLosCapabilities, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(DataSecurityLosCapabilities, s.get(**b))


@router.patch(
    "/redfish/v1/StorageServices/{storage_service_id}/DataSecurityLoSCapabilities",
    response_model_exclude_none=True,
)
@authenticate
async def patch1(
    storage_service_id: str,
    request: Request,
    response: Response,
    body: DataSecurityLosCapabilitiesOnUpdate,
) -> DataSecurityLosCapabilities:
    s: Service = get_service(DataSecurityLosCapabilities, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(DataSecurityLosCapabilities, s.patch(**b))
