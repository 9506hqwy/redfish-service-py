from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..model.software_inventory_collection import SoftwareInventoryCollection
from ..service import Service
from ..util import get_service

router = APIRouter()


@router.get("/redfish/v1/UpdateService/SoftwareInventory", response_model_exclude_none=True)
@router.head("/redfish/v1/UpdateService/SoftwareInventory", response_model_exclude_none=True)
async def get1(request: Request, response: Response) -> SoftwareInventoryCollection:
    s: Service = get_service(SoftwareInventoryCollection, request)
    b: dict[str, Any] = {"request": request, "response": response}
    return cast(SoftwareInventoryCollection, s.get(**b))


@router.get("/redfish/v1/UpdateService/FirmwareInventory", response_model_exclude_none=True)
@router.head("/redfish/v1/UpdateService/FirmwareInventory", response_model_exclude_none=True)
async def get2(request: Request, response: Response) -> SoftwareInventoryCollection:
    s: Service = get_service(SoftwareInventoryCollection, request)
    b: dict[str, Any] = {"request": request, "response": response}
    return cast(SoftwareInventoryCollection, s.get(**b))
