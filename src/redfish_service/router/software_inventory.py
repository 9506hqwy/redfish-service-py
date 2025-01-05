from typing import Any, cast

from fastapi import APIRouter

from ..authenticate import authenticate
from ..model.software_inventory import SoftwareInventory
from ..service import Service, find_service

router = APIRouter()


@router.get(
    "/redfish/v1/UpdateService/SoftwareInventory/{software_inventory_id}",
    response_model_exclude_none=True,
)
@authenticate
async def get1(software_inventory_id: str) -> SoftwareInventory:
    s: Service = find_service(SoftwareInventory)
    b: dict[str, Any] = {"software_inventory_id": software_inventory_id}
    return cast(SoftwareInventory, s.get(**b))


@router.get(
    "/redfish/v1/UpdateService/FirmwareInventory/{software_inventory_id}",
    response_model_exclude_none=True,
)
@authenticate
async def get2(software_inventory_id: str) -> SoftwareInventory:
    s: Service = find_service(SoftwareInventory)
    b: dict[str, Any] = {"software_inventory_id": software_inventory_id}
    return cast(SoftwareInventory, s.get(**b))
