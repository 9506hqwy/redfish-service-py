from typing import Any, cast

from fastapi import APIRouter

from ..model.battery_metrics import BatteryMetrics
from ..service import Service, find_service
from . import authenticate

router = APIRouter()


@router.get(
    "/redfish/v1/Chassis/{chassis_id}/PowerSubsystem/Batteries/{battery_id}/Metrics",
    response_model_exclude_none=True,
)
@authenticate
async def get1(chassis_id: str, battery_id: str) -> BatteryMetrics:
    s: Service = find_service(BatteryMetrics)
    b: dict[str, Any] = {"chassis_id": chassis_id, "battery_id": battery_id}
    return cast(BatteryMetrics, s.get(**b))
