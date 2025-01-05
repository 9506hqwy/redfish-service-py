from typing import Any, cast

from fastapi import APIRouter

from ..model.cxl_logical_device_collection import CxlLogicalDeviceCollection
from ..service import Service, find_service
from . import authenticate

router = APIRouter()


@router.get(
    "/redfish/v1/Chassis/{chassis_id}/PCIeDevices/{pcie_device_id}/CXLLogicalDevices",
    response_model_exclude_none=True,
)
@authenticate
async def get1(chassis_id: str, pcie_device_id: str) -> CxlLogicalDeviceCollection:
    s: Service = find_service(CxlLogicalDeviceCollection)
    b: dict[str, Any] = {"chassis_id": chassis_id, "pcie_device_id": pcie_device_id}
    return cast(CxlLogicalDeviceCollection, s.get(**b))
