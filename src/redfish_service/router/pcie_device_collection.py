from typing import Any, cast

from fastapi import APIRouter

from ..model.pcie_device_collection import PcieDeviceCollection
from ..service import Service, find_service
from . import authenticate

router = APIRouter()


@router.get("/redfish/v1/Chassis/{chassis_id}/PCIeDevices", response_model_exclude_none=True)
@authenticate
async def get1(chassis_id: str) -> PcieDeviceCollection:
    s: Service = find_service(PcieDeviceCollection)
    b: dict[str, Any] = {"chassis_id": chassis_id}
    return cast(PcieDeviceCollection, s.get(**b))


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/PCIeDevices", response_model_exclude_none=True
)
@authenticate
async def get2(computer_system_id: str) -> PcieDeviceCollection:
    s: Service = find_service(PcieDeviceCollection)
    b: dict[str, Any] = {"computer_system_id": computer_system_id}
    return cast(PcieDeviceCollection, s.get(**b))


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/PCIeDevices",
    response_model_exclude_none=True,
)
@authenticate
async def get3(resource_block_id: str, computer_system_id: str) -> PcieDeviceCollection:
    s: Service = find_service(PcieDeviceCollection)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
    }
    return cast(PcieDeviceCollection, s.get(**b))


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/PCIeDevices",
    response_model_exclude_none=True,
)
@authenticate
async def get4(resource_block_id: str, computer_system_id: str) -> PcieDeviceCollection:
    s: Service = find_service(PcieDeviceCollection)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
    }
    return cast(PcieDeviceCollection, s.get(**b))
