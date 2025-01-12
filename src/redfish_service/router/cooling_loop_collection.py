from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..model.cooling_loop_collection import CoolingLoopCollection
from ..service import Service
from ..util import get_service

router = APIRouter()


@router.get("/redfish/v1/ThermalEquipment/CoolingLoops", response_model_exclude_none=True)
@router.head("/redfish/v1/ThermalEquipment/CoolingLoops", response_model_exclude_none=True)
async def get1(request: Request, response: Response) -> CoolingLoopCollection:
    s: Service = get_service(CoolingLoopCollection, request)
    b: dict[str, Any] = {"request": request, "response": response}
    return cast(CoolingLoopCollection, s.get(**b))
