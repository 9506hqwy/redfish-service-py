from typing import Any, cast

from fastapi import APIRouter

from ..authenticate import authenticate
from ..model.processor_collection import ProcessorCollection
from ..service import Service, find_service

router = APIRouter()


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/Processors", response_model_exclude_none=True
)
@authenticate
async def get1(computer_system_id: str) -> ProcessorCollection:
    s: Service = find_service(ProcessorCollection)
    b: dict[str, Any] = {"computer_system_id": computer_system_id}
    return cast(ProcessorCollection, s.get(**b))


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/Processors/{processor_id}/SubProcessors",
    response_model_exclude_none=True,
)
@authenticate
async def get2(computer_system_id: str, processor_id: str) -> ProcessorCollection:
    s: Service = find_service(ProcessorCollection)
    b: dict[str, Any] = {"computer_system_id": computer_system_id, "processor_id": processor_id}
    return cast(ProcessorCollection, s.get(**b))


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/Processors/{processor_id}/SubProcessors/{processor_id2}/SubProcessors",
    response_model_exclude_none=True,
)
@authenticate
async def get3(
    computer_system_id: str, processor_id: str, processor_id2: str
) -> ProcessorCollection:
    s: Service = find_service(ProcessorCollection)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "processor_id": processor_id,
        "processor_id2": processor_id2,
    }
    return cast(ProcessorCollection, s.get(**b))


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Processors/{processor_id}/SubProcessors",
    response_model_exclude_none=True,
)
@authenticate
async def get4(resource_block_id: str, processor_id: str) -> ProcessorCollection:
    s: Service = find_service(ProcessorCollection)
    b: dict[str, Any] = {"resource_block_id": resource_block_id, "processor_id": processor_id}
    return cast(ProcessorCollection, s.get(**b))


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Processors/{processor_id}/SubProcessors/{processor_id2}/SubProcessors",
    response_model_exclude_none=True,
)
@authenticate
async def get5(
    resource_block_id: str, processor_id: str, processor_id2: str
) -> ProcessorCollection:
    s: Service = find_service(ProcessorCollection)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "processor_id": processor_id,
        "processor_id2": processor_id2,
    }
    return cast(ProcessorCollection, s.get(**b))


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Processors",
    response_model_exclude_none=True,
)
@authenticate
async def get6(resource_block_id: str, computer_system_id: str) -> ProcessorCollection:
    s: Service = find_service(ProcessorCollection)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
    }
    return cast(ProcessorCollection, s.get(**b))


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Processors/{processor_id}/SubProcessors",
    response_model_exclude_none=True,
)
@authenticate
async def get7(
    resource_block_id: str, computer_system_id: str, processor_id: str
) -> ProcessorCollection:
    s: Service = find_service(ProcessorCollection)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "processor_id": processor_id,
    }
    return cast(ProcessorCollection, s.get(**b))


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Processors/{processor_id}/SubProcessors/{processor_id2}/SubProcessors",
    response_model_exclude_none=True,
)
@authenticate
async def get8(
    resource_block_id: str, computer_system_id: str, processor_id: str, processor_id2: str
) -> ProcessorCollection:
    s: Service = find_service(ProcessorCollection)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "processor_id": processor_id,
        "processor_id2": processor_id2,
    }
    return cast(ProcessorCollection, s.get(**b))


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Processors/{processor_id}/SubProcessors",
    response_model_exclude_none=True,
)
@authenticate
async def get9(resource_block_id: str, processor_id: str) -> ProcessorCollection:
    s: Service = find_service(ProcessorCollection)
    b: dict[str, Any] = {"resource_block_id": resource_block_id, "processor_id": processor_id}
    return cast(ProcessorCollection, s.get(**b))


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Processors/{processor_id}/SubProcessors/{processor_id2}/SubProcessors",
    response_model_exclude_none=True,
)
@authenticate
async def get10(
    resource_block_id: str, processor_id: str, processor_id2: str
) -> ProcessorCollection:
    s: Service = find_service(ProcessorCollection)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "processor_id": processor_id,
        "processor_id2": processor_id2,
    }
    return cast(ProcessorCollection, s.get(**b))


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Processors",
    response_model_exclude_none=True,
)
@authenticate
async def get11(resource_block_id: str, computer_system_id: str) -> ProcessorCollection:
    s: Service = find_service(ProcessorCollection)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
    }
    return cast(ProcessorCollection, s.get(**b))


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Processors/{processor_id}/SubProcessors",
    response_model_exclude_none=True,
)
@authenticate
async def get12(
    resource_block_id: str, computer_system_id: str, processor_id: str
) -> ProcessorCollection:
    s: Service = find_service(ProcessorCollection)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "processor_id": processor_id,
    }
    return cast(ProcessorCollection, s.get(**b))


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Processors/{processor_id}/SubProcessors/{processor_id2}/SubProcessors",
    response_model_exclude_none=True,
)
@authenticate
async def get13(
    resource_block_id: str, computer_system_id: str, processor_id: str, processor_id2: str
) -> ProcessorCollection:
    s: Service = find_service(ProcessorCollection)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "processor_id": processor_id,
        "processor_id2": processor_id2,
    }
    return cast(ProcessorCollection, s.get(**b))


@router.get(
    "/redfish/v1/Chassis/{chassis_id}/NetworkAdapters/{network_adapter_id}/Processors",
    response_model_exclude_none=True,
)
@authenticate
async def get14(chassis_id: str, network_adapter_id: str) -> ProcessorCollection:
    s: Service = find_service(ProcessorCollection)
    b: dict[str, Any] = {"chassis_id": chassis_id, "network_adapter_id": network_adapter_id}
    return cast(ProcessorCollection, s.get(**b))


@router.get(
    "/redfish/v1/Chassis/{chassis_id}/NetworkAdapters/{network_adapter_id}/Processors/{processor_id}/SubProcessors",
    response_model_exclude_none=True,
)
@authenticate
async def get15(
    chassis_id: str, network_adapter_id: str, processor_id: str
) -> ProcessorCollection:
    s: Service = find_service(ProcessorCollection)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "network_adapter_id": network_adapter_id,
        "processor_id": processor_id,
    }
    return cast(ProcessorCollection, s.get(**b))


@router.get(
    "/redfish/v1/Chassis/{chassis_id}/NetworkAdapters/{network_adapter_id}/Processors/{processor_id}/SubProcessors/{processor_id2}/SubProcessors",
    response_model_exclude_none=True,
)
@authenticate
async def get16(
    chassis_id: str, network_adapter_id: str, processor_id: str, processor_id2: str
) -> ProcessorCollection:
    s: Service = find_service(ProcessorCollection)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "network_adapter_id": network_adapter_id,
        "processor_id": processor_id,
        "processor_id2": processor_id2,
    }
    return cast(ProcessorCollection, s.get(**b))


@router.get("/redfish/v1/Chassis/{chassis_id}/Processors", response_model_exclude_none=True)
@authenticate
async def get17(chassis_id: str) -> ProcessorCollection:
    s: Service = find_service(ProcessorCollection)
    b: dict[str, Any] = {"chassis_id": chassis_id}
    return cast(ProcessorCollection, s.get(**b))


@router.get(
    "/redfish/v1/Chassis/{chassis_id}/Processors/{processor_id}/SubProcessors",
    response_model_exclude_none=True,
)
@authenticate
async def get18(chassis_id: str, processor_id: str) -> ProcessorCollection:
    s: Service = find_service(ProcessorCollection)
    b: dict[str, Any] = {"chassis_id": chassis_id, "processor_id": processor_id}
    return cast(ProcessorCollection, s.get(**b))


@router.get(
    "/redfish/v1/Chassis/{chassis_id}/Processors/{processor_id}/SubProcessors/{processor_id2}/SubProcessors",
    response_model_exclude_none=True,
)
@authenticate
async def get19(chassis_id: str, processor_id: str, processor_id2: str) -> ProcessorCollection:
    s: Service = find_service(ProcessorCollection)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "processor_id": processor_id,
        "processor_id2": processor_id2,
    }
    return cast(ProcessorCollection, s.get(**b))
