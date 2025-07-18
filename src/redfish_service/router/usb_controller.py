from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..model.usb_controller import UsbController
from ..service import Service
from ..util import get_service, set_link_header

router = APIRouter()


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/USBControllers/{usb_controller_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Systems/{computer_system_id}/USBControllers/{usb_controller_id}",
    response_model_exclude_none=True,
)
async def get1(
    computer_system_id: str, usb_controller_id: str, request: Request, response: Response
) -> UsbController:
    s: Service = get_service(UsbController, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "usb_controller_id": usb_controller_id,
        "request": request,
        "response": response,
    }
    m = cast(UsbController, s.get(**b))
    set_link_header(m, response)
    return m
