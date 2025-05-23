from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..model.usb_controller_collection import UsbControllerCollection
from ..service import Service
from ..util import get_service, set_link_header

router = APIRouter()


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/USBControllers", response_model_exclude_none=True
)
@router.head(
    "/redfish/v1/Systems/{computer_system_id}/USBControllers", response_model_exclude_none=True
)
async def get1(
    computer_system_id: str, request: Request, response: Response
) -> UsbControllerCollection:
    s: Service = get_service(UsbControllerCollection, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "request": request,
        "response": response,
    }
    m = cast(UsbControllerCollection, s.get(**b))
    set_link_header(m, response)
    return m
