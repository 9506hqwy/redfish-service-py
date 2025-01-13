from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.processor import Processor, ProcessorOnUpdate, ResetRequest
from ..model.redfish_error import RedfishError
from ..service import Service
from ..util import get_service

router = APIRouter()


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/Processors/{processor_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Systems/{computer_system_id}/Processors/{processor_id}",
    response_model_exclude_none=True,
)
async def get1(
    computer_system_id: str, processor_id: str, request: Request, response: Response
) -> Processor:
    s: Service = get_service(Processor, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "processor_id": processor_id,
        "request": request,
        "response": response,
    }
    return cast(Processor, s.get(**b))


@router.patch(
    "/redfish/v1/Systems/{computer_system_id}/Processors/{processor_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch1(
    computer_system_id: str,
    processor_id: str,
    request: Request,
    response: Response,
    body: ProcessorOnUpdate,
) -> Processor:
    s: Service = get_service(Processor, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "processor_id": processor_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Processor, s.patch(**b))


@router.post(
    "/redfish/v1/Systems/{computer_system_id}/Processors/{processor_id}/Actions/Processor.Reset",
    response_model_exclude_none=True,
)
@authenticate
async def reset1(
    computer_system_id: str,
    processor_id: str,
    request: Request,
    response: Response,
    body: ResetRequest,
) -> RedfishError:
    s: Service = get_service(Processor, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "processor_id": processor_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Reset",
    }
    return s.action(**b)


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/Processors/{processor_id}/SubProcessors/{processor_id2}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Systems/{computer_system_id}/Processors/{processor_id}/SubProcessors/{processor_id2}",
    response_model_exclude_none=True,
)
async def get2(
    computer_system_id: str,
    processor_id: str,
    processor_id2: str,
    request: Request,
    response: Response,
) -> Processor:
    s: Service = get_service(Processor, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "processor_id": processor_id,
        "processor_id2": processor_id2,
        "request": request,
        "response": response,
    }
    return cast(Processor, s.get(**b))


@router.patch(
    "/redfish/v1/Systems/{computer_system_id}/Processors/{processor_id}/SubProcessors/{processor_id2}",
    response_model_exclude_none=True,
)
@authenticate
async def patch2(
    computer_system_id: str,
    processor_id: str,
    processor_id2: str,
    request: Request,
    response: Response,
    body: ProcessorOnUpdate,
) -> Processor:
    s: Service = get_service(Processor, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "processor_id": processor_id,
        "processor_id2": processor_id2,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Processor, s.patch(**b))


@router.post(
    "/redfish/v1/Systems/{computer_system_id}/Processors/{processor_id}/SubProcessors/{processor_id2}/Actions/Processor.Reset",
    response_model_exclude_none=True,
)
@authenticate
async def reset2(
    computer_system_id: str,
    processor_id: str,
    processor_id2: str,
    request: Request,
    response: Response,
    body: ResetRequest,
) -> RedfishError:
    s: Service = get_service(Processor, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "processor_id": processor_id,
        "processor_id2": processor_id2,
        "request": request,
        "response": response,
        "body": body,
        "action": "Reset",
    }
    return s.action(**b)


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/Processors/{processor_id}/SubProcessors/{processor_id2}/SubProcessors/{processor_id3}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Systems/{computer_system_id}/Processors/{processor_id}/SubProcessors/{processor_id2}/SubProcessors/{processor_id3}",
    response_model_exclude_none=True,
)
async def get3(
    computer_system_id: str,
    processor_id: str,
    processor_id2: str,
    processor_id3: str,
    request: Request,
    response: Response,
) -> Processor:
    s: Service = get_service(Processor, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "processor_id": processor_id,
        "processor_id2": processor_id2,
        "processor_id3": processor_id3,
        "request": request,
        "response": response,
    }
    return cast(Processor, s.get(**b))


@router.patch(
    "/redfish/v1/Systems/{computer_system_id}/Processors/{processor_id}/SubProcessors/{processor_id2}/SubProcessors/{processor_id3}",
    response_model_exclude_none=True,
)
@authenticate
async def patch3(
    computer_system_id: str,
    processor_id: str,
    processor_id2: str,
    processor_id3: str,
    request: Request,
    response: Response,
    body: ProcessorOnUpdate,
) -> Processor:
    s: Service = get_service(Processor, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "processor_id": processor_id,
        "processor_id2": processor_id2,
        "processor_id3": processor_id3,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Processor, s.patch(**b))


@router.post(
    "/redfish/v1/Systems/{computer_system_id}/Processors/{processor_id}/SubProcessors/{processor_id2}/SubProcessors/{processor_id3}/Actions/Processor.Reset",
    response_model_exclude_none=True,
)
@authenticate
async def reset3(
    computer_system_id: str,
    processor_id: str,
    processor_id2: str,
    processor_id3: str,
    request: Request,
    response: Response,
    body: ResetRequest,
) -> RedfishError:
    s: Service = get_service(Processor, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "processor_id": processor_id,
        "processor_id2": processor_id2,
        "processor_id3": processor_id3,
        "request": request,
        "response": response,
        "body": body,
        "action": "Reset",
    }
    return s.action(**b)


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Processors/{processor_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Processors/{processor_id}",
    response_model_exclude_none=True,
)
async def get4(
    resource_block_id: str, processor_id: str, request: Request, response: Response
) -> Processor:
    s: Service = get_service(Processor, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "processor_id": processor_id,
        "request": request,
        "response": response,
    }
    return cast(Processor, s.get(**b))


@router.patch(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Processors/{processor_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch4(
    resource_block_id: str,
    processor_id: str,
    request: Request,
    response: Response,
    body: ProcessorOnUpdate,
) -> Processor:
    s: Service = get_service(Processor, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "processor_id": processor_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Processor, s.patch(**b))


@router.post(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Processors/{processor_id}/Actions/Processor.Reset",
    response_model_exclude_none=True,
)
@authenticate
async def reset4(
    resource_block_id: str,
    processor_id: str,
    request: Request,
    response: Response,
    body: ResetRequest,
) -> RedfishError:
    s: Service = get_service(Processor, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "processor_id": processor_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Reset",
    }
    return s.action(**b)


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Processors/{processor_id}/SubProcessors/{processor_id2}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Processors/{processor_id}/SubProcessors/{processor_id2}",
    response_model_exclude_none=True,
)
async def get5(
    resource_block_id: str,
    processor_id: str,
    processor_id2: str,
    request: Request,
    response: Response,
) -> Processor:
    s: Service = get_service(Processor, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "processor_id": processor_id,
        "processor_id2": processor_id2,
        "request": request,
        "response": response,
    }
    return cast(Processor, s.get(**b))


@router.patch(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Processors/{processor_id}/SubProcessors/{processor_id2}",
    response_model_exclude_none=True,
)
@authenticate
async def patch5(
    resource_block_id: str,
    processor_id: str,
    processor_id2: str,
    request: Request,
    response: Response,
    body: ProcessorOnUpdate,
) -> Processor:
    s: Service = get_service(Processor, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "processor_id": processor_id,
        "processor_id2": processor_id2,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Processor, s.patch(**b))


@router.post(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Processors/{processor_id}/SubProcessors/{processor_id2}/Actions/Processor.Reset",
    response_model_exclude_none=True,
)
@authenticate
async def reset5(
    resource_block_id: str,
    processor_id: str,
    processor_id2: str,
    request: Request,
    response: Response,
    body: ResetRequest,
) -> RedfishError:
    s: Service = get_service(Processor, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "processor_id": processor_id,
        "processor_id2": processor_id2,
        "request": request,
        "response": response,
        "body": body,
        "action": "Reset",
    }
    return s.action(**b)


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Processors/{processor_id}/SubProcessors/{processor_id2}/SubProcessors/{processor_id3}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Processors/{processor_id}/SubProcessors/{processor_id2}/SubProcessors/{processor_id3}",
    response_model_exclude_none=True,
)
async def get6(
    resource_block_id: str,
    processor_id: str,
    processor_id2: str,
    processor_id3: str,
    request: Request,
    response: Response,
) -> Processor:
    s: Service = get_service(Processor, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "processor_id": processor_id,
        "processor_id2": processor_id2,
        "processor_id3": processor_id3,
        "request": request,
        "response": response,
    }
    return cast(Processor, s.get(**b))


@router.patch(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Processors/{processor_id}/SubProcessors/{processor_id2}/SubProcessors/{processor_id3}",
    response_model_exclude_none=True,
)
@authenticate
async def patch6(
    resource_block_id: str,
    processor_id: str,
    processor_id2: str,
    processor_id3: str,
    request: Request,
    response: Response,
    body: ProcessorOnUpdate,
) -> Processor:
    s: Service = get_service(Processor, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "processor_id": processor_id,
        "processor_id2": processor_id2,
        "processor_id3": processor_id3,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Processor, s.patch(**b))


@router.post(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Processors/{processor_id}/SubProcessors/{processor_id2}/SubProcessors/{processor_id3}/Actions/Processor.Reset",
    response_model_exclude_none=True,
)
@authenticate
async def reset6(
    resource_block_id: str,
    processor_id: str,
    processor_id2: str,
    processor_id3: str,
    request: Request,
    response: Response,
    body: ResetRequest,
) -> RedfishError:
    s: Service = get_service(Processor, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "processor_id": processor_id,
        "processor_id2": processor_id2,
        "processor_id3": processor_id3,
        "request": request,
        "response": response,
        "body": body,
        "action": "Reset",
    }
    return s.action(**b)


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Processors/{processor_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Processors/{processor_id}",
    response_model_exclude_none=True,
)
async def get7(
    resource_block_id: str,
    computer_system_id: str,
    processor_id: str,
    request: Request,
    response: Response,
) -> Processor:
    s: Service = get_service(Processor, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "processor_id": processor_id,
        "request": request,
        "response": response,
    }
    return cast(Processor, s.get(**b))


@router.patch(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Processors/{processor_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch7(
    resource_block_id: str,
    computer_system_id: str,
    processor_id: str,
    request: Request,
    response: Response,
    body: ProcessorOnUpdate,
) -> Processor:
    s: Service = get_service(Processor, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "processor_id": processor_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Processor, s.patch(**b))


@router.post(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Processors/{processor_id}/Actions/Processor.Reset",
    response_model_exclude_none=True,
)
@authenticate
async def reset7(
    resource_block_id: str,
    computer_system_id: str,
    processor_id: str,
    request: Request,
    response: Response,
    body: ResetRequest,
) -> RedfishError:
    s: Service = get_service(Processor, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "processor_id": processor_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Reset",
    }
    return s.action(**b)


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Processors/{processor_id}/SubProcessors/{processor_id2}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Processors/{processor_id}/SubProcessors/{processor_id2}",
    response_model_exclude_none=True,
)
async def get8(
    resource_block_id: str,
    computer_system_id: str,
    processor_id: str,
    processor_id2: str,
    request: Request,
    response: Response,
) -> Processor:
    s: Service = get_service(Processor, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "processor_id": processor_id,
        "processor_id2": processor_id2,
        "request": request,
        "response": response,
    }
    return cast(Processor, s.get(**b))


@router.patch(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Processors/{processor_id}/SubProcessors/{processor_id2}",
    response_model_exclude_none=True,
)
@authenticate
async def patch8(
    resource_block_id: str,
    computer_system_id: str,
    processor_id: str,
    processor_id2: str,
    request: Request,
    response: Response,
    body: ProcessorOnUpdate,
) -> Processor:
    s: Service = get_service(Processor, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "processor_id": processor_id,
        "processor_id2": processor_id2,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Processor, s.patch(**b))


@router.post(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Processors/{processor_id}/SubProcessors/{processor_id2}/Actions/Processor.Reset",
    response_model_exclude_none=True,
)
@authenticate
async def reset8(
    resource_block_id: str,
    computer_system_id: str,
    processor_id: str,
    processor_id2: str,
    request: Request,
    response: Response,
    body: ResetRequest,
) -> RedfishError:
    s: Service = get_service(Processor, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "processor_id": processor_id,
        "processor_id2": processor_id2,
        "request": request,
        "response": response,
        "body": body,
        "action": "Reset",
    }
    return s.action(**b)


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Processors/{processor_id}/SubProcessors/{processor_id2}/SubProcessors/{processor_id3}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Processors/{processor_id}/SubProcessors/{processor_id2}/SubProcessors/{processor_id3}",
    response_model_exclude_none=True,
)
async def get9(
    resource_block_id: str,
    computer_system_id: str,
    processor_id: str,
    processor_id2: str,
    processor_id3: str,
    request: Request,
    response: Response,
) -> Processor:
    s: Service = get_service(Processor, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "processor_id": processor_id,
        "processor_id2": processor_id2,
        "processor_id3": processor_id3,
        "request": request,
        "response": response,
    }
    return cast(Processor, s.get(**b))


@router.patch(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Processors/{processor_id}/SubProcessors/{processor_id2}/SubProcessors/{processor_id3}",
    response_model_exclude_none=True,
)
@authenticate
async def patch9(
    resource_block_id: str,
    computer_system_id: str,
    processor_id: str,
    processor_id2: str,
    processor_id3: str,
    request: Request,
    response: Response,
    body: ProcessorOnUpdate,
) -> Processor:
    s: Service = get_service(Processor, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "processor_id": processor_id,
        "processor_id2": processor_id2,
        "processor_id3": processor_id3,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Processor, s.patch(**b))


@router.post(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Processors/{processor_id}/SubProcessors/{processor_id2}/SubProcessors/{processor_id3}/Actions/Processor.Reset",
    response_model_exclude_none=True,
)
@authenticate
async def reset9(
    resource_block_id: str,
    computer_system_id: str,
    processor_id: str,
    processor_id2: str,
    processor_id3: str,
    request: Request,
    response: Response,
    body: ResetRequest,
) -> RedfishError:
    s: Service = get_service(Processor, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "processor_id": processor_id,
        "processor_id2": processor_id2,
        "processor_id3": processor_id3,
        "request": request,
        "response": response,
        "body": body,
        "action": "Reset",
    }
    return s.action(**b)


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Processors/{processor_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Processors/{processor_id}",
    response_model_exclude_none=True,
)
async def get10(
    resource_block_id: str, processor_id: str, request: Request, response: Response
) -> Processor:
    s: Service = get_service(Processor, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "processor_id": processor_id,
        "request": request,
        "response": response,
    }
    return cast(Processor, s.get(**b))


@router.patch(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Processors/{processor_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch10(
    resource_block_id: str,
    processor_id: str,
    request: Request,
    response: Response,
    body: ProcessorOnUpdate,
) -> Processor:
    s: Service = get_service(Processor, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "processor_id": processor_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Processor, s.patch(**b))


@router.post(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Processors/{processor_id}/Actions/Processor.Reset",
    response_model_exclude_none=True,
)
@authenticate
async def reset10(
    resource_block_id: str,
    processor_id: str,
    request: Request,
    response: Response,
    body: ResetRequest,
) -> RedfishError:
    s: Service = get_service(Processor, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "processor_id": processor_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Reset",
    }
    return s.action(**b)


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Processors/{processor_id}/SubProcessors/{processor_id2}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Processors/{processor_id}/SubProcessors/{processor_id2}",
    response_model_exclude_none=True,
)
async def get11(
    resource_block_id: str,
    processor_id: str,
    processor_id2: str,
    request: Request,
    response: Response,
) -> Processor:
    s: Service = get_service(Processor, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "processor_id": processor_id,
        "processor_id2": processor_id2,
        "request": request,
        "response": response,
    }
    return cast(Processor, s.get(**b))


@router.patch(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Processors/{processor_id}/SubProcessors/{processor_id2}",
    response_model_exclude_none=True,
)
@authenticate
async def patch11(
    resource_block_id: str,
    processor_id: str,
    processor_id2: str,
    request: Request,
    response: Response,
    body: ProcessorOnUpdate,
) -> Processor:
    s: Service = get_service(Processor, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "processor_id": processor_id,
        "processor_id2": processor_id2,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Processor, s.patch(**b))


@router.post(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Processors/{processor_id}/SubProcessors/{processor_id2}/Actions/Processor.Reset",
    response_model_exclude_none=True,
)
@authenticate
async def reset11(
    resource_block_id: str,
    processor_id: str,
    processor_id2: str,
    request: Request,
    response: Response,
    body: ResetRequest,
) -> RedfishError:
    s: Service = get_service(Processor, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "processor_id": processor_id,
        "processor_id2": processor_id2,
        "request": request,
        "response": response,
        "body": body,
        "action": "Reset",
    }
    return s.action(**b)


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Processors/{processor_id}/SubProcessors/{processor_id2}/SubProcessors/{processor_id3}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Processors/{processor_id}/SubProcessors/{processor_id2}/SubProcessors/{processor_id3}",
    response_model_exclude_none=True,
)
async def get12(
    resource_block_id: str,
    processor_id: str,
    processor_id2: str,
    processor_id3: str,
    request: Request,
    response: Response,
) -> Processor:
    s: Service = get_service(Processor, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "processor_id": processor_id,
        "processor_id2": processor_id2,
        "processor_id3": processor_id3,
        "request": request,
        "response": response,
    }
    return cast(Processor, s.get(**b))


@router.patch(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Processors/{processor_id}/SubProcessors/{processor_id2}/SubProcessors/{processor_id3}",
    response_model_exclude_none=True,
)
@authenticate
async def patch12(
    resource_block_id: str,
    processor_id: str,
    processor_id2: str,
    processor_id3: str,
    request: Request,
    response: Response,
    body: ProcessorOnUpdate,
) -> Processor:
    s: Service = get_service(Processor, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "processor_id": processor_id,
        "processor_id2": processor_id2,
        "processor_id3": processor_id3,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Processor, s.patch(**b))


@router.post(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Processors/{processor_id}/SubProcessors/{processor_id2}/SubProcessors/{processor_id3}/Actions/Processor.Reset",
    response_model_exclude_none=True,
)
@authenticate
async def reset12(
    resource_block_id: str,
    processor_id: str,
    processor_id2: str,
    processor_id3: str,
    request: Request,
    response: Response,
    body: ResetRequest,
) -> RedfishError:
    s: Service = get_service(Processor, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "processor_id": processor_id,
        "processor_id2": processor_id2,
        "processor_id3": processor_id3,
        "request": request,
        "response": response,
        "body": body,
        "action": "Reset",
    }
    return s.action(**b)


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Processors/{processor_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Processors/{processor_id}",
    response_model_exclude_none=True,
)
async def get13(
    resource_block_id: str,
    computer_system_id: str,
    processor_id: str,
    request: Request,
    response: Response,
) -> Processor:
    s: Service = get_service(Processor, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "processor_id": processor_id,
        "request": request,
        "response": response,
    }
    return cast(Processor, s.get(**b))


@router.patch(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Processors/{processor_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch13(
    resource_block_id: str,
    computer_system_id: str,
    processor_id: str,
    request: Request,
    response: Response,
    body: ProcessorOnUpdate,
) -> Processor:
    s: Service = get_service(Processor, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "processor_id": processor_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Processor, s.patch(**b))


@router.post(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Processors/{processor_id}/Actions/Processor.Reset",
    response_model_exclude_none=True,
)
@authenticate
async def reset13(
    resource_block_id: str,
    computer_system_id: str,
    processor_id: str,
    request: Request,
    response: Response,
    body: ResetRequest,
) -> RedfishError:
    s: Service = get_service(Processor, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "processor_id": processor_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Reset",
    }
    return s.action(**b)


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Processors/{processor_id}/SubProcessors/{processor_id2}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Processors/{processor_id}/SubProcessors/{processor_id2}",
    response_model_exclude_none=True,
)
async def get14(
    resource_block_id: str,
    computer_system_id: str,
    processor_id: str,
    processor_id2: str,
    request: Request,
    response: Response,
) -> Processor:
    s: Service = get_service(Processor, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "processor_id": processor_id,
        "processor_id2": processor_id2,
        "request": request,
        "response": response,
    }
    return cast(Processor, s.get(**b))


@router.patch(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Processors/{processor_id}/SubProcessors/{processor_id2}",
    response_model_exclude_none=True,
)
@authenticate
async def patch14(
    resource_block_id: str,
    computer_system_id: str,
    processor_id: str,
    processor_id2: str,
    request: Request,
    response: Response,
    body: ProcessorOnUpdate,
) -> Processor:
    s: Service = get_service(Processor, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "processor_id": processor_id,
        "processor_id2": processor_id2,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Processor, s.patch(**b))


@router.post(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Processors/{processor_id}/SubProcessors/{processor_id2}/Actions/Processor.Reset",
    response_model_exclude_none=True,
)
@authenticate
async def reset14(
    resource_block_id: str,
    computer_system_id: str,
    processor_id: str,
    processor_id2: str,
    request: Request,
    response: Response,
    body: ResetRequest,
) -> RedfishError:
    s: Service = get_service(Processor, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "processor_id": processor_id,
        "processor_id2": processor_id2,
        "request": request,
        "response": response,
        "body": body,
        "action": "Reset",
    }
    return s.action(**b)


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Processors/{processor_id}/SubProcessors/{processor_id2}/SubProcessors/{processor_id3}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Processors/{processor_id}/SubProcessors/{processor_id2}/SubProcessors/{processor_id3}",
    response_model_exclude_none=True,
)
async def get15(
    resource_block_id: str,
    computer_system_id: str,
    processor_id: str,
    processor_id2: str,
    processor_id3: str,
    request: Request,
    response: Response,
) -> Processor:
    s: Service = get_service(Processor, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "processor_id": processor_id,
        "processor_id2": processor_id2,
        "processor_id3": processor_id3,
        "request": request,
        "response": response,
    }
    return cast(Processor, s.get(**b))


@router.patch(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Processors/{processor_id}/SubProcessors/{processor_id2}/SubProcessors/{processor_id3}",
    response_model_exclude_none=True,
)
@authenticate
async def patch15(
    resource_block_id: str,
    computer_system_id: str,
    processor_id: str,
    processor_id2: str,
    processor_id3: str,
    request: Request,
    response: Response,
    body: ProcessorOnUpdate,
) -> Processor:
    s: Service = get_service(Processor, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "processor_id": processor_id,
        "processor_id2": processor_id2,
        "processor_id3": processor_id3,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Processor, s.patch(**b))


@router.post(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Processors/{processor_id}/SubProcessors/{processor_id2}/SubProcessors/{processor_id3}/Actions/Processor.Reset",
    response_model_exclude_none=True,
)
@authenticate
async def reset15(
    resource_block_id: str,
    computer_system_id: str,
    processor_id: str,
    processor_id2: str,
    processor_id3: str,
    request: Request,
    response: Response,
    body: ResetRequest,
) -> RedfishError:
    s: Service = get_service(Processor, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "processor_id": processor_id,
        "processor_id2": processor_id2,
        "processor_id3": processor_id3,
        "request": request,
        "response": response,
        "body": body,
        "action": "Reset",
    }
    return s.action(**b)


@router.get(
    "/redfish/v1/Chassis/{chassis_id}/NetworkAdapters/{network_adapter_id}/Processors/{processor_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Chassis/{chassis_id}/NetworkAdapters/{network_adapter_id}/Processors/{processor_id}",
    response_model_exclude_none=True,
)
async def get16(
    chassis_id: str,
    network_adapter_id: str,
    processor_id: str,
    request: Request,
    response: Response,
) -> Processor:
    s: Service = get_service(Processor, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "network_adapter_id": network_adapter_id,
        "processor_id": processor_id,
        "request": request,
        "response": response,
    }
    return cast(Processor, s.get(**b))


@router.patch(
    "/redfish/v1/Chassis/{chassis_id}/NetworkAdapters/{network_adapter_id}/Processors/{processor_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch16(
    chassis_id: str,
    network_adapter_id: str,
    processor_id: str,
    request: Request,
    response: Response,
    body: ProcessorOnUpdate,
) -> Processor:
    s: Service = get_service(Processor, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "network_adapter_id": network_adapter_id,
        "processor_id": processor_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Processor, s.patch(**b))


@router.post(
    "/redfish/v1/Chassis/{chassis_id}/NetworkAdapters/{network_adapter_id}/Processors/{processor_id}/Actions/Processor.Reset",
    response_model_exclude_none=True,
)
@authenticate
async def reset16(
    chassis_id: str,
    network_adapter_id: str,
    processor_id: str,
    request: Request,
    response: Response,
    body: ResetRequest,
) -> RedfishError:
    s: Service = get_service(Processor, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "network_adapter_id": network_adapter_id,
        "processor_id": processor_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Reset",
    }
    return s.action(**b)


@router.get(
    "/redfish/v1/Chassis/{chassis_id}/NetworkAdapters/{network_adapter_id}/Processors/{processor_id}/SubProcessors/{processor_id2}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Chassis/{chassis_id}/NetworkAdapters/{network_adapter_id}/Processors/{processor_id}/SubProcessors/{processor_id2}",
    response_model_exclude_none=True,
)
async def get17(
    chassis_id: str,
    network_adapter_id: str,
    processor_id: str,
    processor_id2: str,
    request: Request,
    response: Response,
) -> Processor:
    s: Service = get_service(Processor, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "network_adapter_id": network_adapter_id,
        "processor_id": processor_id,
        "processor_id2": processor_id2,
        "request": request,
        "response": response,
    }
    return cast(Processor, s.get(**b))


@router.patch(
    "/redfish/v1/Chassis/{chassis_id}/NetworkAdapters/{network_adapter_id}/Processors/{processor_id}/SubProcessors/{processor_id2}",
    response_model_exclude_none=True,
)
@authenticate
async def patch17(
    chassis_id: str,
    network_adapter_id: str,
    processor_id: str,
    processor_id2: str,
    request: Request,
    response: Response,
    body: ProcessorOnUpdate,
) -> Processor:
    s: Service = get_service(Processor, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "network_adapter_id": network_adapter_id,
        "processor_id": processor_id,
        "processor_id2": processor_id2,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Processor, s.patch(**b))


@router.post(
    "/redfish/v1/Chassis/{chassis_id}/NetworkAdapters/{network_adapter_id}/Processors/{processor_id}/SubProcessors/{processor_id2}/Actions/Processor.Reset",
    response_model_exclude_none=True,
)
@authenticate
async def reset17(
    chassis_id: str,
    network_adapter_id: str,
    processor_id: str,
    processor_id2: str,
    request: Request,
    response: Response,
    body: ResetRequest,
) -> RedfishError:
    s: Service = get_service(Processor, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "network_adapter_id": network_adapter_id,
        "processor_id": processor_id,
        "processor_id2": processor_id2,
        "request": request,
        "response": response,
        "body": body,
        "action": "Reset",
    }
    return s.action(**b)


@router.get(
    "/redfish/v1/Chassis/{chassis_id}/NetworkAdapters/{network_adapter_id}/Processors/{processor_id}/SubProcessors/{processor_id2}/SubProcessors/{processor_id3}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Chassis/{chassis_id}/NetworkAdapters/{network_adapter_id}/Processors/{processor_id}/SubProcessors/{processor_id2}/SubProcessors/{processor_id3}",
    response_model_exclude_none=True,
)
async def get18(
    chassis_id: str,
    network_adapter_id: str,
    processor_id: str,
    processor_id2: str,
    processor_id3: str,
    request: Request,
    response: Response,
) -> Processor:
    s: Service = get_service(Processor, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "network_adapter_id": network_adapter_id,
        "processor_id": processor_id,
        "processor_id2": processor_id2,
        "processor_id3": processor_id3,
        "request": request,
        "response": response,
    }
    return cast(Processor, s.get(**b))


@router.patch(
    "/redfish/v1/Chassis/{chassis_id}/NetworkAdapters/{network_adapter_id}/Processors/{processor_id}/SubProcessors/{processor_id2}/SubProcessors/{processor_id3}",
    response_model_exclude_none=True,
)
@authenticate
async def patch18(
    chassis_id: str,
    network_adapter_id: str,
    processor_id: str,
    processor_id2: str,
    processor_id3: str,
    request: Request,
    response: Response,
    body: ProcessorOnUpdate,
) -> Processor:
    s: Service = get_service(Processor, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "network_adapter_id": network_adapter_id,
        "processor_id": processor_id,
        "processor_id2": processor_id2,
        "processor_id3": processor_id3,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Processor, s.patch(**b))


@router.post(
    "/redfish/v1/Chassis/{chassis_id}/NetworkAdapters/{network_adapter_id}/Processors/{processor_id}/SubProcessors/{processor_id2}/SubProcessors/{processor_id3}/Actions/Processor.Reset",
    response_model_exclude_none=True,
)
@authenticate
async def reset18(
    chassis_id: str,
    network_adapter_id: str,
    processor_id: str,
    processor_id2: str,
    processor_id3: str,
    request: Request,
    response: Response,
    body: ResetRequest,
) -> RedfishError:
    s: Service = get_service(Processor, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "network_adapter_id": network_adapter_id,
        "processor_id": processor_id,
        "processor_id2": processor_id2,
        "processor_id3": processor_id3,
        "request": request,
        "response": response,
        "body": body,
        "action": "Reset",
    }
    return s.action(**b)


@router.get(
    "/redfish/v1/Chassis/{chassis_id}/Processors/{processor_id}", response_model_exclude_none=True
)
@router.head(
    "/redfish/v1/Chassis/{chassis_id}/Processors/{processor_id}", response_model_exclude_none=True
)
async def get19(
    chassis_id: str, processor_id: str, request: Request, response: Response
) -> Processor:
    s: Service = get_service(Processor, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "processor_id": processor_id,
        "request": request,
        "response": response,
    }
    return cast(Processor, s.get(**b))


@router.patch(
    "/redfish/v1/Chassis/{chassis_id}/Processors/{processor_id}", response_model_exclude_none=True
)
@authenticate
async def patch19(
    chassis_id: str,
    processor_id: str,
    request: Request,
    response: Response,
    body: ProcessorOnUpdate,
) -> Processor:
    s: Service = get_service(Processor, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "processor_id": processor_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Processor, s.patch(**b))


@router.post(
    "/redfish/v1/Chassis/{chassis_id}/Processors/{processor_id}/Actions/Processor.Reset",
    response_model_exclude_none=True,
)
@authenticate
async def reset19(
    chassis_id: str, processor_id: str, request: Request, response: Response, body: ResetRequest
) -> RedfishError:
    s: Service = get_service(Processor, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "processor_id": processor_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Reset",
    }
    return s.action(**b)


@router.get(
    "/redfish/v1/Chassis/{chassis_id}/Processors/{processor_id}/SubProcessors/{processor_id2}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Chassis/{chassis_id}/Processors/{processor_id}/SubProcessors/{processor_id2}",
    response_model_exclude_none=True,
)
async def get20(
    chassis_id: str, processor_id: str, processor_id2: str, request: Request, response: Response
) -> Processor:
    s: Service = get_service(Processor, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "processor_id": processor_id,
        "processor_id2": processor_id2,
        "request": request,
        "response": response,
    }
    return cast(Processor, s.get(**b))


@router.patch(
    "/redfish/v1/Chassis/{chassis_id}/Processors/{processor_id}/SubProcessors/{processor_id2}",
    response_model_exclude_none=True,
)
@authenticate
async def patch20(
    chassis_id: str,
    processor_id: str,
    processor_id2: str,
    request: Request,
    response: Response,
    body: ProcessorOnUpdate,
) -> Processor:
    s: Service = get_service(Processor, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "processor_id": processor_id,
        "processor_id2": processor_id2,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Processor, s.patch(**b))


@router.post(
    "/redfish/v1/Chassis/{chassis_id}/Processors/{processor_id}/SubProcessors/{processor_id2}/Actions/Processor.Reset",
    response_model_exclude_none=True,
)
@authenticate
async def reset20(
    chassis_id: str,
    processor_id: str,
    processor_id2: str,
    request: Request,
    response: Response,
    body: ResetRequest,
) -> RedfishError:
    s: Service = get_service(Processor, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "processor_id": processor_id,
        "processor_id2": processor_id2,
        "request": request,
        "response": response,
        "body": body,
        "action": "Reset",
    }
    return s.action(**b)


@router.get(
    "/redfish/v1/Chassis/{chassis_id}/Processors/{processor_id}/SubProcessors/{processor_id2}/SubProcessors/{processor_id3}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Chassis/{chassis_id}/Processors/{processor_id}/SubProcessors/{processor_id2}/SubProcessors/{processor_id3}",
    response_model_exclude_none=True,
)
async def get21(
    chassis_id: str,
    processor_id: str,
    processor_id2: str,
    processor_id3: str,
    request: Request,
    response: Response,
) -> Processor:
    s: Service = get_service(Processor, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "processor_id": processor_id,
        "processor_id2": processor_id2,
        "processor_id3": processor_id3,
        "request": request,
        "response": response,
    }
    return cast(Processor, s.get(**b))


@router.patch(
    "/redfish/v1/Chassis/{chassis_id}/Processors/{processor_id}/SubProcessors/{processor_id2}/SubProcessors/{processor_id3}",
    response_model_exclude_none=True,
)
@authenticate
async def patch21(
    chassis_id: str,
    processor_id: str,
    processor_id2: str,
    processor_id3: str,
    request: Request,
    response: Response,
    body: ProcessorOnUpdate,
) -> Processor:
    s: Service = get_service(Processor, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "processor_id": processor_id,
        "processor_id2": processor_id2,
        "processor_id3": processor_id3,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Processor, s.patch(**b))


@router.post(
    "/redfish/v1/Chassis/{chassis_id}/Processors/{processor_id}/SubProcessors/{processor_id2}/SubProcessors/{processor_id3}/Actions/Processor.Reset",
    response_model_exclude_none=True,
)
@authenticate
async def reset21(
    chassis_id: str,
    processor_id: str,
    processor_id2: str,
    processor_id3: str,
    request: Request,
    response: Response,
    body: ResetRequest,
) -> RedfishError:
    s: Service = get_service(Processor, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "processor_id": processor_id,
        "processor_id2": processor_id2,
        "processor_id3": processor_id3,
        "request": request,
        "response": response,
        "body": body,
        "action": "Reset",
    }
    return s.action(**b)
