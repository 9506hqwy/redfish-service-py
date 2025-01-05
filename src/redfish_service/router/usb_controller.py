from typing import Any, cast

from fastapi import APIRouter

from ..model.usb_controller import UsbController
from ..service import Service, find_service
from . import authenticate

router = APIRouter()


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/USBControllers/{controller_id}",
    response_model_exclude_none=True,
)
@authenticate
async def get1(computer_system_id: str, controller_id: str) -> UsbController:
    s: Service = find_service(UsbController)
    b: dict[str, Any] = {"computer_system_id": computer_system_id, "controller_id": controller_id}
    return cast(UsbController, s.get(**b))
