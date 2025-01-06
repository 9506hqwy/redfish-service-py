from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.memory_region_collection import MemoryRegionCollection
from ..service import Service, find_service

router = APIRouter()


@router.get(
    "/redfish/v1/Chassis/{chassis_id}/PCIeDevices/{pcie_device_id}/CXLLogicalDevices/{cxl_logical_device_id}/MemoryRegions",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Chassis/{chassis_id}/PCIeDevices/{pcie_device_id}/CXLLogicalDevices/{cxl_logical_device_id}/MemoryRegions",
    response_model_exclude_none=True,
)
@authenticate
async def get1(
    chassis_id: str,
    pcie_device_id: str,
    cxl_logical_device_id: str,
    request: Request,
    response: Response,
) -> MemoryRegionCollection:
    s: Service = find_service(MemoryRegionCollection)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "pcie_device_id": pcie_device_id,
        "cxl_logical_device_id": cxl_logical_device_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(MemoryRegionCollection, s.get(**b))
