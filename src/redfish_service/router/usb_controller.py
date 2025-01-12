from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..model.usb_controller import UsbController
from ..service import Service
from ..util import get_service

router = APIRouter()


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/USBControllers/{controller_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Systems/{computer_system_id}/USBControllers/{controller_id}",
    response_model_exclude_none=True,
)
async def get1(
    computer_system_id: str, controller_id: str, request: Request, response: Response
) -> UsbController:
    s: Service = get_service(UsbController, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "controller_id": controller_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(UsbController, s.get(**b))
