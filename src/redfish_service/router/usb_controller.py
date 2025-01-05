from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.usb_controller import UsbController
from ..service import Service, find_service

router = APIRouter()


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/USBControllers/{controller_id}",
    response_model_exclude_none=True,
)
@authenticate
async def get1(
    computer_system_id: str, controller_id: str, request: Request, response: Response
) -> UsbController:
    s: Service = find_service(UsbController)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "controller_id": controller_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(UsbController, s.get(**b))
