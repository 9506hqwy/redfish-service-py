from typing import Any, cast

from fastapi import APIRouter

from ..model.pcie_function_collection import PcieFunctionCollection
from ..service import Service, find_service
from . import authenticate

router = APIRouter()


@router.get(
    "/redfish/v1/Chassis/{chassis_id}/PCIeDevices/{pcie_device_id}/PCIeFunctions",
    response_model_exclude_none=True,
)
@authenticate
async def get1(chassis_id: str, pcie_device_id: str) -> PcieFunctionCollection:
    s: Service = find_service(PcieFunctionCollection)
    b: dict[str, Any] = {"chassis_id": chassis_id, "pcie_device_id": pcie_device_id}
    return cast(PcieFunctionCollection, s.get(**b))


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/PCIeDevices/{pcie_device_id}/PCIeFunctions",
    response_model_exclude_none=True,
)
@authenticate
async def get2(computer_system_id: str, pcie_device_id: str) -> PcieFunctionCollection:
    s: Service = find_service(PcieFunctionCollection)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "pcie_device_id": pcie_device_id,
    }
    return cast(PcieFunctionCollection, s.get(**b))


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/PCIeDevices/{pcie_device_id}/PCIeFunctions",
    response_model_exclude_none=True,
)
@authenticate
async def get3(
    resource_block_id: str, computer_system_id: str, pcie_device_id: str
) -> PcieFunctionCollection:
    s: Service = find_service(PcieFunctionCollection)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "pcie_device_id": pcie_device_id,
    }
    return cast(PcieFunctionCollection, s.get(**b))


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/PCIeDevices/{pcie_device_id}/PCIeFunctions",
    response_model_exclude_none=True,
)
@authenticate
async def get4(
    resource_block_id: str, computer_system_id: str, pcie_device_id: str
) -> PcieFunctionCollection:
    s: Service = find_service(PcieFunctionCollection)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "pcie_device_id": pcie_device_id,
    }
    return cast(PcieFunctionCollection, s.get(**b))
