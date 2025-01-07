from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.ethernet_interface import EthernetInterface, EthernetInterfaceOnCreate
from ..model.ethernet_interface_collection import EthernetInterfaceCollection
from ..service import Service, ServiceCollection, find_service, find_service_collection

router = APIRouter()


@router.get(
    "/redfish/v1/Managers/{manager_id}/EthernetInterfaces", response_model_exclude_none=True
)
@router.head(
    "/redfish/v1/Managers/{manager_id}/EthernetInterfaces", response_model_exclude_none=True
)
@authenticate
async def get1(
    manager_id: str, request: Request, response: Response
) -> EthernetInterfaceCollection:
    s: Service = find_service(EthernetInterfaceCollection)
    b: dict[str, Any] = {"manager_id": manager_id, "request": request, "response": response}

    response.headers["OData-Version"] = "4.0"

    return cast(EthernetInterfaceCollection, s.get(**b))


@router.post(
    "/redfish/v1/Managers/{manager_id}/EthernetInterfaces", response_model_exclude_none=True
)
@router.post(
    "/redfish/v1/Managers/{manager_id}/EthernetInterfaces/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post1(
    manager_id: str, request: Request, response: Response, body: EthernetInterfaceOnCreate
) -> EthernetInterface:
    s: ServiceCollection = find_service_collection(EthernetInterfaceCollection)
    b: dict[str, Any] = {
        "manager_id": manager_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(EthernetInterface, s.post(**b))


@router.get(
    "/redfish/v1/Managers/{manager_id}/HostInterfaces/{host_interface_id}/HostEthernetInterfaces",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Managers/{manager_id}/HostInterfaces/{host_interface_id}/HostEthernetInterfaces",
    response_model_exclude_none=True,
)
@authenticate
async def get2(
    manager_id: str, host_interface_id: str, request: Request, response: Response
) -> EthernetInterfaceCollection:
    s: Service = find_service(EthernetInterfaceCollection)
    b: dict[str, Any] = {
        "manager_id": manager_id,
        "host_interface_id": host_interface_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(EthernetInterfaceCollection, s.get(**b))


@router.post(
    "/redfish/v1/Managers/{manager_id}/HostInterfaces/{host_interface_id}/HostEthernetInterfaces",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/Managers/{manager_id}/HostInterfaces/{host_interface_id}/HostEthernetInterfaces/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post2(
    manager_id: str,
    host_interface_id: str,
    request: Request,
    response: Response,
    body: EthernetInterfaceOnCreate,
) -> EthernetInterface:
    s: ServiceCollection = find_service_collection(EthernetInterfaceCollection)
    b: dict[str, Any] = {
        "manager_id": manager_id,
        "host_interface_id": host_interface_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(EthernetInterface, s.post(**b))


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/EthernetInterfaces", response_model_exclude_none=True
)
@router.head(
    "/redfish/v1/Systems/{computer_system_id}/EthernetInterfaces", response_model_exclude_none=True
)
@authenticate
async def get3(
    computer_system_id: str, request: Request, response: Response
) -> EthernetInterfaceCollection:
    s: Service = find_service(EthernetInterfaceCollection)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(EthernetInterfaceCollection, s.get(**b))


@router.post(
    "/redfish/v1/Systems/{computer_system_id}/EthernetInterfaces", response_model_exclude_none=True
)
@router.post(
    "/redfish/v1/Systems/{computer_system_id}/EthernetInterfaces/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post3(
    computer_system_id: str, request: Request, response: Response, body: EthernetInterfaceOnCreate
) -> EthernetInterface:
    s: ServiceCollection = find_service_collection(EthernetInterfaceCollection)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(EthernetInterface, s.post(**b))


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/EthernetInterfaces",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/EthernetInterfaces",
    response_model_exclude_none=True,
)
@authenticate
async def get4(
    resource_block_id: str, computer_system_id: str, request: Request, response: Response
) -> EthernetInterfaceCollection:
    s: Service = find_service(EthernetInterfaceCollection)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(EthernetInterfaceCollection, s.get(**b))


@router.post(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/EthernetInterfaces",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/EthernetInterfaces/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post4(
    resource_block_id: str,
    computer_system_id: str,
    request: Request,
    response: Response,
    body: EthernetInterfaceOnCreate,
) -> EthernetInterface:
    s: ServiceCollection = find_service_collection(EthernetInterfaceCollection)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(EthernetInterface, s.post(**b))


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/EthernetInterfaces",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/EthernetInterfaces",
    response_model_exclude_none=True,
)
@authenticate
async def get5(
    resource_block_id: str, computer_system_id: str, request: Request, response: Response
) -> EthernetInterfaceCollection:
    s: Service = find_service(EthernetInterfaceCollection)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(EthernetInterfaceCollection, s.get(**b))


@router.post(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/EthernetInterfaces",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/EthernetInterfaces/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post5(
    resource_block_id: str,
    computer_system_id: str,
    request: Request,
    response: Response,
    body: EthernetInterfaceOnCreate,
) -> EthernetInterface:
    s: ServiceCollection = find_service_collection(EthernetInterfaceCollection)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(EthernetInterface, s.post(**b))


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/OperatingSystem/Containers/EthernetInterfaces",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Systems/{computer_system_id}/OperatingSystem/Containers/EthernetInterfaces",
    response_model_exclude_none=True,
)
@authenticate
async def get6(
    computer_system_id: str, request: Request, response: Response
) -> EthernetInterfaceCollection:
    s: Service = find_service(EthernetInterfaceCollection)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(EthernetInterfaceCollection, s.get(**b))


@router.post(
    "/redfish/v1/Systems/{computer_system_id}/OperatingSystem/Containers/EthernetInterfaces",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/Systems/{computer_system_id}/OperatingSystem/Containers/EthernetInterfaces/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post6(
    computer_system_id: str, request: Request, response: Response, body: EthernetInterfaceOnCreate
) -> EthernetInterface:
    s: ServiceCollection = find_service_collection(EthernetInterfaceCollection)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(EthernetInterface, s.post(**b))


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/OperatingSystem/Containers/EthernetInterfaces",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/OperatingSystem/Containers/EthernetInterfaces",
    response_model_exclude_none=True,
)
@authenticate
async def get7(
    resource_block_id: str, computer_system_id: str, request: Request, response: Response
) -> EthernetInterfaceCollection:
    s: Service = find_service(EthernetInterfaceCollection)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(EthernetInterfaceCollection, s.get(**b))


@router.post(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/OperatingSystem/Containers/EthernetInterfaces",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/OperatingSystem/Containers/EthernetInterfaces/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post7(
    resource_block_id: str,
    computer_system_id: str,
    request: Request,
    response: Response,
    body: EthernetInterfaceOnCreate,
) -> EthernetInterface:
    s: ServiceCollection = find_service_collection(EthernetInterfaceCollection)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(EthernetInterface, s.post(**b))


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/OperatingSystem/Containers/EthernetInterfaces",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/OperatingSystem/Containers/EthernetInterfaces",
    response_model_exclude_none=True,
)
@authenticate
async def get8(
    resource_block_id: str, computer_system_id: str, request: Request, response: Response
) -> EthernetInterfaceCollection:
    s: Service = find_service(EthernetInterfaceCollection)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(EthernetInterfaceCollection, s.get(**b))


@router.post(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/OperatingSystem/Containers/EthernetInterfaces",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/OperatingSystem/Containers/EthernetInterfaces/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post8(
    resource_block_id: str,
    computer_system_id: str,
    request: Request,
    response: Response,
    body: EthernetInterfaceOnCreate,
) -> EthernetInterface:
    s: ServiceCollection = find_service_collection(EthernetInterfaceCollection)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(EthernetInterface, s.post(**b))


@router.get(
    "/redfish/v1/Chassis/{chassis_id}/NetworkAdapters/{network_adapter_id}/NetworkDeviceFunctions/{network_device_function_id}/EthernetInterfaces",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Chassis/{chassis_id}/NetworkAdapters/{network_adapter_id}/NetworkDeviceFunctions/{network_device_function_id}/EthernetInterfaces",
    response_model_exclude_none=True,
)
@authenticate
async def get9(
    chassis_id: str,
    network_adapter_id: str,
    network_device_function_id: str,
    request: Request,
    response: Response,
) -> EthernetInterfaceCollection:
    s: Service = find_service(EthernetInterfaceCollection)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "network_adapter_id": network_adapter_id,
        "network_device_function_id": network_device_function_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(EthernetInterfaceCollection, s.get(**b))


@router.post(
    "/redfish/v1/Chassis/{chassis_id}/NetworkAdapters/{network_adapter_id}/NetworkDeviceFunctions/{network_device_function_id}/EthernetInterfaces",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/Chassis/{chassis_id}/NetworkAdapters/{network_adapter_id}/NetworkDeviceFunctions/{network_device_function_id}/EthernetInterfaces/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post9(
    chassis_id: str,
    network_adapter_id: str,
    network_device_function_id: str,
    request: Request,
    response: Response,
    body: EthernetInterfaceOnCreate,
) -> EthernetInterface:
    s: ServiceCollection = find_service_collection(EthernetInterfaceCollection)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "network_adapter_id": network_adapter_id,
        "network_device_function_id": network_device_function_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(EthernetInterface, s.post(**b))
