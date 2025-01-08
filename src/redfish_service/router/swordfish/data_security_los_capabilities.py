from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ...model.swordfish.data_security_los_capabilities import DataSecurityLosCapabilities
from ...service import Service, find_service

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
    s: Service = find_service(DataSecurityLosCapabilities)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(DataSecurityLosCapabilities, s.get(**b))
