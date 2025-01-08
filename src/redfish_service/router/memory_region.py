from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..model.memory_region import MemoryRegion
from ..service import Service, find_service

router = APIRouter()


@router.get(
    "/redfish/v1/Chassis/{chassis_id}/PCIeDevices/{pcie_device_id}/CXLLogicalDevices/{cxl_logical_device_id}/MemoryRegions/{memory_region_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Chassis/{chassis_id}/PCIeDevices/{pcie_device_id}/CXLLogicalDevices/{cxl_logical_device_id}/MemoryRegions/{memory_region_id}",
    response_model_exclude_none=True,
)
async def get1(
    chassis_id: str,
    pcie_device_id: str,
    cxl_logical_device_id: str,
    memory_region_id: str,
    request: Request,
    response: Response,
) -> MemoryRegion:
    s: Service = find_service(MemoryRegion)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "pcie_device_id": pcie_device_id,
        "cxl_logical_device_id": cxl_logical_device_id,
        "memory_region_id": memory_region_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(MemoryRegion, s.get(**b))
