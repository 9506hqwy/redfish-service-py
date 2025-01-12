from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.fabric_adapter import FabricAdapter, FabricAdapterOnUpdate
from ..service import Service
from ..util import get_service

router = APIRouter()


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}",
    response_model_exclude_none=True,
)
async def get1(
    computer_system_id: str, fabric_adapter_id: str, request: Request, response: Response
) -> FabricAdapter:
    s: Service = get_service(FabricAdapter, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "request": request,
        "response": response,
    }
    return cast(FabricAdapter, s.get(**b))


@router.patch(
    "/redfish/v1/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch1(
    computer_system_id: str,
    fabric_adapter_id: str,
    request: Request,
    response: Response,
    body: FabricAdapterOnUpdate,
) -> FabricAdapter:
    s: Service = get_service(FabricAdapter, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(FabricAdapter, s.patch(**b))


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}",
    response_model_exclude_none=True,
)
async def get2(
    resource_block_id: str,
    computer_system_id: str,
    fabric_adapter_id: str,
    request: Request,
    response: Response,
) -> FabricAdapter:
    s: Service = get_service(FabricAdapter, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "request": request,
        "response": response,
    }
    return cast(FabricAdapter, s.get(**b))


@router.patch(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch2(
    resource_block_id: str,
    computer_system_id: str,
    fabric_adapter_id: str,
    request: Request,
    response: Response,
    body: FabricAdapterOnUpdate,
) -> FabricAdapter:
    s: Service = get_service(FabricAdapter, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(FabricAdapter, s.patch(**b))


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}",
    response_model_exclude_none=True,
)
async def get3(
    resource_block_id: str,
    computer_system_id: str,
    fabric_adapter_id: str,
    request: Request,
    response: Response,
) -> FabricAdapter:
    s: Service = get_service(FabricAdapter, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "request": request,
        "response": response,
    }
    return cast(FabricAdapter, s.get(**b))


@router.patch(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch3(
    resource_block_id: str,
    computer_system_id: str,
    fabric_adapter_id: str,
    request: Request,
    response: Response,
    body: FabricAdapterOnUpdate,
) -> FabricAdapter:
    s: Service = get_service(FabricAdapter, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(FabricAdapter, s.patch(**b))


@router.get(
    "/redfish/v1/Chassis/{chassis_id}/FabricAdapters/{fabric_adapter_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Chassis/{chassis_id}/FabricAdapters/{fabric_adapter_id}",
    response_model_exclude_none=True,
)
async def get4(
    chassis_id: str, fabric_adapter_id: str, request: Request, response: Response
) -> FabricAdapter:
    s: Service = get_service(FabricAdapter, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "fabric_adapter_id": fabric_adapter_id,
        "request": request,
        "response": response,
    }
    return cast(FabricAdapter, s.get(**b))


@router.patch(
    "/redfish/v1/Chassis/{chassis_id}/FabricAdapters/{fabric_adapter_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch4(
    chassis_id: str,
    fabric_adapter_id: str,
    request: Request,
    response: Response,
    body: FabricAdapterOnUpdate,
) -> FabricAdapter:
    s: Service = get_service(FabricAdapter, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "fabric_adapter_id": fabric_adapter_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(FabricAdapter, s.patch(**b))
