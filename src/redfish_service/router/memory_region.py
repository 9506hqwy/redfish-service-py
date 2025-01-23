from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.memory_region import MemoryRegion, MemoryRegionOnUpdate
from ..service import Service
from ..util import get_service, set_link_header

router = APIRouter()


@router.delete(
    "/redfish/v1/Chassis/{chassis_id}/PCIeDevices/{pcie_device_id}/CXLLogicalDevices/{cxl_logical_device_id}/MemoryRegions/{memory_region_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete1(
    chassis_id: str,
    pcie_device_id: str,
    cxl_logical_device_id: str,
    memory_region_id: str,
    request: Request,
    response: Response,
) -> None:
    s: Service = get_service(MemoryRegion, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "pcie_device_id": pcie_device_id,
        "cxl_logical_device_id": cxl_logical_device_id,
        "memory_region_id": memory_region_id,
        "request": request,
        "response": response,
    }
    return s.delete(**b)


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
    s: Service = get_service(MemoryRegion, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "pcie_device_id": pcie_device_id,
        "cxl_logical_device_id": cxl_logical_device_id,
        "memory_region_id": memory_region_id,
        "request": request,
        "response": response,
    }
    m = cast(MemoryRegion, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/Chassis/{chassis_id}/PCIeDevices/{pcie_device_id}/CXLLogicalDevices/{cxl_logical_device_id}/MemoryRegions/{memory_region_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch1(
    chassis_id: str,
    pcie_device_id: str,
    cxl_logical_device_id: str,
    memory_region_id: str,
    request: Request,
    response: Response,
    body: MemoryRegionOnUpdate,
) -> MemoryRegion:
    s: Service = get_service(MemoryRegion, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "pcie_device_id": pcie_device_id,
        "cxl_logical_device_id": cxl_logical_device_id,
        "memory_region_id": memory_region_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(MemoryRegion, s.patch(**b))
