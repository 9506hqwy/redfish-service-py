from typing import Any, cast

from fastapi import APIRouter

from ..authenticate import authenticate
from ..model.acceleration_function import AccelerationFunction
from ..service import Service, find_service

router = APIRouter()


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/Processors/{processor_id}/AccelerationFunctions/{acceleration_function_id}",
    response_model_exclude_none=True,
)
@authenticate
async def get1(
    computer_system_id: str, processor_id: str, acceleration_function_id: str
) -> AccelerationFunction:
    s: Service = find_service(AccelerationFunction)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "processor_id": processor_id,
        "acceleration_function_id": acceleration_function_id,
    }
    return cast(AccelerationFunction, s.get(**b))


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Processors/{processor_id}/AccelerationFunctions/{acceleration_function_id}",
    response_model_exclude_none=True,
)
@authenticate
async def get2(
    resource_block_id: str, processor_id: str, acceleration_function_id: str
) -> AccelerationFunction:
    s: Service = find_service(AccelerationFunction)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "processor_id": processor_id,
        "acceleration_function_id": acceleration_function_id,
    }
    return cast(AccelerationFunction, s.get(**b))


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Processors/{processor_id}/AccelerationFunctions/{acceleration_function_id}",
    response_model_exclude_none=True,
)
@authenticate
async def get3(
    resource_block_id: str,
    computer_system_id: str,
    processor_id: str,
    acceleration_function_id: str,
) -> AccelerationFunction:
    s: Service = find_service(AccelerationFunction)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "processor_id": processor_id,
        "acceleration_function_id": acceleration_function_id,
    }
    return cast(AccelerationFunction, s.get(**b))


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Processors/{processor_id}/AccelerationFunctions/{acceleration_function_id}",
    response_model_exclude_none=True,
)
@authenticate
async def get4(
    resource_block_id: str, processor_id: str, acceleration_function_id: str
) -> AccelerationFunction:
    s: Service = find_service(AccelerationFunction)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "processor_id": processor_id,
        "acceleration_function_id": acceleration_function_id,
    }
    return cast(AccelerationFunction, s.get(**b))


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Processors/{processor_id}/AccelerationFunctions/{acceleration_function_id}",
    response_model_exclude_none=True,
)
@authenticate
async def get5(
    resource_block_id: str,
    computer_system_id: str,
    processor_id: str,
    acceleration_function_id: str,
) -> AccelerationFunction:
    s: Service = find_service(AccelerationFunction)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "processor_id": processor_id,
        "acceleration_function_id": acceleration_function_id,
    }
    return cast(AccelerationFunction, s.get(**b))
