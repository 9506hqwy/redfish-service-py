from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.redfish_error import RedfishError
from ..model.storage import (
    ResetToDefaultsRequest,
    SetControllerPasswordRequest,
    SetEncryptionKeyRequest,
    Storage,
    StorageOnUpdate,
)
from ..service import Service
from ..util import get_service, set_link_header

router = APIRouter()


@router.get("/redfish/v1/Storage/{storage_id}", response_model_exclude_none=True)
@router.head("/redfish/v1/Storage/{storage_id}", response_model_exclude_none=True)
async def get1(storage_id: str, request: Request, response: Response) -> Storage:
    s: Service = get_service(Storage, request)
    b: dict[str, Any] = {"storage_id": storage_id, "request": request, "response": response}
    m = cast(Storage, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch("/redfish/v1/Storage/{storage_id}", response_model_exclude_none=True)
@authenticate
async def patch1(
    storage_id: str, request: Request, response: Response, body: StorageOnUpdate
) -> Storage:
    s: Service = get_service(Storage, request)
    b: dict[str, Any] = {
        "storage_id": storage_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Storage, s.patch(**b))


@router.post(
    "/redfish/v1/Storage/{storage_id}/Actions/Storage.ResetToDefaults",
    response_model_exclude_none=True,
)
@authenticate
async def reset_to_defaults1(
    storage_id: str, request: Request, response: Response, body: ResetToDefaultsRequest
) -> RedfishError:
    s: Service = get_service(Storage, request)
    b: dict[str, Any] = {
        "storage_id": storage_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "ResetToDefaults",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Storage/{storage_id}/Actions/Storage.SetControllerPassword",
    response_model_exclude_none=True,
)
@authenticate
async def set_controller_password1(
    storage_id: str, request: Request, response: Response, body: SetControllerPasswordRequest
) -> RedfishError:
    s: Service = get_service(Storage, request)
    b: dict[str, Any] = {
        "storage_id": storage_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "SetControllerPassword",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Storage/{storage_id}/Actions/Storage.SetEncryptionKey",
    response_model_exclude_none=True,
)
@authenticate
async def set_encryption_key1(
    storage_id: str, request: Request, response: Response, body: SetEncryptionKeyRequest
) -> RedfishError:
    s: Service = get_service(Storage, request)
    b: dict[str, Any] = {
        "storage_id": storage_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "SetEncryptionKey",
    }
    return s.action(**b)


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}",
    response_model_exclude_none=True,
)
async def get2(
    computer_system_id: str, storage_id: str, request: Request, response: Response
) -> Storage:
    s: Service = get_service(Storage, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "request": request,
        "response": response,
    }
    m = cast(Storage, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch2(
    computer_system_id: str,
    storage_id: str,
    request: Request,
    response: Response,
    body: StorageOnUpdate,
) -> Storage:
    s: Service = get_service(Storage, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Storage, s.patch(**b))


@router.post(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/Actions/Storage.ResetToDefaults",
    response_model_exclude_none=True,
)
@authenticate
async def reset_to_defaults2(
    computer_system_id: str,
    storage_id: str,
    request: Request,
    response: Response,
    body: ResetToDefaultsRequest,
) -> RedfishError:
    s: Service = get_service(Storage, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "ResetToDefaults",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/Actions/Storage.SetControllerPassword",
    response_model_exclude_none=True,
)
@authenticate
async def set_controller_password2(
    computer_system_id: str,
    storage_id: str,
    request: Request,
    response: Response,
    body: SetControllerPasswordRequest,
) -> RedfishError:
    s: Service = get_service(Storage, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "SetControllerPassword",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/Actions/Storage.SetEncryptionKey",
    response_model_exclude_none=True,
)
@authenticate
async def set_encryption_key2(
    computer_system_id: str,
    storage_id: str,
    request: Request,
    response: Response,
    body: SetEncryptionKeyRequest,
) -> RedfishError:
    s: Service = get_service(Storage, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "SetEncryptionKey",
    }
    return s.action(**b)


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Storage/{storage_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Storage/{storage_id}",
    response_model_exclude_none=True,
)
async def get3(
    resource_block_id: str, storage_id: str, request: Request, response: Response
) -> Storage:
    s: Service = get_service(Storage, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "storage_id": storage_id,
        "request": request,
        "response": response,
    }
    m = cast(Storage, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Storage/{storage_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch3(
    resource_block_id: str,
    storage_id: str,
    request: Request,
    response: Response,
    body: StorageOnUpdate,
) -> Storage:
    s: Service = get_service(Storage, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "storage_id": storage_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Storage, s.patch(**b))


@router.post(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Storage/{storage_id}/Actions/Storage.ResetToDefaults",
    response_model_exclude_none=True,
)
@authenticate
async def reset_to_defaults3(
    resource_block_id: str,
    storage_id: str,
    request: Request,
    response: Response,
    body: ResetToDefaultsRequest,
) -> RedfishError:
    s: Service = get_service(Storage, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "storage_id": storage_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "ResetToDefaults",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Storage/{storage_id}/Actions/Storage.SetControllerPassword",
    response_model_exclude_none=True,
)
@authenticate
async def set_controller_password3(
    resource_block_id: str,
    storage_id: str,
    request: Request,
    response: Response,
    body: SetControllerPasswordRequest,
) -> RedfishError:
    s: Service = get_service(Storage, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "storage_id": storage_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "SetControllerPassword",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Storage/{storage_id}/Actions/Storage.SetEncryptionKey",
    response_model_exclude_none=True,
)
@authenticate
async def set_encryption_key3(
    resource_block_id: str,
    storage_id: str,
    request: Request,
    response: Response,
    body: SetEncryptionKeyRequest,
) -> RedfishError:
    s: Service = get_service(Storage, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "storage_id": storage_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "SetEncryptionKey",
    }
    return s.action(**b)


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Storage/{storage_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Storage/{storage_id}",
    response_model_exclude_none=True,
)
async def get4(
    resource_block_id: str,
    computer_system_id: str,
    storage_id: str,
    request: Request,
    response: Response,
) -> Storage:
    s: Service = get_service(Storage, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "request": request,
        "response": response,
    }
    m = cast(Storage, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Storage/{storage_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch4(
    resource_block_id: str,
    computer_system_id: str,
    storage_id: str,
    request: Request,
    response: Response,
    body: StorageOnUpdate,
) -> Storage:
    s: Service = get_service(Storage, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Storage, s.patch(**b))


@router.post(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Storage/{storage_id}/Actions/Storage.ResetToDefaults",
    response_model_exclude_none=True,
)
@authenticate
async def reset_to_defaults4(
    resource_block_id: str,
    computer_system_id: str,
    storage_id: str,
    request: Request,
    response: Response,
    body: ResetToDefaultsRequest,
) -> RedfishError:
    s: Service = get_service(Storage, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "ResetToDefaults",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Storage/{storage_id}/Actions/Storage.SetControllerPassword",
    response_model_exclude_none=True,
)
@authenticate
async def set_controller_password4(
    resource_block_id: str,
    computer_system_id: str,
    storage_id: str,
    request: Request,
    response: Response,
    body: SetControllerPasswordRequest,
) -> RedfishError:
    s: Service = get_service(Storage, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "SetControllerPassword",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Storage/{storage_id}/Actions/Storage.SetEncryptionKey",
    response_model_exclude_none=True,
)
@authenticate
async def set_encryption_key4(
    resource_block_id: str,
    computer_system_id: str,
    storage_id: str,
    request: Request,
    response: Response,
    body: SetEncryptionKeyRequest,
) -> RedfishError:
    s: Service = get_service(Storage, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "SetEncryptionKey",
    }
    return s.action(**b)


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Storage/{storage_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Storage/{storage_id}",
    response_model_exclude_none=True,
)
async def get5(
    resource_block_id: str, storage_id: str, request: Request, response: Response
) -> Storage:
    s: Service = get_service(Storage, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "storage_id": storage_id,
        "request": request,
        "response": response,
    }
    m = cast(Storage, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Storage/{storage_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch5(
    resource_block_id: str,
    storage_id: str,
    request: Request,
    response: Response,
    body: StorageOnUpdate,
) -> Storage:
    s: Service = get_service(Storage, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "storage_id": storage_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Storage, s.patch(**b))


@router.post(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Storage/{storage_id}/Actions/Storage.ResetToDefaults",
    response_model_exclude_none=True,
)
@authenticate
async def reset_to_defaults5(
    resource_block_id: str,
    storage_id: str,
    request: Request,
    response: Response,
    body: ResetToDefaultsRequest,
) -> RedfishError:
    s: Service = get_service(Storage, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "storage_id": storage_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "ResetToDefaults",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Storage/{storage_id}/Actions/Storage.SetControllerPassword",
    response_model_exclude_none=True,
)
@authenticate
async def set_controller_password5(
    resource_block_id: str,
    storage_id: str,
    request: Request,
    response: Response,
    body: SetControllerPasswordRequest,
) -> RedfishError:
    s: Service = get_service(Storage, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "storage_id": storage_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "SetControllerPassword",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Storage/{storage_id}/Actions/Storage.SetEncryptionKey",
    response_model_exclude_none=True,
)
@authenticate
async def set_encryption_key5(
    resource_block_id: str,
    storage_id: str,
    request: Request,
    response: Response,
    body: SetEncryptionKeyRequest,
) -> RedfishError:
    s: Service = get_service(Storage, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "storage_id": storage_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "SetEncryptionKey",
    }
    return s.action(**b)


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Storage/{storage_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Storage/{storage_id}",
    response_model_exclude_none=True,
)
async def get6(
    resource_block_id: str,
    computer_system_id: str,
    storage_id: str,
    request: Request,
    response: Response,
) -> Storage:
    s: Service = get_service(Storage, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "request": request,
        "response": response,
    }
    m = cast(Storage, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Storage/{storage_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch6(
    resource_block_id: str,
    computer_system_id: str,
    storage_id: str,
    request: Request,
    response: Response,
    body: StorageOnUpdate,
) -> Storage:
    s: Service = get_service(Storage, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Storage, s.patch(**b))


@router.post(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Storage/{storage_id}/Actions/Storage.ResetToDefaults",
    response_model_exclude_none=True,
)
@authenticate
async def reset_to_defaults6(
    resource_block_id: str,
    computer_system_id: str,
    storage_id: str,
    request: Request,
    response: Response,
    body: ResetToDefaultsRequest,
) -> RedfishError:
    s: Service = get_service(Storage, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "ResetToDefaults",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Storage/{storage_id}/Actions/Storage.SetControllerPassword",
    response_model_exclude_none=True,
)
@authenticate
async def set_controller_password6(
    resource_block_id: str,
    computer_system_id: str,
    storage_id: str,
    request: Request,
    response: Response,
    body: SetControllerPasswordRequest,
) -> RedfishError:
    s: Service = get_service(Storage, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "SetControllerPassword",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Storage/{storage_id}/Actions/Storage.SetEncryptionKey",
    response_model_exclude_none=True,
)
@authenticate
async def set_encryption_key6(
    resource_block_id: str,
    computer_system_id: str,
    storage_id: str,
    request: Request,
    response: Response,
    body: SetEncryptionKeyRequest,
) -> RedfishError:
    s: Service = get_service(Storage, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "SetEncryptionKey",
    }
    return s.action(**b)
