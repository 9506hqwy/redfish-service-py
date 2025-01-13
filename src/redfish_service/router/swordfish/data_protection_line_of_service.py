from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ...authenticate import authenticate
from ...model.redfish_error import RedfishError
from ...model.swordfish.data_protection_line_of_service import (
    CreateReplicasRequest,
    DataProtectionLineOfService,
    DataProtectionLineOfServiceOnUpdate,
)
from ...service import Service
from ...util import get_service

router = APIRouter()


@router.delete(
    "/redfish/v1/StorageServices/{storage_service_id}/LinesOfService/DataProtectionLinesOfService/{data_protection_line_of_service_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete1(
    storage_service_id: str,
    data_protection_line_of_service_id: str,
    request: Request,
    response: Response,
) -> None:
    s: Service = get_service(DataProtectionLineOfService, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "data_protection_line_of_service_id": data_protection_line_of_service_id,
        "request": request,
        "response": response,
    }
    return s.delete(**b)


@router.get(
    "/redfish/v1/StorageServices/{storage_service_id}/LinesOfService/DataProtectionLinesOfService/{data_protection_line_of_service_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/StorageServices/{storage_service_id}/LinesOfService/DataProtectionLinesOfService/{data_protection_line_of_service_id}",
    response_model_exclude_none=True,
)
async def get1(
    storage_service_id: str,
    data_protection_line_of_service_id: str,
    request: Request,
    response: Response,
) -> DataProtectionLineOfService:
    s: Service = get_service(DataProtectionLineOfService, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "data_protection_line_of_service_id": data_protection_line_of_service_id,
        "request": request,
        "response": response,
    }
    return cast(DataProtectionLineOfService, s.get(**b))


@router.patch(
    "/redfish/v1/StorageServices/{storage_service_id}/LinesOfService/DataProtectionLinesOfService/{data_protection_line_of_service_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch1(
    storage_service_id: str,
    data_protection_line_of_service_id: str,
    request: Request,
    response: Response,
    body: DataProtectionLineOfServiceOnUpdate,
) -> DataProtectionLineOfService:
    s: Service = get_service(DataProtectionLineOfService, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "data_protection_line_of_service_id": data_protection_line_of_service_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(DataProtectionLineOfService, s.patch(**b))


@router.post(
    "/redfish/v1/StorageServices/{storage_service_id}/LinesOfService/DataProtectionLinesOfService/{data_protection_line_of_service_id}/Actions/DataProtectionLineOfService.CreateReplicas",
    response_model_exclude_none=True,
)
@authenticate
async def create_replicas1(
    storage_service_id: str,
    data_protection_line_of_service_id: str,
    request: Request,
    response: Response,
    body: CreateReplicasRequest,
) -> RedfishError:
    s: Service = get_service(DataProtectionLineOfService, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "data_protection_line_of_service_id": data_protection_line_of_service_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "CreateReplicas",
    }
    return s.action(**b)


@router.delete(
    "/redfish/v1/StorageServices/{storage_service_id}/ClassesOfService/{class_of_service_id}/DataProtectionLinesOfService/{data_protection_line_of_service_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete2(
    storage_service_id: str,
    class_of_service_id: str,
    data_protection_line_of_service_id: str,
    request: Request,
    response: Response,
) -> None:
    s: Service = get_service(DataProtectionLineOfService, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "class_of_service_id": class_of_service_id,
        "data_protection_line_of_service_id": data_protection_line_of_service_id,
        "request": request,
        "response": response,
    }
    return s.delete(**b)


@router.get(
    "/redfish/v1/StorageServices/{storage_service_id}/ClassesOfService/{class_of_service_id}/DataProtectionLinesOfService/{data_protection_line_of_service_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/StorageServices/{storage_service_id}/ClassesOfService/{class_of_service_id}/DataProtectionLinesOfService/{data_protection_line_of_service_id}",
    response_model_exclude_none=True,
)
async def get2(
    storage_service_id: str,
    class_of_service_id: str,
    data_protection_line_of_service_id: str,
    request: Request,
    response: Response,
) -> DataProtectionLineOfService:
    s: Service = get_service(DataProtectionLineOfService, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "class_of_service_id": class_of_service_id,
        "data_protection_line_of_service_id": data_protection_line_of_service_id,
        "request": request,
        "response": response,
    }
    return cast(DataProtectionLineOfService, s.get(**b))


@router.patch(
    "/redfish/v1/StorageServices/{storage_service_id}/ClassesOfService/{class_of_service_id}/DataProtectionLinesOfService/{data_protection_line_of_service_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch2(
    storage_service_id: str,
    class_of_service_id: str,
    data_protection_line_of_service_id: str,
    request: Request,
    response: Response,
    body: DataProtectionLineOfServiceOnUpdate,
) -> DataProtectionLineOfService:
    s: Service = get_service(DataProtectionLineOfService, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "class_of_service_id": class_of_service_id,
        "data_protection_line_of_service_id": data_protection_line_of_service_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(DataProtectionLineOfService, s.patch(**b))


@router.post(
    "/redfish/v1/StorageServices/{storage_service_id}/ClassesOfService/{class_of_service_id}/DataProtectionLinesOfService/{data_protection_line_of_service_id}/Actions/DataProtectionLineOfService.CreateReplicas",
    response_model_exclude_none=True,
)
@authenticate
async def create_replicas2(
    storage_service_id: str,
    class_of_service_id: str,
    data_protection_line_of_service_id: str,
    request: Request,
    response: Response,
    body: CreateReplicasRequest,
) -> RedfishError:
    s: Service = get_service(DataProtectionLineOfService, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "class_of_service_id": class_of_service_id,
        "data_protection_line_of_service_id": data_protection_line_of_service_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "CreateReplicas",
    }
    return s.action(**b)
