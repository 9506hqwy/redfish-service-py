from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ...authenticate import authenticate
from ...model.swordfish.consistency_group import ConsistencyGroup, ConsistencyGroupOnUpdate
from ...service import Service
from ...util import get_service

router = APIRouter()


@router.delete(
    "/redfish/v1/Storage/{storage_id}/ConsistencyGroups/{consistency_group_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete1(
    storage_id: str, consistency_group_id: str, request: Request, response: Response
) -> None:
    s: Service = get_service(ConsistencyGroup, request)
    b: dict[str, Any] = {
        "storage_id": storage_id,
        "consistency_group_id": consistency_group_id,
        "request": request,
        "response": response,
    }
    return s.delete(**b)


@router.get(
    "/redfish/v1/Storage/{storage_id}/ConsistencyGroups/{consistency_group_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Storage/{storage_id}/ConsistencyGroups/{consistency_group_id}",
    response_model_exclude_none=True,
)
async def get1(
    storage_id: str, consistency_group_id: str, request: Request, response: Response
) -> ConsistencyGroup:
    s: Service = get_service(ConsistencyGroup, request)
    b: dict[str, Any] = {
        "storage_id": storage_id,
        "consistency_group_id": consistency_group_id,
        "request": request,
        "response": response,
    }
    return cast(ConsistencyGroup, s.get(**b))


@router.patch(
    "/redfish/v1/Storage/{storage_id}/ConsistencyGroups/{consistency_group_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch1(
    storage_id: str,
    consistency_group_id: str,
    request: Request,
    response: Response,
    body: ConsistencyGroupOnUpdate,
) -> ConsistencyGroup:
    s: Service = get_service(ConsistencyGroup, request)
    b: dict[str, Any] = {
        "storage_id": storage_id,
        "consistency_group_id": consistency_group_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(ConsistencyGroup, s.patch(**b))


@router.delete(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/ConsistencyGroups/{consistency_group_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete2(
    computer_system_id: str,
    storage_id: str,
    consistency_group_id: str,
    request: Request,
    response: Response,
) -> None:
    s: Service = get_service(ConsistencyGroup, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "consistency_group_id": consistency_group_id,
        "request": request,
        "response": response,
    }
    return s.delete(**b)


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/ConsistencyGroups/{consistency_group_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/ConsistencyGroups/{consistency_group_id}",
    response_model_exclude_none=True,
)
async def get2(
    computer_system_id: str,
    storage_id: str,
    consistency_group_id: str,
    request: Request,
    response: Response,
) -> ConsistencyGroup:
    s: Service = get_service(ConsistencyGroup, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "consistency_group_id": consistency_group_id,
        "request": request,
        "response": response,
    }
    return cast(ConsistencyGroup, s.get(**b))


@router.patch(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/ConsistencyGroups/{consistency_group_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch2(
    computer_system_id: str,
    storage_id: str,
    consistency_group_id: str,
    request: Request,
    response: Response,
    body: ConsistencyGroupOnUpdate,
) -> ConsistencyGroup:
    s: Service = get_service(ConsistencyGroup, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "consistency_group_id": consistency_group_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(ConsistencyGroup, s.patch(**b))


@router.delete(
    "/redfish/v1/StorageServices/{storage_service_id}/ConsistencyGroups/{consistency_group_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete3(
    storage_service_id: str, consistency_group_id: str, request: Request, response: Response
) -> None:
    s: Service = get_service(ConsistencyGroup, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "consistency_group_id": consistency_group_id,
        "request": request,
        "response": response,
    }
    return s.delete(**b)


@router.get(
    "/redfish/v1/StorageServices/{storage_service_id}/ConsistencyGroups/{consistency_group_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/StorageServices/{storage_service_id}/ConsistencyGroups/{consistency_group_id}",
    response_model_exclude_none=True,
)
async def get3(
    storage_service_id: str, consistency_group_id: str, request: Request, response: Response
) -> ConsistencyGroup:
    s: Service = get_service(ConsistencyGroup, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "consistency_group_id": consistency_group_id,
        "request": request,
        "response": response,
    }
    return cast(ConsistencyGroup, s.get(**b))


@router.patch(
    "/redfish/v1/StorageServices/{storage_service_id}/ConsistencyGroups/{consistency_group_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch3(
    storage_service_id: str,
    consistency_group_id: str,
    request: Request,
    response: Response,
    body: ConsistencyGroupOnUpdate,
) -> ConsistencyGroup:
    s: Service = get_service(ConsistencyGroup, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "consistency_group_id": consistency_group_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(ConsistencyGroup, s.patch(**b))


@router.delete(
    "/redfish/v1/StorageServices/{storage_service_id}/Volumes/{volume_id}/ConsistencyGroups/{consistency_group_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete4(
    storage_service_id: str,
    volume_id: str,
    consistency_group_id: str,
    request: Request,
    response: Response,
) -> None:
    s: Service = get_service(ConsistencyGroup, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "volume_id": volume_id,
        "consistency_group_id": consistency_group_id,
        "request": request,
        "response": response,
    }
    return s.delete(**b)


@router.get(
    "/redfish/v1/StorageServices/{storage_service_id}/Volumes/{volume_id}/ConsistencyGroups/{consistency_group_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/StorageServices/{storage_service_id}/Volumes/{volume_id}/ConsistencyGroups/{consistency_group_id}",
    response_model_exclude_none=True,
)
async def get4(
    storage_service_id: str,
    volume_id: str,
    consistency_group_id: str,
    request: Request,
    response: Response,
) -> ConsistencyGroup:
    s: Service = get_service(ConsistencyGroup, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "volume_id": volume_id,
        "consistency_group_id": consistency_group_id,
        "request": request,
        "response": response,
    }
    return cast(ConsistencyGroup, s.get(**b))


@router.patch(
    "/redfish/v1/StorageServices/{storage_service_id}/Volumes/{volume_id}/ConsistencyGroups/{consistency_group_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch4(
    storage_service_id: str,
    volume_id: str,
    consistency_group_id: str,
    request: Request,
    response: Response,
    body: ConsistencyGroupOnUpdate,
) -> ConsistencyGroup:
    s: Service = get_service(ConsistencyGroup, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "volume_id": volume_id,
        "consistency_group_id": consistency_group_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(ConsistencyGroup, s.patch(**b))
