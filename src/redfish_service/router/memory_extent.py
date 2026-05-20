from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.memory_extent import MemoryExtent
from ..service import Service
from ..util import get_service, set_link_header

router = APIRouter()


@router.delete(
    "/redfish/v1/Chassis/{chassis_id}/PCIeDevices/{pcie_device_id}/MemoryExtents/{memory_extent_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete1(
    chassis_id: str,
    pcie_device_id: str,
    memory_extent_id: str,
    request: Request,
    response: Response,
) -> None:
    s: Service = get_service(MemoryExtent, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "pcie_device_id": pcie_device_id,
        "memory_extent_id": memory_extent_id,
        "request": request,
        "response": response,
    }
    return s.delete(**b)


@router.get(
    "/redfish/v1/Chassis/{chassis_id}/PCIeDevices/{pcie_device_id}/MemoryExtents/{memory_extent_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Chassis/{chassis_id}/PCIeDevices/{pcie_device_id}/MemoryExtents/{memory_extent_id}",
    response_model_exclude_none=True,
)
async def get1(
    chassis_id: str,
    pcie_device_id: str,
    memory_extent_id: str,
    request: Request,
    response: Response,
) -> MemoryExtent:
    s: Service = get_service(MemoryExtent, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "pcie_device_id": pcie_device_id,
        "memory_extent_id": memory_extent_id,
        "request": request,
        "response": response,
    }
    m = cast(MemoryExtent, s.get(**b))
    set_link_header(m, response)
    return m
