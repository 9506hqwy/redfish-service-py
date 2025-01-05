from typing import Any, cast

from fastapi import APIRouter

from ..authenticate import authenticate
from ..model.fan_collection import FanCollection
from ..service import Service, find_service

router = APIRouter()


@router.get(
    "/redfish/v1/Chassis/{chassis_id}/ThermalSubsystem/Fans", response_model_exclude_none=True
)
@authenticate
async def get1(chassis_id: str) -> FanCollection:
    s: Service = find_service(FanCollection)
    b: dict[str, Any] = {"chassis_id": chassis_id}
    return cast(FanCollection, s.get(**b))
