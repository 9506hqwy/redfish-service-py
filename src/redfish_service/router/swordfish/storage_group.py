from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ...authenticate import authenticate
from ...model.swordfish.storage_group import StorageGroup, StorageGroupOnUpdate
from ...service import Service
from ...util import get_service

router = APIRouter()


@router.delete(
    "/redfish/v1/StorageServices/{storage_service_id}/StorageGroups/{storage_group_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete1(
    storage_service_id: str, storage_group_id: str, request: Request, response: Response
) -> None:
    s: Service = get_service(StorageGroup, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "storage_group_id": storage_group_id,
        "request": request,
        "response": response,
    }
    return s.delete(**b)


@router.get(
    "/redfish/v1/StorageServices/{storage_service_id}/StorageGroups/{storage_group_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/StorageServices/{storage_service_id}/StorageGroups/{storage_group_id}",
    response_model_exclude_none=True,
)
async def get1(
    storage_service_id: str, storage_group_id: str, request: Request, response: Response
) -> StorageGroup:
    s: Service = get_service(StorageGroup, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "storage_group_id": storage_group_id,
        "request": request,
        "response": response,
    }
    return cast(StorageGroup, s.get(**b))


@router.patch(
    "/redfish/v1/StorageServices/{storage_service_id}/StorageGroups/{storage_group_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch1(
    storage_service_id: str,
    storage_group_id: str,
    request: Request,
    response: Response,
    body: StorageGroupOnUpdate,
) -> StorageGroup:
    s: Service = get_service(StorageGroup, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "storage_group_id": storage_group_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(StorageGroup, s.patch(**b))


@router.delete(
    "/redfish/v1/StorageServices/{storage_service_id}/Volumes/{volume_id}/StorageGroups/{storage_group_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete2(
    storage_service_id: str,
    volume_id: str,
    storage_group_id: str,
    request: Request,
    response: Response,
) -> None:
    s: Service = get_service(StorageGroup, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "volume_id": volume_id,
        "storage_group_id": storage_group_id,
        "request": request,
        "response": response,
    }
    return s.delete(**b)


@router.get(
    "/redfish/v1/StorageServices/{storage_service_id}/Volumes/{volume_id}/StorageGroups/{storage_group_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/StorageServices/{storage_service_id}/Volumes/{volume_id}/StorageGroups/{storage_group_id}",
    response_model_exclude_none=True,
)
async def get2(
    storage_service_id: str,
    volume_id: str,
    storage_group_id: str,
    request: Request,
    response: Response,
) -> StorageGroup:
    s: Service = get_service(StorageGroup, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "volume_id": volume_id,
        "storage_group_id": storage_group_id,
        "request": request,
        "response": response,
    }
    return cast(StorageGroup, s.get(**b))


@router.patch(
    "/redfish/v1/StorageServices/{storage_service_id}/Volumes/{volume_id}/StorageGroups/{storage_group_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch2(
    storage_service_id: str,
    volume_id: str,
    storage_group_id: str,
    request: Request,
    response: Response,
    body: StorageGroupOnUpdate,
) -> StorageGroup:
    s: Service = get_service(StorageGroup, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "volume_id": volume_id,
        "storage_group_id": storage_group_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(StorageGroup, s.patch(**b))


@router.delete(
    "/redfish/v1/Storage/{storage_id}/StorageGroups/{storage_group_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete3(
    storage_id: str, storage_group_id: str, request: Request, response: Response
) -> None:
    s: Service = get_service(StorageGroup, request)
    b: dict[str, Any] = {
        "storage_id": storage_id,
        "storage_group_id": storage_group_id,
        "request": request,
        "response": response,
    }
    return s.delete(**b)


@router.get(
    "/redfish/v1/Storage/{storage_id}/StorageGroups/{storage_group_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Storage/{storage_id}/StorageGroups/{storage_group_id}",
    response_model_exclude_none=True,
)
async def get3(
    storage_id: str, storage_group_id: str, request: Request, response: Response
) -> StorageGroup:
    s: Service = get_service(StorageGroup, request)
    b: dict[str, Any] = {
        "storage_id": storage_id,
        "storage_group_id": storage_group_id,
        "request": request,
        "response": response,
    }
    return cast(StorageGroup, s.get(**b))


@router.patch(
    "/redfish/v1/Storage/{storage_id}/StorageGroups/{storage_group_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch3(
    storage_id: str,
    storage_group_id: str,
    request: Request,
    response: Response,
    body: StorageGroupOnUpdate,
) -> StorageGroup:
    s: Service = get_service(StorageGroup, request)
    b: dict[str, Any] = {
        "storage_id": storage_id,
        "storage_group_id": storage_group_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(StorageGroup, s.patch(**b))


@router.delete(
    "/redfish/v1/Storage/{storage_id}/Volumes/{volume_id}/StorageGroups/{storage_group_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete4(
    storage_id: str, volume_id: str, storage_group_id: str, request: Request, response: Response
) -> None:
    s: Service = get_service(StorageGroup, request)
    b: dict[str, Any] = {
        "storage_id": storage_id,
        "volume_id": volume_id,
        "storage_group_id": storage_group_id,
        "request": request,
        "response": response,
    }
    return s.delete(**b)


@router.get(
    "/redfish/v1/Storage/{storage_id}/Volumes/{volume_id}/StorageGroups/{storage_group_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Storage/{storage_id}/Volumes/{volume_id}/StorageGroups/{storage_group_id}",
    response_model_exclude_none=True,
)
async def get4(
    storage_id: str, volume_id: str, storage_group_id: str, request: Request, response: Response
) -> StorageGroup:
    s: Service = get_service(StorageGroup, request)
    b: dict[str, Any] = {
        "storage_id": storage_id,
        "volume_id": volume_id,
        "storage_group_id": storage_group_id,
        "request": request,
        "response": response,
    }
    return cast(StorageGroup, s.get(**b))


@router.patch(
    "/redfish/v1/Storage/{storage_id}/Volumes/{volume_id}/StorageGroups/{storage_group_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch4(
    storage_id: str,
    volume_id: str,
    storage_group_id: str,
    request: Request,
    response: Response,
    body: StorageGroupOnUpdate,
) -> StorageGroup:
    s: Service = get_service(StorageGroup, request)
    b: dict[str, Any] = {
        "storage_id": storage_id,
        "volume_id": volume_id,
        "storage_group_id": storage_group_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(StorageGroup, s.patch(**b))
