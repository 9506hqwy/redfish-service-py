from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..model.pump_collection import PumpCollection
from ..service import Service
from ..util import get_service, set_link_header

router = APIRouter()


@router.get(
    "/redfish/v1/ThermalEquipment/CDUs/{cooling_unit_id}/Pumps", response_model_exclude_none=True
)
@router.head(
    "/redfish/v1/ThermalEquipment/CDUs/{cooling_unit_id}/Pumps", response_model_exclude_none=True
)
async def get1(cooling_unit_id: str, request: Request, response: Response) -> PumpCollection:
    s: Service = get_service(PumpCollection, request)
    b: dict[str, Any] = {
        "cooling_unit_id": cooling_unit_id,
        "request": request,
        "response": response,
    }
    m = cast(PumpCollection, s.get(**b))
    set_link_header(m, response)
    return m


@router.get(
    "/redfish/v1/ThermalEquipment/ImmersionUnits/{cooling_unit_id}/Pumps",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ThermalEquipment/ImmersionUnits/{cooling_unit_id}/Pumps",
    response_model_exclude_none=True,
)
async def get2(cooling_unit_id: str, request: Request, response: Response) -> PumpCollection:
    s: Service = get_service(PumpCollection, request)
    b: dict[str, Any] = {
        "cooling_unit_id": cooling_unit_id,
        "request": request,
        "response": response,
    }
    m = cast(PumpCollection, s.get(**b))
    set_link_header(m, response)
    return m


@router.get(
    "/redfish/v1/ThermalEquipment/HeatExchangers/{cooling_unit_id}/Pumps",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ThermalEquipment/HeatExchangers/{cooling_unit_id}/Pumps",
    response_model_exclude_none=True,
)
async def get3(cooling_unit_id: str, request: Request, response: Response) -> PumpCollection:
    s: Service = get_service(PumpCollection, request)
    b: dict[str, Any] = {
        "cooling_unit_id": cooling_unit_id,
        "request": request,
        "response": response,
    }
    m = cast(PumpCollection, s.get(**b))
    set_link_header(m, response)
    return m


@router.get(
    "/redfish/v1/ThermalEquipment/RPUs/{cooling_unit_id}/Pumps", response_model_exclude_none=True
)
@router.head(
    "/redfish/v1/ThermalEquipment/RPUs/{cooling_unit_id}/Pumps", response_model_exclude_none=True
)
async def get4(cooling_unit_id: str, request: Request, response: Response) -> PumpCollection:
    s: Service = get_service(PumpCollection, request)
    b: dict[str, Any] = {
        "cooling_unit_id": cooling_unit_id,
        "request": request,
        "response": response,
    }
    m = cast(PumpCollection, s.get(**b))
    set_link_header(m, response)
    return m


@router.get(
    "/redfish/v1/Chassis/{chassis_id}/ThermalSubsystem/Pumps", response_model_exclude_none=True
)
@router.head(
    "/redfish/v1/Chassis/{chassis_id}/ThermalSubsystem/Pumps", response_model_exclude_none=True
)
async def get5(chassis_id: str, request: Request, response: Response) -> PumpCollection:
    s: Service = get_service(PumpCollection, request)
    b: dict[str, Any] = {"chassis_id": chassis_id, "request": request, "response": response}
    m = cast(PumpCollection, s.get(**b))
    set_link_header(m, response)
    return m
