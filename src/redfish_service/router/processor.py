from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.processor import Processor
from ..service import Service, find_service

router = APIRouter()


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/Processors/{processor_id}",
    response_model_exclude_none=True,
)
@authenticate
async def get1(
    computer_system_id: str, processor_id: str, request: Request, response: Response
) -> Processor:
    s: Service = find_service(Processor)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "processor_id": processor_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(Processor, s.get(**b))


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/Processors/{processor_id}/SubProcessors/{processor_id2}",
    response_model_exclude_none=True,
)
@authenticate
async def get2(
    computer_system_id: str,
    processor_id: str,
    processor_id2: str,
    request: Request,
    response: Response,
) -> Processor:
    s: Service = find_service(Processor)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "processor_id": processor_id,
        "processor_id2": processor_id2,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(Processor, s.get(**b))


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/Processors/{processor_id}/SubProcessors/{processor_id2}/SubProcessors/{processor_id3}",
    response_model_exclude_none=True,
)
@authenticate
async def get3(
    computer_system_id: str,
    processor_id: str,
    processor_id2: str,
    processor_id3: str,
    request: Request,
    response: Response,
) -> Processor:
    s: Service = find_service(Processor)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "processor_id": processor_id,
        "processor_id2": processor_id2,
        "processor_id3": processor_id3,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(Processor, s.get(**b))


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Processors/{processor_id}",
    response_model_exclude_none=True,
)
@authenticate
async def get4(
    resource_block_id: str, processor_id: str, request: Request, response: Response
) -> Processor:
    s: Service = find_service(Processor)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "processor_id": processor_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(Processor, s.get(**b))


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Processors/{processor_id}/SubProcessors/{processor_id2}",
    response_model_exclude_none=True,
)
@authenticate
async def get5(
    resource_block_id: str,
    processor_id: str,
    processor_id2: str,
    request: Request,
    response: Response,
) -> Processor:
    s: Service = find_service(Processor)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "processor_id": processor_id,
        "processor_id2": processor_id2,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(Processor, s.get(**b))


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Processors/{processor_id}/SubProcessors/{processor_id2}/SubProcessors/{processor_id3}",
    response_model_exclude_none=True,
)
@authenticate
async def get6(
    resource_block_id: str,
    processor_id: str,
    processor_id2: str,
    processor_id3: str,
    request: Request,
    response: Response,
) -> Processor:
    s: Service = find_service(Processor)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "processor_id": processor_id,
        "processor_id2": processor_id2,
        "processor_id3": processor_id3,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(Processor, s.get(**b))


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Processors/{processor_id}",
    response_model_exclude_none=True,
)
@authenticate
async def get7(
    resource_block_id: str,
    computer_system_id: str,
    processor_id: str,
    request: Request,
    response: Response,
) -> Processor:
    s: Service = find_service(Processor)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "processor_id": processor_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(Processor, s.get(**b))


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Processors/{processor_id}/SubProcessors/{processor_id2}",
    response_model_exclude_none=True,
)
@authenticate
async def get8(
    resource_block_id: str,
    computer_system_id: str,
    processor_id: str,
    processor_id2: str,
    request: Request,
    response: Response,
) -> Processor:
    s: Service = find_service(Processor)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "processor_id": processor_id,
        "processor_id2": processor_id2,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(Processor, s.get(**b))


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Processors/{processor_id}/SubProcessors/{processor_id2}/SubProcessors/{processor_id3}",
    response_model_exclude_none=True,
)
@authenticate
async def get9(
    resource_block_id: str,
    computer_system_id: str,
    processor_id: str,
    processor_id2: str,
    processor_id3: str,
    request: Request,
    response: Response,
) -> Processor:
    s: Service = find_service(Processor)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "processor_id": processor_id,
        "processor_id2": processor_id2,
        "processor_id3": processor_id3,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(Processor, s.get(**b))


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Processors/{processor_id}",
    response_model_exclude_none=True,
)
@authenticate
async def get10(
    resource_block_id: str, processor_id: str, request: Request, response: Response
) -> Processor:
    s: Service = find_service(Processor)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "processor_id": processor_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(Processor, s.get(**b))


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Processors/{processor_id}/SubProcessors/{processor_id2}",
    response_model_exclude_none=True,
)
@authenticate
async def get11(
    resource_block_id: str,
    processor_id: str,
    processor_id2: str,
    request: Request,
    response: Response,
) -> Processor:
    s: Service = find_service(Processor)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "processor_id": processor_id,
        "processor_id2": processor_id2,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(Processor, s.get(**b))


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Processors/{processor_id}/SubProcessors/{processor_id2}/SubProcessors/{processor_id3}",
    response_model_exclude_none=True,
)
@authenticate
async def get12(
    resource_block_id: str,
    processor_id: str,
    processor_id2: str,
    processor_id3: str,
    request: Request,
    response: Response,
) -> Processor:
    s: Service = find_service(Processor)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "processor_id": processor_id,
        "processor_id2": processor_id2,
        "processor_id3": processor_id3,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(Processor, s.get(**b))


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Processors/{processor_id}",
    response_model_exclude_none=True,
)
@authenticate
async def get13(
    resource_block_id: str,
    computer_system_id: str,
    processor_id: str,
    request: Request,
    response: Response,
) -> Processor:
    s: Service = find_service(Processor)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "processor_id": processor_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(Processor, s.get(**b))


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Processors/{processor_id}/SubProcessors/{processor_id2}",
    response_model_exclude_none=True,
)
@authenticate
async def get14(
    resource_block_id: str,
    computer_system_id: str,
    processor_id: str,
    processor_id2: str,
    request: Request,
    response: Response,
) -> Processor:
    s: Service = find_service(Processor)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "processor_id": processor_id,
        "processor_id2": processor_id2,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(Processor, s.get(**b))


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Processors/{processor_id}/SubProcessors/{processor_id2}/SubProcessors/{processor_id3}",
    response_model_exclude_none=True,
)
@authenticate
async def get15(
    resource_block_id: str,
    computer_system_id: str,
    processor_id: str,
    processor_id2: str,
    processor_id3: str,
    request: Request,
    response: Response,
) -> Processor:
    s: Service = find_service(Processor)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "processor_id": processor_id,
        "processor_id2": processor_id2,
        "processor_id3": processor_id3,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(Processor, s.get(**b))


@router.get(
    "/redfish/v1/Chassis/{chassis_id}/NetworkAdapters/{network_adapter_id}/Processors/{processor_id}",
    response_model_exclude_none=True,
)
@authenticate
async def get16(
    chassis_id: str,
    network_adapter_id: str,
    processor_id: str,
    request: Request,
    response: Response,
) -> Processor:
    s: Service = find_service(Processor)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "network_adapter_id": network_adapter_id,
        "processor_id": processor_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(Processor, s.get(**b))


@router.get(
    "/redfish/v1/Chassis/{chassis_id}/NetworkAdapters/{network_adapter_id}/Processors/{processor_id}/SubProcessors/{processor_id2}",
    response_model_exclude_none=True,
)
@authenticate
async def get17(
    chassis_id: str,
    network_adapter_id: str,
    processor_id: str,
    processor_id2: str,
    request: Request,
    response: Response,
) -> Processor:
    s: Service = find_service(Processor)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "network_adapter_id": network_adapter_id,
        "processor_id": processor_id,
        "processor_id2": processor_id2,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(Processor, s.get(**b))


@router.get(
    "/redfish/v1/Chassis/{chassis_id}/NetworkAdapters/{network_adapter_id}/Processors/{processor_id}/SubProcessors/{processor_id2}/SubProcessors/{processor_id3}",
    response_model_exclude_none=True,
)
@authenticate
async def get18(
    chassis_id: str,
    network_adapter_id: str,
    processor_id: str,
    processor_id2: str,
    processor_id3: str,
    request: Request,
    response: Response,
) -> Processor:
    s: Service = find_service(Processor)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "network_adapter_id": network_adapter_id,
        "processor_id": processor_id,
        "processor_id2": processor_id2,
        "processor_id3": processor_id3,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(Processor, s.get(**b))


@router.get(
    "/redfish/v1/Chassis/{chassis_id}/Processors/{processor_id}", response_model_exclude_none=True
)
@authenticate
async def get19(
    chassis_id: str, processor_id: str, request: Request, response: Response
) -> Processor:
    s: Service = find_service(Processor)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "processor_id": processor_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(Processor, s.get(**b))


@router.get(
    "/redfish/v1/Chassis/{chassis_id}/Processors/{processor_id}/SubProcessors/{processor_id2}",
    response_model_exclude_none=True,
)
@authenticate
async def get20(
    chassis_id: str, processor_id: str, processor_id2: str, request: Request, response: Response
) -> Processor:
    s: Service = find_service(Processor)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "processor_id": processor_id,
        "processor_id2": processor_id2,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(Processor, s.get(**b))


@router.get(
    "/redfish/v1/Chassis/{chassis_id}/Processors/{processor_id}/SubProcessors/{processor_id2}/SubProcessors/{processor_id3}",
    response_model_exclude_none=True,
)
@authenticate
async def get21(
    chassis_id: str,
    processor_id: str,
    processor_id2: str,
    processor_id3: str,
    request: Request,
    response: Response,
) -> Processor:
    s: Service = find_service(Processor)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "processor_id": processor_id,
        "processor_id2": processor_id2,
        "processor_id3": processor_id3,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(Processor, s.get(**b))
