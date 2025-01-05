from typing import Any, cast

from fastapi import APIRouter

from ..model.serial_interface import SerialInterface
from ..service import Service, find_service
from . import authenticate

router = APIRouter()


@router.get(
    "/redfish/v1/Managers/{manager_id}/SerialInterfaces/{serial_interface_id}",
    response_model_exclude_none=True,
)
@authenticate
async def get1(manager_id: str, serial_interface_id: str) -> SerialInterface:
    s: Service = find_service(SerialInterface)
    b: dict[str, Any] = {"manager_id": manager_id, "serial_interface_id": serial_interface_id}
    return cast(SerialInterface, s.get(**b))
