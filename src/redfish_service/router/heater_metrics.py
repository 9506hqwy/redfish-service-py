from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..model.heater_metrics import HeaterMetrics
from ..service import Service
from ..util import get_service, set_link_header

router = APIRouter()


@router.get(
    "/redfish/v1/Chassis/{chassis_id}/ThermalSubsystem/Heaters/{header_id}/Metrics",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Chassis/{chassis_id}/ThermalSubsystem/Heaters/{header_id}/Metrics",
    response_model_exclude_none=True,
)
async def get1(
    chassis_id: str, header_id: str, request: Request, response: Response
) -> HeaterMetrics:
    s: Service = get_service(HeaterMetrics, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "header_id": header_id,
        "request": request,
        "response": response,
    }
    m = cast(HeaterMetrics, s.get(**b))
    set_link_header(m, response)
    return m
