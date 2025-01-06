from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.software_inventory_collection import SoftwareInventoryCollection
from ..service import Service, find_service

router = APIRouter()


@router.get("/redfish/v1/UpdateService/SoftwareInventory", response_model_exclude_none=True)
@router.head("/redfish/v1/UpdateService/SoftwareInventory", response_model_exclude_none=True)
@authenticate
async def get1(request: Request, response: Response) -> SoftwareInventoryCollection:
    s: Service = find_service(SoftwareInventoryCollection)
    b: dict[str, Any] = {"request": request, "response": response}

    response.headers["OData-Version"] = "4.0"

    return cast(SoftwareInventoryCollection, s.get(**b))


@router.get("/redfish/v1/UpdateService/FirmwareInventory", response_model_exclude_none=True)
@router.head("/redfish/v1/UpdateService/FirmwareInventory", response_model_exclude_none=True)
@authenticate
async def get2(request: Request, response: Response) -> SoftwareInventoryCollection:
    s: Service = find_service(SoftwareInventoryCollection)
    b: dict[str, Any] = {"request": request, "response": response}

    response.headers["OData-Version"] = "4.0"

    return cast(SoftwareInventoryCollection, s.get(**b))
