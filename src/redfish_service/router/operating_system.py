from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.operating_system import OperatingSystem
from ..service import Service, find_service

router = APIRouter()


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/OperatingSystem", response_model_exclude_none=True
)
@router.head(
    "/redfish/v1/Systems/{computer_system_id}/OperatingSystem", response_model_exclude_none=True
)
@authenticate
async def get1(computer_system_id: str, request: Request, response: Response) -> OperatingSystem:
    s: Service = find_service(OperatingSystem)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(OperatingSystem, s.get(**b))


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/OperatingSystem",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/OperatingSystem",
    response_model_exclude_none=True,
)
@authenticate
async def get2(
    resource_block_id: str, computer_system_id: str, request: Request, response: Response
) -> OperatingSystem:
    s: Service = find_service(OperatingSystem)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(OperatingSystem, s.get(**b))


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/OperatingSystem",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/OperatingSystem",
    response_model_exclude_none=True,
)
@authenticate
async def get3(
    resource_block_id: str, computer_system_id: str, request: Request, response: Response
) -> OperatingSystem:
    s: Service = find_service(OperatingSystem)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(OperatingSystem, s.get(**b))
