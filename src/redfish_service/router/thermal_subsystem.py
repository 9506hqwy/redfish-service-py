from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..model.thermal_subsystem import ThermalSubsystem
from ..service import Service
from ..util import get_service, set_link_header

router = APIRouter()


@router.get("/redfish/v1/Chassis/{chassis_id}/ThermalSubsystem", response_model_exclude_none=True)
@router.head("/redfish/v1/Chassis/{chassis_id}/ThermalSubsystem", response_model_exclude_none=True)
async def get1(chassis_id: str, request: Request, response: Response) -> ThermalSubsystem:
    s: Service = get_service(ThermalSubsystem, request)
    b: dict[str, Any] = {"chassis_id": chassis_id, "request": request, "response": response}
    m = cast(ThermalSubsystem, s.get(**b))
    set_link_header(m, response)
    return m
