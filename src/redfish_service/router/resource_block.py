from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.resource_block import ResourceBlock, ResourceBlockOnUpdate
from ..service import Service
from ..util import get_service

router = APIRouter()


@router.delete(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete1(resource_block_id: str, request: Request, response: Response) -> None:
    s: Service = get_service(ResourceBlock, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return s.delete(**b)


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}",
    response_model_exclude_none=True,
)
async def get1(resource_block_id: str, request: Request, response: Response) -> ResourceBlock:
    s: Service = get_service(ResourceBlock, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(ResourceBlock, s.get(**b))


@router.patch(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch1(
    resource_block_id: str, request: Request, response: Response, body: ResourceBlockOnUpdate
) -> ResourceBlock:
    s: Service = get_service(ResourceBlock, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(ResourceBlock, s.patch(**b))


@router.delete("/redfish/v1/ResourceBlocks/{resource_block_id}", response_model_exclude_none=True)
@authenticate
async def delete2(resource_block_id: str, request: Request, response: Response) -> None:
    s: Service = get_service(ResourceBlock, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return s.delete(**b)


@router.get("/redfish/v1/ResourceBlocks/{resource_block_id}", response_model_exclude_none=True)
@router.head("/redfish/v1/ResourceBlocks/{resource_block_id}", response_model_exclude_none=True)
async def get2(resource_block_id: str, request: Request, response: Response) -> ResourceBlock:
    s: Service = get_service(ResourceBlock, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(ResourceBlock, s.get(**b))


@router.patch("/redfish/v1/ResourceBlocks/{resource_block_id}", response_model_exclude_none=True)
@authenticate
async def patch2(
    resource_block_id: str, request: Request, response: Response, body: ResourceBlockOnUpdate
) -> ResourceBlock:
    s: Service = get_service(ResourceBlock, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(ResourceBlock, s.patch(**b))
