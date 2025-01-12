from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.fan import Fan, FanOnUpdate
from ..service import Service
from ..util import get_service

router = APIRouter()


@router.get(
    "/redfish/v1/Chassis/{chassis_id}/ThermalSubsystem/Fans/{fan_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Chassis/{chassis_id}/ThermalSubsystem/Fans/{fan_id}",
    response_model_exclude_none=True,
)
async def get1(chassis_id: str, fan_id: str, request: Request, response: Response) -> Fan:
    s: Service = get_service(Fan, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "fan_id": fan_id,
        "request": request,
        "response": response,
    }
    return cast(Fan, s.get(**b))


@router.patch(
    "/redfish/v1/Chassis/{chassis_id}/ThermalSubsystem/Fans/{fan_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch1(
    chassis_id: str, fan_id: str, request: Request, response: Response, body: FanOnUpdate
) -> Fan:
    s: Service = get_service(Fan, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "fan_id": fan_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Fan, s.patch(**b))
