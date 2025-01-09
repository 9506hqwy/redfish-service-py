from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.computer_system import ComputerSystem
from ..service import Service, find_service

router = APIRouter()


@router.delete("/redfish/v1/Systems/{computer_system_id}", response_model_exclude_none=True)
@authenticate
async def delete1(computer_system_id: str, request: Request, response: Response) -> None:
    s: Service = find_service(ComputerSystem)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return s.delete(**b)


@router.get("/redfish/v1/Systems/{computer_system_id}", response_model_exclude_none=True)
@router.head("/redfish/v1/Systems/{computer_system_id}", response_model_exclude_none=True)
async def get1(computer_system_id: str, request: Request, response: Response) -> ComputerSystem:
    s: Service = find_service(ComputerSystem)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(ComputerSystem, s.get(**b))


@router.delete(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete2(
    resource_block_id: str, computer_system_id: str, request: Request, response: Response
) -> None:
    s: Service = find_service(ComputerSystem)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return s.delete(**b)


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}",
    response_model_exclude_none=True,
)
async def get2(
    resource_block_id: str, computer_system_id: str, request: Request, response: Response
) -> ComputerSystem:
    s: Service = find_service(ComputerSystem)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(ComputerSystem, s.get(**b))


@router.delete(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete3(
    resource_block_id: str, computer_system_id: str, request: Request, response: Response
) -> None:
    s: Service = find_service(ComputerSystem)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return s.delete(**b)


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}",
    response_model_exclude_none=True,
)
async def get3(
    resource_block_id: str, computer_system_id: str, request: Request, response: Response
) -> ComputerSystem:
    s: Service = find_service(ComputerSystem)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(ComputerSystem, s.get(**b))
