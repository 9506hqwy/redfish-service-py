from typing import Any, cast

from fastapi import APIRouter

from ..authenticate import authenticate
from ..model.battery import Battery
from ..service import Service, find_service

router = APIRouter()


@router.get(
    "/redfish/v1/Chassis/{chassis_id}/PowerSubsystem/Batteries/{battery_id}",
    response_model_exclude_none=True,
)
@authenticate
async def get1(chassis_id: str, battery_id: str) -> Battery:
    s: Service = find_service(Battery)
    b: dict[str, Any] = {"chassis_id": chassis_id, "battery_id": battery_id}
    return cast(Battery, s.get(**b))
