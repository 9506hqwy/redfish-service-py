from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.pump import Pump
from ..service import Service, find_service

router = APIRouter()


@router.get(
    "/redfish/v1/ThermalEquipment/CDUs/{cooling_unit_id}/Pumps/{pump_id}",
    response_model_exclude_none=True,
)
@authenticate
async def get1(cooling_unit_id: str, pump_id: str, request: Request, response: Response) -> Pump:
    s: Service = find_service(Pump)
    b: dict[str, Any] = {
        "cooling_unit_id": cooling_unit_id,
        "pump_id": pump_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(Pump, s.get(**b))


@router.get(
    "/redfish/v1/ThermalEquipment/ImmersionUnits/{cooling_unit_id}/Pumps/{pump_id}",
    response_model_exclude_none=True,
)
@authenticate
async def get2(cooling_unit_id: str, pump_id: str, request: Request, response: Response) -> Pump:
    s: Service = find_service(Pump)
    b: dict[str, Any] = {
        "cooling_unit_id": cooling_unit_id,
        "pump_id": pump_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(Pump, s.get(**b))


@router.get(
    "/redfish/v1/ThermalEquipment/HeatExchangers/{cooling_unit_id}/Pumps/{pump_id}",
    response_model_exclude_none=True,
)
@authenticate
async def get3(cooling_unit_id: str, pump_id: str, request: Request, response: Response) -> Pump:
    s: Service = find_service(Pump)
    b: dict[str, Any] = {
        "cooling_unit_id": cooling_unit_id,
        "pump_id": pump_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(Pump, s.get(**b))


@router.get(
    "/redfish/v1/Chassis/{chassis_id}/ThermalSubsystem/Pumps/{pump_id}",
    response_model_exclude_none=True,
)
@authenticate
async def get4(chassis_id: str, pump_id: str, request: Request, response: Response) -> Pump:
    s: Service = find_service(Pump)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "pump_id": pump_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(Pump, s.get(**b))
