from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.log_service import (
    ClearLogRequest,
    CollectDiagnosticDataRequest,
    LogService,
    LogServiceOnUpdate,
    PushDiagnosticDataRequest,
)
from ..model.redfish_error import RedfishError
from ..service import Service
from ..util import get_service, set_link_header

router = APIRouter()


@router.get(
    "/redfish/v1/Managers/{manager_id}/LogServices/{log_service_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Managers/{manager_id}/LogServices/{log_service_id}",
    response_model_exclude_none=True,
)
async def get1(
    manager_id: str, log_service_id: str, request: Request, response: Response
) -> LogService:
    s: Service = get_service(LogService, request)
    b: dict[str, Any] = {
        "manager_id": manager_id,
        "log_service_id": log_service_id,
        "request": request,
        "response": response,
    }
    m = cast(LogService, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/Managers/{manager_id}/LogServices/{log_service_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch1(
    manager_id: str,
    log_service_id: str,
    request: Request,
    response: Response,
    body: LogServiceOnUpdate,
) -> LogService:
    s: Service = get_service(LogService, request)
    b: dict[str, Any] = {
        "manager_id": manager_id,
        "log_service_id": log_service_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(LogService, s.patch(**b))


@router.post(
    "/redfish/v1/Managers/{manager_id}/LogServices/{log_service_id}/Actions/LogService.ClearLog",
    response_model_exclude_none=True,
)
@authenticate
async def clear_log1(
    manager_id: str,
    log_service_id: str,
    request: Request,
    response: Response,
    body: ClearLogRequest,
) -> RedfishError:
    s: Service = get_service(LogService, request)
    b: dict[str, Any] = {
        "manager_id": manager_id,
        "log_service_id": log_service_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "ClearLog",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Managers/{manager_id}/LogServices/{log_service_id}/Actions/LogService.CollectDiagnosticData",
    response_model_exclude_none=True,
)
@authenticate
async def collect_diagnostic_data1(
    manager_id: str,
    log_service_id: str,
    request: Request,
    response: Response,
    body: CollectDiagnosticDataRequest,
) -> RedfishError:
    s: Service = get_service(LogService, request)
    b: dict[str, Any] = {
        "manager_id": manager_id,
        "log_service_id": log_service_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "CollectDiagnosticData",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Managers/{manager_id}/LogServices/{log_service_id}/Actions/LogService.PushDiagnosticData",
    response_model_exclude_none=True,
)
@authenticate
async def push_diagnostic_data1(
    manager_id: str,
    log_service_id: str,
    request: Request,
    response: Response,
    body: PushDiagnosticDataRequest,
) -> RedfishError:
    s: Service = get_service(LogService, request)
    b: dict[str, Any] = {
        "manager_id": manager_id,
        "log_service_id": log_service_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "PushDiagnosticData",
    }
    return s.action(**b)


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/LogServices/{log_service_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Systems/{computer_system_id}/LogServices/{log_service_id}",
    response_model_exclude_none=True,
)
async def get2(
    computer_system_id: str, log_service_id: str, request: Request, response: Response
) -> LogService:
    s: Service = get_service(LogService, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "log_service_id": log_service_id,
        "request": request,
        "response": response,
    }
    m = cast(LogService, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/Systems/{computer_system_id}/LogServices/{log_service_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch2(
    computer_system_id: str,
    log_service_id: str,
    request: Request,
    response: Response,
    body: LogServiceOnUpdate,
) -> LogService:
    s: Service = get_service(LogService, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "log_service_id": log_service_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(LogService, s.patch(**b))


@router.post(
    "/redfish/v1/Systems/{computer_system_id}/LogServices/{log_service_id}/Actions/LogService.ClearLog",
    response_model_exclude_none=True,
)
@authenticate
async def clear_log2(
    computer_system_id: str,
    log_service_id: str,
    request: Request,
    response: Response,
    body: ClearLogRequest,
) -> RedfishError:
    s: Service = get_service(LogService, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "log_service_id": log_service_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "ClearLog",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Systems/{computer_system_id}/LogServices/{log_service_id}/Actions/LogService.CollectDiagnosticData",
    response_model_exclude_none=True,
)
@authenticate
async def collect_diagnostic_data2(
    computer_system_id: str,
    log_service_id: str,
    request: Request,
    response: Response,
    body: CollectDiagnosticDataRequest,
) -> RedfishError:
    s: Service = get_service(LogService, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "log_service_id": log_service_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "CollectDiagnosticData",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Systems/{computer_system_id}/LogServices/{log_service_id}/Actions/LogService.PushDiagnosticData",
    response_model_exclude_none=True,
)
@authenticate
async def push_diagnostic_data2(
    computer_system_id: str,
    log_service_id: str,
    request: Request,
    response: Response,
    body: PushDiagnosticDataRequest,
) -> RedfishError:
    s: Service = get_service(LogService, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "log_service_id": log_service_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "PushDiagnosticData",
    }
    return s.action(**b)


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/LogServices/{log_service_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/LogServices/{log_service_id}",
    response_model_exclude_none=True,
)
async def get3(
    resource_block_id: str,
    computer_system_id: str,
    log_service_id: str,
    request: Request,
    response: Response,
) -> LogService:
    s: Service = get_service(LogService, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "log_service_id": log_service_id,
        "request": request,
        "response": response,
    }
    m = cast(LogService, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/LogServices/{log_service_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch3(
    resource_block_id: str,
    computer_system_id: str,
    log_service_id: str,
    request: Request,
    response: Response,
    body: LogServiceOnUpdate,
) -> LogService:
    s: Service = get_service(LogService, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "log_service_id": log_service_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(LogService, s.patch(**b))


@router.post(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/LogServices/{log_service_id}/Actions/LogService.ClearLog",
    response_model_exclude_none=True,
)
@authenticate
async def clear_log3(
    resource_block_id: str,
    computer_system_id: str,
    log_service_id: str,
    request: Request,
    response: Response,
    body: ClearLogRequest,
) -> RedfishError:
    s: Service = get_service(LogService, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "log_service_id": log_service_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "ClearLog",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/LogServices/{log_service_id}/Actions/LogService.CollectDiagnosticData",
    response_model_exclude_none=True,
)
@authenticate
async def collect_diagnostic_data3(
    resource_block_id: str,
    computer_system_id: str,
    log_service_id: str,
    request: Request,
    response: Response,
    body: CollectDiagnosticDataRequest,
) -> RedfishError:
    s: Service = get_service(LogService, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "log_service_id": log_service_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "CollectDiagnosticData",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/LogServices/{log_service_id}/Actions/LogService.PushDiagnosticData",
    response_model_exclude_none=True,
)
@authenticate
async def push_diagnostic_data3(
    resource_block_id: str,
    computer_system_id: str,
    log_service_id: str,
    request: Request,
    response: Response,
    body: PushDiagnosticDataRequest,
) -> RedfishError:
    s: Service = get_service(LogService, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "log_service_id": log_service_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "PushDiagnosticData",
    }
    return s.action(**b)


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/LogServices/{log_service_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/LogServices/{log_service_id}",
    response_model_exclude_none=True,
)
async def get4(
    resource_block_id: str,
    computer_system_id: str,
    log_service_id: str,
    request: Request,
    response: Response,
) -> LogService:
    s: Service = get_service(LogService, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "log_service_id": log_service_id,
        "request": request,
        "response": response,
    }
    m = cast(LogService, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/LogServices/{log_service_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch4(
    resource_block_id: str,
    computer_system_id: str,
    log_service_id: str,
    request: Request,
    response: Response,
    body: LogServiceOnUpdate,
) -> LogService:
    s: Service = get_service(LogService, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "log_service_id": log_service_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(LogService, s.patch(**b))


@router.post(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/LogServices/{log_service_id}/Actions/LogService.ClearLog",
    response_model_exclude_none=True,
)
@authenticate
async def clear_log4(
    resource_block_id: str,
    computer_system_id: str,
    log_service_id: str,
    request: Request,
    response: Response,
    body: ClearLogRequest,
) -> RedfishError:
    s: Service = get_service(LogService, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "log_service_id": log_service_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "ClearLog",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/LogServices/{log_service_id}/Actions/LogService.CollectDiagnosticData",
    response_model_exclude_none=True,
)
@authenticate
async def collect_diagnostic_data4(
    resource_block_id: str,
    computer_system_id: str,
    log_service_id: str,
    request: Request,
    response: Response,
    body: CollectDiagnosticDataRequest,
) -> RedfishError:
    s: Service = get_service(LogService, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "log_service_id": log_service_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "CollectDiagnosticData",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/LogServices/{log_service_id}/Actions/LogService.PushDiagnosticData",
    response_model_exclude_none=True,
)
@authenticate
async def push_diagnostic_data4(
    resource_block_id: str,
    computer_system_id: str,
    log_service_id: str,
    request: Request,
    response: Response,
    body: PushDiagnosticDataRequest,
) -> RedfishError:
    s: Service = get_service(LogService, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "log_service_id": log_service_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "PushDiagnosticData",
    }
    return s.action(**b)


@router.get(
    "/redfish/v1/Chassis/{chassis_id}/LogServices/{log_service_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Chassis/{chassis_id}/LogServices/{log_service_id}",
    response_model_exclude_none=True,
)
async def get5(
    chassis_id: str, log_service_id: str, request: Request, response: Response
) -> LogService:
    s: Service = get_service(LogService, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "log_service_id": log_service_id,
        "request": request,
        "response": response,
    }
    m = cast(LogService, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/Chassis/{chassis_id}/LogServices/{log_service_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch5(
    chassis_id: str,
    log_service_id: str,
    request: Request,
    response: Response,
    body: LogServiceOnUpdate,
) -> LogService:
    s: Service = get_service(LogService, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "log_service_id": log_service_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(LogService, s.patch(**b))


@router.post(
    "/redfish/v1/Chassis/{chassis_id}/LogServices/{log_service_id}/Actions/LogService.ClearLog",
    response_model_exclude_none=True,
)
@authenticate
async def clear_log5(
    chassis_id: str,
    log_service_id: str,
    request: Request,
    response: Response,
    body: ClearLogRequest,
) -> RedfishError:
    s: Service = get_service(LogService, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "log_service_id": log_service_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "ClearLog",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Chassis/{chassis_id}/LogServices/{log_service_id}/Actions/LogService.CollectDiagnosticData",
    response_model_exclude_none=True,
)
@authenticate
async def collect_diagnostic_data5(
    chassis_id: str,
    log_service_id: str,
    request: Request,
    response: Response,
    body: CollectDiagnosticDataRequest,
) -> RedfishError:
    s: Service = get_service(LogService, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "log_service_id": log_service_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "CollectDiagnosticData",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Chassis/{chassis_id}/LogServices/{log_service_id}/Actions/LogService.PushDiagnosticData",
    response_model_exclude_none=True,
)
@authenticate
async def push_diagnostic_data5(
    chassis_id: str,
    log_service_id: str,
    request: Request,
    response: Response,
    body: PushDiagnosticDataRequest,
) -> RedfishError:
    s: Service = get_service(LogService, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "log_service_id": log_service_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "PushDiagnosticData",
    }
    return s.action(**b)


@router.get("/redfish/v1/JobService/Log", response_model_exclude_none=True)
@router.head("/redfish/v1/JobService/Log", response_model_exclude_none=True)
async def get6(request: Request, response: Response) -> LogService:
    s: Service = get_service(LogService, request)
    b: dict[str, Any] = {"request": request, "response": response}
    m = cast(LogService, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch("/redfish/v1/JobService/Log", response_model_exclude_none=True)
@authenticate
async def patch6(request: Request, response: Response, body: LogServiceOnUpdate) -> LogService:
    s: Service = get_service(LogService, request)
    b: dict[str, Any] = {"request": request, "response": response, "body": body}
    return cast(LogService, s.patch(**b))


@router.post(
    "/redfish/v1/JobService/Log/Actions/LogService.ClearLog", response_model_exclude_none=True
)
@authenticate
async def clear_log6(request: Request, response: Response, body: ClearLogRequest) -> RedfishError:
    s: Service = get_service(LogService, request)
    b: dict[str, Any] = {
        "request": request,
        "response": response,
        "body": body,
        "action": "ClearLog",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/JobService/Log/Actions/LogService.CollectDiagnosticData",
    response_model_exclude_none=True,
)
@authenticate
async def collect_diagnostic_data6(
    request: Request, response: Response, body: CollectDiagnosticDataRequest
) -> RedfishError:
    s: Service = get_service(LogService, request)
    b: dict[str, Any] = {
        "request": request,
        "response": response,
        "body": body,
        "action": "CollectDiagnosticData",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/JobService/Log/Actions/LogService.PushDiagnosticData",
    response_model_exclude_none=True,
)
@authenticate
async def push_diagnostic_data6(
    request: Request, response: Response, body: PushDiagnosticDataRequest
) -> RedfishError:
    s: Service = get_service(LogService, request)
    b: dict[str, Any] = {
        "request": request,
        "response": response,
        "body": body,
        "action": "PushDiagnosticData",
    }
    return s.action(**b)


@router.get("/redfish/v1/TelemetryService/LogService", response_model_exclude_none=True)
@router.head("/redfish/v1/TelemetryService/LogService", response_model_exclude_none=True)
async def get7(request: Request, response: Response) -> LogService:
    s: Service = get_service(LogService, request)
    b: dict[str, Any] = {"request": request, "response": response}
    m = cast(LogService, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch("/redfish/v1/TelemetryService/LogService", response_model_exclude_none=True)
@authenticate
async def patch7(request: Request, response: Response, body: LogServiceOnUpdate) -> LogService:
    s: Service = get_service(LogService, request)
    b: dict[str, Any] = {"request": request, "response": response, "body": body}
    return cast(LogService, s.patch(**b))


@router.post(
    "/redfish/v1/TelemetryService/LogService/Actions/LogService.ClearLog",
    response_model_exclude_none=True,
)
@authenticate
async def clear_log7(request: Request, response: Response, body: ClearLogRequest) -> RedfishError:
    s: Service = get_service(LogService, request)
    b: dict[str, Any] = {
        "request": request,
        "response": response,
        "body": body,
        "action": "ClearLog",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/TelemetryService/LogService/Actions/LogService.CollectDiagnosticData",
    response_model_exclude_none=True,
)
@authenticate
async def collect_diagnostic_data7(
    request: Request, response: Response, body: CollectDiagnosticDataRequest
) -> RedfishError:
    s: Service = get_service(LogService, request)
    b: dict[str, Any] = {
        "request": request,
        "response": response,
        "body": body,
        "action": "CollectDiagnosticData",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/TelemetryService/LogService/Actions/LogService.PushDiagnosticData",
    response_model_exclude_none=True,
)
@authenticate
async def push_diagnostic_data7(
    request: Request, response: Response, body: PushDiagnosticDataRequest
) -> RedfishError:
    s: Service = get_service(LogService, request)
    b: dict[str, Any] = {
        "request": request,
        "response": response,
        "body": body,
        "action": "PushDiagnosticData",
    }
    return s.action(**b)


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/Memory/{memory_id}/DeviceLog",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Systems/{computer_system_id}/Memory/{memory_id}/DeviceLog",
    response_model_exclude_none=True,
)
async def get8(
    computer_system_id: str, memory_id: str, request: Request, response: Response
) -> LogService:
    s: Service = get_service(LogService, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "memory_id": memory_id,
        "request": request,
        "response": response,
    }
    m = cast(LogService, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/Systems/{computer_system_id}/Memory/{memory_id}/DeviceLog",
    response_model_exclude_none=True,
)
@authenticate
async def patch8(
    computer_system_id: str,
    memory_id: str,
    request: Request,
    response: Response,
    body: LogServiceOnUpdate,
) -> LogService:
    s: Service = get_service(LogService, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "memory_id": memory_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(LogService, s.patch(**b))


@router.post(
    "/redfish/v1/Systems/{computer_system_id}/Memory/{memory_id}/DeviceLog/Actions/LogService.ClearLog",
    response_model_exclude_none=True,
)
@authenticate
async def clear_log8(
    computer_system_id: str,
    memory_id: str,
    request: Request,
    response: Response,
    body: ClearLogRequest,
) -> RedfishError:
    s: Service = get_service(LogService, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "memory_id": memory_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "ClearLog",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Systems/{computer_system_id}/Memory/{memory_id}/DeviceLog/Actions/LogService.CollectDiagnosticData",
    response_model_exclude_none=True,
)
@authenticate
async def collect_diagnostic_data8(
    computer_system_id: str,
    memory_id: str,
    request: Request,
    response: Response,
    body: CollectDiagnosticDataRequest,
) -> RedfishError:
    s: Service = get_service(LogService, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "memory_id": memory_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "CollectDiagnosticData",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Systems/{computer_system_id}/Memory/{memory_id}/DeviceLog/Actions/LogService.PushDiagnosticData",
    response_model_exclude_none=True,
)
@authenticate
async def push_diagnostic_data8(
    computer_system_id: str,
    memory_id: str,
    request: Request,
    response: Response,
    body: PushDiagnosticDataRequest,
) -> RedfishError:
    s: Service = get_service(LogService, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "memory_id": memory_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "PushDiagnosticData",
    }
    return s.action(**b)


@router.get(
    "/redfish/v1/Chassis/{chassis_id}/PCIeDevices/{pcie_device_id}/CXLLogicalDevices/{cxl_logical_device_id}/DeviceLog",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Chassis/{chassis_id}/PCIeDevices/{pcie_device_id}/CXLLogicalDevices/{cxl_logical_device_id}/DeviceLog",
    response_model_exclude_none=True,
)
async def get9(
    chassis_id: str,
    pcie_device_id: str,
    cxl_logical_device_id: str,
    request: Request,
    response: Response,
) -> LogService:
    s: Service = get_service(LogService, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "pcie_device_id": pcie_device_id,
        "cxl_logical_device_id": cxl_logical_device_id,
        "request": request,
        "response": response,
    }
    m = cast(LogService, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/Chassis/{chassis_id}/PCIeDevices/{pcie_device_id}/CXLLogicalDevices/{cxl_logical_device_id}/DeviceLog",
    response_model_exclude_none=True,
)
@authenticate
async def patch9(
    chassis_id: str,
    pcie_device_id: str,
    cxl_logical_device_id: str,
    request: Request,
    response: Response,
    body: LogServiceOnUpdate,
) -> LogService:
    s: Service = get_service(LogService, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "pcie_device_id": pcie_device_id,
        "cxl_logical_device_id": cxl_logical_device_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(LogService, s.patch(**b))


@router.post(
    "/redfish/v1/Chassis/{chassis_id}/PCIeDevices/{pcie_device_id}/CXLLogicalDevices/{cxl_logical_device_id}/DeviceLog/Actions/LogService.ClearLog",
    response_model_exclude_none=True,
)
@authenticate
async def clear_log9(
    chassis_id: str,
    pcie_device_id: str,
    cxl_logical_device_id: str,
    request: Request,
    response: Response,
    body: ClearLogRequest,
) -> RedfishError:
    s: Service = get_service(LogService, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "pcie_device_id": pcie_device_id,
        "cxl_logical_device_id": cxl_logical_device_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "ClearLog",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Chassis/{chassis_id}/PCIeDevices/{pcie_device_id}/CXLLogicalDevices/{cxl_logical_device_id}/DeviceLog/Actions/LogService.CollectDiagnosticData",
    response_model_exclude_none=True,
)
@authenticate
async def collect_diagnostic_data9(
    chassis_id: str,
    pcie_device_id: str,
    cxl_logical_device_id: str,
    request: Request,
    response: Response,
    body: CollectDiagnosticDataRequest,
) -> RedfishError:
    s: Service = get_service(LogService, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "pcie_device_id": pcie_device_id,
        "cxl_logical_device_id": cxl_logical_device_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "CollectDiagnosticData",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Chassis/{chassis_id}/PCIeDevices/{pcie_device_id}/CXLLogicalDevices/{cxl_logical_device_id}/DeviceLog/Actions/LogService.PushDiagnosticData",
    response_model_exclude_none=True,
)
@authenticate
async def push_diagnostic_data9(
    chassis_id: str,
    pcie_device_id: str,
    cxl_logical_device_id: str,
    request: Request,
    response: Response,
    body: PushDiagnosticDataRequest,
) -> RedfishError:
    s: Service = get_service(LogService, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "pcie_device_id": pcie_device_id,
        "cxl_logical_device_id": cxl_logical_device_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "PushDiagnosticData",
    }
    return s.action(**b)
