from typing import Any, cast

from fastapi import APIRouter

from ..model.power_distribution_collection import PowerDistributionCollection
from ..service import Service, find_service
from . import authenticate

router = APIRouter()


@router.get("/redfish/v1/PowerEquipment/FloorPDUs", response_model_exclude_none=True)
@authenticate
async def get1() -> PowerDistributionCollection:
    s: Service = find_service(PowerDistributionCollection)
    b: dict[str, Any] = {}
    return cast(PowerDistributionCollection, s.get(**b))


@router.get("/redfish/v1/PowerEquipment/RackPDUs", response_model_exclude_none=True)
@authenticate
async def get2() -> PowerDistributionCollection:
    s: Service = find_service(PowerDistributionCollection)
    b: dict[str, Any] = {}
    return cast(PowerDistributionCollection, s.get(**b))


@router.get("/redfish/v1/PowerEquipment/Switchgear", response_model_exclude_none=True)
@authenticate
async def get3() -> PowerDistributionCollection:
    s: Service = find_service(PowerDistributionCollection)
    b: dict[str, Any] = {}
    return cast(PowerDistributionCollection, s.get(**b))


@router.get("/redfish/v1/PowerEquipment/TransferSwitches", response_model_exclude_none=True)
@authenticate
async def get4() -> PowerDistributionCollection:
    s: Service = find_service(PowerDistributionCollection)
    b: dict[str, Any] = {}
    return cast(PowerDistributionCollection, s.get(**b))


@router.get("/redfish/v1/PowerEquipment/PowerShelves", response_model_exclude_none=True)
@authenticate
async def get5() -> PowerDistributionCollection:
    s: Service = find_service(PowerDistributionCollection)
    b: dict[str, Any] = {}
    return cast(PowerDistributionCollection, s.get(**b))


@router.get("/redfish/v1/PowerEquipment/ElectricalBuses", response_model_exclude_none=True)
@authenticate
async def get6() -> PowerDistributionCollection:
    s: Service = find_service(PowerDistributionCollection)
    b: dict[str, Any] = {}
    return cast(PowerDistributionCollection, s.get(**b))
