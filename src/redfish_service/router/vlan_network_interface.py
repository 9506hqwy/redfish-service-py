from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.vlan_network_interface import VlanNetworkInterface
from ..service import Service, find_service

router = APIRouter()


@router.get(
    "/redfish/v1/Chassis/{chassis_id}/NetworkAdapters/{network_adapter_id}/NetworkDeviceFunctions/{network_device_function_id}/Ethernet/VLANs/{vlan_network_interface_id}",
    response_model_exclude_none=True,
)
@authenticate
async def get1(
    chassis_id: str,
    network_adapter_id: str,
    network_device_function_id: str,
    vlan_network_interface_id: str,
    request: Request,
    response: Response,
) -> VlanNetworkInterface:
    s: Service = find_service(VlanNetworkInterface)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "network_adapter_id": network_adapter_id,
        "network_device_function_id": network_device_function_id,
        "vlan_network_interface_id": vlan_network_interface_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(VlanNetworkInterface, s.get(**b))


@router.get(
    "/redfish/v1/Managers/{manager_id}/EthernetInterfaces/{ethernet_interface_id}/VLANs/{vlan_network_interface_id}",
    response_model_exclude_none=True,
)
@authenticate
async def get2(
    manager_id: str,
    ethernet_interface_id: str,
    vlan_network_interface_id: str,
    request: Request,
    response: Response,
) -> VlanNetworkInterface:
    s: Service = find_service(VlanNetworkInterface)
    b: dict[str, Any] = {
        "manager_id": manager_id,
        "ethernet_interface_id": ethernet_interface_id,
        "vlan_network_interface_id": vlan_network_interface_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(VlanNetworkInterface, s.get(**b))


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/EthernetInterfaces/{ethernet_interface_id}/VLANs/{vlan_network_interface_id}",
    response_model_exclude_none=True,
)
@authenticate
async def get3(
    computer_system_id: str,
    ethernet_interface_id: str,
    vlan_network_interface_id: str,
    request: Request,
    response: Response,
) -> VlanNetworkInterface:
    s: Service = find_service(VlanNetworkInterface)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "ethernet_interface_id": ethernet_interface_id,
        "vlan_network_interface_id": vlan_network_interface_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(VlanNetworkInterface, s.get(**b))


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/EthernetInterfaces/{ethernet_interface_id}/VLANs/{vlan_network_interface_id}",
    response_model_exclude_none=True,
)
@authenticate
async def get4(
    resource_block_id: str,
    ethernet_interface_id: str,
    vlan_network_interface_id: str,
    request: Request,
    response: Response,
) -> VlanNetworkInterface:
    s: Service = find_service(VlanNetworkInterface)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "ethernet_interface_id": ethernet_interface_id,
        "vlan_network_interface_id": vlan_network_interface_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(VlanNetworkInterface, s.get(**b))


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/EthernetInterfaces/{ethernet_interface_id}/VLANs/{vlan_network_interface_id}",
    response_model_exclude_none=True,
)
@authenticate
async def get5(
    resource_block_id: str,
    computer_system_id: str,
    ethernet_interface_id: str,
    vlan_network_interface_id: str,
    request: Request,
    response: Response,
) -> VlanNetworkInterface:
    s: Service = find_service(VlanNetworkInterface)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "ethernet_interface_id": ethernet_interface_id,
        "vlan_network_interface_id": vlan_network_interface_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(VlanNetworkInterface, s.get(**b))


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/EthernetInterfaces/{ethernet_interface_id}/VLANs/{vlan_network_interface_id}",
    response_model_exclude_none=True,
)
@authenticate
async def get6(
    resource_block_id: str,
    ethernet_interface_id: str,
    vlan_network_interface_id: str,
    request: Request,
    response: Response,
) -> VlanNetworkInterface:
    s: Service = find_service(VlanNetworkInterface)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "ethernet_interface_id": ethernet_interface_id,
        "vlan_network_interface_id": vlan_network_interface_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(VlanNetworkInterface, s.get(**b))


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/EthernetInterfaces/{ethernet_interface_id}/VLANs/{vlan_network_interface_id}",
    response_model_exclude_none=True,
)
@authenticate
async def get7(
    resource_block_id: str,
    computer_system_id: str,
    ethernet_interface_id: str,
    vlan_network_interface_id: str,
    request: Request,
    response: Response,
) -> VlanNetworkInterface:
    s: Service = find_service(VlanNetworkInterface)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "ethernet_interface_id": ethernet_interface_id,
        "vlan_network_interface_id": vlan_network_interface_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(VlanNetworkInterface, s.get(**b))
