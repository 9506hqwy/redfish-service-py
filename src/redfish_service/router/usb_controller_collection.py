from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.usb_controller_collection import UsbControllerCollection
from ..service import Service, find_service

router = APIRouter()


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/USBControllers", response_model_exclude_none=True
)
@router.head(
    "/redfish/v1/Systems/{computer_system_id}/USBControllers", response_model_exclude_none=True
)
@authenticate
async def get1(
    computer_system_id: str, request: Request, response: Response
) -> UsbControllerCollection:
    s: Service = find_service(UsbControllerCollection)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(UsbControllerCollection, s.get(**b))
