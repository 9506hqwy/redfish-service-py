from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ...authenticate import authenticate
from ...model.swordfish.io_connectivity_los_capabilities import (
    IoConnectivityLosCapabilities,
    IoConnectivityLosCapabilitiesOnUpdate,
)
from ...service import Service
from ...util import get_service

router = APIRouter()


@router.get(
    "/redfish/v1/StorageServices/{storage_service_id}/IOConnectivityLoSCapabilities",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/StorageServices/{storage_service_id}/IOConnectivityLoSCapabilities",
    response_model_exclude_none=True,
)
async def get1(
    storage_service_id: str, request: Request, response: Response
) -> IoConnectivityLosCapabilities:
    s: Service = get_service(IoConnectivityLosCapabilities, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "request": request,
        "response": response,
    }
    return cast(IoConnectivityLosCapabilities, s.get(**b))


@router.patch(
    "/redfish/v1/StorageServices/{storage_service_id}/IOConnectivityLoSCapabilities",
    response_model_exclude_none=True,
)
@authenticate
async def patch1(
    storage_service_id: str,
    request: Request,
    response: Response,
    body: IoConnectivityLosCapabilitiesOnUpdate,
) -> IoConnectivityLosCapabilities:
    s: Service = get_service(IoConnectivityLosCapabilities, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(IoConnectivityLosCapabilities, s.patch(**b))
