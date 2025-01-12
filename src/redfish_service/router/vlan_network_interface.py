from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.vlan_network_interface import VlanNetworkInterface, VlanNetworkInterfaceOnUpdate
from ..service import Service
from ..util import get_service

router = APIRouter()


@router.delete(
    "/redfish/v1/Chassis/{chassis_id}/NetworkAdapters/{network_adapter_id}/NetworkDeviceFunctions/{network_device_function_id}/Ethernet/VLANs/{vlan_network_interface_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete1(
    chassis_id: str,
    network_adapter_id: str,
    network_device_function_id: str,
    vlan_network_interface_id: str,
    request: Request,
    response: Response,
) -> None:
    s: Service = get_service(VlanNetworkInterface, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "network_adapter_id": network_adapter_id,
        "network_device_function_id": network_device_function_id,
        "vlan_network_interface_id": vlan_network_interface_id,
        "request": request,
        "response": response,
    }
    return s.delete(**b)


@router.get(
    "/redfish/v1/Chassis/{chassis_id}/NetworkAdapters/{network_adapter_id}/NetworkDeviceFunctions/{network_device_function_id}/Ethernet/VLANs/{vlan_network_interface_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Chassis/{chassis_id}/NetworkAdapters/{network_adapter_id}/NetworkDeviceFunctions/{network_device_function_id}/Ethernet/VLANs/{vlan_network_interface_id}",
    response_model_exclude_none=True,
)
async def get1(
    chassis_id: str,
    network_adapter_id: str,
    network_device_function_id: str,
    vlan_network_interface_id: str,
    request: Request,
    response: Response,
) -> VlanNetworkInterface:
    s: Service = get_service(VlanNetworkInterface, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "network_adapter_id": network_adapter_id,
        "network_device_function_id": network_device_function_id,
        "vlan_network_interface_id": vlan_network_interface_id,
        "request": request,
        "response": response,
    }
    return cast(VlanNetworkInterface, s.get(**b))


@router.patch(
    "/redfish/v1/Chassis/{chassis_id}/NetworkAdapters/{network_adapter_id}/NetworkDeviceFunctions/{network_device_function_id}/Ethernet/VLANs/{vlan_network_interface_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch1(
    chassis_id: str,
    network_adapter_id: str,
    network_device_function_id: str,
    vlan_network_interface_id: str,
    request: Request,
    response: Response,
    body: VlanNetworkInterfaceOnUpdate,
) -> VlanNetworkInterface:
    s: Service = get_service(VlanNetworkInterface, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "network_adapter_id": network_adapter_id,
        "network_device_function_id": network_device_function_id,
        "vlan_network_interface_id": vlan_network_interface_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(VlanNetworkInterface, s.patch(**b))


@router.delete(
    "/redfish/v1/Managers/{manager_id}/EthernetInterfaces/{ethernet_interface_id}/VLANs/{vlan_network_interface_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete2(
    manager_id: str,
    ethernet_interface_id: str,
    vlan_network_interface_id: str,
    request: Request,
    response: Response,
) -> None:
    s: Service = get_service(VlanNetworkInterface, request)
    b: dict[str, Any] = {
        "manager_id": manager_id,
        "ethernet_interface_id": ethernet_interface_id,
        "vlan_network_interface_id": vlan_network_interface_id,
        "request": request,
        "response": response,
    }
    return s.delete(**b)


@router.get(
    "/redfish/v1/Managers/{manager_id}/EthernetInterfaces/{ethernet_interface_id}/VLANs/{vlan_network_interface_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Managers/{manager_id}/EthernetInterfaces/{ethernet_interface_id}/VLANs/{vlan_network_interface_id}",
    response_model_exclude_none=True,
)
async def get2(
    manager_id: str,
    ethernet_interface_id: str,
    vlan_network_interface_id: str,
    request: Request,
    response: Response,
) -> VlanNetworkInterface:
    s: Service = get_service(VlanNetworkInterface, request)
    b: dict[str, Any] = {
        "manager_id": manager_id,
        "ethernet_interface_id": ethernet_interface_id,
        "vlan_network_interface_id": vlan_network_interface_id,
        "request": request,
        "response": response,
    }
    return cast(VlanNetworkInterface, s.get(**b))


@router.patch(
    "/redfish/v1/Managers/{manager_id}/EthernetInterfaces/{ethernet_interface_id}/VLANs/{vlan_network_interface_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch2(
    manager_id: str,
    ethernet_interface_id: str,
    vlan_network_interface_id: str,
    request: Request,
    response: Response,
    body: VlanNetworkInterfaceOnUpdate,
) -> VlanNetworkInterface:
    s: Service = get_service(VlanNetworkInterface, request)
    b: dict[str, Any] = {
        "manager_id": manager_id,
        "ethernet_interface_id": ethernet_interface_id,
        "vlan_network_interface_id": vlan_network_interface_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(VlanNetworkInterface, s.patch(**b))


@router.delete(
    "/redfish/v1/Systems/{computer_system_id}/EthernetInterfaces/{ethernet_interface_id}/VLANs/{vlan_network_interface_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete3(
    computer_system_id: str,
    ethernet_interface_id: str,
    vlan_network_interface_id: str,
    request: Request,
    response: Response,
) -> None:
    s: Service = get_service(VlanNetworkInterface, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "ethernet_interface_id": ethernet_interface_id,
        "vlan_network_interface_id": vlan_network_interface_id,
        "request": request,
        "response": response,
    }
    return s.delete(**b)


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/EthernetInterfaces/{ethernet_interface_id}/VLANs/{vlan_network_interface_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Systems/{computer_system_id}/EthernetInterfaces/{ethernet_interface_id}/VLANs/{vlan_network_interface_id}",
    response_model_exclude_none=True,
)
async def get3(
    computer_system_id: str,
    ethernet_interface_id: str,
    vlan_network_interface_id: str,
    request: Request,
    response: Response,
) -> VlanNetworkInterface:
    s: Service = get_service(VlanNetworkInterface, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "ethernet_interface_id": ethernet_interface_id,
        "vlan_network_interface_id": vlan_network_interface_id,
        "request": request,
        "response": response,
    }
    return cast(VlanNetworkInterface, s.get(**b))


@router.patch(
    "/redfish/v1/Systems/{computer_system_id}/EthernetInterfaces/{ethernet_interface_id}/VLANs/{vlan_network_interface_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch3(
    computer_system_id: str,
    ethernet_interface_id: str,
    vlan_network_interface_id: str,
    request: Request,
    response: Response,
    body: VlanNetworkInterfaceOnUpdate,
) -> VlanNetworkInterface:
    s: Service = get_service(VlanNetworkInterface, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "ethernet_interface_id": ethernet_interface_id,
        "vlan_network_interface_id": vlan_network_interface_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(VlanNetworkInterface, s.patch(**b))


@router.delete(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/EthernetInterfaces/{ethernet_interface_id}/VLANs/{vlan_network_interface_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete4(
    resource_block_id: str,
    ethernet_interface_id: str,
    vlan_network_interface_id: str,
    request: Request,
    response: Response,
) -> None:
    s: Service = get_service(VlanNetworkInterface, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "ethernet_interface_id": ethernet_interface_id,
        "vlan_network_interface_id": vlan_network_interface_id,
        "request": request,
        "response": response,
    }
    return s.delete(**b)


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/EthernetInterfaces/{ethernet_interface_id}/VLANs/{vlan_network_interface_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/EthernetInterfaces/{ethernet_interface_id}/VLANs/{vlan_network_interface_id}",
    response_model_exclude_none=True,
)
async def get4(
    resource_block_id: str,
    ethernet_interface_id: str,
    vlan_network_interface_id: str,
    request: Request,
    response: Response,
) -> VlanNetworkInterface:
    s: Service = get_service(VlanNetworkInterface, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "ethernet_interface_id": ethernet_interface_id,
        "vlan_network_interface_id": vlan_network_interface_id,
        "request": request,
        "response": response,
    }
    return cast(VlanNetworkInterface, s.get(**b))


@router.patch(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/EthernetInterfaces/{ethernet_interface_id}/VLANs/{vlan_network_interface_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch4(
    resource_block_id: str,
    ethernet_interface_id: str,
    vlan_network_interface_id: str,
    request: Request,
    response: Response,
    body: VlanNetworkInterfaceOnUpdate,
) -> VlanNetworkInterface:
    s: Service = get_service(VlanNetworkInterface, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "ethernet_interface_id": ethernet_interface_id,
        "vlan_network_interface_id": vlan_network_interface_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(VlanNetworkInterface, s.patch(**b))


@router.delete(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/EthernetInterfaces/{ethernet_interface_id}/VLANs/{vlan_network_interface_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete5(
    resource_block_id: str,
    computer_system_id: str,
    ethernet_interface_id: str,
    vlan_network_interface_id: str,
    request: Request,
    response: Response,
) -> None:
    s: Service = get_service(VlanNetworkInterface, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "ethernet_interface_id": ethernet_interface_id,
        "vlan_network_interface_id": vlan_network_interface_id,
        "request": request,
        "response": response,
    }
    return s.delete(**b)


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/EthernetInterfaces/{ethernet_interface_id}/VLANs/{vlan_network_interface_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/EthernetInterfaces/{ethernet_interface_id}/VLANs/{vlan_network_interface_id}",
    response_model_exclude_none=True,
)
async def get5(
    resource_block_id: str,
    computer_system_id: str,
    ethernet_interface_id: str,
    vlan_network_interface_id: str,
    request: Request,
    response: Response,
) -> VlanNetworkInterface:
    s: Service = get_service(VlanNetworkInterface, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "ethernet_interface_id": ethernet_interface_id,
        "vlan_network_interface_id": vlan_network_interface_id,
        "request": request,
        "response": response,
    }
    return cast(VlanNetworkInterface, s.get(**b))


@router.patch(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/EthernetInterfaces/{ethernet_interface_id}/VLANs/{vlan_network_interface_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch5(
    resource_block_id: str,
    computer_system_id: str,
    ethernet_interface_id: str,
    vlan_network_interface_id: str,
    request: Request,
    response: Response,
    body: VlanNetworkInterfaceOnUpdate,
) -> VlanNetworkInterface:
    s: Service = get_service(VlanNetworkInterface, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "ethernet_interface_id": ethernet_interface_id,
        "vlan_network_interface_id": vlan_network_interface_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(VlanNetworkInterface, s.patch(**b))


@router.delete(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/EthernetInterfaces/{ethernet_interface_id}/VLANs/{vlan_network_interface_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete6(
    resource_block_id: str,
    ethernet_interface_id: str,
    vlan_network_interface_id: str,
    request: Request,
    response: Response,
) -> None:
    s: Service = get_service(VlanNetworkInterface, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "ethernet_interface_id": ethernet_interface_id,
        "vlan_network_interface_id": vlan_network_interface_id,
        "request": request,
        "response": response,
    }
    return s.delete(**b)


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/EthernetInterfaces/{ethernet_interface_id}/VLANs/{vlan_network_interface_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/EthernetInterfaces/{ethernet_interface_id}/VLANs/{vlan_network_interface_id}",
    response_model_exclude_none=True,
)
async def get6(
    resource_block_id: str,
    ethernet_interface_id: str,
    vlan_network_interface_id: str,
    request: Request,
    response: Response,
) -> VlanNetworkInterface:
    s: Service = get_service(VlanNetworkInterface, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "ethernet_interface_id": ethernet_interface_id,
        "vlan_network_interface_id": vlan_network_interface_id,
        "request": request,
        "response": response,
    }
    return cast(VlanNetworkInterface, s.get(**b))


@router.patch(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/EthernetInterfaces/{ethernet_interface_id}/VLANs/{vlan_network_interface_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch6(
    resource_block_id: str,
    ethernet_interface_id: str,
    vlan_network_interface_id: str,
    request: Request,
    response: Response,
    body: VlanNetworkInterfaceOnUpdate,
) -> VlanNetworkInterface:
    s: Service = get_service(VlanNetworkInterface, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "ethernet_interface_id": ethernet_interface_id,
        "vlan_network_interface_id": vlan_network_interface_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(VlanNetworkInterface, s.patch(**b))


@router.delete(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/EthernetInterfaces/{ethernet_interface_id}/VLANs/{vlan_network_interface_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete7(
    resource_block_id: str,
    computer_system_id: str,
    ethernet_interface_id: str,
    vlan_network_interface_id: str,
    request: Request,
    response: Response,
) -> None:
    s: Service = get_service(VlanNetworkInterface, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "ethernet_interface_id": ethernet_interface_id,
        "vlan_network_interface_id": vlan_network_interface_id,
        "request": request,
        "response": response,
    }
    return s.delete(**b)


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/EthernetInterfaces/{ethernet_interface_id}/VLANs/{vlan_network_interface_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/EthernetInterfaces/{ethernet_interface_id}/VLANs/{vlan_network_interface_id}",
    response_model_exclude_none=True,
)
async def get7(
    resource_block_id: str,
    computer_system_id: str,
    ethernet_interface_id: str,
    vlan_network_interface_id: str,
    request: Request,
    response: Response,
) -> VlanNetworkInterface:
    s: Service = get_service(VlanNetworkInterface, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "ethernet_interface_id": ethernet_interface_id,
        "vlan_network_interface_id": vlan_network_interface_id,
        "request": request,
        "response": response,
    }
    return cast(VlanNetworkInterface, s.get(**b))


@router.patch(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/EthernetInterfaces/{ethernet_interface_id}/VLANs/{vlan_network_interface_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch7(
    resource_block_id: str,
    computer_system_id: str,
    ethernet_interface_id: str,
    vlan_network_interface_id: str,
    request: Request,
    response: Response,
    body: VlanNetworkInterfaceOnUpdate,
) -> VlanNetworkInterface:
    s: Service = get_service(VlanNetworkInterface, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "ethernet_interface_id": ethernet_interface_id,
        "vlan_network_interface_id": vlan_network_interface_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(VlanNetworkInterface, s.patch(**b))
