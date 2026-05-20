from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.pcie_device import (
    CxlReferenceDcMemoryRequest,
    PcieDevice,
    PcieDeviceOnUpdate,
)
from ..model.redfish_error import RedfishError
from ..service import Service
from ..util import get_service, set_link_header

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
    s: Service = get_service(PcieDevice, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "pcie_device_id": pcie_device_id,
        "request": request,
        "response": response,
    }
    m = cast(PcieDevice, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/Chassis/{chassis_id}/PCIeDevices/{pcie_device_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch1(
    chassis_id: str,
    pcie_device_id: str,
    request: Request,
    response: Response,
    body: PcieDeviceOnUpdate,
) -> PcieDevice:
    s: Service = get_service(PcieDevice, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "pcie_device_id": pcie_device_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(PcieDevice, s.patch(**b))


@router.post(
    "/redfish/v1/Chassis/{chassis_id}/PCIeDevices/{pcie_device_id}/Actions/PCIeDevice.CXLReferenceDCMemory",
    response_model_exclude_none=True,
)
@authenticate
async def cxl_reference_dc_memory1(
    chassis_id: str,
    pcie_device_id: str,
    request: Request,
    response: Response,
    body: CxlReferenceDcMemoryRequest,
) -> RedfishError:
    s: Service = get_service(PcieDevice, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "pcie_device_id": pcie_device_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "CXLReferenceDCMemory",
    }
    return s.action(**b)


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
    s: Service = get_service(PcieDevice, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "pcie_device_id": pcie_device_id,
        "request": request,
        "response": response,
    }
    m = cast(PcieDevice, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/Systems/{computer_system_id}/PCIeDevices/{pcie_device_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch2(
    computer_system_id: str,
    pcie_device_id: str,
    request: Request,
    response: Response,
    body: PcieDeviceOnUpdate,
) -> PcieDevice:
    s: Service = get_service(PcieDevice, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "pcie_device_id": pcie_device_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(PcieDevice, s.patch(**b))


@router.post(
    "/redfish/v1/Systems/{computer_system_id}/PCIeDevices/{pcie_device_id}/Actions/PCIeDevice.CXLReferenceDCMemory",
    response_model_exclude_none=True,
)
@authenticate
async def cxl_reference_dc_memory2(
    computer_system_id: str,
    pcie_device_id: str,
    request: Request,
    response: Response,
    body: CxlReferenceDcMemoryRequest,
) -> RedfishError:
    s: Service = get_service(PcieDevice, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "pcie_device_id": pcie_device_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "CXLReferenceDCMemory",
    }
    return s.action(**b)


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
    s: Service = get_service(PcieDevice, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "pcie_device_id": pcie_device_id,
        "request": request,
        "response": response,
    }
    m = cast(PcieDevice, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/PCIeDevices/{pcie_device_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch3(
    resource_block_id: str,
    computer_system_id: str,
    pcie_device_id: str,
    request: Request,
    response: Response,
    body: PcieDeviceOnUpdate,
) -> PcieDevice:
    s: Service = get_service(PcieDevice, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "pcie_device_id": pcie_device_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(PcieDevice, s.patch(**b))


@router.post(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/PCIeDevices/{pcie_device_id}/Actions/PCIeDevice.CXLReferenceDCMemory",
    response_model_exclude_none=True,
)
@authenticate
async def cxl_reference_dc_memory3(
    resource_block_id: str,
    computer_system_id: str,
    pcie_device_id: str,
    request: Request,
    response: Response,
    body: CxlReferenceDcMemoryRequest,
) -> RedfishError:
    s: Service = get_service(PcieDevice, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "pcie_device_id": pcie_device_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "CXLReferenceDCMemory",
    }
    return s.action(**b)


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
    s: Service = get_service(PcieDevice, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "pcie_device_id": pcie_device_id,
        "request": request,
        "response": response,
    }
    m = cast(PcieDevice, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/PCIeDevices/{pcie_device_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch4(
    resource_block_id: str,
    computer_system_id: str,
    pcie_device_id: str,
    request: Request,
    response: Response,
    body: PcieDeviceOnUpdate,
) -> PcieDevice:
    s: Service = get_service(PcieDevice, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "pcie_device_id": pcie_device_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(PcieDevice, s.patch(**b))


@router.post(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/PCIeDevices/{pcie_device_id}/Actions/PCIeDevice.CXLReferenceDCMemory",
    response_model_exclude_none=True,
)
@authenticate
async def cxl_reference_dc_memory4(
    resource_block_id: str,
    computer_system_id: str,
    pcie_device_id: str,
    request: Request,
    response: Response,
    body: CxlReferenceDcMemoryRequest,
) -> RedfishError:
    s: Service = get_service(PcieDevice, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "pcie_device_id": pcie_device_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "CXLReferenceDCMemory",
    }
    return s.action(**b)
