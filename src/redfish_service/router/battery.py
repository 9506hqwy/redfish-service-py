from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.battery import Battery, BatteryOnUpdate, ResetRequest
from ..model.redfish_error import RedfishError
from ..service import Service
from ..util import get_service, set_link_header

router = APIRouter()


@router.get(
    "/redfish/v1/Chassis/{chassis_id}/PowerSubsystem/Batteries/{battery_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Chassis/{chassis_id}/PowerSubsystem/Batteries/{battery_id}",
    response_model_exclude_none=True,
)
async def get1(chassis_id: str, battery_id: str, request: Request, response: Response) -> Battery:
    s: Service = get_service(Battery, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "battery_id": battery_id,
        "request": request,
        "response": response,
    }
    m = cast(Battery, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/Chassis/{chassis_id}/PowerSubsystem/Batteries/{battery_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch1(
    chassis_id: str, battery_id: str, request: Request, response: Response, body: BatteryOnUpdate
) -> Battery:
    s: Service = get_service(Battery, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "battery_id": battery_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Battery, s.patch(**b))


@router.post(
    "/redfish/v1/Chassis/{chassis_id}/PowerSubsystem/Batteries/{battery_id}/Actions/Battery.Reset",
    response_model_exclude_none=True,
)
@authenticate
async def reset1(
    chassis_id: str, battery_id: str, request: Request, response: Response, body: ResetRequest
) -> RedfishError:
    s: Service = get_service(Battery, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "battery_id": battery_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Reset",
    }
    return s.action(**b)
