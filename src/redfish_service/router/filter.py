from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.filter import Filter
from ..service import Service, find_service

router = APIRouter()


@router.get(
    "/redfish/v1/Chassis/{chassis_id}/ThermalSubsystem/Pumps/{pump_id}/Filters/{filter_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Chassis/{chassis_id}/ThermalSubsystem/Pumps/{pump_id}/Filters/{filter_id}",
    response_model_exclude_none=True,
)
@authenticate
async def get1(
    chassis_id: str, pump_id: str, filter_id: str, request: Request, response: Response
) -> Filter:
    s: Service = find_service(Filter)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "pump_id": pump_id,
        "filter_id": filter_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(Filter, s.get(**b))


@router.get(
    "/redfish/v1/ThermalEquipment/CDUs/{cooling_unit_id}/Filters/{filter_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ThermalEquipment/CDUs/{cooling_unit_id}/Filters/{filter_id}",
    response_model_exclude_none=True,
)
@authenticate
async def get2(
    cooling_unit_id: str, filter_id: str, request: Request, response: Response
) -> Filter:
    s: Service = find_service(Filter)
    b: dict[str, Any] = {
        "cooling_unit_id": cooling_unit_id,
        "filter_id": filter_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(Filter, s.get(**b))


@router.get(
    "/redfish/v1/ThermalEquipment/CDUs/{cooling_unit_id}/Reservoirs/{reservoir_id}/Filters/{filter_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ThermalEquipment/CDUs/{cooling_unit_id}/Reservoirs/{reservoir_id}/Filters/{filter_id}",
    response_model_exclude_none=True,
)
@authenticate
async def get3(
    cooling_unit_id: str, reservoir_id: str, filter_id: str, request: Request, response: Response
) -> Filter:
    s: Service = find_service(Filter)
    b: dict[str, Any] = {
        "cooling_unit_id": cooling_unit_id,
        "reservoir_id": reservoir_id,
        "filter_id": filter_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(Filter, s.get(**b))


@router.get(
    "/redfish/v1/ThermalEquipment/CDUs/{cooling_unit_id}/Pumps/{pump_id}/Filters/{filter_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ThermalEquipment/CDUs/{cooling_unit_id}/Pumps/{pump_id}/Filters/{filter_id}",
    response_model_exclude_none=True,
)
@authenticate
async def get4(
    cooling_unit_id: str, pump_id: str, filter_id: str, request: Request, response: Response
) -> Filter:
    s: Service = find_service(Filter)
    b: dict[str, Any] = {
        "cooling_unit_id": cooling_unit_id,
        "pump_id": pump_id,
        "filter_id": filter_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(Filter, s.get(**b))


@router.get(
    "/redfish/v1/ThermalEquipment/ImmersionUnits/{cooling_unit_id}/Filters/{filter_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ThermalEquipment/ImmersionUnits/{cooling_unit_id}/Filters/{filter_id}",
    response_model_exclude_none=True,
)
@authenticate
async def get5(
    cooling_unit_id: str, filter_id: str, request: Request, response: Response
) -> Filter:
    s: Service = find_service(Filter)
    b: dict[str, Any] = {
        "cooling_unit_id": cooling_unit_id,
        "filter_id": filter_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(Filter, s.get(**b))


@router.get(
    "/redfish/v1/ThermalEquipment/ImmersionUnits/{cooling_unit_id}/Reservoirs/{reservoir_id}/Filters/{filter_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ThermalEquipment/ImmersionUnits/{cooling_unit_id}/Reservoirs/{reservoir_id}/Filters/{filter_id}",
    response_model_exclude_none=True,
)
@authenticate
async def get6(
    cooling_unit_id: str, reservoir_id: str, filter_id: str, request: Request, response: Response
) -> Filter:
    s: Service = find_service(Filter)
    b: dict[str, Any] = {
        "cooling_unit_id": cooling_unit_id,
        "reservoir_id": reservoir_id,
        "filter_id": filter_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(Filter, s.get(**b))


@router.get(
    "/redfish/v1/ThermalEquipment/ImmersionUnits/{cooling_unit_id}/Pumps/{pump_id}/Filters/{filter_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ThermalEquipment/ImmersionUnits/{cooling_unit_id}/Pumps/{pump_id}/Filters/{filter_id}",
    response_model_exclude_none=True,
)
@authenticate
async def get7(
    cooling_unit_id: str, pump_id: str, filter_id: str, request: Request, response: Response
) -> Filter:
    s: Service = find_service(Filter)
    b: dict[str, Any] = {
        "cooling_unit_id": cooling_unit_id,
        "pump_id": pump_id,
        "filter_id": filter_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(Filter, s.get(**b))


@router.get(
    "/redfish/v1/ThermalEquipment/HeatExchangers/{cooling_unit_id}/Filters/{filter_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ThermalEquipment/HeatExchangers/{cooling_unit_id}/Filters/{filter_id}",
    response_model_exclude_none=True,
)
@authenticate
async def get8(
    cooling_unit_id: str, filter_id: str, request: Request, response: Response
) -> Filter:
    s: Service = find_service(Filter)
    b: dict[str, Any] = {
        "cooling_unit_id": cooling_unit_id,
        "filter_id": filter_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(Filter, s.get(**b))


@router.get(
    "/redfish/v1/ThermalEquipment/HeatExchangers/{cooling_unit_id}/Reservoirs/{reservoir_id}/Filters/{filter_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ThermalEquipment/HeatExchangers/{cooling_unit_id}/Reservoirs/{reservoir_id}/Filters/{filter_id}",
    response_model_exclude_none=True,
)
@authenticate
async def get9(
    cooling_unit_id: str, reservoir_id: str, filter_id: str, request: Request, response: Response
) -> Filter:
    s: Service = find_service(Filter)
    b: dict[str, Any] = {
        "cooling_unit_id": cooling_unit_id,
        "reservoir_id": reservoir_id,
        "filter_id": filter_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(Filter, s.get(**b))


@router.get(
    "/redfish/v1/ThermalEquipment/HeatExchangers/{cooling_unit_id}/Pumps/{pump_id}/Filters/{filter_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ThermalEquipment/HeatExchangers/{cooling_unit_id}/Pumps/{pump_id}/Filters/{filter_id}",
    response_model_exclude_none=True,
)
@authenticate
async def get10(
    cooling_unit_id: str, pump_id: str, filter_id: str, request: Request, response: Response
) -> Filter:
    s: Service = find_service(Filter)
    b: dict[str, Any] = {
        "cooling_unit_id": cooling_unit_id,
        "pump_id": pump_id,
        "filter_id": filter_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(Filter, s.get(**b))
