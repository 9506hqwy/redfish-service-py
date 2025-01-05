from typing import Any, cast

from fastapi import APIRouter

from ..model.cooling_unit_collection import CoolingUnitCollection
from ..service import Service, find_service
from . import authenticate

router = APIRouter()


@router.get("/redfish/v1/ThermalEquipment/CDUs", response_model_exclude_none=True)
@authenticate
async def get1() -> CoolingUnitCollection:
    s: Service = find_service(CoolingUnitCollection)
    b: dict[str, Any] = {}
    return cast(CoolingUnitCollection, s.get(**b))


@router.get("/redfish/v1/ThermalEquipment/ImmersionUnits", response_model_exclude_none=True)
@authenticate
async def get2() -> CoolingUnitCollection:
    s: Service = find_service(CoolingUnitCollection)
    b: dict[str, Any] = {}
    return cast(CoolingUnitCollection, s.get(**b))


@router.get("/redfish/v1/ThermalEquipment/HeatExchangers", response_model_exclude_none=True)
@authenticate
async def get3() -> CoolingUnitCollection:
    s: Service = find_service(CoolingUnitCollection)
    b: dict[str, Any] = {}
    return cast(CoolingUnitCollection, s.get(**b))
