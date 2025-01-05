from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.resource_block_collection import ResourceBlockCollection
from ..service import Service, find_service

router = APIRouter()


@router.get("/redfish/v1/CompositionService/ActivePool", response_model_exclude_none=True)
@authenticate
async def get1(request: Request, response: Response) -> ResourceBlockCollection:
    s: Service = find_service(ResourceBlockCollection)
    b: dict[str, Any] = {"request": request, "response": response}

    response.headers["OData-Version"] = "4.0"

    return cast(ResourceBlockCollection, s.get(**b))


@router.get("/redfish/v1/CompositionService/FreePool", response_model_exclude_none=True)
@authenticate
async def get2(request: Request, response: Response) -> ResourceBlockCollection:
    s: Service = find_service(ResourceBlockCollection)
    b: dict[str, Any] = {"request": request, "response": response}

    response.headers["OData-Version"] = "4.0"

    return cast(ResourceBlockCollection, s.get(**b))


@router.get("/redfish/v1/CompositionService/ResourceBlocks", response_model_exclude_none=True)
@authenticate
async def get3(request: Request, response: Response) -> ResourceBlockCollection:
    s: Service = find_service(ResourceBlockCollection)
    b: dict[str, Any] = {"request": request, "response": response}

    response.headers["OData-Version"] = "4.0"

    return cast(ResourceBlockCollection, s.get(**b))


@router.get("/redfish/v1/ResourceBlocks", response_model_exclude_none=True)
@authenticate
async def get4(request: Request, response: Response) -> ResourceBlockCollection:
    s: Service = find_service(ResourceBlockCollection)
    b: dict[str, Any] = {"request": request, "response": response}

    response.headers["OData-Version"] = "4.0"

    return cast(ResourceBlockCollection, s.get(**b))
