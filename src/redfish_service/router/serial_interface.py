from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.serial_interface import SerialInterface, SerialInterfaceOnUpdate
from ..service import Service
from ..util import get_service

router = APIRouter()


@router.get(
    "/redfish/v1/Managers/{manager_id}/SerialInterfaces/{serial_interface_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Managers/{manager_id}/SerialInterfaces/{serial_interface_id}",
    response_model_exclude_none=True,
)
async def get1(
    manager_id: str, serial_interface_id: str, request: Request, response: Response
) -> SerialInterface:
    s: Service = get_service(SerialInterface, request)
    b: dict[str, Any] = {
        "manager_id": manager_id,
        "serial_interface_id": serial_interface_id,
        "request": request,
        "response": response,
    }
    return cast(SerialInterface, s.get(**b))


@router.patch(
    "/redfish/v1/Managers/{manager_id}/SerialInterfaces/{serial_interface_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch1(
    manager_id: str,
    serial_interface_id: str,
    request: Request,
    response: Response,
    body: SerialInterfaceOnUpdate,
) -> SerialInterface:
    s: Service = get_service(SerialInterface, request)
    b: dict[str, Any] = {
        "manager_id": manager_id,
        "serial_interface_id": serial_interface_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(SerialInterface, s.patch(**b))
