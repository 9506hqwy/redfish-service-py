from typing import Any, cast

from fastapi import APIRouter

from ..authenticate import authenticate
from ..model.heater_metrics import HeaterMetrics
from ..service import Service, find_service

router = APIRouter()


@router.get(
    "/redfish/v1/Chassis/{chassis_id}/ThermalSubsystem/Heaters/{header_id}/Metrics",
    response_model_exclude_none=True,
)
@authenticate
async def get1(chassis_id: str, header_id: str) -> HeaterMetrics:
    s: Service = find_service(HeaterMetrics)
    b: dict[str, Any] = {"chassis_id": chassis_id, "header_id": header_id}
    return cast(HeaterMetrics, s.get(**b))
