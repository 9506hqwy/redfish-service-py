from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ...authenticate import authenticate
from ...model.swordfish.data_protection_los_capabilities import (
    DataProtectionLosCapabilities,
    DataProtectionLosCapabilitiesOnUpdate,
)
from ...service import Service
from ...util import get_service, set_link_header

router = APIRouter()


@router.get(
    "/redfish/v1/StorageServices/{storage_service_id}/DataProtectionLoSCapabilities",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/StorageServices/{storage_service_id}/DataProtectionLoSCapabilities",
    response_model_exclude_none=True,
)
async def get1(
    storage_service_id: str, request: Request, response: Response
) -> DataProtectionLosCapabilities:
    s: Service = get_service(DataProtectionLosCapabilities, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "request": request,
        "response": response,
    }
    m = cast(DataProtectionLosCapabilities, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/StorageServices/{storage_service_id}/DataProtectionLoSCapabilities",
    response_model_exclude_none=True,
)
@authenticate
async def patch1(
    storage_service_id: str,
    request: Request,
    response: Response,
    body: DataProtectionLosCapabilitiesOnUpdate,
) -> DataProtectionLosCapabilities:
    s: Service = get_service(DataProtectionLosCapabilities, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(DataProtectionLosCapabilities, s.patch(**b))
