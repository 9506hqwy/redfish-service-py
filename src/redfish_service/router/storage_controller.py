from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.storage_controller import StorageController, StorageControllerOnUpdate
from ..service import Service
from ..util import get_service

router = APIRouter()


@router.get(
    "/redfish/v1/Storage/{storage_id}/Controllers/{controller_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Storage/{storage_id}/Controllers/{controller_id}",
    response_model_exclude_none=True,
)
async def get1(
    storage_id: str, controller_id: str, request: Request, response: Response
) -> StorageController:
    s: Service = get_service(StorageController, request)
    b: dict[str, Any] = {
        "storage_id": storage_id,
        "controller_id": controller_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(StorageController, s.get(**b))


@router.patch(
    "/redfish/v1/Storage/{storage_id}/Controllers/{controller_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch1(
    storage_id: str,
    controller_id: str,
    request: Request,
    response: Response,
    body: StorageControllerOnUpdate,
) -> StorageController:
    s: Service = get_service(StorageController, request)
    b: dict[str, Any] = {
        "storage_id": storage_id,
        "controller_id": controller_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(StorageController, s.patch(**b))


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/Controllers/{controller_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/Controllers/{controller_id}",
    response_model_exclude_none=True,
)
async def get2(
    computer_system_id: str,
    storage_id: str,
    controller_id: str,
    request: Request,
    response: Response,
) -> StorageController:
    s: Service = get_service(StorageController, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "controller_id": controller_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(StorageController, s.get(**b))


@router.patch(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/Controllers/{controller_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch2(
    computer_system_id: str,
    storage_id: str,
    controller_id: str,
    request: Request,
    response: Response,
    body: StorageControllerOnUpdate,
) -> StorageController:
    s: Service = get_service(StorageController, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "controller_id": controller_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(StorageController, s.patch(**b))


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Storage/{storage_id}/Controllers/{controller_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Storage/{storage_id}/Controllers/{controller_id}",
    response_model_exclude_none=True,
)
async def get3(
    resource_block_id: str,
    storage_id: str,
    controller_id: str,
    request: Request,
    response: Response,
) -> StorageController:
    s: Service = get_service(StorageController, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "storage_id": storage_id,
        "controller_id": controller_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(StorageController, s.get(**b))


@router.patch(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Storage/{storage_id}/Controllers/{controller_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch3(
    resource_block_id: str,
    storage_id: str,
    controller_id: str,
    request: Request,
    response: Response,
    body: StorageControllerOnUpdate,
) -> StorageController:
    s: Service = get_service(StorageController, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "storage_id": storage_id,
        "controller_id": controller_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(StorageController, s.patch(**b))


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Storage/{storage_id}/Controllers/{controller_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Storage/{storage_id}/Controllers/{controller_id}",
    response_model_exclude_none=True,
)
async def get4(
    resource_block_id: str,
    computer_system_id: str,
    storage_id: str,
    controller_id: str,
    request: Request,
    response: Response,
) -> StorageController:
    s: Service = get_service(StorageController, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "controller_id": controller_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(StorageController, s.get(**b))


@router.patch(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Storage/{storage_id}/Controllers/{controller_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch4(
    resource_block_id: str,
    computer_system_id: str,
    storage_id: str,
    controller_id: str,
    request: Request,
    response: Response,
    body: StorageControllerOnUpdate,
) -> StorageController:
    s: Service = get_service(StorageController, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "controller_id": controller_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(StorageController, s.patch(**b))


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Storage/{storage_id}/Controllers/{controller_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Storage/{storage_id}/Controllers/{controller_id}",
    response_model_exclude_none=True,
)
async def get5(
    resource_block_id: str,
    storage_id: str,
    controller_id: str,
    request: Request,
    response: Response,
) -> StorageController:
    s: Service = get_service(StorageController, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "storage_id": storage_id,
        "controller_id": controller_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(StorageController, s.get(**b))


@router.patch(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Storage/{storage_id}/Controllers/{controller_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch5(
    resource_block_id: str,
    storage_id: str,
    controller_id: str,
    request: Request,
    response: Response,
    body: StorageControllerOnUpdate,
) -> StorageController:
    s: Service = get_service(StorageController, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "storage_id": storage_id,
        "controller_id": controller_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(StorageController, s.patch(**b))


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Storage/{storage_id}/Controllers/{controller_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Storage/{storage_id}/Controllers/{controller_id}",
    response_model_exclude_none=True,
)
async def get6(
    resource_block_id: str,
    computer_system_id: str,
    storage_id: str,
    controller_id: str,
    request: Request,
    response: Response,
) -> StorageController:
    s: Service = get_service(StorageController, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "controller_id": controller_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(StorageController, s.get(**b))


@router.patch(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Storage/{storage_id}/Controllers/{controller_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch6(
    resource_block_id: str,
    computer_system_id: str,
    storage_id: str,
    controller_id: str,
    request: Request,
    response: Response,
    body: StorageControllerOnUpdate,
) -> StorageController:
    s: Service = get_service(StorageController, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "controller_id": controller_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(StorageController, s.patch(**b))
