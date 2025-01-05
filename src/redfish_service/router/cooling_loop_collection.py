from typing import Any, cast

from fastapi import APIRouter

from ..authenticate import authenticate
from ..model.cooling_loop_collection import CoolingLoopCollection
from ..service import Service, find_service

router = APIRouter()


@router.get("/redfish/v1/ThermalEquipment/CoolingLoops", response_model_exclude_none=True)
@authenticate
async def get1() -> CoolingLoopCollection:
    s: Service = find_service(CoolingLoopCollection)
    b: dict[str, Any] = {}
    return cast(CoolingLoopCollection, s.get(**b))
