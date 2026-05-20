from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.memory_extent import MemoryExtent, MemoryExtentOnCreate
from ..model.memory_extent_collection import MemoryExtentCollection
from ..service import Service, ServiceCollection
from ..util import get_service, get_service_collection, set_link_header

router = APIRouter()


@router.get(
    "/redfish/v1/Chassis/{chassis_id}/PCIeDevices/{pcie_device_id}/MemoryExtents",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Chassis/{chassis_id}/PCIeDevices/{pcie_device_id}/MemoryExtents",
    response_model_exclude_none=True,
)
async def get1(
    chassis_id: str, pcie_device_id: str, request: Request, response: Response
) -> MemoryExtentCollection:
    s: Service = get_service(MemoryExtentCollection, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "pcie_device_id": pcie_device_id,
        "request": request,
        "response": response,
    }
    m = cast(MemoryExtentCollection, s.get(**b))
    set_link_header(m, response)
    return m


@router.post(
    "/redfish/v1/Chassis/{chassis_id}/PCIeDevices/{pcie_device_id}/MemoryExtents",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/Chassis/{chassis_id}/PCIeDevices/{pcie_device_id}/MemoryExtents/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post1(
    chassis_id: str,
    pcie_device_id: str,
    request: Request,
    response: Response,
    body: MemoryExtentOnCreate,
) -> MemoryExtent:
    s: ServiceCollection = get_service_collection(MemoryExtentCollection, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "pcie_device_id": pcie_device_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(MemoryExtent, s.post(**b))
