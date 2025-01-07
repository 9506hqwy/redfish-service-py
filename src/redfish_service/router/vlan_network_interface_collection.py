from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.vlan_network_interface import VlanNetworkInterface, VlanNetworkInterfaceOnCreate
from ..model.vlan_network_interface_collection import VlanNetworkInterfaceCollection
from ..service import Service, ServiceCollection, find_service, find_service_collection

router = APIRouter()


@router.get(
    "/redfish/v1/Chassis/{chassis_id}/NetworkAdapters/{network_adapter_id}/NetworkDeviceFunctions/{network_device_function_id}/Ethernet/VLANs",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Chassis/{chassis_id}/NetworkAdapters/{network_adapter_id}/NetworkDeviceFunctions/{network_device_function_id}/Ethernet/VLANs",
    response_model_exclude_none=True,
)
@authenticate
async def get1(
    chassis_id: str,
    network_adapter_id: str,
    network_device_function_id: str,
    request: Request,
    response: Response,
) -> VlanNetworkInterfaceCollection:
    s: Service = find_service(VlanNetworkInterfaceCollection)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "network_adapter_id": network_adapter_id,
        "network_device_function_id": network_device_function_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(VlanNetworkInterfaceCollection, s.get(**b))


@router.post(
    "/redfish/v1/Chassis/{chassis_id}/NetworkAdapters/{network_adapter_id}/NetworkDeviceFunctions/{network_device_function_id}/Ethernet/VLANs",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/Chassis/{chassis_id}/NetworkAdapters/{network_adapter_id}/NetworkDeviceFunctions/{network_device_function_id}/Ethernet/VLANs/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post1(
    chassis_id: str,
    network_adapter_id: str,
    network_device_function_id: str,
    request: Request,
    response: Response,
    body: VlanNetworkInterfaceOnCreate,
) -> VlanNetworkInterface:
    s: ServiceCollection = find_service_collection(VlanNetworkInterfaceCollection)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "network_adapter_id": network_adapter_id,
        "network_device_function_id": network_device_function_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(VlanNetworkInterface, s.post(**b))


@router.get(
    "/redfish/v1/Managers/{manager_id}/EthernetInterfaces/{ethernet_interface_id}/VLANs",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Managers/{manager_id}/EthernetInterfaces/{ethernet_interface_id}/VLANs",
    response_model_exclude_none=True,
)
@authenticate
async def get2(
    manager_id: str, ethernet_interface_id: str, request: Request, response: Response
) -> VlanNetworkInterfaceCollection:
    s: Service = find_service(VlanNetworkInterfaceCollection)
    b: dict[str, Any] = {
        "manager_id": manager_id,
        "ethernet_interface_id": ethernet_interface_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(VlanNetworkInterfaceCollection, s.get(**b))


@router.post(
    "/redfish/v1/Managers/{manager_id}/EthernetInterfaces/{ethernet_interface_id}/VLANs",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/Managers/{manager_id}/EthernetInterfaces/{ethernet_interface_id}/VLANs/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post2(
    manager_id: str,
    ethernet_interface_id: str,
    request: Request,
    response: Response,
    body: VlanNetworkInterfaceOnCreate,
) -> VlanNetworkInterface:
    s: ServiceCollection = find_service_collection(VlanNetworkInterfaceCollection)
    b: dict[str, Any] = {
        "manager_id": manager_id,
        "ethernet_interface_id": ethernet_interface_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(VlanNetworkInterface, s.post(**b))


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/EthernetInterfaces/{ethernet_interface_id}/VLANs",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Systems/{computer_system_id}/EthernetInterfaces/{ethernet_interface_id}/VLANs",
    response_model_exclude_none=True,
)
@authenticate
async def get3(
    computer_system_id: str, ethernet_interface_id: str, request: Request, response: Response
) -> VlanNetworkInterfaceCollection:
    s: Service = find_service(VlanNetworkInterfaceCollection)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "ethernet_interface_id": ethernet_interface_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(VlanNetworkInterfaceCollection, s.get(**b))


@router.post(
    "/redfish/v1/Systems/{computer_system_id}/EthernetInterfaces/{ethernet_interface_id}/VLANs",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/Systems/{computer_system_id}/EthernetInterfaces/{ethernet_interface_id}/VLANs/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post3(
    computer_system_id: str,
    ethernet_interface_id: str,
    request: Request,
    response: Response,
    body: VlanNetworkInterfaceOnCreate,
) -> VlanNetworkInterface:
    s: ServiceCollection = find_service_collection(VlanNetworkInterfaceCollection)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "ethernet_interface_id": ethernet_interface_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(VlanNetworkInterface, s.post(**b))


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/EthernetInterfaces/{ethernet_interface_id}/VLANs",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/EthernetInterfaces/{ethernet_interface_id}/VLANs",
    response_model_exclude_none=True,
)
@authenticate
async def get4(
    resource_block_id: str, ethernet_interface_id: str, request: Request, response: Response
) -> VlanNetworkInterfaceCollection:
    s: Service = find_service(VlanNetworkInterfaceCollection)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "ethernet_interface_id": ethernet_interface_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(VlanNetworkInterfaceCollection, s.get(**b))


@router.post(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/EthernetInterfaces/{ethernet_interface_id}/VLANs",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/EthernetInterfaces/{ethernet_interface_id}/VLANs/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post4(
    resource_block_id: str,
    ethernet_interface_id: str,
    request: Request,
    response: Response,
    body: VlanNetworkInterfaceOnCreate,
) -> VlanNetworkInterface:
    s: ServiceCollection = find_service_collection(VlanNetworkInterfaceCollection)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "ethernet_interface_id": ethernet_interface_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(VlanNetworkInterface, s.post(**b))


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/EthernetInterfaces/{ethernet_interface_id}/VLANs",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/EthernetInterfaces/{ethernet_interface_id}/VLANs",
    response_model_exclude_none=True,
)
@authenticate
async def get5(
    resource_block_id: str,
    computer_system_id: str,
    ethernet_interface_id: str,
    request: Request,
    response: Response,
) -> VlanNetworkInterfaceCollection:
    s: Service = find_service(VlanNetworkInterfaceCollection)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "ethernet_interface_id": ethernet_interface_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(VlanNetworkInterfaceCollection, s.get(**b))


@router.post(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/EthernetInterfaces/{ethernet_interface_id}/VLANs",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/EthernetInterfaces/{ethernet_interface_id}/VLANs/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post5(
    resource_block_id: str,
    computer_system_id: str,
    ethernet_interface_id: str,
    request: Request,
    response: Response,
    body: VlanNetworkInterfaceOnCreate,
) -> VlanNetworkInterface:
    s: ServiceCollection = find_service_collection(VlanNetworkInterfaceCollection)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "ethernet_interface_id": ethernet_interface_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(VlanNetworkInterface, s.post(**b))


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/EthernetInterfaces/{ethernet_interface_id}/VLANs",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/EthernetInterfaces/{ethernet_interface_id}/VLANs",
    response_model_exclude_none=True,
)
@authenticate
async def get6(
    resource_block_id: str, ethernet_interface_id: str, request: Request, response: Response
) -> VlanNetworkInterfaceCollection:
    s: Service = find_service(VlanNetworkInterfaceCollection)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "ethernet_interface_id": ethernet_interface_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(VlanNetworkInterfaceCollection, s.get(**b))


@router.post(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/EthernetInterfaces/{ethernet_interface_id}/VLANs",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/EthernetInterfaces/{ethernet_interface_id}/VLANs/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post6(
    resource_block_id: str,
    ethernet_interface_id: str,
    request: Request,
    response: Response,
    body: VlanNetworkInterfaceOnCreate,
) -> VlanNetworkInterface:
    s: ServiceCollection = find_service_collection(VlanNetworkInterfaceCollection)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "ethernet_interface_id": ethernet_interface_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(VlanNetworkInterface, s.post(**b))


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/EthernetInterfaces/{ethernet_interface_id}/VLANs",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/EthernetInterfaces/{ethernet_interface_id}/VLANs",
    response_model_exclude_none=True,
)
@authenticate
async def get7(
    resource_block_id: str,
    computer_system_id: str,
    ethernet_interface_id: str,
    request: Request,
    response: Response,
) -> VlanNetworkInterfaceCollection:
    s: Service = find_service(VlanNetworkInterfaceCollection)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "ethernet_interface_id": ethernet_interface_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(VlanNetworkInterfaceCollection, s.get(**b))


@router.post(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/EthernetInterfaces/{ethernet_interface_id}/VLANs",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/EthernetInterfaces/{ethernet_interface_id}/VLANs/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post7(
    resource_block_id: str,
    computer_system_id: str,
    ethernet_interface_id: str,
    request: Request,
    response: Response,
    body: VlanNetworkInterfaceOnCreate,
) -> VlanNetworkInterface:
    s: ServiceCollection = find_service_collection(VlanNetworkInterfaceCollection)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "ethernet_interface_id": ethernet_interface_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(VlanNetworkInterface, s.post(**b))
