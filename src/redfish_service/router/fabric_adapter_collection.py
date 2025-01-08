from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..model.fabric_adapter_collection import FabricAdapterCollection
from ..service import Service, find_service

router = APIRouter()


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/FabricAdapters", response_model_exclude_none=True
)
@router.head(
    "/redfish/v1/Systems/{computer_system_id}/FabricAdapters", response_model_exclude_none=True
)
async def get1(
    computer_system_id: str, request: Request, response: Response
) -> FabricAdapterCollection:
    s: Service = find_service(FabricAdapterCollection)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(FabricAdapterCollection, s.get(**b))


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/FabricAdapters",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/FabricAdapters",
    response_model_exclude_none=True,
)
async def get2(
    resource_block_id: str, computer_system_id: str, request: Request, response: Response
) -> FabricAdapterCollection:
    s: Service = find_service(FabricAdapterCollection)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(FabricAdapterCollection, s.get(**b))


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/FabricAdapters",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/FabricAdapters",
    response_model_exclude_none=True,
)
async def get3(
    resource_block_id: str, computer_system_id: str, request: Request, response: Response
) -> FabricAdapterCollection:
    s: Service = find_service(FabricAdapterCollection)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(FabricAdapterCollection, s.get(**b))


@router.get("/redfish/v1/Chassis/{chassis_id}/FabricAdapters", response_model_exclude_none=True)
@router.head("/redfish/v1/Chassis/{chassis_id}/FabricAdapters", response_model_exclude_none=True)
async def get4(chassis_id: str, request: Request, response: Response) -> FabricAdapterCollection:
    s: Service = find_service(FabricAdapterCollection)
    b: dict[str, Any] = {"chassis_id": chassis_id, "request": request, "response": response}

    response.headers["OData-Version"] = "4.0"

    return cast(FabricAdapterCollection, s.get(**b))
