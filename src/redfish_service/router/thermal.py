from typing import Any, cast

from fastapi import APIRouter

from ..authenticate import authenticate
from ..model.thermal import Thermal
from ..service import Service, find_service

router = APIRouter()


@router.get("/redfish/v1/Chassis/{chassis_id}/Thermal", response_model_exclude_none=True)
@authenticate
async def get1(chassis_id: str) -> Thermal:
    s: Service = find_service(Thermal)
    b: dict[str, Any] = {"chassis_id": chassis_id}
    return cast(Thermal, s.get(**b))
