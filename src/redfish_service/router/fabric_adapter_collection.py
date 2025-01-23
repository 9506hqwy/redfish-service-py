from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..model.fabric_adapter_collection import FabricAdapterCollection
from ..service import Service
from ..util import get_service, set_link_header

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
    s: Service = get_service(FabricAdapterCollection, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "request": request,
        "response": response,
    }
    m = cast(FabricAdapterCollection, s.get(**b))
    set_link_header(m, response)
    return m


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
    s: Service = get_service(FabricAdapterCollection, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "request": request,
        "response": response,
    }
    m = cast(FabricAdapterCollection, s.get(**b))
    set_link_header(m, response)
    return m


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
    s: Service = get_service(FabricAdapterCollection, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "request": request,
        "response": response,
    }
    m = cast(FabricAdapterCollection, s.get(**b))
    set_link_header(m, response)
    return m


@router.get("/redfish/v1/Chassis/{chassis_id}/FabricAdapters", response_model_exclude_none=True)
@router.head("/redfish/v1/Chassis/{chassis_id}/FabricAdapters", response_model_exclude_none=True)
async def get4(chassis_id: str, request: Request, response: Response) -> FabricAdapterCollection:
    s: Service = get_service(FabricAdapterCollection, request)
    b: dict[str, Any] = {"chassis_id": chassis_id, "request": request, "response": response}
    m = cast(FabricAdapterCollection, s.get(**b))
    set_link_header(m, response)
    return m
