from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.serial_interface import SerialInterface
from ..service import Service, find_service

router = APIRouter()


@router.get(
    "/redfish/v1/Managers/{manager_id}/SerialInterfaces/{serial_interface_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Managers/{manager_id}/SerialInterfaces/{serial_interface_id}",
    response_model_exclude_none=True,
)
@authenticate
async def get1(
    manager_id: str, serial_interface_id: str, request: Request, response: Response
) -> SerialInterface:
    s: Service = find_service(SerialInterface)
    b: dict[str, Any] = {
        "manager_id": manager_id,
        "serial_interface_id": serial_interface_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(SerialInterface, s.get(**b))
