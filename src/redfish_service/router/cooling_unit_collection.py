from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..model.cooling_unit_collection import CoolingUnitCollection
from ..service import Service
from ..util import get_service, set_link_header

router = APIRouter()


@router.get("/redfish/v1/ThermalEquipment/CDUs", response_model_exclude_none=True)
@router.head("/redfish/v1/ThermalEquipment/CDUs", response_model_exclude_none=True)
async def get1(request: Request, response: Response) -> CoolingUnitCollection:
    s: Service = get_service(CoolingUnitCollection, request)
    b: dict[str, Any] = {"request": request, "response": response}
    m = cast(CoolingUnitCollection, s.get(**b))
    set_link_header(m, response)
    return m


@router.get("/redfish/v1/ThermalEquipment/ImmersionUnits", response_model_exclude_none=True)
@router.head("/redfish/v1/ThermalEquipment/ImmersionUnits", response_model_exclude_none=True)
async def get2(request: Request, response: Response) -> CoolingUnitCollection:
    s: Service = get_service(CoolingUnitCollection, request)
    b: dict[str, Any] = {"request": request, "response": response}
    m = cast(CoolingUnitCollection, s.get(**b))
    set_link_header(m, response)
    return m


@router.get("/redfish/v1/ThermalEquipment/HeatExchangers", response_model_exclude_none=True)
@router.head("/redfish/v1/ThermalEquipment/HeatExchangers", response_model_exclude_none=True)
async def get3(request: Request, response: Response) -> CoolingUnitCollection:
    s: Service = get_service(CoolingUnitCollection, request)
    b: dict[str, Any] = {"request": request, "response": response}
    m = cast(CoolingUnitCollection, s.get(**b))
    set_link_header(m, response)
    return m
