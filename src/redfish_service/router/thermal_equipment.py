from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..model.thermal_equipment import ThermalEquipment
from ..service import Service
from ..util import get_service

router = APIRouter()


@router.get("/redfish/v1/ThermalEquipment", response_model_exclude_none=True)
@router.head("/redfish/v1/ThermalEquipment", response_model_exclude_none=True)
async def get1(request: Request, response: Response) -> ThermalEquipment:
    s: Service = get_service(ThermalEquipment, request)
    b: dict[str, Any] = {"request": request, "response": response}
    return cast(ThermalEquipment, s.get(**b))
