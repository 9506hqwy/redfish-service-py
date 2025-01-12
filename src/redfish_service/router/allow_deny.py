from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.allow_deny import AllowDeny, AllowDenyOnUpdate
from ..service import Service
from ..util import get_service

router = APIRouter()


@router.delete(
    "/redfish/v1/Chassis/{chassis_id}/NetworkAdapters/{network_adapter_id}/NetworkDeviceFunctions/{network_device_function_id}/AllowDeny/{allow_deny_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete1(
    chassis_id: str,
    network_adapter_id: str,
    network_device_function_id: str,
    allow_deny_id: str,
    request: Request,
    response: Response,
) -> None:
    s: Service = get_service(AllowDeny, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "network_adapter_id": network_adapter_id,
        "network_device_function_id": network_device_function_id,
        "allow_deny_id": allow_deny_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return s.delete(**b)


@router.get(
    "/redfish/v1/Chassis/{chassis_id}/NetworkAdapters/{network_adapter_id}/NetworkDeviceFunctions/{network_device_function_id}/AllowDeny/{allow_deny_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Chassis/{chassis_id}/NetworkAdapters/{network_adapter_id}/NetworkDeviceFunctions/{network_device_function_id}/AllowDeny/{allow_deny_id}",
    response_model_exclude_none=True,
)
async def get1(
    chassis_id: str,
    network_adapter_id: str,
    network_device_function_id: str,
    allow_deny_id: str,
    request: Request,
    response: Response,
) -> AllowDeny:
    s: Service = get_service(AllowDeny, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "network_adapter_id": network_adapter_id,
        "network_device_function_id": network_device_function_id,
        "allow_deny_id": allow_deny_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(AllowDeny, s.get(**b))


@router.patch(
    "/redfish/v1/Chassis/{chassis_id}/NetworkAdapters/{network_adapter_id}/NetworkDeviceFunctions/{network_device_function_id}/AllowDeny/{allow_deny_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch1(
    chassis_id: str,
    network_adapter_id: str,
    network_device_function_id: str,
    allow_deny_id: str,
    request: Request,
    response: Response,
    body: AllowDenyOnUpdate,
) -> AllowDeny:
    s: Service = get_service(AllowDeny, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "network_adapter_id": network_adapter_id,
        "network_device_function_id": network_device_function_id,
        "allow_deny_id": allow_deny_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(AllowDeny, s.patch(**b))


@router.delete(
    "/redfish/v1/Systems/{computer_system_id}/NetworkInterfaces/{network_interface_id}/NetworkDeviceFunctions/{network_device_function_id}/AllowDeny/{allow_deny_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete2(
    computer_system_id: str,
    network_interface_id: str,
    network_device_function_id: str,
    allow_deny_id: str,
    request: Request,
    response: Response,
) -> None:
    s: Service = get_service(AllowDeny, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "network_interface_id": network_interface_id,
        "network_device_function_id": network_device_function_id,
        "allow_deny_id": allow_deny_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return s.delete(**b)


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/NetworkInterfaces/{network_interface_id}/NetworkDeviceFunctions/{network_device_function_id}/AllowDeny/{allow_deny_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Systems/{computer_system_id}/NetworkInterfaces/{network_interface_id}/NetworkDeviceFunctions/{network_device_function_id}/AllowDeny/{allow_deny_id}",
    response_model_exclude_none=True,
)
async def get2(
    computer_system_id: str,
    network_interface_id: str,
    network_device_function_id: str,
    allow_deny_id: str,
    request: Request,
    response: Response,
) -> AllowDeny:
    s: Service = get_service(AllowDeny, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "network_interface_id": network_interface_id,
        "network_device_function_id": network_device_function_id,
        "allow_deny_id": allow_deny_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(AllowDeny, s.get(**b))


@router.patch(
    "/redfish/v1/Systems/{computer_system_id}/NetworkInterfaces/{network_interface_id}/NetworkDeviceFunctions/{network_device_function_id}/AllowDeny/{allow_deny_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch2(
    computer_system_id: str,
    network_interface_id: str,
    network_device_function_id: str,
    allow_deny_id: str,
    request: Request,
    response: Response,
    body: AllowDenyOnUpdate,
) -> AllowDeny:
    s: Service = get_service(AllowDeny, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "network_interface_id": network_interface_id,
        "network_device_function_id": network_device_function_id,
        "allow_deny_id": allow_deny_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(AllowDeny, s.patch(**b))


@router.delete(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/NetworkInterfaces/{network_interface_id}/NetworkDeviceFunctions/{network_device_function_id}/AllowDeny/{allow_deny_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete3(
    resource_block_id: str,
    network_interface_id: str,
    network_device_function_id: str,
    allow_deny_id: str,
    request: Request,
    response: Response,
) -> None:
    s: Service = get_service(AllowDeny, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "network_interface_id": network_interface_id,
        "network_device_function_id": network_device_function_id,
        "allow_deny_id": allow_deny_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return s.delete(**b)


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/NetworkInterfaces/{network_interface_id}/NetworkDeviceFunctions/{network_device_function_id}/AllowDeny/{allow_deny_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/NetworkInterfaces/{network_interface_id}/NetworkDeviceFunctions/{network_device_function_id}/AllowDeny/{allow_deny_id}",
    response_model_exclude_none=True,
)
async def get3(
    resource_block_id: str,
    network_interface_id: str,
    network_device_function_id: str,
    allow_deny_id: str,
    request: Request,
    response: Response,
) -> AllowDeny:
    s: Service = get_service(AllowDeny, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "network_interface_id": network_interface_id,
        "network_device_function_id": network_device_function_id,
        "allow_deny_id": allow_deny_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(AllowDeny, s.get(**b))


@router.patch(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/NetworkInterfaces/{network_interface_id}/NetworkDeviceFunctions/{network_device_function_id}/AllowDeny/{allow_deny_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch3(
    resource_block_id: str,
    network_interface_id: str,
    network_device_function_id: str,
    allow_deny_id: str,
    request: Request,
    response: Response,
    body: AllowDenyOnUpdate,
) -> AllowDeny:
    s: Service = get_service(AllowDeny, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "network_interface_id": network_interface_id,
        "network_device_function_id": network_device_function_id,
        "allow_deny_id": allow_deny_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(AllowDeny, s.patch(**b))


@router.delete(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/NetworkInterfaces/{network_interface_id}/NetworkDeviceFunctions/{network_device_function_id}/AllowDeny/{allow_deny_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete4(
    resource_block_id: str,
    computer_system_id: str,
    network_interface_id: str,
    network_device_function_id: str,
    allow_deny_id: str,
    request: Request,
    response: Response,
) -> None:
    s: Service = get_service(AllowDeny, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "network_interface_id": network_interface_id,
        "network_device_function_id": network_device_function_id,
        "allow_deny_id": allow_deny_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return s.delete(**b)


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/NetworkInterfaces/{network_interface_id}/NetworkDeviceFunctions/{network_device_function_id}/AllowDeny/{allow_deny_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/NetworkInterfaces/{network_interface_id}/NetworkDeviceFunctions/{network_device_function_id}/AllowDeny/{allow_deny_id}",
    response_model_exclude_none=True,
)
async def get4(
    resource_block_id: str,
    computer_system_id: str,
    network_interface_id: str,
    network_device_function_id: str,
    allow_deny_id: str,
    request: Request,
    response: Response,
) -> AllowDeny:
    s: Service = get_service(AllowDeny, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "network_interface_id": network_interface_id,
        "network_device_function_id": network_device_function_id,
        "allow_deny_id": allow_deny_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(AllowDeny, s.get(**b))


@router.patch(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/NetworkInterfaces/{network_interface_id}/NetworkDeviceFunctions/{network_device_function_id}/AllowDeny/{allow_deny_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch4(
    resource_block_id: str,
    computer_system_id: str,
    network_interface_id: str,
    network_device_function_id: str,
    allow_deny_id: str,
    request: Request,
    response: Response,
    body: AllowDenyOnUpdate,
) -> AllowDeny:
    s: Service = get_service(AllowDeny, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "network_interface_id": network_interface_id,
        "network_device_function_id": network_device_function_id,
        "allow_deny_id": allow_deny_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(AllowDeny, s.patch(**b))


@router.delete(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/NetworkInterfaces/{network_interface_id}/NetworkDeviceFunctions/{network_device_function_id}/AllowDeny/{allow_deny_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete5(
    resource_block_id: str,
    network_interface_id: str,
    network_device_function_id: str,
    allow_deny_id: str,
    request: Request,
    response: Response,
) -> None:
    s: Service = get_service(AllowDeny, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "network_interface_id": network_interface_id,
        "network_device_function_id": network_device_function_id,
        "allow_deny_id": allow_deny_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return s.delete(**b)


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/NetworkInterfaces/{network_interface_id}/NetworkDeviceFunctions/{network_device_function_id}/AllowDeny/{allow_deny_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/NetworkInterfaces/{network_interface_id}/NetworkDeviceFunctions/{network_device_function_id}/AllowDeny/{allow_deny_id}",
    response_model_exclude_none=True,
)
async def get5(
    resource_block_id: str,
    network_interface_id: str,
    network_device_function_id: str,
    allow_deny_id: str,
    request: Request,
    response: Response,
) -> AllowDeny:
    s: Service = get_service(AllowDeny, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "network_interface_id": network_interface_id,
        "network_device_function_id": network_device_function_id,
        "allow_deny_id": allow_deny_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(AllowDeny, s.get(**b))


@router.patch(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/NetworkInterfaces/{network_interface_id}/NetworkDeviceFunctions/{network_device_function_id}/AllowDeny/{allow_deny_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch5(
    resource_block_id: str,
    network_interface_id: str,
    network_device_function_id: str,
    allow_deny_id: str,
    request: Request,
    response: Response,
    body: AllowDenyOnUpdate,
) -> AllowDeny:
    s: Service = get_service(AllowDeny, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "network_interface_id": network_interface_id,
        "network_device_function_id": network_device_function_id,
        "allow_deny_id": allow_deny_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(AllowDeny, s.patch(**b))


@router.delete(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/NetworkInterfaces/{network_interface_id}/NetworkDeviceFunctions/{network_device_function_id}/AllowDeny/{allow_deny_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete6(
    resource_block_id: str,
    computer_system_id: str,
    network_interface_id: str,
    network_device_function_id: str,
    allow_deny_id: str,
    request: Request,
    response: Response,
) -> None:
    s: Service = get_service(AllowDeny, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "network_interface_id": network_interface_id,
        "network_device_function_id": network_device_function_id,
        "allow_deny_id": allow_deny_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return s.delete(**b)


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/NetworkInterfaces/{network_interface_id}/NetworkDeviceFunctions/{network_device_function_id}/AllowDeny/{allow_deny_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/NetworkInterfaces/{network_interface_id}/NetworkDeviceFunctions/{network_device_function_id}/AllowDeny/{allow_deny_id}",
    response_model_exclude_none=True,
)
async def get6(
    resource_block_id: str,
    computer_system_id: str,
    network_interface_id: str,
    network_device_function_id: str,
    allow_deny_id: str,
    request: Request,
    response: Response,
) -> AllowDeny:
    s: Service = get_service(AllowDeny, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "network_interface_id": network_interface_id,
        "network_device_function_id": network_device_function_id,
        "allow_deny_id": allow_deny_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(AllowDeny, s.get(**b))


@router.patch(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/NetworkInterfaces/{network_interface_id}/NetworkDeviceFunctions/{network_device_function_id}/AllowDeny/{allow_deny_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch6(
    resource_block_id: str,
    computer_system_id: str,
    network_interface_id: str,
    network_device_function_id: str,
    allow_deny_id: str,
    request: Request,
    response: Response,
    body: AllowDenyOnUpdate,
) -> AllowDeny:
    s: Service = get_service(AllowDeny, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "network_interface_id": network_interface_id,
        "network_device_function_id": network_device_function_id,
        "allow_deny_id": allow_deny_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(AllowDeny, s.patch(**b))
