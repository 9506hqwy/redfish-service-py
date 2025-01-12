from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.resource_block import ResourceBlock, ResourceBlockOnCreate
from ..model.resource_block_collection import ResourceBlockCollection
from ..service import Service, ServiceCollection
from ..util import get_service, get_service_collection

router = APIRouter()


@router.get("/redfish/v1/CompositionService/ActivePool", response_model_exclude_none=True)
@router.head("/redfish/v1/CompositionService/ActivePool", response_model_exclude_none=True)
async def get1(request: Request, response: Response) -> ResourceBlockCollection:
    s: Service = get_service(ResourceBlockCollection, request)
    b: dict[str, Any] = {"request": request, "response": response}

    response.headers["OData-Version"] = "4.0"

    return cast(ResourceBlockCollection, s.get(**b))


@router.post("/redfish/v1/CompositionService/ActivePool", response_model_exclude_none=True)
@router.post("/redfish/v1/CompositionService/ActivePool/Members", response_model_exclude_none=True)
@authenticate
async def post1(
    request: Request, response: Response, body: ResourceBlockOnCreate
) -> ResourceBlock:
    s: ServiceCollection = get_service_collection(ResourceBlockCollection, request)
    b: dict[str, Any] = {"request": request, "response": response, "body": body}

    response.headers["OData-Version"] = "4.0"

    return cast(ResourceBlock, s.post(**b))


@router.get("/redfish/v1/CompositionService/FreePool", response_model_exclude_none=True)
@router.head("/redfish/v1/CompositionService/FreePool", response_model_exclude_none=True)
async def get2(request: Request, response: Response) -> ResourceBlockCollection:
    s: Service = get_service(ResourceBlockCollection, request)
    b: dict[str, Any] = {"request": request, "response": response}

    response.headers["OData-Version"] = "4.0"

    return cast(ResourceBlockCollection, s.get(**b))


@router.post("/redfish/v1/CompositionService/FreePool", response_model_exclude_none=True)
@router.post("/redfish/v1/CompositionService/FreePool/Members", response_model_exclude_none=True)
@authenticate
async def post2(
    request: Request, response: Response, body: ResourceBlockOnCreate
) -> ResourceBlock:
    s: ServiceCollection = get_service_collection(ResourceBlockCollection, request)
    b: dict[str, Any] = {"request": request, "response": response, "body": body}

    response.headers["OData-Version"] = "4.0"

    return cast(ResourceBlock, s.post(**b))


@router.get("/redfish/v1/CompositionService/ResourceBlocks", response_model_exclude_none=True)
@router.head("/redfish/v1/CompositionService/ResourceBlocks", response_model_exclude_none=True)
async def get3(request: Request, response: Response) -> ResourceBlockCollection:
    s: Service = get_service(ResourceBlockCollection, request)
    b: dict[str, Any] = {"request": request, "response": response}

    response.headers["OData-Version"] = "4.0"

    return cast(ResourceBlockCollection, s.get(**b))


@router.post("/redfish/v1/CompositionService/ResourceBlocks", response_model_exclude_none=True)
@router.post(
    "/redfish/v1/CompositionService/ResourceBlocks/Members", response_model_exclude_none=True
)
@authenticate
async def post3(
    request: Request, response: Response, body: ResourceBlockOnCreate
) -> ResourceBlock:
    s: ServiceCollection = get_service_collection(ResourceBlockCollection, request)
    b: dict[str, Any] = {"request": request, "response": response, "body": body}

    response.headers["OData-Version"] = "4.0"

    return cast(ResourceBlock, s.post(**b))


@router.get("/redfish/v1/ResourceBlocks", response_model_exclude_none=True)
@router.head("/redfish/v1/ResourceBlocks", response_model_exclude_none=True)
async def get4(request: Request, response: Response) -> ResourceBlockCollection:
    s: Service = get_service(ResourceBlockCollection, request)
    b: dict[str, Any] = {"request": request, "response": response}

    response.headers["OData-Version"] = "4.0"

    return cast(ResourceBlockCollection, s.get(**b))


@router.post("/redfish/v1/ResourceBlocks", response_model_exclude_none=True)
@router.post("/redfish/v1/ResourceBlocks/Members", response_model_exclude_none=True)
@authenticate
async def post4(
    request: Request, response: Response, body: ResourceBlockOnCreate
) -> ResourceBlock:
    s: ServiceCollection = get_service_collection(ResourceBlockCollection, request)
    b: dict[str, Any] = {"request": request, "response": response, "body": body}

    response.headers["OData-Version"] = "4.0"

    return cast(ResourceBlock, s.post(**b))
