from typing import Any, cast

from fastapi import APIRouter

from ..model.fan import Fan
from ..service import Service, find_service
from . import authenticate

router = APIRouter()


@router.get(
    "/redfish/v1/Chassis/{chassis_id}/ThermalSubsystem/Fans/{fan_id}",
    response_model_exclude_none=True,
)
@authenticate
async def get1(chassis_id: str, fan_id: str) -> Fan:
    s: Service = find_service(Fan)
    b: dict[str, Any] = {"chassis_id": chassis_id, "fan_id": fan_id}
    return cast(Fan, s.get(**b))
