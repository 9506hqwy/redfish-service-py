from typing import Any, cast

from fastapi import APIRouter

from ..authenticate import authenticate
from ..model.cooling_unit import CoolingUnit
from ..service import Service, find_service

router = APIRouter()


@router.get(
    "/redfish/v1/ThermalEquipment/CDUs/{cooling_unit_id}", response_model_exclude_none=True
)
@authenticate
async def get1(cooling_unit_id: str) -> CoolingUnit:
    s: Service = find_service(CoolingUnit)
    b: dict[str, Any] = {"cooling_unit_id": cooling_unit_id}
    return cast(CoolingUnit, s.get(**b))


@router.get(
    "/redfish/v1/ThermalEquipment/ImmersionUnits/{cooling_unit_id}",
    response_model_exclude_none=True,
)
@authenticate
async def get2(cooling_unit_id: str) -> CoolingUnit:
    s: Service = find_service(CoolingUnit)
    b: dict[str, Any] = {"cooling_unit_id": cooling_unit_id}
    return cast(CoolingUnit, s.get(**b))


@router.get(
    "/redfish/v1/ThermalEquipment/HeatExchangers/{cooling_unit_id}",
    response_model_exclude_none=True,
)
@authenticate
async def get3(cooling_unit_id: str) -> CoolingUnit:
    s: Service = find_service(CoolingUnit)
    b: dict[str, Any] = {"cooling_unit_id": cooling_unit_id}
    return cast(CoolingUnit, s.get(**b))
