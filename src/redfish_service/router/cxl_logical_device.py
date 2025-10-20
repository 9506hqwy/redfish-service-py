from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.cxl_logical_device import (
    CxlLogicalDevice,
    CxlLogicalDeviceOnUpdate,
    DisablePassphraseRequest,
    PassphraseSecureEraseRequest,
    SetPassphraseRequest,
    UnlockRequest,
)
from ..model.redfish_error import RedfishError
from ..service import Service
from ..util import get_service, set_link_header

router = APIRouter()


@router.get(
    "/redfish/v1/Chassis/{chassis_id}/PCIeDevices/{pcie_device_id}/CXLLogicalDevices/{cxl_logical_device_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Chassis/{chassis_id}/PCIeDevices/{pcie_device_id}/CXLLogicalDevices/{cxl_logical_device_id}",
    response_model_exclude_none=True,
)
async def get1(
    chassis_id: str,
    pcie_device_id: str,
    cxl_logical_device_id: str,
    request: Request,
    response: Response,
) -> CxlLogicalDevice:
    s: Service = get_service(CxlLogicalDevice, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "pcie_device_id": pcie_device_id,
        "cxl_logical_device_id": cxl_logical_device_id,
        "request": request,
        "response": response,
    }
    m = cast(CxlLogicalDevice, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/Chassis/{chassis_id}/PCIeDevices/{pcie_device_id}/CXLLogicalDevices/{cxl_logical_device_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch1(
    chassis_id: str,
    pcie_device_id: str,
    cxl_logical_device_id: str,
    request: Request,
    response: Response,
    body: CxlLogicalDeviceOnUpdate,
) -> CxlLogicalDevice:
    s: Service = get_service(CxlLogicalDevice, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "pcie_device_id": pcie_device_id,
        "cxl_logical_device_id": cxl_logical_device_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(CxlLogicalDevice, s.patch(**b))


@router.post(
    "/redfish/v1/Chassis/{chassis_id}/PCIeDevices/{pcie_device_id}/CXLLogicalDevices/{cxl_logical_device_id}/Actions/CXLLogicalDevice.DisablePassphrase",
    response_model_exclude_none=True,
)
@authenticate
async def disable_passphrase1(
    chassis_id: str,
    pcie_device_id: str,
    cxl_logical_device_id: str,
    request: Request,
    response: Response,
    body: DisablePassphraseRequest,
) -> RedfishError:
    s: Service = get_service(CxlLogicalDevice, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "pcie_device_id": pcie_device_id,
        "cxl_logical_device_id": cxl_logical_device_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "DisablePassphrase",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Chassis/{chassis_id}/PCIeDevices/{pcie_device_id}/CXLLogicalDevices/{cxl_logical_device_id}/Actions/CXLLogicalDevice.PassphraseSecureErase",
    response_model_exclude_none=True,
)
@authenticate
async def passphrase_secure_erase1(
    chassis_id: str,
    pcie_device_id: str,
    cxl_logical_device_id: str,
    request: Request,
    response: Response,
    body: PassphraseSecureEraseRequest,
) -> RedfishError:
    s: Service = get_service(CxlLogicalDevice, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "pcie_device_id": pcie_device_id,
        "cxl_logical_device_id": cxl_logical_device_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "PassphraseSecureErase",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Chassis/{chassis_id}/PCIeDevices/{pcie_device_id}/CXLLogicalDevices/{cxl_logical_device_id}/Actions/CXLLogicalDevice.SetPassphrase",
    response_model_exclude_none=True,
)
@authenticate
async def set_passphrase1(
    chassis_id: str,
    pcie_device_id: str,
    cxl_logical_device_id: str,
    request: Request,
    response: Response,
    body: SetPassphraseRequest,
) -> RedfishError:
    s: Service = get_service(CxlLogicalDevice, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "pcie_device_id": pcie_device_id,
        "cxl_logical_device_id": cxl_logical_device_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "SetPassphrase",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Chassis/{chassis_id}/PCIeDevices/{pcie_device_id}/CXLLogicalDevices/{cxl_logical_device_id}/Actions/CXLLogicalDevice.Unlock",
    response_model_exclude_none=True,
)
@authenticate
async def unlock1(
    chassis_id: str,
    pcie_device_id: str,
    cxl_logical_device_id: str,
    request: Request,
    response: Response,
    body: UnlockRequest,
) -> RedfishError:
    s: Service = get_service(CxlLogicalDevice, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "pcie_device_id": pcie_device_id,
        "cxl_logical_device_id": cxl_logical_device_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Unlock",
    }
    return s.action(**b)
