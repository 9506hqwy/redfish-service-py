from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.battery import Battery, BatteryOnUpdate
from ..service import Service, find_service

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
    s: Service = find_service(Battery)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "battery_id": battery_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(Battery, s.get(**b))


@router.patch(
    "/redfish/v1/Chassis/{chassis_id}/PowerSubsystem/Batteries/{battery_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch1(
    chassis_id: str, battery_id: str, request: Request, response: Response, body: BatteryOnUpdate
) -> Battery:
    s: Service = find_service(Battery)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "battery_id": battery_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(Battery, s.patch(**b))
