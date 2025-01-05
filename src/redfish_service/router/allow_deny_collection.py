from typing import Any, cast

from fastapi import APIRouter

from ..authenticate import authenticate
from ..model.allow_deny_collection import AllowDenyCollection
from ..service import Service, find_service

router = APIRouter()


@router.get(
    "/redfish/v1/Chassis/{chassis_id}/NetworkAdapters/{network_adapter_id}/NetworkDeviceFunctions/{network_device_function_id}/AllowDeny",
    response_model_exclude_none=True,
)
@authenticate
async def get1(
    chassis_id: str, network_adapter_id: str, network_device_function_id: str
) -> AllowDenyCollection:
    s: Service = find_service(AllowDenyCollection)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "network_adapter_id": network_adapter_id,
        "network_device_function_id": network_device_function_id,
    }
    return cast(AllowDenyCollection, s.get(**b))


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/NetworkInterfaces/{network_interface_id}/NetworkDeviceFunctions/{network_device_function_id}/AllowDeny",
    response_model_exclude_none=True,
)
@authenticate
async def get2(
    computer_system_id: str, network_interface_id: str, network_device_function_id: str
) -> AllowDenyCollection:
    s: Service = find_service(AllowDenyCollection)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "network_interface_id": network_interface_id,
        "network_device_function_id": network_device_function_id,
    }
    return cast(AllowDenyCollection, s.get(**b))


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/NetworkInterfaces/{network_interface_id}/NetworkDeviceFunctions/{network_device_function_id}/AllowDeny",
    response_model_exclude_none=True,
)
@authenticate
async def get3(
    resource_block_id: str, network_interface_id: str, network_device_function_id: str
) -> AllowDenyCollection:
    s: Service = find_service(AllowDenyCollection)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "network_interface_id": network_interface_id,
        "network_device_function_id": network_device_function_id,
    }
    return cast(AllowDenyCollection, s.get(**b))


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/NetworkInterfaces/{network_interface_id}/NetworkDeviceFunctions/{network_device_function_id}/AllowDeny",
    response_model_exclude_none=True,
)
@authenticate
async def get4(
    resource_block_id: str,
    computer_system_id: str,
    network_interface_id: str,
    network_device_function_id: str,
) -> AllowDenyCollection:
    s: Service = find_service(AllowDenyCollection)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "network_interface_id": network_interface_id,
        "network_device_function_id": network_device_function_id,
    }
    return cast(AllowDenyCollection, s.get(**b))


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/NetworkInterfaces/{network_interface_id}/NetworkDeviceFunctions/{network_device_function_id}/AllowDeny",
    response_model_exclude_none=True,
)
@authenticate
async def get5(
    resource_block_id: str, network_interface_id: str, network_device_function_id: str
) -> AllowDenyCollection:
    s: Service = find_service(AllowDenyCollection)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "network_interface_id": network_interface_id,
        "network_device_function_id": network_device_function_id,
    }
    return cast(AllowDenyCollection, s.get(**b))


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/NetworkInterfaces/{network_interface_id}/NetworkDeviceFunctions/{network_device_function_id}/AllowDeny",
    response_model_exclude_none=True,
)
@authenticate
async def get6(
    resource_block_id: str,
    computer_system_id: str,
    network_interface_id: str,
    network_device_function_id: str,
) -> AllowDenyCollection:
    s: Service = find_service(AllowDenyCollection)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "network_interface_id": network_interface_id,
        "network_device_function_id": network_device_function_id,
    }
    return cast(AllowDenyCollection, s.get(**b))
