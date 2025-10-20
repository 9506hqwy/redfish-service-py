from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.redfish_error import RedfishError
from ..model.software_inventory import (
    ActivateRequest,
    SoftwareInventory,
    SoftwareInventoryOnUpdate,
)
from ..service import Service
from ..util import get_service, set_link_header

router = APIRouter()


@router.delete(
    "/redfish/v1/UpdateService/SoftwareInventory/{software_inventory_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete1(software_inventory_id: str, request: Request, response: Response) -> None:
    s: Service = get_service(SoftwareInventory, request)
    b: dict[str, Any] = {
        "software_inventory_id": software_inventory_id,
        "request": request,
        "response": response,
    }
    return s.delete(**b)


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
    s: Service = get_service(SoftwareInventory, request)
    b: dict[str, Any] = {
        "software_inventory_id": software_inventory_id,
        "request": request,
        "response": response,
    }
    m = cast(SoftwareInventory, s.get(**b))
    set_link_header(m, response)
    return m


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
    s: Service = get_service(SoftwareInventory, request)
    b: dict[str, Any] = {
        "software_inventory_id": software_inventory_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(SoftwareInventory, s.patch(**b))


@router.post(
    "/redfish/v1/UpdateService/SoftwareInventory/{software_inventory_id}/Actions/SoftwareInventory.Activate",
    response_model_exclude_none=True,
)
@authenticate
async def activate1(
    software_inventory_id: str, request: Request, response: Response, body: ActivateRequest
) -> RedfishError:
    s: Service = get_service(SoftwareInventory, request)
    b: dict[str, Any] = {
        "software_inventory_id": software_inventory_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Activate",
    }
    return s.action(**b)


@router.delete(
    "/redfish/v1/UpdateService/FirmwareInventory/{software_inventory_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete2(software_inventory_id: str, request: Request, response: Response) -> None:
    s: Service = get_service(SoftwareInventory, request)
    b: dict[str, Any] = {
        "software_inventory_id": software_inventory_id,
        "request": request,
        "response": response,
    }
    return s.delete(**b)


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
    s: Service = get_service(SoftwareInventory, request)
    b: dict[str, Any] = {
        "software_inventory_id": software_inventory_id,
        "request": request,
        "response": response,
    }
    m = cast(SoftwareInventory, s.get(**b))
    set_link_header(m, response)
    return m


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
    s: Service = get_service(SoftwareInventory, request)
    b: dict[str, Any] = {
        "software_inventory_id": software_inventory_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(SoftwareInventory, s.patch(**b))


@router.post(
    "/redfish/v1/UpdateService/FirmwareInventory/{software_inventory_id}/Actions/SoftwareInventory.Activate",
    response_model_exclude_none=True,
)
@authenticate
async def activate2(
    software_inventory_id: str, request: Request, response: Response, body: ActivateRequest
) -> RedfishError:
    s: Service = get_service(SoftwareInventory, request)
    b: dict[str, Any] = {
        "software_inventory_id": software_inventory_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Activate",
    }
    return s.action(**b)


@router.delete(
    "/redfish/v1/UpdateService/LocalImageStore/{software_inventory_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete3(software_inventory_id: str, request: Request, response: Response) -> None:
    s: Service = get_service(SoftwareInventory, request)
    b: dict[str, Any] = {
        "software_inventory_id": software_inventory_id,
        "request": request,
        "response": response,
    }
    return s.delete(**b)


@router.get(
    "/redfish/v1/UpdateService/LocalImageStore/{software_inventory_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/UpdateService/LocalImageStore/{software_inventory_id}",
    response_model_exclude_none=True,
)
async def get3(
    software_inventory_id: str, request: Request, response: Response
) -> SoftwareInventory:
    s: Service = get_service(SoftwareInventory, request)
    b: dict[str, Any] = {
        "software_inventory_id": software_inventory_id,
        "request": request,
        "response": response,
    }
    m = cast(SoftwareInventory, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/UpdateService/LocalImageStore/{software_inventory_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch3(
    software_inventory_id: str,
    request: Request,
    response: Response,
    body: SoftwareInventoryOnUpdate,
) -> SoftwareInventory:
    s: Service = get_service(SoftwareInventory, request)
    b: dict[str, Any] = {
        "software_inventory_id": software_inventory_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(SoftwareInventory, s.patch(**b))


@router.post(
    "/redfish/v1/UpdateService/LocalImageStore/{software_inventory_id}/Actions/SoftwareInventory.Activate",
    response_model_exclude_none=True,
)
@authenticate
async def activate3(
    software_inventory_id: str, request: Request, response: Response, body: ActivateRequest
) -> RedfishError:
    s: Service = get_service(SoftwareInventory, request)
    b: dict[str, Any] = {
        "software_inventory_id": software_inventory_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Activate",
    }
    return s.action(**b)
