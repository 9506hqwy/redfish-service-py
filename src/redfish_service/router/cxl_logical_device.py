from typing import Any, cast

from fastapi import APIRouter

from ..authenticate import authenticate
from ..model.cxl_logical_device import CxlLogicalDevice
from ..service import Service, find_service

router = APIRouter()


@router.get(
    "/redfish/v1/Chassis/{chassis_id}/PCIeDevices/{pcie_device_id}/CXLLogicalDevices/{cxl_logical_device_id}",
    response_model_exclude_none=True,
)
@authenticate
async def get1(
    chassis_id: str, pcie_device_id: str, cxl_logical_device_id: str
) -> CxlLogicalDevice:
    s: Service = find_service(CxlLogicalDevice)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "pcie_device_id": pcie_device_id,
        "cxl_logical_device_id": cxl_logical_device_id,
    }
    return cast(CxlLogicalDevice, s.get(**b))
