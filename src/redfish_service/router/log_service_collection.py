from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..model.log_service_collection import LogServiceCollection
from ..service import Service
from ..util import get_service, set_link_header

router = APIRouter()


@router.get("/redfish/v1/Managers/{manager_id}/LogServices", response_model_exclude_none=True)
@router.head("/redfish/v1/Managers/{manager_id}/LogServices", response_model_exclude_none=True)
async def get1(manager_id: str, request: Request, response: Response) -> LogServiceCollection:
    s: Service = get_service(LogServiceCollection, request)
    b: dict[str, Any] = {"manager_id": manager_id, "request": request, "response": response}
    m = cast(LogServiceCollection, s.get(**b))
    set_link_header(m, response)
    return m


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/LogServices", response_model_exclude_none=True
)
@router.head(
    "/redfish/v1/Systems/{computer_system_id}/LogServices", response_model_exclude_none=True
)
async def get2(
    computer_system_id: str, request: Request, response: Response
) -> LogServiceCollection:
    s: Service = get_service(LogServiceCollection, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "request": request,
        "response": response,
    }
    m = cast(LogServiceCollection, s.get(**b))
    set_link_header(m, response)
    return m


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/LogServices",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/LogServices",
    response_model_exclude_none=True,
)
async def get3(
    resource_block_id: str, computer_system_id: str, request: Request, response: Response
) -> LogServiceCollection:
    s: Service = get_service(LogServiceCollection, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "request": request,
        "response": response,
    }
    m = cast(LogServiceCollection, s.get(**b))
    set_link_header(m, response)
    return m


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/LogServices",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/LogServices",
    response_model_exclude_none=True,
)
async def get4(
    resource_block_id: str, computer_system_id: str, request: Request, response: Response
) -> LogServiceCollection:
    s: Service = get_service(LogServiceCollection, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "request": request,
        "response": response,
    }
    m = cast(LogServiceCollection, s.get(**b))
    set_link_header(m, response)
    return m


@router.get("/redfish/v1/Chassis/{chassis_id}/LogServices", response_model_exclude_none=True)
@router.head("/redfish/v1/Chassis/{chassis_id}/LogServices", response_model_exclude_none=True)
async def get5(chassis_id: str, request: Request, response: Response) -> LogServiceCollection:
    s: Service = get_service(LogServiceCollection, request)
    b: dict[str, Any] = {"chassis_id": chassis_id, "request": request, "response": response}
    m = cast(LogServiceCollection, s.get(**b))
    set_link_header(m, response)
    return m
