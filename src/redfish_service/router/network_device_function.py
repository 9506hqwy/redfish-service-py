from typing import Any, cast

from fastapi import APIRouter

from ..model.network_device_function import NetworkDeviceFunction
from ..service import Service, find_service
from . import authenticate

router = APIRouter()


@router.get(
    "/redfish/v1/Chassis/{chassis_id}/NetworkAdapters/{network_adapter_id}/NetworkDeviceFunctions/{network_device_function_id}",
    response_model_exclude_none=True,
)
@authenticate
async def get1(
    chassis_id: str, network_adapter_id: str, network_device_function_id: str
) -> NetworkDeviceFunction:
    s: Service = find_service(NetworkDeviceFunction)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "network_adapter_id": network_adapter_id,
        "network_device_function_id": network_device_function_id,
    }
    return cast(NetworkDeviceFunction, s.get(**b))
