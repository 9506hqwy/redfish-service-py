from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.pcie_function import PcieFunction, PcieFunctionOnUpdate
from ..service import Service
from ..util import get_service

router = APIRouter()


@router.get(
    "/redfish/v1/Chassis/{chassis_id}/PCIeDevices/{pcie_device_id}/PCIeFunctions/{pcie_function_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Chassis/{chassis_id}/PCIeDevices/{pcie_device_id}/PCIeFunctions/{pcie_function_id}",
    response_model_exclude_none=True,
)
async def get1(
    chassis_id: str,
    pcie_device_id: str,
    pcie_function_id: str,
    request: Request,
    response: Response,
) -> PcieFunction:
    s: Service = get_service(PcieFunction, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "pcie_device_id": pcie_device_id,
        "pcie_function_id": pcie_function_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(PcieFunction, s.get(**b))


@router.patch(
    "/redfish/v1/Chassis/{chassis_id}/PCIeDevices/{pcie_device_id}/PCIeFunctions/{pcie_function_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch1(
    chassis_id: str,
    pcie_device_id: str,
    pcie_function_id: str,
    request: Request,
    response: Response,
    body: PcieFunctionOnUpdate,
) -> PcieFunction:
    s: Service = get_service(PcieFunction, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "pcie_device_id": pcie_device_id,
        "pcie_function_id": pcie_function_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(PcieFunction, s.patch(**b))


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/PCIeDevices/{pcie_device_id}/PCIeFunctions/{pcie_function_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Systems/{computer_system_id}/PCIeDevices/{pcie_device_id}/PCIeFunctions/{pcie_function_id}",
    response_model_exclude_none=True,
)
async def get2(
    computer_system_id: str,
    pcie_device_id: str,
    pcie_function_id: str,
    request: Request,
    response: Response,
) -> PcieFunction:
    s: Service = get_service(PcieFunction, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "pcie_device_id": pcie_device_id,
        "pcie_function_id": pcie_function_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(PcieFunction, s.get(**b))


@router.patch(
    "/redfish/v1/Systems/{computer_system_id}/PCIeDevices/{pcie_device_id}/PCIeFunctions/{pcie_function_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch2(
    computer_system_id: str,
    pcie_device_id: str,
    pcie_function_id: str,
    request: Request,
    response: Response,
    body: PcieFunctionOnUpdate,
) -> PcieFunction:
    s: Service = get_service(PcieFunction, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "pcie_device_id": pcie_device_id,
        "pcie_function_id": pcie_function_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(PcieFunction, s.patch(**b))


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/PCIeDevices/{pcie_device_id}/PCIeFunctions/{pcie_function_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/PCIeDevices/{pcie_device_id}/PCIeFunctions/{pcie_function_id}",
    response_model_exclude_none=True,
)
async def get3(
    resource_block_id: str,
    computer_system_id: str,
    pcie_device_id: str,
    pcie_function_id: str,
    request: Request,
    response: Response,
) -> PcieFunction:
    s: Service = get_service(PcieFunction, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "pcie_device_id": pcie_device_id,
        "pcie_function_id": pcie_function_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(PcieFunction, s.get(**b))


@router.patch(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/PCIeDevices/{pcie_device_id}/PCIeFunctions/{pcie_function_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch3(
    resource_block_id: str,
    computer_system_id: str,
    pcie_device_id: str,
    pcie_function_id: str,
    request: Request,
    response: Response,
    body: PcieFunctionOnUpdate,
) -> PcieFunction:
    s: Service = get_service(PcieFunction, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "pcie_device_id": pcie_device_id,
        "pcie_function_id": pcie_function_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(PcieFunction, s.patch(**b))


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/PCIeDevices/{pcie_device_id}/PCIeFunctions/{pcie_function_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/PCIeDevices/{pcie_device_id}/PCIeFunctions/{pcie_function_id}",
    response_model_exclude_none=True,
)
async def get4(
    resource_block_id: str,
    computer_system_id: str,
    pcie_device_id: str,
    pcie_function_id: str,
    request: Request,
    response: Response,
) -> PcieFunction:
    s: Service = get_service(PcieFunction, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "pcie_device_id": pcie_device_id,
        "pcie_function_id": pcie_function_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(PcieFunction, s.get(**b))


@router.patch(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/PCIeDevices/{pcie_device_id}/PCIeFunctions/{pcie_function_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch4(
    resource_block_id: str,
    computer_system_id: str,
    pcie_device_id: str,
    pcie_function_id: str,
    request: Request,
    response: Response,
    body: PcieFunctionOnUpdate,
) -> PcieFunction:
    s: Service = get_service(PcieFunction, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "pcie_device_id": pcie_device_id,
        "pcie_function_id": pcie_function_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(PcieFunction, s.patch(**b))
