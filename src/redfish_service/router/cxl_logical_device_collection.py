from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.cxl_logical_device_collection import CxlLogicalDeviceCollection
from ..service import Service, find_service

router = APIRouter()


@router.get(
    "/redfish/v1/Chassis/{chassis_id}/PCIeDevices/{pcie_device_id}/CXLLogicalDevices",
    response_model_exclude_none=True,
)
@authenticate
async def get1(
    chassis_id: str, pcie_device_id: str, request: Request, response: Response
) -> CxlLogicalDeviceCollection:
    s: Service = find_service(CxlLogicalDeviceCollection)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "pcie_device_id": pcie_device_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(CxlLogicalDeviceCollection, s.get(**b))
