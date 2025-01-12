from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.allow_deny import AllowDeny, AllowDenyOnCreate
from ..model.allow_deny_collection import AllowDenyCollection
from ..service import Service, ServiceCollection
from ..util import get_service, get_service_collection

router = APIRouter()


@router.get(
    "/redfish/v1/Chassis/{chassis_id}/NetworkAdapters/{network_adapter_id}/NetworkDeviceFunctions/{network_device_function_id}/AllowDeny",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Chassis/{chassis_id}/NetworkAdapters/{network_adapter_id}/NetworkDeviceFunctions/{network_device_function_id}/AllowDeny",
    response_model_exclude_none=True,
)
async def get1(
    chassis_id: str,
    network_adapter_id: str,
    network_device_function_id: str,
    request: Request,
    response: Response,
) -> AllowDenyCollection:
    s: Service = get_service(AllowDenyCollection, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "network_adapter_id": network_adapter_id,
        "network_device_function_id": network_device_function_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(AllowDenyCollection, s.get(**b))


@router.post(
    "/redfish/v1/Chassis/{chassis_id}/NetworkAdapters/{network_adapter_id}/NetworkDeviceFunctions/{network_device_function_id}/AllowDeny",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/Chassis/{chassis_id}/NetworkAdapters/{network_adapter_id}/NetworkDeviceFunctions/{network_device_function_id}/AllowDeny/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post1(
    chassis_id: str,
    network_adapter_id: str,
    network_device_function_id: str,
    request: Request,
    response: Response,
    body: AllowDenyOnCreate,
) -> AllowDeny:
    s: ServiceCollection = get_service_collection(AllowDenyCollection, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "network_adapter_id": network_adapter_id,
        "network_device_function_id": network_device_function_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(AllowDeny, s.post(**b))


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/NetworkInterfaces/{network_interface_id}/NetworkDeviceFunctions/{network_device_function_id}/AllowDeny",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Systems/{computer_system_id}/NetworkInterfaces/{network_interface_id}/NetworkDeviceFunctions/{network_device_function_id}/AllowDeny",
    response_model_exclude_none=True,
)
async def get2(
    computer_system_id: str,
    network_interface_id: str,
    network_device_function_id: str,
    request: Request,
    response: Response,
) -> AllowDenyCollection:
    s: Service = get_service(AllowDenyCollection, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "network_interface_id": network_interface_id,
        "network_device_function_id": network_device_function_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(AllowDenyCollection, s.get(**b))


@router.post(
    "/redfish/v1/Systems/{computer_system_id}/NetworkInterfaces/{network_interface_id}/NetworkDeviceFunctions/{network_device_function_id}/AllowDeny",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/Systems/{computer_system_id}/NetworkInterfaces/{network_interface_id}/NetworkDeviceFunctions/{network_device_function_id}/AllowDeny/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post2(
    computer_system_id: str,
    network_interface_id: str,
    network_device_function_id: str,
    request: Request,
    response: Response,
    body: AllowDenyOnCreate,
) -> AllowDeny:
    s: ServiceCollection = get_service_collection(AllowDenyCollection, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "network_interface_id": network_interface_id,
        "network_device_function_id": network_device_function_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(AllowDeny, s.post(**b))


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/NetworkInterfaces/{network_interface_id}/NetworkDeviceFunctions/{network_device_function_id}/AllowDeny",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/NetworkInterfaces/{network_interface_id}/NetworkDeviceFunctions/{network_device_function_id}/AllowDeny",
    response_model_exclude_none=True,
)
async def get3(
    resource_block_id: str,
    network_interface_id: str,
    network_device_function_id: str,
    request: Request,
    response: Response,
) -> AllowDenyCollection:
    s: Service = get_service(AllowDenyCollection, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "network_interface_id": network_interface_id,
        "network_device_function_id": network_device_function_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(AllowDenyCollection, s.get(**b))


@router.post(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/NetworkInterfaces/{network_interface_id}/NetworkDeviceFunctions/{network_device_function_id}/AllowDeny",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/NetworkInterfaces/{network_interface_id}/NetworkDeviceFunctions/{network_device_function_id}/AllowDeny/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post3(
    resource_block_id: str,
    network_interface_id: str,
    network_device_function_id: str,
    request: Request,
    response: Response,
    body: AllowDenyOnCreate,
) -> AllowDeny:
    s: ServiceCollection = get_service_collection(AllowDenyCollection, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "network_interface_id": network_interface_id,
        "network_device_function_id": network_device_function_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(AllowDeny, s.post(**b))


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/NetworkInterfaces/{network_interface_id}/NetworkDeviceFunctions/{network_device_function_id}/AllowDeny",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/NetworkInterfaces/{network_interface_id}/NetworkDeviceFunctions/{network_device_function_id}/AllowDeny",
    response_model_exclude_none=True,
)
async def get4(
    resource_block_id: str,
    computer_system_id: str,
    network_interface_id: str,
    network_device_function_id: str,
    request: Request,
    response: Response,
) -> AllowDenyCollection:
    s: Service = get_service(AllowDenyCollection, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "network_interface_id": network_interface_id,
        "network_device_function_id": network_device_function_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(AllowDenyCollection, s.get(**b))


@router.post(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/NetworkInterfaces/{network_interface_id}/NetworkDeviceFunctions/{network_device_function_id}/AllowDeny",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/NetworkInterfaces/{network_interface_id}/NetworkDeviceFunctions/{network_device_function_id}/AllowDeny/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post4(
    resource_block_id: str,
    computer_system_id: str,
    network_interface_id: str,
    network_device_function_id: str,
    request: Request,
    response: Response,
    body: AllowDenyOnCreate,
) -> AllowDeny:
    s: ServiceCollection = get_service_collection(AllowDenyCollection, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "network_interface_id": network_interface_id,
        "network_device_function_id": network_device_function_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(AllowDeny, s.post(**b))


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/NetworkInterfaces/{network_interface_id}/NetworkDeviceFunctions/{network_device_function_id}/AllowDeny",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/NetworkInterfaces/{network_interface_id}/NetworkDeviceFunctions/{network_device_function_id}/AllowDeny",
    response_model_exclude_none=True,
)
async def get5(
    resource_block_id: str,
    network_interface_id: str,
    network_device_function_id: str,
    request: Request,
    response: Response,
) -> AllowDenyCollection:
    s: Service = get_service(AllowDenyCollection, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "network_interface_id": network_interface_id,
        "network_device_function_id": network_device_function_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(AllowDenyCollection, s.get(**b))


@router.post(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/NetworkInterfaces/{network_interface_id}/NetworkDeviceFunctions/{network_device_function_id}/AllowDeny",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/NetworkInterfaces/{network_interface_id}/NetworkDeviceFunctions/{network_device_function_id}/AllowDeny/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post5(
    resource_block_id: str,
    network_interface_id: str,
    network_device_function_id: str,
    request: Request,
    response: Response,
    body: AllowDenyOnCreate,
) -> AllowDeny:
    s: ServiceCollection = get_service_collection(AllowDenyCollection, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "network_interface_id": network_interface_id,
        "network_device_function_id": network_device_function_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(AllowDeny, s.post(**b))


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/NetworkInterfaces/{network_interface_id}/NetworkDeviceFunctions/{network_device_function_id}/AllowDeny",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/NetworkInterfaces/{network_interface_id}/NetworkDeviceFunctions/{network_device_function_id}/AllowDeny",
    response_model_exclude_none=True,
)
async def get6(
    resource_block_id: str,
    computer_system_id: str,
    network_interface_id: str,
    network_device_function_id: str,
    request: Request,
    response: Response,
) -> AllowDenyCollection:
    s: Service = get_service(AllowDenyCollection, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "network_interface_id": network_interface_id,
        "network_device_function_id": network_device_function_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(AllowDenyCollection, s.get(**b))


@router.post(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/NetworkInterfaces/{network_interface_id}/NetworkDeviceFunctions/{network_device_function_id}/AllowDeny",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/NetworkInterfaces/{network_interface_id}/NetworkDeviceFunctions/{network_device_function_id}/AllowDeny/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post6(
    resource_block_id: str,
    computer_system_id: str,
    network_interface_id: str,
    network_device_function_id: str,
    request: Request,
    response: Response,
    body: AllowDenyOnCreate,
) -> AllowDeny:
    s: ServiceCollection = get_service_collection(AllowDenyCollection, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "network_interface_id": network_interface_id,
        "network_device_function_id": network_device_function_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(AllowDeny, s.post(**b))
