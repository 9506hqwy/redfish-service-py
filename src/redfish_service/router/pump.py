from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.pump import Pump, PumpOnUpdate
from ..service import Service
from ..util import get_service

router = APIRouter()


@router.get(
    "/redfish/v1/ThermalEquipment/CDUs/{cooling_unit_id}/Pumps/{pump_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ThermalEquipment/CDUs/{cooling_unit_id}/Pumps/{pump_id}",
    response_model_exclude_none=True,
)
async def get1(cooling_unit_id: str, pump_id: str, request: Request, response: Response) -> Pump:
    s: Service = get_service(Pump, request)
    b: dict[str, Any] = {
        "cooling_unit_id": cooling_unit_id,
        "pump_id": pump_id,
        "request": request,
        "response": response,
    }
    return cast(Pump, s.get(**b))


@router.patch(
    "/redfish/v1/ThermalEquipment/CDUs/{cooling_unit_id}/Pumps/{pump_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch1(
    cooling_unit_id: str, pump_id: str, request: Request, response: Response, body: PumpOnUpdate
) -> Pump:
    s: Service = get_service(Pump, request)
    b: dict[str, Any] = {
        "cooling_unit_id": cooling_unit_id,
        "pump_id": pump_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Pump, s.patch(**b))


@router.get(
    "/redfish/v1/ThermalEquipment/ImmersionUnits/{cooling_unit_id}/Pumps/{pump_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ThermalEquipment/ImmersionUnits/{cooling_unit_id}/Pumps/{pump_id}",
    response_model_exclude_none=True,
)
async def get2(cooling_unit_id: str, pump_id: str, request: Request, response: Response) -> Pump:
    s: Service = get_service(Pump, request)
    b: dict[str, Any] = {
        "cooling_unit_id": cooling_unit_id,
        "pump_id": pump_id,
        "request": request,
        "response": response,
    }
    return cast(Pump, s.get(**b))


@router.patch(
    "/redfish/v1/ThermalEquipment/ImmersionUnits/{cooling_unit_id}/Pumps/{pump_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch2(
    cooling_unit_id: str, pump_id: str, request: Request, response: Response, body: PumpOnUpdate
) -> Pump:
    s: Service = get_service(Pump, request)
    b: dict[str, Any] = {
        "cooling_unit_id": cooling_unit_id,
        "pump_id": pump_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Pump, s.patch(**b))


@router.get(
    "/redfish/v1/ThermalEquipment/HeatExchangers/{cooling_unit_id}/Pumps/{pump_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ThermalEquipment/HeatExchangers/{cooling_unit_id}/Pumps/{pump_id}",
    response_model_exclude_none=True,
)
async def get3(cooling_unit_id: str, pump_id: str, request: Request, response: Response) -> Pump:
    s: Service = get_service(Pump, request)
    b: dict[str, Any] = {
        "cooling_unit_id": cooling_unit_id,
        "pump_id": pump_id,
        "request": request,
        "response": response,
    }
    return cast(Pump, s.get(**b))


@router.patch(
    "/redfish/v1/ThermalEquipment/HeatExchangers/{cooling_unit_id}/Pumps/{pump_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch3(
    cooling_unit_id: str, pump_id: str, request: Request, response: Response, body: PumpOnUpdate
) -> Pump:
    s: Service = get_service(Pump, request)
    b: dict[str, Any] = {
        "cooling_unit_id": cooling_unit_id,
        "pump_id": pump_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Pump, s.patch(**b))


@router.get(
    "/redfish/v1/Chassis/{chassis_id}/ThermalSubsystem/Pumps/{pump_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Chassis/{chassis_id}/ThermalSubsystem/Pumps/{pump_id}",
    response_model_exclude_none=True,
)
async def get4(chassis_id: str, pump_id: str, request: Request, response: Response) -> Pump:
    s: Service = get_service(Pump, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "pump_id": pump_id,
        "request": request,
        "response": response,
    }
    return cast(Pump, s.get(**b))


@router.patch(
    "/redfish/v1/Chassis/{chassis_id}/ThermalSubsystem/Pumps/{pump_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch4(
    chassis_id: str, pump_id: str, request: Request, response: Response, body: PumpOnUpdate
) -> Pump:
    s: Service = get_service(Pump, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "pump_id": pump_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Pump, s.patch(**b))
