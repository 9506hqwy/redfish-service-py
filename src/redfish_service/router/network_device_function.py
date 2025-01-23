from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.network_device_function import (
    NetworkDeviceFunction,
    NetworkDeviceFunctionOnUpdate,
)
from ..service import Service
from ..util import get_service, set_link_header

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
    s: Service = get_service(NetworkDeviceFunction, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "network_adapter_id": network_adapter_id,
        "network_device_function_id": network_device_function_id,
        "request": request,
        "response": response,
    }
    m = cast(NetworkDeviceFunction, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/Chassis/{chassis_id}/NetworkAdapters/{network_adapter_id}/NetworkDeviceFunctions/{network_device_function_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch1(
    chassis_id: str,
    network_adapter_id: str,
    network_device_function_id: str,
    request: Request,
    response: Response,
    body: NetworkDeviceFunctionOnUpdate,
) -> NetworkDeviceFunction:
    s: Service = get_service(NetworkDeviceFunction, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "network_adapter_id": network_adapter_id,
        "network_device_function_id": network_device_function_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(NetworkDeviceFunction, s.patch(**b))
