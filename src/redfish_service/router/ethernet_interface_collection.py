from typing import Any, cast

from fastapi import APIRouter

from ..authenticate import authenticate
from ..model.ethernet_interface_collection import EthernetInterfaceCollection
from ..service import Service, find_service

router = APIRouter()


@router.get(
    "/redfish/v1/Managers/{manager_id}/EthernetInterfaces", response_model_exclude_none=True
)
@authenticate
async def get1(manager_id: str) -> EthernetInterfaceCollection:
    s: Service = find_service(EthernetInterfaceCollection)
    b: dict[str, Any] = {"manager_id": manager_id}
    return cast(EthernetInterfaceCollection, s.get(**b))


@router.get(
    "/redfish/v1/Managers/{manager_id}/HostInterfaces/{host_interface_id}/HostEthernetInterfaces",
    response_model_exclude_none=True,
)
@authenticate
async def get2(manager_id: str, host_interface_id: str) -> EthernetInterfaceCollection:
    s: Service = find_service(EthernetInterfaceCollection)
    b: dict[str, Any] = {"manager_id": manager_id, "host_interface_id": host_interface_id}
    return cast(EthernetInterfaceCollection, s.get(**b))


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/EthernetInterfaces", response_model_exclude_none=True
)
@authenticate
async def get3(computer_system_id: str) -> EthernetInterfaceCollection:
    s: Service = find_service(EthernetInterfaceCollection)
    b: dict[str, Any] = {"computer_system_id": computer_system_id}
    return cast(EthernetInterfaceCollection, s.get(**b))


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/EthernetInterfaces",
    response_model_exclude_none=True,
)
@authenticate
async def get4(resource_block_id: str, computer_system_id: str) -> EthernetInterfaceCollection:
    s: Service = find_service(EthernetInterfaceCollection)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
    }
    return cast(EthernetInterfaceCollection, s.get(**b))


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/EthernetInterfaces",
    response_model_exclude_none=True,
)
@authenticate
async def get5(resource_block_id: str, computer_system_id: str) -> EthernetInterfaceCollection:
    s: Service = find_service(EthernetInterfaceCollection)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
    }
    return cast(EthernetInterfaceCollection, s.get(**b))


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/OperatingSystem/Containers/EthernetInterfaces",
    response_model_exclude_none=True,
)
@authenticate
async def get6(computer_system_id: str) -> EthernetInterfaceCollection:
    s: Service = find_service(EthernetInterfaceCollection)
    b: dict[str, Any] = {"computer_system_id": computer_system_id}
    return cast(EthernetInterfaceCollection, s.get(**b))


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/OperatingSystem/Containers/EthernetInterfaces",
    response_model_exclude_none=True,
)
@authenticate
async def get7(resource_block_id: str, computer_system_id: str) -> EthernetInterfaceCollection:
    s: Service = find_service(EthernetInterfaceCollection)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
    }
    return cast(EthernetInterfaceCollection, s.get(**b))


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/OperatingSystem/Containers/EthernetInterfaces",
    response_model_exclude_none=True,
)
@authenticate
async def get8(resource_block_id: str, computer_system_id: str) -> EthernetInterfaceCollection:
    s: Service = find_service(EthernetInterfaceCollection)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
    }
    return cast(EthernetInterfaceCollection, s.get(**b))


@router.get(
    "/redfish/v1/Chassis/{chassis_id}/NetworkAdapters/{network_adapter_id}/NetworkDeviceFunctions/{network_device_function_id}/EthernetInterfaces",
    response_model_exclude_none=True,
)
@authenticate
async def get9(
    chassis_id: str, network_adapter_id: str, network_device_function_id: str
) -> EthernetInterfaceCollection:
    s: Service = find_service(EthernetInterfaceCollection)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "network_adapter_id": network_adapter_id,
        "network_device_function_id": network_device_function_id,
    }
    return cast(EthernetInterfaceCollection, s.get(**b))
