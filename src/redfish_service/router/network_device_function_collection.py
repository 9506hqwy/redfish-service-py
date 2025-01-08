from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..model.network_device_function_collection import NetworkDeviceFunctionCollection
from ..service import Service, find_service

router = APIRouter()


@router.get(
    "/redfish/v1/Chassis/{chassis_id}/NetworkAdapters/{network_adapter_id}/NetworkDeviceFunctions",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Chassis/{chassis_id}/NetworkAdapters/{network_adapter_id}/NetworkDeviceFunctions",
    response_model_exclude_none=True,
)
async def get1(
    chassis_id: str, network_adapter_id: str, request: Request, response: Response
) -> NetworkDeviceFunctionCollection:
    s: Service = find_service(NetworkDeviceFunctionCollection)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "network_adapter_id": network_adapter_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(NetworkDeviceFunctionCollection, s.get(**b))


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/NetworkInterfaces/{network_interface_id}/NetworkDeviceFunctions",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Systems/{computer_system_id}/NetworkInterfaces/{network_interface_id}/NetworkDeviceFunctions",
    response_model_exclude_none=True,
)
async def get2(
    computer_system_id: str, network_interface_id: str, request: Request, response: Response
) -> NetworkDeviceFunctionCollection:
    s: Service = find_service(NetworkDeviceFunctionCollection)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "network_interface_id": network_interface_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(NetworkDeviceFunctionCollection, s.get(**b))


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/NetworkInterfaces/{network_interface_id}/NetworkDeviceFunctions",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/NetworkInterfaces/{network_interface_id}/NetworkDeviceFunctions",
    response_model_exclude_none=True,
)
async def get3(
    resource_block_id: str, network_interface_id: str, request: Request, response: Response
) -> NetworkDeviceFunctionCollection:
    s: Service = find_service(NetworkDeviceFunctionCollection)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "network_interface_id": network_interface_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(NetworkDeviceFunctionCollection, s.get(**b))


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/NetworkInterfaces/{network_interface_id}/NetworkDeviceFunctions",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/NetworkInterfaces/{network_interface_id}/NetworkDeviceFunctions",
    response_model_exclude_none=True,
)
async def get4(
    resource_block_id: str,
    computer_system_id: str,
    network_interface_id: str,
    request: Request,
    response: Response,
) -> NetworkDeviceFunctionCollection:
    s: Service = find_service(NetworkDeviceFunctionCollection)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "network_interface_id": network_interface_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(NetworkDeviceFunctionCollection, s.get(**b))


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/NetworkInterfaces/{network_interface_id}/NetworkDeviceFunctions",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/NetworkInterfaces/{network_interface_id}/NetworkDeviceFunctions",
    response_model_exclude_none=True,
)
async def get5(
    resource_block_id: str, network_interface_id: str, request: Request, response: Response
) -> NetworkDeviceFunctionCollection:
    s: Service = find_service(NetworkDeviceFunctionCollection)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "network_interface_id": network_interface_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(NetworkDeviceFunctionCollection, s.get(**b))


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/NetworkInterfaces/{network_interface_id}/NetworkDeviceFunctions",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/NetworkInterfaces/{network_interface_id}/NetworkDeviceFunctions",
    response_model_exclude_none=True,
)
async def get6(
    resource_block_id: str,
    computer_system_id: str,
    network_interface_id: str,
    request: Request,
    response: Response,
) -> NetworkDeviceFunctionCollection:
    s: Service = find_service(NetworkDeviceFunctionCollection)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "network_interface_id": network_interface_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(NetworkDeviceFunctionCollection, s.get(**b))
