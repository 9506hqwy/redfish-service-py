from typing import Any, cast

from fastapi import APIRouter

from ..authenticate import authenticate
from ..model.power_subsystem import PowerSubsystem
from ..service import Service, find_service

router = APIRouter()


@router.get("/redfish/v1/Chassis/{chassis_id}/PowerSubsystem", response_model_exclude_none=True)
@authenticate
async def get1(chassis_id: str) -> PowerSubsystem:
    s: Service = find_service(PowerSubsystem)
    b: dict[str, Any] = {"chassis_id": chassis_id}
    return cast(PowerSubsystem, s.get(**b))
