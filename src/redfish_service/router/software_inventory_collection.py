from typing import Any, cast

from fastapi import APIRouter

from ..model.software_inventory_collection import SoftwareInventoryCollection
from ..service import Service, find_service
from . import authenticate

router = APIRouter()


@router.get("/redfish/v1/UpdateService/SoftwareInventory", response_model_exclude_none=True)
@authenticate
async def get1() -> SoftwareInventoryCollection:
    s: Service = find_service(SoftwareInventoryCollection)
    b: dict[str, Any] = {}
    return cast(SoftwareInventoryCollection, s.get(**b))


@router.get("/redfish/v1/UpdateService/FirmwareInventory", response_model_exclude_none=True)
@authenticate
async def get2() -> SoftwareInventoryCollection:
    s: Service = find_service(SoftwareInventoryCollection)
    b: dict[str, Any] = {}
    return cast(SoftwareInventoryCollection, s.get(**b))
