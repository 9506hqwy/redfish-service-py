from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..model.fan import Fan
from ..service import Service, find_service

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
    s: Service = find_service(Fan)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "fan_id": fan_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(Fan, s.get(**b))
