from typing import Any, cast

from fastapi import APIRouter

from ..model.power_equipment import PowerEquipment
from ..service import Service, find_service
from . import authenticate

router = APIRouter()


@router.get("/redfish/v1/PowerEquipment", response_model_exclude_none=True)
@authenticate
async def get1() -> PowerEquipment:
    s: Service = find_service(PowerEquipment)
    b: dict[str, Any] = {}
    return cast(PowerEquipment, s.get(**b))
