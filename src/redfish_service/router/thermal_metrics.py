from typing import Any, cast

from fastapi import APIRouter

from ..authenticate import authenticate
from ..model.thermal_metrics import ThermalMetrics
from ..service import Service, find_service

router = APIRouter()


@router.get(
    "/redfish/v1/Chassis/{chassis_id}/ThermalSubsystem/ThermalMetrics",
    response_model_exclude_none=True,
)
@authenticate
async def get1(chassis_id: str) -> ThermalMetrics:
    s: Service = find_service(ThermalMetrics)
    b: dict[str, Any] = {"chassis_id": chassis_id}
    return cast(ThermalMetrics, s.get(**b))
