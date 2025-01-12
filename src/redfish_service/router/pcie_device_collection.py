from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..model.pcie_device_collection import PcieDeviceCollection
from ..service import Service
from ..util import get_service

router = APIRouter()


@router.get("/redfish/v1/Chassis/{chassis_id}/PCIeDevices", response_model_exclude_none=True)
@router.head("/redfish/v1/Chassis/{chassis_id}/PCIeDevices", response_model_exclude_none=True)
async def get1(chassis_id: str, request: Request, response: Response) -> PcieDeviceCollection:
    s: Service = get_service(PcieDeviceCollection, request)
    b: dict[str, Any] = {"chassis_id": chassis_id, "request": request, "response": response}
    return cast(PcieDeviceCollection, s.get(**b))


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/PCIeDevices", response_model_exclude_none=True
)
@router.head(
    "/redfish/v1/Systems/{computer_system_id}/PCIeDevices", response_model_exclude_none=True
)
async def get2(
    computer_system_id: str, request: Request, response: Response
) -> PcieDeviceCollection:
    s: Service = get_service(PcieDeviceCollection, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "request": request,
        "response": response,
    }
    return cast(PcieDeviceCollection, s.get(**b))


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/PCIeDevices",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/PCIeDevices",
    response_model_exclude_none=True,
)
async def get3(
    resource_block_id: str, computer_system_id: str, request: Request, response: Response
) -> PcieDeviceCollection:
    s: Service = get_service(PcieDeviceCollection, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "request": request,
        "response": response,
    }
    return cast(PcieDeviceCollection, s.get(**b))


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/PCIeDevices",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/PCIeDevices",
    response_model_exclude_none=True,
)
async def get4(
    resource_block_id: str, computer_system_id: str, request: Request, response: Response
) -> PcieDeviceCollection:
    s: Service = get_service(PcieDeviceCollection, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "request": request,
        "response": response,
    }
    return cast(PcieDeviceCollection, s.get(**b))
