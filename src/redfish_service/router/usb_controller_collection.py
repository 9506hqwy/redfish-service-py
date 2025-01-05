from typing import Any, cast

from fastapi import APIRouter

from ..model.usb_controller_collection import UsbControllerCollection
from ..service import Service, find_service
from . import authenticate

router = APIRouter()


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/USBControllers", response_model_exclude_none=True
)
@authenticate
async def get1(computer_system_id: str) -> UsbControllerCollection:
    s: Service = find_service(UsbControllerCollection)
    b: dict[str, Any] = {"computer_system_id": computer_system_id}
    return cast(UsbControllerCollection, s.get(**b))
