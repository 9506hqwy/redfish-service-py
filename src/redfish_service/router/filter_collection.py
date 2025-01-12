from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..model.filter_collection import FilterCollection
from ..service import Service
from ..util import get_service

router = APIRouter()


@router.get(
    "/redfish/v1/Chassis/{chassis_id}/ThermalSubsystem/Pumps/{pump_id}/Filters",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Chassis/{chassis_id}/ThermalSubsystem/Pumps/{pump_id}/Filters",
    response_model_exclude_none=True,
)
async def get1(
    chassis_id: str, pump_id: str, request: Request, response: Response
) -> FilterCollection:
    s: Service = get_service(FilterCollection, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "pump_id": pump_id,
        "request": request,
        "response": response,
    }
    return cast(FilterCollection, s.get(**b))


@router.get(
    "/redfish/v1/ThermalEquipment/CDUs/{cooling_unit_id}/Filters", response_model_exclude_none=True
)
@router.head(
    "/redfish/v1/ThermalEquipment/CDUs/{cooling_unit_id}/Filters", response_model_exclude_none=True
)
async def get2(cooling_unit_id: str, request: Request, response: Response) -> FilterCollection:
    s: Service = get_service(FilterCollection, request)
    b: dict[str, Any] = {
        "cooling_unit_id": cooling_unit_id,
        "request": request,
        "response": response,
    }
    return cast(FilterCollection, s.get(**b))


@router.get(
    "/redfish/v1/ThermalEquipment/CDUs/{cooling_unit_id}/Reservoirs/{reservoir_id}/Filters",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ThermalEquipment/CDUs/{cooling_unit_id}/Reservoirs/{reservoir_id}/Filters",
    response_model_exclude_none=True,
)
async def get3(
    cooling_unit_id: str, reservoir_id: str, request: Request, response: Response
) -> FilterCollection:
    s: Service = get_service(FilterCollection, request)
    b: dict[str, Any] = {
        "cooling_unit_id": cooling_unit_id,
        "reservoir_id": reservoir_id,
        "request": request,
        "response": response,
    }
    return cast(FilterCollection, s.get(**b))


@router.get(
    "/redfish/v1/ThermalEquipment/CDUs/{cooling_unit_id}/Pumps/{pump_id}/Filters",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ThermalEquipment/CDUs/{cooling_unit_id}/Pumps/{pump_id}/Filters",
    response_model_exclude_none=True,
)
async def get4(
    cooling_unit_id: str, pump_id: str, request: Request, response: Response
) -> FilterCollection:
    s: Service = get_service(FilterCollection, request)
    b: dict[str, Any] = {
        "cooling_unit_id": cooling_unit_id,
        "pump_id": pump_id,
        "request": request,
        "response": response,
    }
    return cast(FilterCollection, s.get(**b))


@router.get(
    "/redfish/v1/ThermalEquipment/ImmersionUnits/{cooling_unit_id}/Filters",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ThermalEquipment/ImmersionUnits/{cooling_unit_id}/Filters",
    response_model_exclude_none=True,
)
async def get5(cooling_unit_id: str, request: Request, response: Response) -> FilterCollection:
    s: Service = get_service(FilterCollection, request)
    b: dict[str, Any] = {
        "cooling_unit_id": cooling_unit_id,
        "request": request,
        "response": response,
    }
    return cast(FilterCollection, s.get(**b))


@router.get(
    "/redfish/v1/ThermalEquipment/ImmersionUnits/{cooling_unit_id}/Reservoirs/{reservoir_id}/Filters",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ThermalEquipment/ImmersionUnits/{cooling_unit_id}/Reservoirs/{reservoir_id}/Filters",
    response_model_exclude_none=True,
)
async def get6(
    cooling_unit_id: str, reservoir_id: str, request: Request, response: Response
) -> FilterCollection:
    s: Service = get_service(FilterCollection, request)
    b: dict[str, Any] = {
        "cooling_unit_id": cooling_unit_id,
        "reservoir_id": reservoir_id,
        "request": request,
        "response": response,
    }
    return cast(FilterCollection, s.get(**b))


@router.get(
    "/redfish/v1/ThermalEquipment/ImmersionUnits/{cooling_unit_id}/Pumps/{pump_id}/Filters",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ThermalEquipment/ImmersionUnits/{cooling_unit_id}/Pumps/{pump_id}/Filters",
    response_model_exclude_none=True,
)
async def get7(
    cooling_unit_id: str, pump_id: str, request: Request, response: Response
) -> FilterCollection:
    s: Service = get_service(FilterCollection, request)
    b: dict[str, Any] = {
        "cooling_unit_id": cooling_unit_id,
        "pump_id": pump_id,
        "request": request,
        "response": response,
    }
    return cast(FilterCollection, s.get(**b))


@router.get(
    "/redfish/v1/ThermalEquipment/HeatExchangers/{cooling_unit_id}/Filters",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ThermalEquipment/HeatExchangers/{cooling_unit_id}/Filters",
    response_model_exclude_none=True,
)
async def get8(cooling_unit_id: str, request: Request, response: Response) -> FilterCollection:
    s: Service = get_service(FilterCollection, request)
    b: dict[str, Any] = {
        "cooling_unit_id": cooling_unit_id,
        "request": request,
        "response": response,
    }
    return cast(FilterCollection, s.get(**b))


@router.get(
    "/redfish/v1/ThermalEquipment/HeatExchangers/{cooling_unit_id}/Reservoirs/{reservoir_id}/Filters",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ThermalEquipment/HeatExchangers/{cooling_unit_id}/Reservoirs/{reservoir_id}/Filters",
    response_model_exclude_none=True,
)
async def get9(
    cooling_unit_id: str, reservoir_id: str, request: Request, response: Response
) -> FilterCollection:
    s: Service = get_service(FilterCollection, request)
    b: dict[str, Any] = {
        "cooling_unit_id": cooling_unit_id,
        "reservoir_id": reservoir_id,
        "request": request,
        "response": response,
    }
    return cast(FilterCollection, s.get(**b))


@router.get(
    "/redfish/v1/ThermalEquipment/HeatExchangers/{cooling_unit_id}/Pumps/{pump_id}/Filters",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ThermalEquipment/HeatExchangers/{cooling_unit_id}/Pumps/{pump_id}/Filters",
    response_model_exclude_none=True,
)
async def get10(
    cooling_unit_id: str, pump_id: str, request: Request, response: Response
) -> FilterCollection:
    s: Service = get_service(FilterCollection, request)
    b: dict[str, Any] = {
        "cooling_unit_id": cooling_unit_id,
        "pump_id": pump_id,
        "request": request,
        "response": response,
    }
    return cast(FilterCollection, s.get(**b))
