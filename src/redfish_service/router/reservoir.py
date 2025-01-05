from typing import Any, cast

from fastapi import APIRouter

from ..model.reservoir import Reservoir
from ..service import Service, find_service
from . import authenticate

router = APIRouter()


@router.get(
    "/redfish/v1/ThermalEquipment/CDUs/{cooling_unit_id}/Reservoirs/{reservoir_id}",
    response_model_exclude_none=True,
)
@authenticate
async def get1(cooling_unit_id: str, reservoir_id: str) -> Reservoir:
    s: Service = find_service(Reservoir)
    b: dict[str, Any] = {"cooling_unit_id": cooling_unit_id, "reservoir_id": reservoir_id}
    return cast(Reservoir, s.get(**b))


@router.get(
    "/redfish/v1/ThermalEquipment/ImmersionUnits/{cooling_unit_id}/Reservoirs/{reservoir_id}",
    response_model_exclude_none=True,
)
@authenticate
async def get2(cooling_unit_id: str, reservoir_id: str) -> Reservoir:
    s: Service = find_service(Reservoir)
    b: dict[str, Any] = {"cooling_unit_id": cooling_unit_id, "reservoir_id": reservoir_id}
    return cast(Reservoir, s.get(**b))


@router.get(
    "/redfish/v1/ThermalEquipment/HeatExchangers/{cooling_unit_id}/Reservoirs/{reservoir_id}",
    response_model_exclude_none=True,
)
@authenticate
async def get3(cooling_unit_id: str, reservoir_id: str) -> Reservoir:
    s: Service = find_service(Reservoir)
    b: dict[str, Any] = {"cooling_unit_id": cooling_unit_id, "reservoir_id": reservoir_id}
    return cast(Reservoir, s.get(**b))
