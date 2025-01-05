from typing import Any, cast

from fastapi import APIRouter

from ..model.heater_collection import HeaterCollection
from ..service import Service, find_service
from . import authenticate

router = APIRouter()


@router.get(
    "/redfish/v1/Chassis/{chassis_id}/ThermalSubsystem/Heaters", response_model_exclude_none=True
)
@authenticate
async def get1(chassis_id: str) -> HeaterCollection:
    s: Service = find_service(HeaterCollection)
    b: dict[str, Any] = {"chassis_id": chassis_id}
    return cast(HeaterCollection, s.get(**b))
