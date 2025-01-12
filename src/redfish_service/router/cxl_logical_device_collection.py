from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..model.cxl_logical_device_collection import CxlLogicalDeviceCollection
from ..service import Service
from ..util import get_service

router = APIRouter()


@router.get(
    "/redfish/v1/Chassis/{chassis_id}/PCIeDevices/{pcie_device_id}/CXLLogicalDevices",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Chassis/{chassis_id}/PCIeDevices/{pcie_device_id}/CXLLogicalDevices",
    response_model_exclude_none=True,
)
async def get1(
    chassis_id: str, pcie_device_id: str, request: Request, response: Response
) -> CxlLogicalDeviceCollection:
    s: Service = get_service(CxlLogicalDeviceCollection, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "pcie_device_id": pcie_device_id,
        "request": request,
        "response": response,
    }
    return cast(CxlLogicalDeviceCollection, s.get(**b))
