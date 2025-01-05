from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.cooling_unit_collection import CoolingUnitCollection
from ..service import Service, find_service

router = APIRouter()


@router.get("/redfish/v1/ThermalEquipment/CDUs", response_model_exclude_none=True)
@authenticate
async def get1(request: Request, response: Response) -> CoolingUnitCollection:
    s: Service = find_service(CoolingUnitCollection)
    b: dict[str, Any] = {"request": request, "response": response}

    response.headers["OData-Version"] = "4.0"

    return cast(CoolingUnitCollection, s.get(**b))


@router.get("/redfish/v1/ThermalEquipment/ImmersionUnits", response_model_exclude_none=True)
@authenticate
async def get2(request: Request, response: Response) -> CoolingUnitCollection:
    s: Service = find_service(CoolingUnitCollection)
    b: dict[str, Any] = {"request": request, "response": response}

    response.headers["OData-Version"] = "4.0"

    return cast(CoolingUnitCollection, s.get(**b))


@router.get("/redfish/v1/ThermalEquipment/HeatExchangers", response_model_exclude_none=True)
@authenticate
async def get3(request: Request, response: Response) -> CoolingUnitCollection:
    s: Service = find_service(CoolingUnitCollection)
    b: dict[str, Any] = {"request": request, "response": response}

    response.headers["OData-Version"] = "4.0"

    return cast(CoolingUnitCollection, s.get(**b))
