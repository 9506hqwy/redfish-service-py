from typing import Any, cast

from fastapi import APIRouter

from ..model.cooling_loop import CoolingLoop
from ..service import Service, find_service
from . import authenticate

router = APIRouter()


@router.get(
    "/redfish/v1/ThermalEquipment/CoolingLoops/{cooling_loop_id}", response_model_exclude_none=True
)
@authenticate
async def get1(cooling_loop_id: str) -> CoolingLoop:
    s: Service = find_service(CoolingLoop)
    b: dict[str, Any] = {"cooling_loop_id": cooling_loop_id}
    return cast(CoolingLoop, s.get(**b))
