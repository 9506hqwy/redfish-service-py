from typing import Any, cast

from fastapi import APIRouter

from ..authenticate import authenticate
from ..model.ethernet_interface import EthernetInterface
from ..service import Service, find_service

router = APIRouter()


@router.get(
    "/redfish/v1/Managers/{manager_id}/EthernetInterfaces/{ethernet_interface_id}",
    response_model_exclude_none=True,
)
@authenticate
async def get1(manager_id: str, ethernet_interface_id: str) -> EthernetInterface:
    s: Service = find_service(EthernetInterface)
    b: dict[str, Any] = {"manager_id": manager_id, "ethernet_interface_id": ethernet_interface_id}
    return cast(EthernetInterface, s.get(**b))


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/EthernetInterfaces/{ethernet_interface_id}",
    response_model_exclude_none=True,
)
@authenticate
async def get2(computer_system_id: str, ethernet_interface_id: str) -> EthernetInterface:
    s: Service = find_service(EthernetInterface)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "ethernet_interface_id": ethernet_interface_id,
    }
    return cast(EthernetInterface, s.get(**b))


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/EthernetInterfaces/{ethernet_interface_id}",
    response_model_exclude_none=True,
)
@authenticate
async def get3(resource_block_id: str, ethernet_interface_id: str) -> EthernetInterface:
    s: Service = find_service(EthernetInterface)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "ethernet_interface_id": ethernet_interface_id,
    }
    return cast(EthernetInterface, s.get(**b))


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/EthernetInterfaces/{ethernet_interface_id}",
    response_model_exclude_none=True,
)
@authenticate
async def get4(
    resource_block_id: str, computer_system_id: str, ethernet_interface_id: str
) -> EthernetInterface:
    s: Service = find_service(EthernetInterface)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "ethernet_interface_id": ethernet_interface_id,
    }
    return cast(EthernetInterface, s.get(**b))


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/EthernetInterfaces/{ethernet_interface_id}",
    response_model_exclude_none=True,
)
@authenticate
async def get5(resource_block_id: str, ethernet_interface_id: str) -> EthernetInterface:
    s: Service = find_service(EthernetInterface)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "ethernet_interface_id": ethernet_interface_id,
    }
    return cast(EthernetInterface, s.get(**b))


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/EthernetInterfaces/{ethernet_interface_id}",
    response_model_exclude_none=True,
)
@authenticate
async def get6(
    resource_block_id: str, computer_system_id: str, ethernet_interface_id: str
) -> EthernetInterface:
    s: Service = find_service(EthernetInterface)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "ethernet_interface_id": ethernet_interface_id,
    }
    return cast(EthernetInterface, s.get(**b))


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/OperatingSystem/Containers/EthernetInterfaces/{ethernet_interface_id}",
    response_model_exclude_none=True,
)
@authenticate
async def get7(computer_system_id: str, ethernet_interface_id: str) -> EthernetInterface:
    s: Service = find_service(EthernetInterface)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "ethernet_interface_id": ethernet_interface_id,
    }
    return cast(EthernetInterface, s.get(**b))


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/OperatingSystem/Containers/EthernetInterfaces/{ethernet_interface_id}",
    response_model_exclude_none=True,
)
@authenticate
async def get8(
    resource_block_id: str, computer_system_id: str, ethernet_interface_id: str
) -> EthernetInterface:
    s: Service = find_service(EthernetInterface)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "ethernet_interface_id": ethernet_interface_id,
    }
    return cast(EthernetInterface, s.get(**b))


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/OperatingSystem/Containers/EthernetInterfaces/{ethernet_interface_id}",
    response_model_exclude_none=True,
)
@authenticate
async def get9(
    resource_block_id: str, computer_system_id: str, ethernet_interface_id: str
) -> EthernetInterface:
    s: Service = find_service(EthernetInterface)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "ethernet_interface_id": ethernet_interface_id,
    }
    return cast(EthernetInterface, s.get(**b))


@router.get(
    "/redfish/v1/Chassis/{chassis_id}/NetworkAdapters/{network_adapter_id}/NetworkDeviceFunctions/{network_device_function_id}/EthernetInterfaces/{ethernet_interface_id}",
    response_model_exclude_none=True,
)
@authenticate
async def get10(
    chassis_id: str,
    network_adapter_id: str,
    network_device_function_id: str,
    ethernet_interface_id: str,
) -> EthernetInterface:
    s: Service = find_service(EthernetInterface)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "network_adapter_id": network_adapter_id,
        "network_device_function_id": network_device_function_id,
        "ethernet_interface_id": ethernet_interface_id,
    }
    return cast(EthernetInterface, s.get(**b))
