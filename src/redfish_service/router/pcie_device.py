from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..model.pcie_device import PcieDevice
from ..service import Service, find_service

router = APIRouter()


@router.get(
    "/redfish/v1/Chassis/{chassis_id}/PCIeDevices/{pcie_device_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Chassis/{chassis_id}/PCIeDevices/{pcie_device_id}",
    response_model_exclude_none=True,
)
async def get1(
    chassis_id: str, pcie_device_id: str, request: Request, response: Response
) -> PcieDevice:
    s: Service = find_service(PcieDevice)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "pcie_device_id": pcie_device_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(PcieDevice, s.get(**b))


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/PCIeDevices/{pcie_device_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Systems/{computer_system_id}/PCIeDevices/{pcie_device_id}",
    response_model_exclude_none=True,
)
async def get2(
    computer_system_id: str, pcie_device_id: str, request: Request, response: Response
) -> PcieDevice:
    s: Service = find_service(PcieDevice)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "pcie_device_id": pcie_device_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(PcieDevice, s.get(**b))


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/PCIeDevices/{pcie_device_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/PCIeDevices/{pcie_device_id}",
    response_model_exclude_none=True,
)
async def get3(
    resource_block_id: str,
    computer_system_id: str,
    pcie_device_id: str,
    request: Request,
    response: Response,
) -> PcieDevice:
    s: Service = find_service(PcieDevice)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "pcie_device_id": pcie_device_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(PcieDevice, s.get(**b))


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/PCIeDevices/{pcie_device_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/PCIeDevices/{pcie_device_id}",
    response_model_exclude_none=True,
)
async def get4(
    resource_block_id: str,
    computer_system_id: str,
    pcie_device_id: str,
    request: Request,
    response: Response,
) -> PcieDevice:
    s: Service = find_service(PcieDevice)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "pcie_device_id": pcie_device_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(PcieDevice, s.get(**b))
