from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.cooling_unit import CoolingUnit, CoolingUnitOnUpdate
from ..service import Service, find_service

router = APIRouter()


@router.get(
    "/redfish/v1/ThermalEquipment/CDUs/{cooling_unit_id}", response_model_exclude_none=True
)
@router.head(
    "/redfish/v1/ThermalEquipment/CDUs/{cooling_unit_id}", response_model_exclude_none=True
)
async def get1(cooling_unit_id: str, request: Request, response: Response) -> CoolingUnit:
    s: Service = find_service(CoolingUnit)
    b: dict[str, Any] = {
        "cooling_unit_id": cooling_unit_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(CoolingUnit, s.get(**b))


@router.patch(
    "/redfish/v1/ThermalEquipment/CDUs/{cooling_unit_id}", response_model_exclude_none=True
)
@authenticate
async def patch1(
    cooling_unit_id: str, request: Request, response: Response, body: CoolingUnitOnUpdate
) -> CoolingUnit:
    s: Service = find_service(CoolingUnit)
    b: dict[str, Any] = {
        "cooling_unit_id": cooling_unit_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(CoolingUnit, s.patch(**b))


@router.get(
    "/redfish/v1/ThermalEquipment/ImmersionUnits/{cooling_unit_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ThermalEquipment/ImmersionUnits/{cooling_unit_id}",
    response_model_exclude_none=True,
)
async def get2(cooling_unit_id: str, request: Request, response: Response) -> CoolingUnit:
    s: Service = find_service(CoolingUnit)
    b: dict[str, Any] = {
        "cooling_unit_id": cooling_unit_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(CoolingUnit, s.get(**b))


@router.patch(
    "/redfish/v1/ThermalEquipment/ImmersionUnits/{cooling_unit_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch2(
    cooling_unit_id: str, request: Request, response: Response, body: CoolingUnitOnUpdate
) -> CoolingUnit:
    s: Service = find_service(CoolingUnit)
    b: dict[str, Any] = {
        "cooling_unit_id": cooling_unit_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(CoolingUnit, s.patch(**b))


@router.get(
    "/redfish/v1/ThermalEquipment/HeatExchangers/{cooling_unit_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ThermalEquipment/HeatExchangers/{cooling_unit_id}",
    response_model_exclude_none=True,
)
async def get3(cooling_unit_id: str, request: Request, response: Response) -> CoolingUnit:
    s: Service = find_service(CoolingUnit)
    b: dict[str, Any] = {
        "cooling_unit_id": cooling_unit_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(CoolingUnit, s.get(**b))


@router.patch(
    "/redfish/v1/ThermalEquipment/HeatExchangers/{cooling_unit_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch3(
    cooling_unit_id: str, request: Request, response: Response, body: CoolingUnitOnUpdate
) -> CoolingUnit:
    s: Service = find_service(CoolingUnit)
    b: dict[str, Any] = {
        "cooling_unit_id": cooling_unit_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(CoolingUnit, s.patch(**b))
