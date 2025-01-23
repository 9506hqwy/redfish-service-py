from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.drive import (
    Drive,
    DriveOnUpdate,
    ResetRequest,
    RevertToOriginalFactoryStateRequest,
    SecureEraseRequest,
)
from ..model.redfish_error import RedfishError
from ..service import Service
from ..util import get_service, set_link_header

router = APIRouter()


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/Drives/{drive_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/Drives/{drive_id}",
    response_model_exclude_none=True,
)
async def get1(
    computer_system_id: str, storage_id: str, drive_id: str, request: Request, response: Response
) -> Drive:
    s: Service = get_service(Drive, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "drive_id": drive_id,
        "request": request,
        "response": response,
    }
    m = cast(Drive, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/Drives/{drive_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch1(
    computer_system_id: str,
    storage_id: str,
    drive_id: str,
    request: Request,
    response: Response,
    body: DriveOnUpdate,
) -> Drive:
    s: Service = get_service(Drive, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "drive_id": drive_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Drive, s.patch(**b))


@router.post(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/Drives/{drive_id}/Actions/Drive.Reset",
    response_model_exclude_none=True,
)
@authenticate
async def reset1(
    computer_system_id: str,
    storage_id: str,
    drive_id: str,
    request: Request,
    response: Response,
    body: ResetRequest,
) -> RedfishError:
    s: Service = get_service(Drive, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "drive_id": drive_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Reset",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/Drives/{drive_id}/Actions/Drive.RevertToOriginalFactoryState",
    response_model_exclude_none=True,
)
@authenticate
async def revert_to_original_factory_state1(
    computer_system_id: str,
    storage_id: str,
    drive_id: str,
    request: Request,
    response: Response,
    body: RevertToOriginalFactoryStateRequest,
) -> RedfishError:
    s: Service = get_service(Drive, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "drive_id": drive_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "RevertToOriginalFactoryState",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/Drives/{drive_id}/Actions/Drive.SecureErase",
    response_model_exclude_none=True,
)
@authenticate
async def secure_erase1(
    computer_system_id: str,
    storage_id: str,
    drive_id: str,
    request: Request,
    response: Response,
    body: SecureEraseRequest,
) -> RedfishError:
    s: Service = get_service(Drive, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "drive_id": drive_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "SecureErase",
    }
    return s.action(**b)


@router.get("/redfish/v1/Chassis/{chassis_id}/Drives/{drive_id}", response_model_exclude_none=True)
@router.head(
    "/redfish/v1/Chassis/{chassis_id}/Drives/{drive_id}", response_model_exclude_none=True
)
async def get2(chassis_id: str, drive_id: str, request: Request, response: Response) -> Drive:
    s: Service = get_service(Drive, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "drive_id": drive_id,
        "request": request,
        "response": response,
    }
    m = cast(Drive, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/Chassis/{chassis_id}/Drives/{drive_id}", response_model_exclude_none=True
)
@authenticate
async def patch2(
    chassis_id: str, drive_id: str, request: Request, response: Response, body: DriveOnUpdate
) -> Drive:
    s: Service = get_service(Drive, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "drive_id": drive_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Drive, s.patch(**b))


@router.post(
    "/redfish/v1/Chassis/{chassis_id}/Drives/{drive_id}/Actions/Drive.Reset",
    response_model_exclude_none=True,
)
@authenticate
async def reset2(
    chassis_id: str, drive_id: str, request: Request, response: Response, body: ResetRequest
) -> RedfishError:
    s: Service = get_service(Drive, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "drive_id": drive_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Reset",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Chassis/{chassis_id}/Drives/{drive_id}/Actions/Drive.RevertToOriginalFactoryState",
    response_model_exclude_none=True,
)
@authenticate
async def revert_to_original_factory_state2(
    chassis_id: str,
    drive_id: str,
    request: Request,
    response: Response,
    body: RevertToOriginalFactoryStateRequest,
) -> RedfishError:
    s: Service = get_service(Drive, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "drive_id": drive_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "RevertToOriginalFactoryState",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Chassis/{chassis_id}/Drives/{drive_id}/Actions/Drive.SecureErase",
    response_model_exclude_none=True,
)
@authenticate
async def secure_erase2(
    chassis_id: str, drive_id: str, request: Request, response: Response, body: SecureEraseRequest
) -> RedfishError:
    s: Service = get_service(Drive, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "drive_id": drive_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "SecureErase",
    }
    return s.action(**b)


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Storage/{storage_id}/Drives/{drive_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Storage/{storage_id}/Drives/{drive_id}",
    response_model_exclude_none=True,
)
async def get3(
    resource_block_id: str, storage_id: str, drive_id: str, request: Request, response: Response
) -> Drive:
    s: Service = get_service(Drive, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "storage_id": storage_id,
        "drive_id": drive_id,
        "request": request,
        "response": response,
    }
    m = cast(Drive, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Storage/{storage_id}/Drives/{drive_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch3(
    resource_block_id: str,
    storage_id: str,
    drive_id: str,
    request: Request,
    response: Response,
    body: DriveOnUpdate,
) -> Drive:
    s: Service = get_service(Drive, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "storage_id": storage_id,
        "drive_id": drive_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Drive, s.patch(**b))


@router.post(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Storage/{storage_id}/Drives/{drive_id}/Actions/Drive.Reset",
    response_model_exclude_none=True,
)
@authenticate
async def reset3(
    resource_block_id: str,
    storage_id: str,
    drive_id: str,
    request: Request,
    response: Response,
    body: ResetRequest,
) -> RedfishError:
    s: Service = get_service(Drive, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "storage_id": storage_id,
        "drive_id": drive_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Reset",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Storage/{storage_id}/Drives/{drive_id}/Actions/Drive.RevertToOriginalFactoryState",
    response_model_exclude_none=True,
)
@authenticate
async def revert_to_original_factory_state3(
    resource_block_id: str,
    storage_id: str,
    drive_id: str,
    request: Request,
    response: Response,
    body: RevertToOriginalFactoryStateRequest,
) -> RedfishError:
    s: Service = get_service(Drive, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "storage_id": storage_id,
        "drive_id": drive_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "RevertToOriginalFactoryState",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Storage/{storage_id}/Drives/{drive_id}/Actions/Drive.SecureErase",
    response_model_exclude_none=True,
)
@authenticate
async def secure_erase3(
    resource_block_id: str,
    storage_id: str,
    drive_id: str,
    request: Request,
    response: Response,
    body: SecureEraseRequest,
) -> RedfishError:
    s: Service = get_service(Drive, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "storage_id": storage_id,
        "drive_id": drive_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "SecureErase",
    }
    return s.action(**b)


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Drives/{drive_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Drives/{drive_id}",
    response_model_exclude_none=True,
)
async def get4(
    resource_block_id: str, drive_id: str, request: Request, response: Response
) -> Drive:
    s: Service = get_service(Drive, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "drive_id": drive_id,
        "request": request,
        "response": response,
    }
    m = cast(Drive, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Drives/{drive_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch4(
    resource_block_id: str,
    drive_id: str,
    request: Request,
    response: Response,
    body: DriveOnUpdate,
) -> Drive:
    s: Service = get_service(Drive, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "drive_id": drive_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Drive, s.patch(**b))


@router.post(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Drives/{drive_id}/Actions/Drive.Reset",
    response_model_exclude_none=True,
)
@authenticate
async def reset4(
    resource_block_id: str, drive_id: str, request: Request, response: Response, body: ResetRequest
) -> RedfishError:
    s: Service = get_service(Drive, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "drive_id": drive_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Reset",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Drives/{drive_id}/Actions/Drive.RevertToOriginalFactoryState",
    response_model_exclude_none=True,
)
@authenticate
async def revert_to_original_factory_state4(
    resource_block_id: str,
    drive_id: str,
    request: Request,
    response: Response,
    body: RevertToOriginalFactoryStateRequest,
) -> RedfishError:
    s: Service = get_service(Drive, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "drive_id": drive_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "RevertToOriginalFactoryState",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Drives/{drive_id}/Actions/Drive.SecureErase",
    response_model_exclude_none=True,
)
@authenticate
async def secure_erase4(
    resource_block_id: str,
    drive_id: str,
    request: Request,
    response: Response,
    body: SecureEraseRequest,
) -> RedfishError:
    s: Service = get_service(Drive, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "drive_id": drive_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "SecureErase",
    }
    return s.action(**b)


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Storage/{storage_id}/Drives/{drive_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Storage/{storage_id}/Drives/{drive_id}",
    response_model_exclude_none=True,
)
async def get5(
    resource_block_id: str,
    computer_system_id: str,
    storage_id: str,
    drive_id: str,
    request: Request,
    response: Response,
) -> Drive:
    s: Service = get_service(Drive, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "drive_id": drive_id,
        "request": request,
        "response": response,
    }
    m = cast(Drive, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Storage/{storage_id}/Drives/{drive_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch5(
    resource_block_id: str,
    computer_system_id: str,
    storage_id: str,
    drive_id: str,
    request: Request,
    response: Response,
    body: DriveOnUpdate,
) -> Drive:
    s: Service = get_service(Drive, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "drive_id": drive_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Drive, s.patch(**b))


@router.post(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Storage/{storage_id}/Drives/{drive_id}/Actions/Drive.Reset",
    response_model_exclude_none=True,
)
@authenticate
async def reset5(
    resource_block_id: str,
    computer_system_id: str,
    storage_id: str,
    drive_id: str,
    request: Request,
    response: Response,
    body: ResetRequest,
) -> RedfishError:
    s: Service = get_service(Drive, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "drive_id": drive_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Reset",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Storage/{storage_id}/Drives/{drive_id}/Actions/Drive.RevertToOriginalFactoryState",
    response_model_exclude_none=True,
)
@authenticate
async def revert_to_original_factory_state5(
    resource_block_id: str,
    computer_system_id: str,
    storage_id: str,
    drive_id: str,
    request: Request,
    response: Response,
    body: RevertToOriginalFactoryStateRequest,
) -> RedfishError:
    s: Service = get_service(Drive, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "drive_id": drive_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "RevertToOriginalFactoryState",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Storage/{storage_id}/Drives/{drive_id}/Actions/Drive.SecureErase",
    response_model_exclude_none=True,
)
@authenticate
async def secure_erase5(
    resource_block_id: str,
    computer_system_id: str,
    storage_id: str,
    drive_id: str,
    request: Request,
    response: Response,
    body: SecureEraseRequest,
) -> RedfishError:
    s: Service = get_service(Drive, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "drive_id": drive_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "SecureErase",
    }
    return s.action(**b)


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Storage/{storage_id}/Drives/{drive_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Storage/{storage_id}/Drives/{drive_id}",
    response_model_exclude_none=True,
)
async def get6(
    resource_block_id: str, storage_id: str, drive_id: str, request: Request, response: Response
) -> Drive:
    s: Service = get_service(Drive, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "storage_id": storage_id,
        "drive_id": drive_id,
        "request": request,
        "response": response,
    }
    m = cast(Drive, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Storage/{storage_id}/Drives/{drive_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch6(
    resource_block_id: str,
    storage_id: str,
    drive_id: str,
    request: Request,
    response: Response,
    body: DriveOnUpdate,
) -> Drive:
    s: Service = get_service(Drive, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "storage_id": storage_id,
        "drive_id": drive_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Drive, s.patch(**b))


@router.post(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Storage/{storage_id}/Drives/{drive_id}/Actions/Drive.Reset",
    response_model_exclude_none=True,
)
@authenticate
async def reset6(
    resource_block_id: str,
    storage_id: str,
    drive_id: str,
    request: Request,
    response: Response,
    body: ResetRequest,
) -> RedfishError:
    s: Service = get_service(Drive, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "storage_id": storage_id,
        "drive_id": drive_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Reset",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Storage/{storage_id}/Drives/{drive_id}/Actions/Drive.RevertToOriginalFactoryState",
    response_model_exclude_none=True,
)
@authenticate
async def revert_to_original_factory_state6(
    resource_block_id: str,
    storage_id: str,
    drive_id: str,
    request: Request,
    response: Response,
    body: RevertToOriginalFactoryStateRequest,
) -> RedfishError:
    s: Service = get_service(Drive, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "storage_id": storage_id,
        "drive_id": drive_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "RevertToOriginalFactoryState",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Storage/{storage_id}/Drives/{drive_id}/Actions/Drive.SecureErase",
    response_model_exclude_none=True,
)
@authenticate
async def secure_erase6(
    resource_block_id: str,
    storage_id: str,
    drive_id: str,
    request: Request,
    response: Response,
    body: SecureEraseRequest,
) -> RedfishError:
    s: Service = get_service(Drive, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "storage_id": storage_id,
        "drive_id": drive_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "SecureErase",
    }
    return s.action(**b)


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Drives/{drive_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Drives/{drive_id}",
    response_model_exclude_none=True,
)
async def get7(
    resource_block_id: str, drive_id: str, request: Request, response: Response
) -> Drive:
    s: Service = get_service(Drive, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "drive_id": drive_id,
        "request": request,
        "response": response,
    }
    m = cast(Drive, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Drives/{drive_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch7(
    resource_block_id: str,
    drive_id: str,
    request: Request,
    response: Response,
    body: DriveOnUpdate,
) -> Drive:
    s: Service = get_service(Drive, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "drive_id": drive_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Drive, s.patch(**b))


@router.post(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Drives/{drive_id}/Actions/Drive.Reset",
    response_model_exclude_none=True,
)
@authenticate
async def reset7(
    resource_block_id: str, drive_id: str, request: Request, response: Response, body: ResetRequest
) -> RedfishError:
    s: Service = get_service(Drive, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "drive_id": drive_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Reset",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Drives/{drive_id}/Actions/Drive.RevertToOriginalFactoryState",
    response_model_exclude_none=True,
)
@authenticate
async def revert_to_original_factory_state7(
    resource_block_id: str,
    drive_id: str,
    request: Request,
    response: Response,
    body: RevertToOriginalFactoryStateRequest,
) -> RedfishError:
    s: Service = get_service(Drive, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "drive_id": drive_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "RevertToOriginalFactoryState",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Drives/{drive_id}/Actions/Drive.SecureErase",
    response_model_exclude_none=True,
)
@authenticate
async def secure_erase7(
    resource_block_id: str,
    drive_id: str,
    request: Request,
    response: Response,
    body: SecureEraseRequest,
) -> RedfishError:
    s: Service = get_service(Drive, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "drive_id": drive_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "SecureErase",
    }
    return s.action(**b)


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Storage/{storage_id}/Drives/{drive_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Storage/{storage_id}/Drives/{drive_id}",
    response_model_exclude_none=True,
)
async def get8(
    resource_block_id: str,
    computer_system_id: str,
    storage_id: str,
    drive_id: str,
    request: Request,
    response: Response,
) -> Drive:
    s: Service = get_service(Drive, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "drive_id": drive_id,
        "request": request,
        "response": response,
    }
    m = cast(Drive, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Storage/{storage_id}/Drives/{drive_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch8(
    resource_block_id: str,
    computer_system_id: str,
    storage_id: str,
    drive_id: str,
    request: Request,
    response: Response,
    body: DriveOnUpdate,
) -> Drive:
    s: Service = get_service(Drive, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "drive_id": drive_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Drive, s.patch(**b))


@router.post(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Storage/{storage_id}/Drives/{drive_id}/Actions/Drive.Reset",
    response_model_exclude_none=True,
)
@authenticate
async def reset8(
    resource_block_id: str,
    computer_system_id: str,
    storage_id: str,
    drive_id: str,
    request: Request,
    response: Response,
    body: ResetRequest,
) -> RedfishError:
    s: Service = get_service(Drive, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "drive_id": drive_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Reset",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Storage/{storage_id}/Drives/{drive_id}/Actions/Drive.RevertToOriginalFactoryState",
    response_model_exclude_none=True,
)
@authenticate
async def revert_to_original_factory_state8(
    resource_block_id: str,
    computer_system_id: str,
    storage_id: str,
    drive_id: str,
    request: Request,
    response: Response,
    body: RevertToOriginalFactoryStateRequest,
) -> RedfishError:
    s: Service = get_service(Drive, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "drive_id": drive_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "RevertToOriginalFactoryState",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Storage/{storage_id}/Drives/{drive_id}/Actions/Drive.SecureErase",
    response_model_exclude_none=True,
)
@authenticate
async def secure_erase8(
    resource_block_id: str,
    computer_system_id: str,
    storage_id: str,
    drive_id: str,
    request: Request,
    response: Response,
    body: SecureEraseRequest,
) -> RedfishError:
    s: Service = get_service(Drive, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "drive_id": drive_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "SecureErase",
    }
    return s.action(**b)
