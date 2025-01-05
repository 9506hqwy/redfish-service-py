from typing import Any, cast

from fastapi import APIRouter

from ..model.thermal_subsystem import ThermalSubsystem
from ..service import Service, find_service
from . import authenticate

router = APIRouter()


@router.get("/redfish/v1/Chassis/{chassis_id}/ThermalSubsystem", response_model_exclude_none=True)
@authenticate
async def get1(chassis_id: str) -> ThermalSubsystem:
    s: Service = find_service(ThermalSubsystem)
    b: dict[str, Any] = {"chassis_id": chassis_id}
    return cast(ThermalSubsystem, s.get(**b))
