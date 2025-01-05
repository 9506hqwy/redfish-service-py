from typing import Any, cast

from fastapi import APIRouter

from ..model.pump_collection import PumpCollection
from ..service import Service, find_service
from . import authenticate

router = APIRouter()


@router.get(
    "/redfish/v1/ThermalEquipment/CDUs/{cooling_unit_id}/Pumps", response_model_exclude_none=True
)
@authenticate
async def get1(cooling_unit_id: str) -> PumpCollection:
    s: Service = find_service(PumpCollection)
    b: dict[str, Any] = {"cooling_unit_id": cooling_unit_id}
    return cast(PumpCollection, s.get(**b))


@router.get(
    "/redfish/v1/ThermalEquipment/ImmersionUnits/{cooling_unit_id}/Pumps",
    response_model_exclude_none=True,
)
@authenticate
async def get2(cooling_unit_id: str) -> PumpCollection:
    s: Service = find_service(PumpCollection)
    b: dict[str, Any] = {"cooling_unit_id": cooling_unit_id}
    return cast(PumpCollection, s.get(**b))


@router.get(
    "/redfish/v1/ThermalEquipment/HeatExchangers/{cooling_unit_id}/Pumps",
    response_model_exclude_none=True,
)
@authenticate
async def get3(cooling_unit_id: str) -> PumpCollection:
    s: Service = find_service(PumpCollection)
    b: dict[str, Any] = {"cooling_unit_id": cooling_unit_id}
    return cast(PumpCollection, s.get(**b))


@router.get(
    "/redfish/v1/Chassis/{chassis_id}/ThermalSubsystem/Pumps", response_model_exclude_none=True
)
@authenticate
async def get4(chassis_id: str) -> PumpCollection:
    s: Service = find_service(PumpCollection)
    b: dict[str, Any] = {"chassis_id": chassis_id}
    return cast(PumpCollection, s.get(**b))
