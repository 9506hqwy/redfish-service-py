from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..model.acceleration_function_collection import AccelerationFunctionCollection
from ..service import Service
from ..util import get_service

router = APIRouter()


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/Processors/{processor_id}/AccelerationFunctions",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Systems/{computer_system_id}/Processors/{processor_id}/AccelerationFunctions",
    response_model_exclude_none=True,
)
async def get1(
    computer_system_id: str, processor_id: str, request: Request, response: Response
) -> AccelerationFunctionCollection:
    s: Service = get_service(AccelerationFunctionCollection, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "processor_id": processor_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(AccelerationFunctionCollection, s.get(**b))


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Processors/{processor_id}/AccelerationFunctions",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Processors/{processor_id}/AccelerationFunctions",
    response_model_exclude_none=True,
)
async def get2(
    resource_block_id: str, processor_id: str, request: Request, response: Response
) -> AccelerationFunctionCollection:
    s: Service = get_service(AccelerationFunctionCollection, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "processor_id": processor_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(AccelerationFunctionCollection, s.get(**b))


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Processors/{processor_id}/AccelerationFunctions",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Processors/{processor_id}/AccelerationFunctions",
    response_model_exclude_none=True,
)
async def get3(
    resource_block_id: str,
    computer_system_id: str,
    processor_id: str,
    request: Request,
    response: Response,
) -> AccelerationFunctionCollection:
    s: Service = get_service(AccelerationFunctionCollection, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "processor_id": processor_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(AccelerationFunctionCollection, s.get(**b))


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Processors/{processor_id}/AccelerationFunctions",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Processors/{processor_id}/AccelerationFunctions",
    response_model_exclude_none=True,
)
async def get4(
    resource_block_id: str, processor_id: str, request: Request, response: Response
) -> AccelerationFunctionCollection:
    s: Service = get_service(AccelerationFunctionCollection, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "processor_id": processor_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(AccelerationFunctionCollection, s.get(**b))


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Processors/{processor_id}/AccelerationFunctions",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Processors/{processor_id}/AccelerationFunctions",
    response_model_exclude_none=True,
)
async def get5(
    resource_block_id: str,
    computer_system_id: str,
    processor_id: str,
    request: Request,
    response: Response,
) -> AccelerationFunctionCollection:
    s: Service = get_service(AccelerationFunctionCollection, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "processor_id": processor_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(AccelerationFunctionCollection, s.get(**b))
