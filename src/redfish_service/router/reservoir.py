from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.reservoir import Reservoir, ReservoirOnUpdate
from ..service import Service
from ..util import get_service

router = APIRouter()


@router.get(
    "/redfish/v1/ThermalEquipment/CDUs/{cooling_unit_id}/Reservoirs/{reservoir_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ThermalEquipment/CDUs/{cooling_unit_id}/Reservoirs/{reservoir_id}",
    response_model_exclude_none=True,
)
async def get1(
    cooling_unit_id: str, reservoir_id: str, request: Request, response: Response
) -> Reservoir:
    s: Service = get_service(Reservoir, request)
    b: dict[str, Any] = {
        "cooling_unit_id": cooling_unit_id,
        "reservoir_id": reservoir_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(Reservoir, s.get(**b))


@router.patch(
    "/redfish/v1/ThermalEquipment/CDUs/{cooling_unit_id}/Reservoirs/{reservoir_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch1(
    cooling_unit_id: str,
    reservoir_id: str,
    request: Request,
    response: Response,
    body: ReservoirOnUpdate,
) -> Reservoir:
    s: Service = get_service(Reservoir, request)
    b: dict[str, Any] = {
        "cooling_unit_id": cooling_unit_id,
        "reservoir_id": reservoir_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(Reservoir, s.patch(**b))


@router.get(
    "/redfish/v1/ThermalEquipment/ImmersionUnits/{cooling_unit_id}/Reservoirs/{reservoir_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ThermalEquipment/ImmersionUnits/{cooling_unit_id}/Reservoirs/{reservoir_id}",
    response_model_exclude_none=True,
)
async def get2(
    cooling_unit_id: str, reservoir_id: str, request: Request, response: Response
) -> Reservoir:
    s: Service = get_service(Reservoir, request)
    b: dict[str, Any] = {
        "cooling_unit_id": cooling_unit_id,
        "reservoir_id": reservoir_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(Reservoir, s.get(**b))


@router.patch(
    "/redfish/v1/ThermalEquipment/ImmersionUnits/{cooling_unit_id}/Reservoirs/{reservoir_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch2(
    cooling_unit_id: str,
    reservoir_id: str,
    request: Request,
    response: Response,
    body: ReservoirOnUpdate,
) -> Reservoir:
    s: Service = get_service(Reservoir, request)
    b: dict[str, Any] = {
        "cooling_unit_id": cooling_unit_id,
        "reservoir_id": reservoir_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(Reservoir, s.patch(**b))


@router.get(
    "/redfish/v1/ThermalEquipment/HeatExchangers/{cooling_unit_id}/Reservoirs/{reservoir_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ThermalEquipment/HeatExchangers/{cooling_unit_id}/Reservoirs/{reservoir_id}",
    response_model_exclude_none=True,
)
async def get3(
    cooling_unit_id: str, reservoir_id: str, request: Request, response: Response
) -> Reservoir:
    s: Service = get_service(Reservoir, request)
    b: dict[str, Any] = {
        "cooling_unit_id": cooling_unit_id,
        "reservoir_id": reservoir_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(Reservoir, s.get(**b))


@router.patch(
    "/redfish/v1/ThermalEquipment/HeatExchangers/{cooling_unit_id}/Reservoirs/{reservoir_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch3(
    cooling_unit_id: str,
    reservoir_id: str,
    request: Request,
    response: Response,
    body: ReservoirOnUpdate,
) -> Reservoir:
    s: Service = get_service(Reservoir, request)
    b: dict[str, Any] = {
        "cooling_unit_id": cooling_unit_id,
        "reservoir_id": reservoir_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(Reservoir, s.patch(**b))
