from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..model.network_device_function import NetworkDeviceFunction
from ..service import Service, find_service

router = APIRouter()


@router.get(
    "/redfish/v1/Chassis/{chassis_id}/NetworkAdapters/{network_adapter_id}/NetworkDeviceFunctions/{network_device_function_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Chassis/{chassis_id}/NetworkAdapters/{network_adapter_id}/NetworkDeviceFunctions/{network_device_function_id}",
    response_model_exclude_none=True,
)
async def get1(
    chassis_id: str,
    network_adapter_id: str,
    network_device_function_id: str,
    request: Request,
    response: Response,
) -> NetworkDeviceFunction:
    s: Service = find_service(NetworkDeviceFunction)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "network_adapter_id": network_adapter_id,
        "network_device_function_id": network_device_function_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(NetworkDeviceFunction, s.get(**b))
