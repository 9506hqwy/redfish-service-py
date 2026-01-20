from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.redfish_error import RedfishError
from ..model.storage_controller import (
    AttachNamespacesRequest,
    DetachNamespacesRequest,
    ResetRequest,
    SecurityReceiveRequest,
    SecuritySendRequest,
    StorageController,
    StorageControllerOnUpdate,
)
from ..service import Service
from ..util import get_service, set_link_header

router = APIRouter()


@router.get(
    "/redfish/v1/Storage/{storage_id}/Controllers/{storage_controller_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Storage/{storage_id}/Controllers/{storage_controller_id}",
    response_model_exclude_none=True,
)
async def get1(
    storage_id: str, storage_controller_id: str, request: Request, response: Response
) -> StorageController:
    s: Service = get_service(StorageController, request)
    b: dict[str, Any] = {
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
        "request": request,
        "response": response,
    }
    m = cast(StorageController, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/Storage/{storage_id}/Controllers/{storage_controller_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch1(
    storage_id: str,
    storage_controller_id: str,
    request: Request,
    response: Response,
    body: StorageControllerOnUpdate,
) -> StorageController:
    s: Service = get_service(StorageController, request)
    b: dict[str, Any] = {
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(StorageController, s.patch(**b))


@router.post(
    "/redfish/v1/Storage/{storage_id}/Controllers/{storage_controller_id}/Actions/StorageController.AttachNamespaces",
    response_model_exclude_none=True,
)
@authenticate
async def attach_namespaces1(
    storage_id: str,
    storage_controller_id: str,
    request: Request,
    response: Response,
    body: AttachNamespacesRequest,
) -> RedfishError:
    s: Service = get_service(StorageController, request)
    b: dict[str, Any] = {
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "AttachNamespaces",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Storage/{storage_id}/Controllers/{storage_controller_id}/Actions/StorageController.DetachNamespaces",
    response_model_exclude_none=True,
)
@authenticate
async def detach_namespaces1(
    storage_id: str,
    storage_controller_id: str,
    request: Request,
    response: Response,
    body: DetachNamespacesRequest,
) -> RedfishError:
    s: Service = get_service(StorageController, request)
    b: dict[str, Any] = {
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "DetachNamespaces",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Storage/{storage_id}/Controllers/{storage_controller_id}/Actions/StorageController.Reset",
    response_model_exclude_none=True,
)
@authenticate
async def reset1(
    storage_id: str,
    storage_controller_id: str,
    request: Request,
    response: Response,
    body: ResetRequest,
) -> RedfishError:
    s: Service = get_service(StorageController, request)
    b: dict[str, Any] = {
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Reset",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Storage/{storage_id}/Controllers/{storage_controller_id}/Actions/StorageController.SecurityReceive",
    response_model_exclude_none=True,
)
@authenticate
async def security_receive1(
    storage_id: str,
    storage_controller_id: str,
    request: Request,
    response: Response,
    body: SecurityReceiveRequest,
) -> RedfishError:
    s: Service = get_service(StorageController, request)
    b: dict[str, Any] = {
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "SecurityReceive",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Storage/{storage_id}/Controllers/{storage_controller_id}/Actions/StorageController.SecuritySend",
    response_model_exclude_none=True,
)
@authenticate
async def security_send1(
    storage_id: str,
    storage_controller_id: str,
    request: Request,
    response: Response,
    body: SecuritySendRequest,
) -> RedfishError:
    s: Service = get_service(StorageController, request)
    b: dict[str, Any] = {
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "SecuritySend",
    }
    return s.action(**b)


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/Controllers/{storage_controller_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/Controllers/{storage_controller_id}",
    response_model_exclude_none=True,
)
async def get2(
    computer_system_id: str,
    storage_id: str,
    storage_controller_id: str,
    request: Request,
    response: Response,
) -> StorageController:
    s: Service = get_service(StorageController, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
        "request": request,
        "response": response,
    }
    m = cast(StorageController, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/Controllers/{storage_controller_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch2(
    computer_system_id: str,
    storage_id: str,
    storage_controller_id: str,
    request: Request,
    response: Response,
    body: StorageControllerOnUpdate,
) -> StorageController:
    s: Service = get_service(StorageController, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(StorageController, s.patch(**b))


@router.post(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/Controllers/{storage_controller_id}/Actions/StorageController.AttachNamespaces",
    response_model_exclude_none=True,
)
@authenticate
async def attach_namespaces2(
    computer_system_id: str,
    storage_id: str,
    storage_controller_id: str,
    request: Request,
    response: Response,
    body: AttachNamespacesRequest,
) -> RedfishError:
    s: Service = get_service(StorageController, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "AttachNamespaces",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/Controllers/{storage_controller_id}/Actions/StorageController.DetachNamespaces",
    response_model_exclude_none=True,
)
@authenticate
async def detach_namespaces2(
    computer_system_id: str,
    storage_id: str,
    storage_controller_id: str,
    request: Request,
    response: Response,
    body: DetachNamespacesRequest,
) -> RedfishError:
    s: Service = get_service(StorageController, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "DetachNamespaces",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/Controllers/{storage_controller_id}/Actions/StorageController.Reset",
    response_model_exclude_none=True,
)
@authenticate
async def reset2(
    computer_system_id: str,
    storage_id: str,
    storage_controller_id: str,
    request: Request,
    response: Response,
    body: ResetRequest,
) -> RedfishError:
    s: Service = get_service(StorageController, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Reset",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/Controllers/{storage_controller_id}/Actions/StorageController.SecurityReceive",
    response_model_exclude_none=True,
)
@authenticate
async def security_receive2(
    computer_system_id: str,
    storage_id: str,
    storage_controller_id: str,
    request: Request,
    response: Response,
    body: SecurityReceiveRequest,
) -> RedfishError:
    s: Service = get_service(StorageController, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "SecurityReceive",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/Controllers/{storage_controller_id}/Actions/StorageController.SecuritySend",
    response_model_exclude_none=True,
)
@authenticate
async def security_send2(
    computer_system_id: str,
    storage_id: str,
    storage_controller_id: str,
    request: Request,
    response: Response,
    body: SecuritySendRequest,
) -> RedfishError:
    s: Service = get_service(StorageController, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "SecuritySend",
    }
    return s.action(**b)


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Storage/{storage_id}/Controllers/{storage_controller_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Storage/{storage_id}/Controllers/{storage_controller_id}",
    response_model_exclude_none=True,
)
async def get3(
    resource_block_id: str,
    storage_id: str,
    storage_controller_id: str,
    request: Request,
    response: Response,
) -> StorageController:
    s: Service = get_service(StorageController, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
        "request": request,
        "response": response,
    }
    m = cast(StorageController, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Storage/{storage_id}/Controllers/{storage_controller_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch3(
    resource_block_id: str,
    storage_id: str,
    storage_controller_id: str,
    request: Request,
    response: Response,
    body: StorageControllerOnUpdate,
) -> StorageController:
    s: Service = get_service(StorageController, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(StorageController, s.patch(**b))


@router.post(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Storage/{storage_id}/Controllers/{storage_controller_id}/Actions/StorageController.AttachNamespaces",
    response_model_exclude_none=True,
)
@authenticate
async def attach_namespaces3(
    resource_block_id: str,
    storage_id: str,
    storage_controller_id: str,
    request: Request,
    response: Response,
    body: AttachNamespacesRequest,
) -> RedfishError:
    s: Service = get_service(StorageController, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "AttachNamespaces",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Storage/{storage_id}/Controllers/{storage_controller_id}/Actions/StorageController.DetachNamespaces",
    response_model_exclude_none=True,
)
@authenticate
async def detach_namespaces3(
    resource_block_id: str,
    storage_id: str,
    storage_controller_id: str,
    request: Request,
    response: Response,
    body: DetachNamespacesRequest,
) -> RedfishError:
    s: Service = get_service(StorageController, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "DetachNamespaces",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Storage/{storage_id}/Controllers/{storage_controller_id}/Actions/StorageController.Reset",
    response_model_exclude_none=True,
)
@authenticate
async def reset3(
    resource_block_id: str,
    storage_id: str,
    storage_controller_id: str,
    request: Request,
    response: Response,
    body: ResetRequest,
) -> RedfishError:
    s: Service = get_service(StorageController, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Reset",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Storage/{storage_id}/Controllers/{storage_controller_id}/Actions/StorageController.SecurityReceive",
    response_model_exclude_none=True,
)
@authenticate
async def security_receive3(
    resource_block_id: str,
    storage_id: str,
    storage_controller_id: str,
    request: Request,
    response: Response,
    body: SecurityReceiveRequest,
) -> RedfishError:
    s: Service = get_service(StorageController, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "SecurityReceive",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Storage/{storage_id}/Controllers/{storage_controller_id}/Actions/StorageController.SecuritySend",
    response_model_exclude_none=True,
)
@authenticate
async def security_send3(
    resource_block_id: str,
    storage_id: str,
    storage_controller_id: str,
    request: Request,
    response: Response,
    body: SecuritySendRequest,
) -> RedfishError:
    s: Service = get_service(StorageController, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "SecuritySend",
    }
    return s.action(**b)


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Storage/{storage_id}/Controllers/{storage_controller_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Storage/{storage_id}/Controllers/{storage_controller_id}",
    response_model_exclude_none=True,
)
async def get4(
    resource_block_id: str,
    computer_system_id: str,
    storage_id: str,
    storage_controller_id: str,
    request: Request,
    response: Response,
) -> StorageController:
    s: Service = get_service(StorageController, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
        "request": request,
        "response": response,
    }
    m = cast(StorageController, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Storage/{storage_id}/Controllers/{storage_controller_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch4(
    resource_block_id: str,
    computer_system_id: str,
    storage_id: str,
    storage_controller_id: str,
    request: Request,
    response: Response,
    body: StorageControllerOnUpdate,
) -> StorageController:
    s: Service = get_service(StorageController, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(StorageController, s.patch(**b))


@router.post(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Storage/{storage_id}/Controllers/{storage_controller_id}/Actions/StorageController.AttachNamespaces",
    response_model_exclude_none=True,
)
@authenticate
async def attach_namespaces4(
    resource_block_id: str,
    computer_system_id: str,
    storage_id: str,
    storage_controller_id: str,
    request: Request,
    response: Response,
    body: AttachNamespacesRequest,
) -> RedfishError:
    s: Service = get_service(StorageController, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "AttachNamespaces",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Storage/{storage_id}/Controllers/{storage_controller_id}/Actions/StorageController.DetachNamespaces",
    response_model_exclude_none=True,
)
@authenticate
async def detach_namespaces4(
    resource_block_id: str,
    computer_system_id: str,
    storage_id: str,
    storage_controller_id: str,
    request: Request,
    response: Response,
    body: DetachNamespacesRequest,
) -> RedfishError:
    s: Service = get_service(StorageController, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "DetachNamespaces",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Storage/{storage_id}/Controllers/{storage_controller_id}/Actions/StorageController.Reset",
    response_model_exclude_none=True,
)
@authenticate
async def reset4(
    resource_block_id: str,
    computer_system_id: str,
    storage_id: str,
    storage_controller_id: str,
    request: Request,
    response: Response,
    body: ResetRequest,
) -> RedfishError:
    s: Service = get_service(StorageController, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Reset",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Storage/{storage_id}/Controllers/{storage_controller_id}/Actions/StorageController.SecurityReceive",
    response_model_exclude_none=True,
)
@authenticate
async def security_receive4(
    resource_block_id: str,
    computer_system_id: str,
    storage_id: str,
    storage_controller_id: str,
    request: Request,
    response: Response,
    body: SecurityReceiveRequest,
) -> RedfishError:
    s: Service = get_service(StorageController, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "SecurityReceive",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Storage/{storage_id}/Controllers/{storage_controller_id}/Actions/StorageController.SecuritySend",
    response_model_exclude_none=True,
)
@authenticate
async def security_send4(
    resource_block_id: str,
    computer_system_id: str,
    storage_id: str,
    storage_controller_id: str,
    request: Request,
    response: Response,
    body: SecuritySendRequest,
) -> RedfishError:
    s: Service = get_service(StorageController, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "SecuritySend",
    }
    return s.action(**b)


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Storage/{storage_id}/Controllers/{storage_controller_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Storage/{storage_id}/Controllers/{storage_controller_id}",
    response_model_exclude_none=True,
)
async def get5(
    resource_block_id: str,
    storage_id: str,
    storage_controller_id: str,
    request: Request,
    response: Response,
) -> StorageController:
    s: Service = get_service(StorageController, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
        "request": request,
        "response": response,
    }
    m = cast(StorageController, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Storage/{storage_id}/Controllers/{storage_controller_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch5(
    resource_block_id: str,
    storage_id: str,
    storage_controller_id: str,
    request: Request,
    response: Response,
    body: StorageControllerOnUpdate,
) -> StorageController:
    s: Service = get_service(StorageController, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(StorageController, s.patch(**b))


@router.post(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Storage/{storage_id}/Controllers/{storage_controller_id}/Actions/StorageController.AttachNamespaces",
    response_model_exclude_none=True,
)
@authenticate
async def attach_namespaces5(
    resource_block_id: str,
    storage_id: str,
    storage_controller_id: str,
    request: Request,
    response: Response,
    body: AttachNamespacesRequest,
) -> RedfishError:
    s: Service = get_service(StorageController, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "AttachNamespaces",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Storage/{storage_id}/Controllers/{storage_controller_id}/Actions/StorageController.DetachNamespaces",
    response_model_exclude_none=True,
)
@authenticate
async def detach_namespaces5(
    resource_block_id: str,
    storage_id: str,
    storage_controller_id: str,
    request: Request,
    response: Response,
    body: DetachNamespacesRequest,
) -> RedfishError:
    s: Service = get_service(StorageController, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "DetachNamespaces",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Storage/{storage_id}/Controllers/{storage_controller_id}/Actions/StorageController.Reset",
    response_model_exclude_none=True,
)
@authenticate
async def reset5(
    resource_block_id: str,
    storage_id: str,
    storage_controller_id: str,
    request: Request,
    response: Response,
    body: ResetRequest,
) -> RedfishError:
    s: Service = get_service(StorageController, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Reset",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Storage/{storage_id}/Controllers/{storage_controller_id}/Actions/StorageController.SecurityReceive",
    response_model_exclude_none=True,
)
@authenticate
async def security_receive5(
    resource_block_id: str,
    storage_id: str,
    storage_controller_id: str,
    request: Request,
    response: Response,
    body: SecurityReceiveRequest,
) -> RedfishError:
    s: Service = get_service(StorageController, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "SecurityReceive",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Storage/{storage_id}/Controllers/{storage_controller_id}/Actions/StorageController.SecuritySend",
    response_model_exclude_none=True,
)
@authenticate
async def security_send5(
    resource_block_id: str,
    storage_id: str,
    storage_controller_id: str,
    request: Request,
    response: Response,
    body: SecuritySendRequest,
) -> RedfishError:
    s: Service = get_service(StorageController, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "SecuritySend",
    }
    return s.action(**b)


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Storage/{storage_id}/Controllers/{storage_controller_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Storage/{storage_id}/Controllers/{storage_controller_id}",
    response_model_exclude_none=True,
)
async def get6(
    resource_block_id: str,
    computer_system_id: str,
    storage_id: str,
    storage_controller_id: str,
    request: Request,
    response: Response,
) -> StorageController:
    s: Service = get_service(StorageController, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
        "request": request,
        "response": response,
    }
    m = cast(StorageController, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Storage/{storage_id}/Controllers/{storage_controller_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch6(
    resource_block_id: str,
    computer_system_id: str,
    storage_id: str,
    storage_controller_id: str,
    request: Request,
    response: Response,
    body: StorageControllerOnUpdate,
) -> StorageController:
    s: Service = get_service(StorageController, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(StorageController, s.patch(**b))


@router.post(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Storage/{storage_id}/Controllers/{storage_controller_id}/Actions/StorageController.AttachNamespaces",
    response_model_exclude_none=True,
)
@authenticate
async def attach_namespaces6(
    resource_block_id: str,
    computer_system_id: str,
    storage_id: str,
    storage_controller_id: str,
    request: Request,
    response: Response,
    body: AttachNamespacesRequest,
) -> RedfishError:
    s: Service = get_service(StorageController, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "AttachNamespaces",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Storage/{storage_id}/Controllers/{storage_controller_id}/Actions/StorageController.DetachNamespaces",
    response_model_exclude_none=True,
)
@authenticate
async def detach_namespaces6(
    resource_block_id: str,
    computer_system_id: str,
    storage_id: str,
    storage_controller_id: str,
    request: Request,
    response: Response,
    body: DetachNamespacesRequest,
) -> RedfishError:
    s: Service = get_service(StorageController, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "DetachNamespaces",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Storage/{storage_id}/Controllers/{storage_controller_id}/Actions/StorageController.Reset",
    response_model_exclude_none=True,
)
@authenticate
async def reset6(
    resource_block_id: str,
    computer_system_id: str,
    storage_id: str,
    storage_controller_id: str,
    request: Request,
    response: Response,
    body: ResetRequest,
) -> RedfishError:
    s: Service = get_service(StorageController, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Reset",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Storage/{storage_id}/Controllers/{storage_controller_id}/Actions/StorageController.SecurityReceive",
    response_model_exclude_none=True,
)
@authenticate
async def security_receive6(
    resource_block_id: str,
    computer_system_id: str,
    storage_id: str,
    storage_controller_id: str,
    request: Request,
    response: Response,
    body: SecurityReceiveRequest,
) -> RedfishError:
    s: Service = get_service(StorageController, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "SecurityReceive",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Storage/{storage_id}/Controllers/{storage_controller_id}/Actions/StorageController.SecuritySend",
    response_model_exclude_none=True,
)
@authenticate
async def security_send6(
    resource_block_id: str,
    computer_system_id: str,
    storage_id: str,
    storage_controller_id: str,
    request: Request,
    response: Response,
    body: SecuritySendRequest,
) -> RedfishError:
    s: Service = get_service(StorageController, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "SecuritySend",
    }
    return s.action(**b)
