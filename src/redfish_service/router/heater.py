from typing import Any, cast

from fastapi import APIRouter

from ..authenticate import authenticate
from ..model.heater import Heater
from ..service import Service, find_service

router = APIRouter()


@router.get(
    "/redfish/v1/Chassis/{chassis_id}/ThermalSubsystem/Heaters/{heater_id}",
    response_model_exclude_none=True,
)
@authenticate
async def get1(chassis_id: str, heater_id: str) -> Heater:
    s: Service = find_service(Heater)
    b: dict[str, Any] = {"chassis_id": chassis_id, "heater_id": heater_id}
    return cast(Heater, s.get(**b))
