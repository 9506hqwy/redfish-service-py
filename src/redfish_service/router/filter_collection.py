from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..model.filter_collection import FilterCollection
from ..service import Service
from ..util import get_service, set_link_header

router = APIRouter()


@router.get(
    "/redfish/v1/Chassis/{chassis_id}/ThermalSubsystem/Filters", response_model_exclude_none=True
)
@router.head(
    "/redfish/v1/Chassis/{chassis_id}/ThermalSubsystem/Filters", response_model_exclude_none=True
)
async def get1(chassis_id: str, request: Request, response: Response) -> FilterCollection:
    s: Service = get_service(FilterCollection, request)
    b: dict[str, Any] = {"chassis_id": chassis_id, "request": request, "response": response}
    m = cast(FilterCollection, s.get(**b))
    set_link_header(m, response)
    return m


@router.get(
    "/redfish/v1/Chassis/{chassis_id}/ThermalSubsystem/Pumps/{pump_id}/Filters",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Chassis/{chassis_id}/ThermalSubsystem/Pumps/{pump_id}/Filters",
    response_model_exclude_none=True,
)
async def get2(
    chassis_id: str, pump_id: str, request: Request, response: Response
) -> FilterCollection:
    s: Service = get_service(FilterCollection, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "pump_id": pump_id,
        "request": request,
        "response": response,
    }
    m = cast(FilterCollection, s.get(**b))
    set_link_header(m, response)
    return m


@router.get(
    "/redfish/v1/ThermalEquipment/CDUs/{cooling_unit_id}/Filters", response_model_exclude_none=True
)
@router.head(
    "/redfish/v1/ThermalEquipment/CDUs/{cooling_unit_id}/Filters", response_model_exclude_none=True
)
async def get3(cooling_unit_id: str, request: Request, response: Response) -> FilterCollection:
    s: Service = get_service(FilterCollection, request)
    b: dict[str, Any] = {
        "cooling_unit_id": cooling_unit_id,
        "request": request,
        "response": response,
    }
    m = cast(FilterCollection, s.get(**b))
    set_link_header(m, response)
    return m


@router.get(
    "/redfish/v1/ThermalEquipment/CDUs/{cooling_unit_id}/Reservoirs/{reservoir_id}/Filters",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ThermalEquipment/CDUs/{cooling_unit_id}/Reservoirs/{reservoir_id}/Filters",
    response_model_exclude_none=True,
)
async def get4(
    cooling_unit_id: str, reservoir_id: str, request: Request, response: Response
) -> FilterCollection:
    s: Service = get_service(FilterCollection, request)
    b: dict[str, Any] = {
        "cooling_unit_id": cooling_unit_id,
        "reservoir_id": reservoir_id,
        "request": request,
        "response": response,
    }
    m = cast(FilterCollection, s.get(**b))
    set_link_header(m, response)
    return m


@router.get(
    "/redfish/v1/ThermalEquipment/CDUs/{cooling_unit_id}/Pumps/{pump_id}/Filters",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ThermalEquipment/CDUs/{cooling_unit_id}/Pumps/{pump_id}/Filters",
    response_model_exclude_none=True,
)
async def get5(
    cooling_unit_id: str, pump_id: str, request: Request, response: Response
) -> FilterCollection:
    s: Service = get_service(FilterCollection, request)
    b: dict[str, Any] = {
        "cooling_unit_id": cooling_unit_id,
        "pump_id": pump_id,
        "request": request,
        "response": response,
    }
    m = cast(FilterCollection, s.get(**b))
    set_link_header(m, response)
    return m


@router.get(
    "/redfish/v1/ThermalEquipment/ImmersionUnits/{cooling_unit_id}/Filters",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ThermalEquipment/ImmersionUnits/{cooling_unit_id}/Filters",
    response_model_exclude_none=True,
)
async def get6(cooling_unit_id: str, request: Request, response: Response) -> FilterCollection:
    s: Service = get_service(FilterCollection, request)
    b: dict[str, Any] = {
        "cooling_unit_id": cooling_unit_id,
        "request": request,
        "response": response,
    }
    m = cast(FilterCollection, s.get(**b))
    set_link_header(m, response)
    return m


@router.get(
    "/redfish/v1/ThermalEquipment/ImmersionUnits/{cooling_unit_id}/Reservoirs/{reservoir_id}/Filters",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ThermalEquipment/ImmersionUnits/{cooling_unit_id}/Reservoirs/{reservoir_id}/Filters",
    response_model_exclude_none=True,
)
async def get7(
    cooling_unit_id: str, reservoir_id: str, request: Request, response: Response
) -> FilterCollection:
    s: Service = get_service(FilterCollection, request)
    b: dict[str, Any] = {
        "cooling_unit_id": cooling_unit_id,
        "reservoir_id": reservoir_id,
        "request": request,
        "response": response,
    }
    m = cast(FilterCollection, s.get(**b))
    set_link_header(m, response)
    return m


@router.get(
    "/redfish/v1/ThermalEquipment/ImmersionUnits/{cooling_unit_id}/Pumps/{pump_id}/Filters",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ThermalEquipment/ImmersionUnits/{cooling_unit_id}/Pumps/{pump_id}/Filters",
    response_model_exclude_none=True,
)
async def get8(
    cooling_unit_id: str, pump_id: str, request: Request, response: Response
) -> FilterCollection:
    s: Service = get_service(FilterCollection, request)
    b: dict[str, Any] = {
        "cooling_unit_id": cooling_unit_id,
        "pump_id": pump_id,
        "request": request,
        "response": response,
    }
    m = cast(FilterCollection, s.get(**b))
    set_link_header(m, response)
    return m


@router.get(
    "/redfish/v1/ThermalEquipment/HeatExchangers/{cooling_unit_id}/Filters",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ThermalEquipment/HeatExchangers/{cooling_unit_id}/Filters",
    response_model_exclude_none=True,
)
async def get9(cooling_unit_id: str, request: Request, response: Response) -> FilterCollection:
    s: Service = get_service(FilterCollection, request)
    b: dict[str, Any] = {
        "cooling_unit_id": cooling_unit_id,
        "request": request,
        "response": response,
    }
    m = cast(FilterCollection, s.get(**b))
    set_link_header(m, response)
    return m


@router.get(
    "/redfish/v1/ThermalEquipment/HeatExchangers/{cooling_unit_id}/Reservoirs/{reservoir_id}/Filters",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ThermalEquipment/HeatExchangers/{cooling_unit_id}/Reservoirs/{reservoir_id}/Filters",
    response_model_exclude_none=True,
)
async def get10(
    cooling_unit_id: str, reservoir_id: str, request: Request, response: Response
) -> FilterCollection:
    s: Service = get_service(FilterCollection, request)
    b: dict[str, Any] = {
        "cooling_unit_id": cooling_unit_id,
        "reservoir_id": reservoir_id,
        "request": request,
        "response": response,
    }
    m = cast(FilterCollection, s.get(**b))
    set_link_header(m, response)
    return m


@router.get(
    "/redfish/v1/ThermalEquipment/HeatExchangers/{cooling_unit_id}/Pumps/{pump_id}/Filters",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ThermalEquipment/HeatExchangers/{cooling_unit_id}/Pumps/{pump_id}/Filters",
    response_model_exclude_none=True,
)
async def get11(
    cooling_unit_id: str, pump_id: str, request: Request, response: Response
) -> FilterCollection:
    s: Service = get_service(FilterCollection, request)
    b: dict[str, Any] = {
        "cooling_unit_id": cooling_unit_id,
        "pump_id": pump_id,
        "request": request,
        "response": response,
    }
    m = cast(FilterCollection, s.get(**b))
    set_link_header(m, response)
    return m


@router.get(
    "/redfish/v1/ThermalEquipment/RPUs/{cooling_unit_id}/Filters", response_model_exclude_none=True
)
@router.head(
    "/redfish/v1/ThermalEquipment/RPUs/{cooling_unit_id}/Filters", response_model_exclude_none=True
)
async def get12(cooling_unit_id: str, request: Request, response: Response) -> FilterCollection:
    s: Service = get_service(FilterCollection, request)
    b: dict[str, Any] = {
        "cooling_unit_id": cooling_unit_id,
        "request": request,
        "response": response,
    }
    m = cast(FilterCollection, s.get(**b))
    set_link_header(m, response)
    return m


@router.get(
    "/redfish/v1/ThermalEquipment/RPUs/{cooling_unit_id}/Reservoirs/{reservoir_id}/Filters",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ThermalEquipment/RPUs/{cooling_unit_id}/Reservoirs/{reservoir_id}/Filters",
    response_model_exclude_none=True,
)
async def get13(
    cooling_unit_id: str, reservoir_id: str, request: Request, response: Response
) -> FilterCollection:
    s: Service = get_service(FilterCollection, request)
    b: dict[str, Any] = {
        "cooling_unit_id": cooling_unit_id,
        "reservoir_id": reservoir_id,
        "request": request,
        "response": response,
    }
    m = cast(FilterCollection, s.get(**b))
    set_link_header(m, response)
    return m


@router.get(
    "/redfish/v1/ThermalEquipment/RPUs/{cooling_unit_id}/Pumps/{pump_id}/Filters",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ThermalEquipment/RPUs/{cooling_unit_id}/Pumps/{pump_id}/Filters",
    response_model_exclude_none=True,
)
async def get14(
    cooling_unit_id: str, pump_id: str, request: Request, response: Response
) -> FilterCollection:
    s: Service = get_service(FilterCollection, request)
    b: dict[str, Any] = {
        "cooling_unit_id": cooling_unit_id,
        "pump_id": pump_id,
        "request": request,
        "response": response,
    }
    m = cast(FilterCollection, s.get(**b))
    set_link_header(m, response)
    return m
