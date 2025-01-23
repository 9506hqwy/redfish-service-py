from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.filter import Filter, FilterOnUpdate
from ..service import Service
from ..util import get_service, set_link_header

router = APIRouter()


@router.get(
    "/redfish/v1/Chassis/{chassis_id}/ThermalSubsystem/Pumps/{pump_id}/Filters/{filter_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Chassis/{chassis_id}/ThermalSubsystem/Pumps/{pump_id}/Filters/{filter_id}",
    response_model_exclude_none=True,
)
async def get1(
    chassis_id: str, pump_id: str, filter_id: str, request: Request, response: Response
) -> Filter:
    s: Service = get_service(Filter, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "pump_id": pump_id,
        "filter_id": filter_id,
        "request": request,
        "response": response,
    }
    m = cast(Filter, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/Chassis/{chassis_id}/ThermalSubsystem/Pumps/{pump_id}/Filters/{filter_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch1(
    chassis_id: str,
    pump_id: str,
    filter_id: str,
    request: Request,
    response: Response,
    body: FilterOnUpdate,
) -> Filter:
    s: Service = get_service(Filter, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "pump_id": pump_id,
        "filter_id": filter_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Filter, s.patch(**b))


@router.get(
    "/redfish/v1/ThermalEquipment/CDUs/{cooling_unit_id}/Filters/{filter_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ThermalEquipment/CDUs/{cooling_unit_id}/Filters/{filter_id}",
    response_model_exclude_none=True,
)
async def get2(
    cooling_unit_id: str, filter_id: str, request: Request, response: Response
) -> Filter:
    s: Service = get_service(Filter, request)
    b: dict[str, Any] = {
        "cooling_unit_id": cooling_unit_id,
        "filter_id": filter_id,
        "request": request,
        "response": response,
    }
    m = cast(Filter, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/ThermalEquipment/CDUs/{cooling_unit_id}/Filters/{filter_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch2(
    cooling_unit_id: str,
    filter_id: str,
    request: Request,
    response: Response,
    body: FilterOnUpdate,
) -> Filter:
    s: Service = get_service(Filter, request)
    b: dict[str, Any] = {
        "cooling_unit_id": cooling_unit_id,
        "filter_id": filter_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Filter, s.patch(**b))


@router.get(
    "/redfish/v1/ThermalEquipment/CDUs/{cooling_unit_id}/Reservoirs/{reservoir_id}/Filters/{filter_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ThermalEquipment/CDUs/{cooling_unit_id}/Reservoirs/{reservoir_id}/Filters/{filter_id}",
    response_model_exclude_none=True,
)
async def get3(
    cooling_unit_id: str, reservoir_id: str, filter_id: str, request: Request, response: Response
) -> Filter:
    s: Service = get_service(Filter, request)
    b: dict[str, Any] = {
        "cooling_unit_id": cooling_unit_id,
        "reservoir_id": reservoir_id,
        "filter_id": filter_id,
        "request": request,
        "response": response,
    }
    m = cast(Filter, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/ThermalEquipment/CDUs/{cooling_unit_id}/Reservoirs/{reservoir_id}/Filters/{filter_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch3(
    cooling_unit_id: str,
    reservoir_id: str,
    filter_id: str,
    request: Request,
    response: Response,
    body: FilterOnUpdate,
) -> Filter:
    s: Service = get_service(Filter, request)
    b: dict[str, Any] = {
        "cooling_unit_id": cooling_unit_id,
        "reservoir_id": reservoir_id,
        "filter_id": filter_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Filter, s.patch(**b))


@router.get(
    "/redfish/v1/ThermalEquipment/CDUs/{cooling_unit_id}/Pumps/{pump_id}/Filters/{filter_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ThermalEquipment/CDUs/{cooling_unit_id}/Pumps/{pump_id}/Filters/{filter_id}",
    response_model_exclude_none=True,
)
async def get4(
    cooling_unit_id: str, pump_id: str, filter_id: str, request: Request, response: Response
) -> Filter:
    s: Service = get_service(Filter, request)
    b: dict[str, Any] = {
        "cooling_unit_id": cooling_unit_id,
        "pump_id": pump_id,
        "filter_id": filter_id,
        "request": request,
        "response": response,
    }
    m = cast(Filter, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/ThermalEquipment/CDUs/{cooling_unit_id}/Pumps/{pump_id}/Filters/{filter_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch4(
    cooling_unit_id: str,
    pump_id: str,
    filter_id: str,
    request: Request,
    response: Response,
    body: FilterOnUpdate,
) -> Filter:
    s: Service = get_service(Filter, request)
    b: dict[str, Any] = {
        "cooling_unit_id": cooling_unit_id,
        "pump_id": pump_id,
        "filter_id": filter_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Filter, s.patch(**b))


@router.get(
    "/redfish/v1/ThermalEquipment/ImmersionUnits/{cooling_unit_id}/Filters/{filter_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ThermalEquipment/ImmersionUnits/{cooling_unit_id}/Filters/{filter_id}",
    response_model_exclude_none=True,
)
async def get5(
    cooling_unit_id: str, filter_id: str, request: Request, response: Response
) -> Filter:
    s: Service = get_service(Filter, request)
    b: dict[str, Any] = {
        "cooling_unit_id": cooling_unit_id,
        "filter_id": filter_id,
        "request": request,
        "response": response,
    }
    m = cast(Filter, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/ThermalEquipment/ImmersionUnits/{cooling_unit_id}/Filters/{filter_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch5(
    cooling_unit_id: str,
    filter_id: str,
    request: Request,
    response: Response,
    body: FilterOnUpdate,
) -> Filter:
    s: Service = get_service(Filter, request)
    b: dict[str, Any] = {
        "cooling_unit_id": cooling_unit_id,
        "filter_id": filter_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Filter, s.patch(**b))


@router.get(
    "/redfish/v1/ThermalEquipment/ImmersionUnits/{cooling_unit_id}/Reservoirs/{reservoir_id}/Filters/{filter_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ThermalEquipment/ImmersionUnits/{cooling_unit_id}/Reservoirs/{reservoir_id}/Filters/{filter_id}",
    response_model_exclude_none=True,
)
async def get6(
    cooling_unit_id: str, reservoir_id: str, filter_id: str, request: Request, response: Response
) -> Filter:
    s: Service = get_service(Filter, request)
    b: dict[str, Any] = {
        "cooling_unit_id": cooling_unit_id,
        "reservoir_id": reservoir_id,
        "filter_id": filter_id,
        "request": request,
        "response": response,
    }
    m = cast(Filter, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/ThermalEquipment/ImmersionUnits/{cooling_unit_id}/Reservoirs/{reservoir_id}/Filters/{filter_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch6(
    cooling_unit_id: str,
    reservoir_id: str,
    filter_id: str,
    request: Request,
    response: Response,
    body: FilterOnUpdate,
) -> Filter:
    s: Service = get_service(Filter, request)
    b: dict[str, Any] = {
        "cooling_unit_id": cooling_unit_id,
        "reservoir_id": reservoir_id,
        "filter_id": filter_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Filter, s.patch(**b))


@router.get(
    "/redfish/v1/ThermalEquipment/ImmersionUnits/{cooling_unit_id}/Pumps/{pump_id}/Filters/{filter_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ThermalEquipment/ImmersionUnits/{cooling_unit_id}/Pumps/{pump_id}/Filters/{filter_id}",
    response_model_exclude_none=True,
)
async def get7(
    cooling_unit_id: str, pump_id: str, filter_id: str, request: Request, response: Response
) -> Filter:
    s: Service = get_service(Filter, request)
    b: dict[str, Any] = {
        "cooling_unit_id": cooling_unit_id,
        "pump_id": pump_id,
        "filter_id": filter_id,
        "request": request,
        "response": response,
    }
    m = cast(Filter, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/ThermalEquipment/ImmersionUnits/{cooling_unit_id}/Pumps/{pump_id}/Filters/{filter_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch7(
    cooling_unit_id: str,
    pump_id: str,
    filter_id: str,
    request: Request,
    response: Response,
    body: FilterOnUpdate,
) -> Filter:
    s: Service = get_service(Filter, request)
    b: dict[str, Any] = {
        "cooling_unit_id": cooling_unit_id,
        "pump_id": pump_id,
        "filter_id": filter_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Filter, s.patch(**b))


@router.get(
    "/redfish/v1/ThermalEquipment/HeatExchangers/{cooling_unit_id}/Filters/{filter_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ThermalEquipment/HeatExchangers/{cooling_unit_id}/Filters/{filter_id}",
    response_model_exclude_none=True,
)
async def get8(
    cooling_unit_id: str, filter_id: str, request: Request, response: Response
) -> Filter:
    s: Service = get_service(Filter, request)
    b: dict[str, Any] = {
        "cooling_unit_id": cooling_unit_id,
        "filter_id": filter_id,
        "request": request,
        "response": response,
    }
    m = cast(Filter, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/ThermalEquipment/HeatExchangers/{cooling_unit_id}/Filters/{filter_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch8(
    cooling_unit_id: str,
    filter_id: str,
    request: Request,
    response: Response,
    body: FilterOnUpdate,
) -> Filter:
    s: Service = get_service(Filter, request)
    b: dict[str, Any] = {
        "cooling_unit_id": cooling_unit_id,
        "filter_id": filter_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Filter, s.patch(**b))


@router.get(
    "/redfish/v1/ThermalEquipment/HeatExchangers/{cooling_unit_id}/Reservoirs/{reservoir_id}/Filters/{filter_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ThermalEquipment/HeatExchangers/{cooling_unit_id}/Reservoirs/{reservoir_id}/Filters/{filter_id}",
    response_model_exclude_none=True,
)
async def get9(
    cooling_unit_id: str, reservoir_id: str, filter_id: str, request: Request, response: Response
) -> Filter:
    s: Service = get_service(Filter, request)
    b: dict[str, Any] = {
        "cooling_unit_id": cooling_unit_id,
        "reservoir_id": reservoir_id,
        "filter_id": filter_id,
        "request": request,
        "response": response,
    }
    m = cast(Filter, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/ThermalEquipment/HeatExchangers/{cooling_unit_id}/Reservoirs/{reservoir_id}/Filters/{filter_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch9(
    cooling_unit_id: str,
    reservoir_id: str,
    filter_id: str,
    request: Request,
    response: Response,
    body: FilterOnUpdate,
) -> Filter:
    s: Service = get_service(Filter, request)
    b: dict[str, Any] = {
        "cooling_unit_id": cooling_unit_id,
        "reservoir_id": reservoir_id,
        "filter_id": filter_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Filter, s.patch(**b))


@router.get(
    "/redfish/v1/ThermalEquipment/HeatExchangers/{cooling_unit_id}/Pumps/{pump_id}/Filters/{filter_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ThermalEquipment/HeatExchangers/{cooling_unit_id}/Pumps/{pump_id}/Filters/{filter_id}",
    response_model_exclude_none=True,
)
async def get10(
    cooling_unit_id: str, pump_id: str, filter_id: str, request: Request, response: Response
) -> Filter:
    s: Service = get_service(Filter, request)
    b: dict[str, Any] = {
        "cooling_unit_id": cooling_unit_id,
        "pump_id": pump_id,
        "filter_id": filter_id,
        "request": request,
        "response": response,
    }
    m = cast(Filter, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/ThermalEquipment/HeatExchangers/{cooling_unit_id}/Pumps/{pump_id}/Filters/{filter_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch10(
    cooling_unit_id: str,
    pump_id: str,
    filter_id: str,
    request: Request,
    response: Response,
    body: FilterOnUpdate,
) -> Filter:
    s: Service = get_service(Filter, request)
    b: dict[str, Any] = {
        "cooling_unit_id": cooling_unit_id,
        "pump_id": pump_id,
        "filter_id": filter_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Filter, s.patch(**b))
