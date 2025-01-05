from typing import Any, cast

from fastapi import APIRouter

from ..model.battery_collection import BatteryCollection
from ..service import Service, find_service
from . import authenticate

router = APIRouter()


@router.get(
    "/redfish/v1/Chassis/{chassis_id}/PowerSubsystem/Batteries", response_model_exclude_none=True
)
@authenticate
async def get1(chassis_id: str) -> BatteryCollection:
    s: Service = find_service(BatteryCollection)
    b: dict[str, Any] = {"chassis_id": chassis_id}
    return cast(BatteryCollection, s.get(**b))
