from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.software_inventory import SoftwareInventory, SoftwareInventoryOnUpdate
from ..service import Service, find_service

router = APIRouter()


@router.get(
    "/redfish/v1/UpdateService/SoftwareInventory/{software_inventory_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/UpdateService/SoftwareInventory/{software_inventory_id}",
    response_model_exclude_none=True,
)
async def get1(
    software_inventory_id: str, request: Request, response: Response
) -> SoftwareInventory:
    s: Service = find_service(SoftwareInventory)
    b: dict[str, Any] = {
        "software_inventory_id": software_inventory_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(SoftwareInventory, s.get(**b))


@router.patch(
    "/redfish/v1/UpdateService/SoftwareInventory/{software_inventory_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch1(
    software_inventory_id: str,
    request: Request,
    response: Response,
    body: SoftwareInventoryOnUpdate,
) -> SoftwareInventory:
    s: Service = find_service(SoftwareInventory)
    b: dict[str, Any] = {
        "software_inventory_id": software_inventory_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(SoftwareInventory, s.patch(**b))


@router.get(
    "/redfish/v1/UpdateService/FirmwareInventory/{software_inventory_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/UpdateService/FirmwareInventory/{software_inventory_id}",
    response_model_exclude_none=True,
)
async def get2(
    software_inventory_id: str, request: Request, response: Response
) -> SoftwareInventory:
    s: Service = find_service(SoftwareInventory)
    b: dict[str, Any] = {
        "software_inventory_id": software_inventory_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(SoftwareInventory, s.get(**b))


@router.patch(
    "/redfish/v1/UpdateService/FirmwareInventory/{software_inventory_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch2(
    software_inventory_id: str,
    request: Request,
    response: Response,
    body: SoftwareInventoryOnUpdate,
) -> SoftwareInventory:
    s: Service = find_service(SoftwareInventory)
    b: dict[str, Any] = {
        "software_inventory_id": software_inventory_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(SoftwareInventory, s.patch(**b))
