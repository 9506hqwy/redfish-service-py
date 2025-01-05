from typing import Any, cast

from fastapi import APIRouter

from ..authenticate import authenticate
from ..model.thermal_equipment import ThermalEquipment
from ..service import Service, find_service

router = APIRouter()


@router.get("/redfish/v1/ThermalEquipment", response_model_exclude_none=True)
@authenticate
async def get1() -> ThermalEquipment:
    s: Service = find_service(ThermalEquipment)
    b: dict[str, Any] = {}
    return cast(ThermalEquipment, s.get(**b))
