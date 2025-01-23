from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..model.battery_metrics import BatteryMetrics
from ..service import Service
from ..util import get_service, set_link_header

router = APIRouter()


@router.get(
    "/redfish/v1/Chassis/{chassis_id}/PowerSubsystem/Batteries/{battery_id}/Metrics",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Chassis/{chassis_id}/PowerSubsystem/Batteries/{battery_id}/Metrics",
    response_model_exclude_none=True,
)
async def get1(
    chassis_id: str, battery_id: str, request: Request, response: Response
) -> BatteryMetrics:
    s: Service = get_service(BatteryMetrics, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "battery_id": battery_id,
        "request": request,
        "response": response,
    }
    m = cast(BatteryMetrics, s.get(**b))
    set_link_header(m, response)
    return m
