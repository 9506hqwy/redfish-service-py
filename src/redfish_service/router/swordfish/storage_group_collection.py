from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ...authenticate import authenticate
from ...model.swordfish.storage_group import StorageGroup, StorageGroupOnCreate
from ...model.swordfish.storage_group_collection import StorageGroupCollection
from ...service import Service, ServiceCollection, find_service, find_service_collection

router = APIRouter()


@router.get(
    "/redfish/v1/StorageServices/{storage_service_id}/StorageGroups",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/StorageServices/{storage_service_id}/StorageGroups",
    response_model_exclude_none=True,
)
async def get1(
    storage_service_id: str, request: Request, response: Response
) -> StorageGroupCollection:
    s: Service = find_service(StorageGroupCollection)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(StorageGroupCollection, s.get(**b))


@router.post(
    "/redfish/v1/StorageServices/{storage_service_id}/StorageGroups",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/StorageServices/{storage_service_id}/StorageGroups/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post1(
    storage_service_id: str, request: Request, response: Response, body: StorageGroupOnCreate
) -> StorageGroup:
    s: ServiceCollection = find_service_collection(StorageGroupCollection)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(StorageGroup, s.post(**b))


@router.get(
    "/redfish/v1/StorageServices/{storage_service_id}/Volumes/{volume_id}/StorageGroups",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/StorageServices/{storage_service_id}/Volumes/{volume_id}/StorageGroups",
    response_model_exclude_none=True,
)
async def get2(
    storage_service_id: str, volume_id: str, request: Request, response: Response
) -> StorageGroupCollection:
    s: Service = find_service(StorageGroupCollection)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(StorageGroupCollection, s.get(**b))


@router.post(
    "/redfish/v1/StorageServices/{storage_service_id}/Volumes/{volume_id}/StorageGroups",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/StorageServices/{storage_service_id}/Volumes/{volume_id}/StorageGroups/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post2(
    storage_service_id: str,
    volume_id: str,
    request: Request,
    response: Response,
    body: StorageGroupOnCreate,
) -> StorageGroup:
    s: ServiceCollection = find_service_collection(StorageGroupCollection)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(StorageGroup, s.post(**b))


@router.get("/redfish/v1/Storage/{storage_id}/StorageGroups", response_model_exclude_none=True)
@router.head("/redfish/v1/Storage/{storage_id}/StorageGroups", response_model_exclude_none=True)
async def get3(storage_id: str, request: Request, response: Response) -> StorageGroupCollection:
    s: Service = find_service(StorageGroupCollection)
    b: dict[str, Any] = {"storage_id": storage_id, "request": request, "response": response}

    response.headers["OData-Version"] = "4.0"

    return cast(StorageGroupCollection, s.get(**b))


@router.post("/redfish/v1/Storage/{storage_id}/StorageGroups", response_model_exclude_none=True)
@router.post(
    "/redfish/v1/Storage/{storage_id}/StorageGroups/Members", response_model_exclude_none=True
)
@authenticate
async def post3(
    storage_id: str, request: Request, response: Response, body: StorageGroupOnCreate
) -> StorageGroup:
    s: ServiceCollection = find_service_collection(StorageGroupCollection)
    b: dict[str, Any] = {
        "storage_id": storage_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(StorageGroup, s.post(**b))


@router.get(
    "/redfish/v1/Storage/{storage_id}/Volumes/{volume_id}/StorageGroups",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Storage/{storage_id}/Volumes/{volume_id}/StorageGroups",
    response_model_exclude_none=True,
)
async def get4(
    storage_id: str, volume_id: str, request: Request, response: Response
) -> StorageGroupCollection:
    s: Service = find_service(StorageGroupCollection)
    b: dict[str, Any] = {
        "storage_id": storage_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(StorageGroupCollection, s.get(**b))


@router.post(
    "/redfish/v1/Storage/{storage_id}/Volumes/{volume_id}/StorageGroups",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/Storage/{storage_id}/Volumes/{volume_id}/StorageGroups/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post4(
    storage_id: str,
    volume_id: str,
    request: Request,
    response: Response,
    body: StorageGroupOnCreate,
) -> StorageGroup:
    s: ServiceCollection = find_service_collection(StorageGroupCollection)
    b: dict[str, Any] = {
        "storage_id": storage_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(StorageGroup, s.post(**b))
