from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..model.pcie_function_collection import PcieFunctionCollection
from ..service import Service
from ..util import get_service, set_link_header

router = APIRouter()


@router.get(
    "/redfish/v1/Chassis/{chassis_id}/PCIeDevices/{pcie_device_id}/PCIeFunctions",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Chassis/{chassis_id}/PCIeDevices/{pcie_device_id}/PCIeFunctions",
    response_model_exclude_none=True,
)
async def get1(
    chassis_id: str, pcie_device_id: str, request: Request, response: Response
) -> PcieFunctionCollection:
    s: Service = get_service(PcieFunctionCollection, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "pcie_device_id": pcie_device_id,
        "request": request,
        "response": response,
    }
    m = cast(PcieFunctionCollection, s.get(**b))
    set_link_header(m, response)
    return m


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/PCIeDevices/{pcie_device_id}/PCIeFunctions",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Systems/{computer_system_id}/PCIeDevices/{pcie_device_id}/PCIeFunctions",
    response_model_exclude_none=True,
)
async def get2(
    computer_system_id: str, pcie_device_id: str, request: Request, response: Response
) -> PcieFunctionCollection:
    s: Service = get_service(PcieFunctionCollection, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "pcie_device_id": pcie_device_id,
        "request": request,
        "response": response,
    }
    m = cast(PcieFunctionCollection, s.get(**b))
    set_link_header(m, response)
    return m


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/PCIeDevices/{pcie_device_id}/PCIeFunctions",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/PCIeDevices/{pcie_device_id}/PCIeFunctions",
    response_model_exclude_none=True,
)
async def get3(
    resource_block_id: str,
    computer_system_id: str,
    pcie_device_id: str,
    request: Request,
    response: Response,
) -> PcieFunctionCollection:
    s: Service = get_service(PcieFunctionCollection, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "pcie_device_id": pcie_device_id,
        "request": request,
        "response": response,
    }
    m = cast(PcieFunctionCollection, s.get(**b))
    set_link_header(m, response)
    return m


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/PCIeDevices/{pcie_device_id}/PCIeFunctions",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/PCIeDevices/{pcie_device_id}/PCIeFunctions",
    response_model_exclude_none=True,
)
async def get4(
    resource_block_id: str,
    computer_system_id: str,
    pcie_device_id: str,
    request: Request,
    response: Response,
) -> PcieFunctionCollection:
    s: Service = get_service(PcieFunctionCollection, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "pcie_device_id": pcie_device_id,
        "request": request,
        "response": response,
    }
    m = cast(PcieFunctionCollection, s.get(**b))
    set_link_header(m, response)
    return m
