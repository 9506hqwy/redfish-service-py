from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..model.reservoir_collection import ReservoirCollection
from ..service import Service
from ..util import get_service, set_link_header

router = APIRouter()


@router.get(
    "/redfish/v1/ThermalEquipment/CDUs/{cooling_unit_id}/Reservoirs",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ThermalEquipment/CDUs/{cooling_unit_id}/Reservoirs",
    response_model_exclude_none=True,
)
async def get1(cooling_unit_id: str, request: Request, response: Response) -> ReservoirCollection:
    s: Service = get_service(ReservoirCollection, request)
    b: dict[str, Any] = {
        "cooling_unit_id": cooling_unit_id,
        "request": request,
        "response": response,
    }
    m = cast(ReservoirCollection, s.get(**b))
    set_link_header(m, response)
    return m


@router.get(
    "/redfish/v1/ThermalEquipment/ImmersionUnits/{cooling_unit_id}/Reservoirs",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ThermalEquipment/ImmersionUnits/{cooling_unit_id}/Reservoirs",
    response_model_exclude_none=True,
)
async def get2(cooling_unit_id: str, request: Request, response: Response) -> ReservoirCollection:
    s: Service = get_service(ReservoirCollection, request)
    b: dict[str, Any] = {
        "cooling_unit_id": cooling_unit_id,
        "request": request,
        "response": response,
    }
    m = cast(ReservoirCollection, s.get(**b))
    set_link_header(m, response)
    return m


@router.get(
    "/redfish/v1/ThermalEquipment/HeatExchangers/{cooling_unit_id}/Reservoirs",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ThermalEquipment/HeatExchangers/{cooling_unit_id}/Reservoirs",
    response_model_exclude_none=True,
)
async def get3(cooling_unit_id: str, request: Request, response: Response) -> ReservoirCollection:
    s: Service = get_service(ReservoirCollection, request)
    b: dict[str, Any] = {
        "cooling_unit_id": cooling_unit_id,
        "request": request,
        "response": response,
    }
    m = cast(ReservoirCollection, s.get(**b))
    set_link_header(m, response)
    return m
