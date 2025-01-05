from typing import Any, cast

from fastapi import APIRouter

from ..model.chassis import Chassis
from ..service import Service, find_service
from . import authenticate

router = APIRouter()


@router.get("/redfish/v1/Chassis/{chassis_id}", response_model_exclude_none=True)
@authenticate
async def get1(chassis_id: str) -> Chassis:
    s: Service = find_service(Chassis)
    b: dict[str, Any] = {"chassis_id": chassis_id}
    return cast(Chassis, s.get(**b))
