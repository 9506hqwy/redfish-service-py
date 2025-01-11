from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.ethernet_interface import EthernetInterface, EthernetInterfaceOnUpdate
from ..service import Service, find_service

router = APIRouter()


@router.delete(
    "/redfish/v1/Managers/{manager_id}/EthernetInterfaces/{ethernet_interface_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete1(
    manager_id: str, ethernet_interface_id: str, request: Request, response: Response
) -> None:
    s: Service = find_service(EthernetInterface)
    b: dict[str, Any] = {
        "manager_id": manager_id,
        "ethernet_interface_id": ethernet_interface_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return s.delete(**b)


@router.get(
    "/redfish/v1/Managers/{manager_id}/EthernetInterfaces/{ethernet_interface_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Managers/{manager_id}/EthernetInterfaces/{ethernet_interface_id}",
    response_model_exclude_none=True,
)
async def get1(
    manager_id: str, ethernet_interface_id: str, request: Request, response: Response
) -> EthernetInterface:
    s: Service = find_service(EthernetInterface)
    b: dict[str, Any] = {
        "manager_id": manager_id,
        "ethernet_interface_id": ethernet_interface_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(EthernetInterface, s.get(**b))


@router.patch(
    "/redfish/v1/Managers/{manager_id}/EthernetInterfaces/{ethernet_interface_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch1(
    manager_id: str,
    ethernet_interface_id: str,
    request: Request,
    response: Response,
    body: EthernetInterfaceOnUpdate,
) -> EthernetInterface:
    s: Service = find_service(EthernetInterface)
    b: dict[str, Any] = {
        "manager_id": manager_id,
        "ethernet_interface_id": ethernet_interface_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(EthernetInterface, s.patch(**b))


@router.delete(
    "/redfish/v1/Systems/{computer_system_id}/EthernetInterfaces/{ethernet_interface_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete2(
    computer_system_id: str, ethernet_interface_id: str, request: Request, response: Response
) -> None:
    s: Service = find_service(EthernetInterface)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "ethernet_interface_id": ethernet_interface_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return s.delete(**b)


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/EthernetInterfaces/{ethernet_interface_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Systems/{computer_system_id}/EthernetInterfaces/{ethernet_interface_id}",
    response_model_exclude_none=True,
)
async def get2(
    computer_system_id: str, ethernet_interface_id: str, request: Request, response: Response
) -> EthernetInterface:
    s: Service = find_service(EthernetInterface)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "ethernet_interface_id": ethernet_interface_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(EthernetInterface, s.get(**b))


@router.patch(
    "/redfish/v1/Systems/{computer_system_id}/EthernetInterfaces/{ethernet_interface_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch2(
    computer_system_id: str,
    ethernet_interface_id: str,
    request: Request,
    response: Response,
    body: EthernetInterfaceOnUpdate,
) -> EthernetInterface:
    s: Service = find_service(EthernetInterface)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "ethernet_interface_id": ethernet_interface_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(EthernetInterface, s.patch(**b))


@router.delete(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/EthernetInterfaces/{ethernet_interface_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete3(
    resource_block_id: str, ethernet_interface_id: str, request: Request, response: Response
) -> None:
    s: Service = find_service(EthernetInterface)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "ethernet_interface_id": ethernet_interface_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return s.delete(**b)


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/EthernetInterfaces/{ethernet_interface_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/EthernetInterfaces/{ethernet_interface_id}",
    response_model_exclude_none=True,
)
async def get3(
    resource_block_id: str, ethernet_interface_id: str, request: Request, response: Response
) -> EthernetInterface:
    s: Service = find_service(EthernetInterface)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "ethernet_interface_id": ethernet_interface_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(EthernetInterface, s.get(**b))


@router.patch(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/EthernetInterfaces/{ethernet_interface_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch3(
    resource_block_id: str,
    ethernet_interface_id: str,
    request: Request,
    response: Response,
    body: EthernetInterfaceOnUpdate,
) -> EthernetInterface:
    s: Service = find_service(EthernetInterface)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "ethernet_interface_id": ethernet_interface_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(EthernetInterface, s.patch(**b))


@router.delete(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/EthernetInterfaces/{ethernet_interface_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete4(
    resource_block_id: str,
    computer_system_id: str,
    ethernet_interface_id: str,
    request: Request,
    response: Response,
) -> None:
    s: Service = find_service(EthernetInterface)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "ethernet_interface_id": ethernet_interface_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return s.delete(**b)


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/EthernetInterfaces/{ethernet_interface_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/EthernetInterfaces/{ethernet_interface_id}",
    response_model_exclude_none=True,
)
async def get4(
    resource_block_id: str,
    computer_system_id: str,
    ethernet_interface_id: str,
    request: Request,
    response: Response,
) -> EthernetInterface:
    s: Service = find_service(EthernetInterface)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "ethernet_interface_id": ethernet_interface_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(EthernetInterface, s.get(**b))


@router.patch(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/EthernetInterfaces/{ethernet_interface_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch4(
    resource_block_id: str,
    computer_system_id: str,
    ethernet_interface_id: str,
    request: Request,
    response: Response,
    body: EthernetInterfaceOnUpdate,
) -> EthernetInterface:
    s: Service = find_service(EthernetInterface)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "ethernet_interface_id": ethernet_interface_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(EthernetInterface, s.patch(**b))


@router.delete(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/EthernetInterfaces/{ethernet_interface_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete5(
    resource_block_id: str, ethernet_interface_id: str, request: Request, response: Response
) -> None:
    s: Service = find_service(EthernetInterface)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "ethernet_interface_id": ethernet_interface_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return s.delete(**b)


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/EthernetInterfaces/{ethernet_interface_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/EthernetInterfaces/{ethernet_interface_id}",
    response_model_exclude_none=True,
)
async def get5(
    resource_block_id: str, ethernet_interface_id: str, request: Request, response: Response
) -> EthernetInterface:
    s: Service = find_service(EthernetInterface)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "ethernet_interface_id": ethernet_interface_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(EthernetInterface, s.get(**b))


@router.patch(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/EthernetInterfaces/{ethernet_interface_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch5(
    resource_block_id: str,
    ethernet_interface_id: str,
    request: Request,
    response: Response,
    body: EthernetInterfaceOnUpdate,
) -> EthernetInterface:
    s: Service = find_service(EthernetInterface)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "ethernet_interface_id": ethernet_interface_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(EthernetInterface, s.patch(**b))


@router.delete(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/EthernetInterfaces/{ethernet_interface_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete6(
    resource_block_id: str,
    computer_system_id: str,
    ethernet_interface_id: str,
    request: Request,
    response: Response,
) -> None:
    s: Service = find_service(EthernetInterface)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "ethernet_interface_id": ethernet_interface_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return s.delete(**b)


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/EthernetInterfaces/{ethernet_interface_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/EthernetInterfaces/{ethernet_interface_id}",
    response_model_exclude_none=True,
)
async def get6(
    resource_block_id: str,
    computer_system_id: str,
    ethernet_interface_id: str,
    request: Request,
    response: Response,
) -> EthernetInterface:
    s: Service = find_service(EthernetInterface)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "ethernet_interface_id": ethernet_interface_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(EthernetInterface, s.get(**b))


@router.patch(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/EthernetInterfaces/{ethernet_interface_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch6(
    resource_block_id: str,
    computer_system_id: str,
    ethernet_interface_id: str,
    request: Request,
    response: Response,
    body: EthernetInterfaceOnUpdate,
) -> EthernetInterface:
    s: Service = find_service(EthernetInterface)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "ethernet_interface_id": ethernet_interface_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(EthernetInterface, s.patch(**b))


@router.delete(
    "/redfish/v1/Systems/{computer_system_id}/OperatingSystem/Containers/EthernetInterfaces/{ethernet_interface_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete7(
    computer_system_id: str, ethernet_interface_id: str, request: Request, response: Response
) -> None:
    s: Service = find_service(EthernetInterface)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "ethernet_interface_id": ethernet_interface_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return s.delete(**b)


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/OperatingSystem/Containers/EthernetInterfaces/{ethernet_interface_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Systems/{computer_system_id}/OperatingSystem/Containers/EthernetInterfaces/{ethernet_interface_id}",
    response_model_exclude_none=True,
)
async def get7(
    computer_system_id: str, ethernet_interface_id: str, request: Request, response: Response
) -> EthernetInterface:
    s: Service = find_service(EthernetInterface)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "ethernet_interface_id": ethernet_interface_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(EthernetInterface, s.get(**b))


@router.patch(
    "/redfish/v1/Systems/{computer_system_id}/OperatingSystem/Containers/EthernetInterfaces/{ethernet_interface_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch7(
    computer_system_id: str,
    ethernet_interface_id: str,
    request: Request,
    response: Response,
    body: EthernetInterfaceOnUpdate,
) -> EthernetInterface:
    s: Service = find_service(EthernetInterface)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "ethernet_interface_id": ethernet_interface_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(EthernetInterface, s.patch(**b))


@router.delete(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/OperatingSystem/Containers/EthernetInterfaces/{ethernet_interface_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete8(
    resource_block_id: str,
    computer_system_id: str,
    ethernet_interface_id: str,
    request: Request,
    response: Response,
) -> None:
    s: Service = find_service(EthernetInterface)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "ethernet_interface_id": ethernet_interface_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return s.delete(**b)


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/OperatingSystem/Containers/EthernetInterfaces/{ethernet_interface_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/OperatingSystem/Containers/EthernetInterfaces/{ethernet_interface_id}",
    response_model_exclude_none=True,
)
async def get8(
    resource_block_id: str,
    computer_system_id: str,
    ethernet_interface_id: str,
    request: Request,
    response: Response,
) -> EthernetInterface:
    s: Service = find_service(EthernetInterface)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "ethernet_interface_id": ethernet_interface_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(EthernetInterface, s.get(**b))


@router.patch(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/OperatingSystem/Containers/EthernetInterfaces/{ethernet_interface_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch8(
    resource_block_id: str,
    computer_system_id: str,
    ethernet_interface_id: str,
    request: Request,
    response: Response,
    body: EthernetInterfaceOnUpdate,
) -> EthernetInterface:
    s: Service = find_service(EthernetInterface)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "ethernet_interface_id": ethernet_interface_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(EthernetInterface, s.patch(**b))


@router.delete(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/OperatingSystem/Containers/EthernetInterfaces/{ethernet_interface_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete9(
    resource_block_id: str,
    computer_system_id: str,
    ethernet_interface_id: str,
    request: Request,
    response: Response,
) -> None:
    s: Service = find_service(EthernetInterface)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "ethernet_interface_id": ethernet_interface_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return s.delete(**b)


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/OperatingSystem/Containers/EthernetInterfaces/{ethernet_interface_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/OperatingSystem/Containers/EthernetInterfaces/{ethernet_interface_id}",
    response_model_exclude_none=True,
)
async def get9(
    resource_block_id: str,
    computer_system_id: str,
    ethernet_interface_id: str,
    request: Request,
    response: Response,
) -> EthernetInterface:
    s: Service = find_service(EthernetInterface)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "ethernet_interface_id": ethernet_interface_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(EthernetInterface, s.get(**b))


@router.patch(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/OperatingSystem/Containers/EthernetInterfaces/{ethernet_interface_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch9(
    resource_block_id: str,
    computer_system_id: str,
    ethernet_interface_id: str,
    request: Request,
    response: Response,
    body: EthernetInterfaceOnUpdate,
) -> EthernetInterface:
    s: Service = find_service(EthernetInterface)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "ethernet_interface_id": ethernet_interface_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(EthernetInterface, s.patch(**b))


@router.delete(
    "/redfish/v1/Chassis/{chassis_id}/NetworkAdapters/{network_adapter_id}/NetworkDeviceFunctions/{network_device_function_id}/EthernetInterfaces/{ethernet_interface_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete10(
    chassis_id: str,
    network_adapter_id: str,
    network_device_function_id: str,
    ethernet_interface_id: str,
    request: Request,
    response: Response,
) -> None:
    s: Service = find_service(EthernetInterface)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "network_adapter_id": network_adapter_id,
        "network_device_function_id": network_device_function_id,
        "ethernet_interface_id": ethernet_interface_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return s.delete(**b)


@router.get(
    "/redfish/v1/Chassis/{chassis_id}/NetworkAdapters/{network_adapter_id}/NetworkDeviceFunctions/{network_device_function_id}/EthernetInterfaces/{ethernet_interface_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Chassis/{chassis_id}/NetworkAdapters/{network_adapter_id}/NetworkDeviceFunctions/{network_device_function_id}/EthernetInterfaces/{ethernet_interface_id}",
    response_model_exclude_none=True,
)
async def get10(
    chassis_id: str,
    network_adapter_id: str,
    network_device_function_id: str,
    ethernet_interface_id: str,
    request: Request,
    response: Response,
) -> EthernetInterface:
    s: Service = find_service(EthernetInterface)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "network_adapter_id": network_adapter_id,
        "network_device_function_id": network_device_function_id,
        "ethernet_interface_id": ethernet_interface_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(EthernetInterface, s.get(**b))


@router.patch(
    "/redfish/v1/Chassis/{chassis_id}/NetworkAdapters/{network_adapter_id}/NetworkDeviceFunctions/{network_device_function_id}/EthernetInterfaces/{ethernet_interface_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch10(
    chassis_id: str,
    network_adapter_id: str,
    network_device_function_id: str,
    ethernet_interface_id: str,
    request: Request,
    response: Response,
    body: EthernetInterfaceOnUpdate,
) -> EthernetInterface:
    s: Service = find_service(EthernetInterface)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "network_adapter_id": network_adapter_id,
        "network_device_function_id": network_device_function_id,
        "ethernet_interface_id": ethernet_interface_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(EthernetInterface, s.patch(**b))
