from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..model.power_distribution_collection import PowerDistributionCollection
from ..service import Service, find_service

router = APIRouter()


@router.get("/redfish/v1/PowerEquipment/FloorPDUs", response_model_exclude_none=True)
@router.head("/redfish/v1/PowerEquipment/FloorPDUs", response_model_exclude_none=True)
async def get1(request: Request, response: Response) -> PowerDistributionCollection:
    s: Service = find_service(PowerDistributionCollection)
    b: dict[str, Any] = {"request": request, "response": response}

    response.headers["OData-Version"] = "4.0"

    return cast(PowerDistributionCollection, s.get(**b))


@router.get("/redfish/v1/PowerEquipment/RackPDUs", response_model_exclude_none=True)
@router.head("/redfish/v1/PowerEquipment/RackPDUs", response_model_exclude_none=True)
async def get2(request: Request, response: Response) -> PowerDistributionCollection:
    s: Service = find_service(PowerDistributionCollection)
    b: dict[str, Any] = {"request": request, "response": response}

    response.headers["OData-Version"] = "4.0"

    return cast(PowerDistributionCollection, s.get(**b))


@router.get("/redfish/v1/PowerEquipment/Switchgear", response_model_exclude_none=True)
@router.head("/redfish/v1/PowerEquipment/Switchgear", response_model_exclude_none=True)
async def get3(request: Request, response: Response) -> PowerDistributionCollection:
    s: Service = find_service(PowerDistributionCollection)
    b: dict[str, Any] = {"request": request, "response": response}

    response.headers["OData-Version"] = "4.0"

    return cast(PowerDistributionCollection, s.get(**b))


@router.get("/redfish/v1/PowerEquipment/TransferSwitches", response_model_exclude_none=True)
@router.head("/redfish/v1/PowerEquipment/TransferSwitches", response_model_exclude_none=True)
async def get4(request: Request, response: Response) -> PowerDistributionCollection:
    s: Service = find_service(PowerDistributionCollection)
    b: dict[str, Any] = {"request": request, "response": response}

    response.headers["OData-Version"] = "4.0"

    return cast(PowerDistributionCollection, s.get(**b))


@router.get("/redfish/v1/PowerEquipment/PowerShelves", response_model_exclude_none=True)
@router.head("/redfish/v1/PowerEquipment/PowerShelves", response_model_exclude_none=True)
async def get5(request: Request, response: Response) -> PowerDistributionCollection:
    s: Service = find_service(PowerDistributionCollection)
    b: dict[str, Any] = {"request": request, "response": response}

    response.headers["OData-Version"] = "4.0"

    return cast(PowerDistributionCollection, s.get(**b))


@router.get("/redfish/v1/PowerEquipment/ElectricalBuses", response_model_exclude_none=True)
@router.head("/redfish/v1/PowerEquipment/ElectricalBuses", response_model_exclude_none=True)
async def get6(request: Request, response: Response) -> PowerDistributionCollection:
    s: Service = find_service(PowerDistributionCollection)
    b: dict[str, Any] = {"request": request, "response": response}

    response.headers["OData-Version"] = "4.0"

    return cast(PowerDistributionCollection, s.get(**b))
