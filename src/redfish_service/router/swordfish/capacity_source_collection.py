from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ...model.swordfish.capacity_source_collection import CapacitySourceCollection
from ...service import Service
from ...util import get_service, set_link_header

router = APIRouter()


@router.get(
    "/redfish/v1/StorageServices/{storage_service_id}/StoragePools/{storage_pool_id}/CapacitySources",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/StorageServices/{storage_service_id}/StoragePools/{storage_pool_id}/CapacitySources",
    response_model_exclude_none=True,
)
async def get1(
    storage_service_id: str, storage_pool_id: str, request: Request, response: Response
) -> CapacitySourceCollection:
    s: Service = get_service(CapacitySourceCollection, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "storage_pool_id": storage_pool_id,
        "request": request,
        "response": response,
    }
    m = cast(CapacitySourceCollection, s.get(**b))
    set_link_header(m, response)
    return m


@router.get(
    "/redfish/v1/StorageServices/{storage_service_id}/Volumes/{volume_id}/CapacitySources",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/StorageServices/{storage_service_id}/Volumes/{volume_id}/CapacitySources",
    response_model_exclude_none=True,
)
async def get2(
    storage_service_id: str, volume_id: str, request: Request, response: Response
) -> CapacitySourceCollection:
    s: Service = get_service(CapacitySourceCollection, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
    }
    m = cast(CapacitySourceCollection, s.get(**b))
    set_link_header(m, response)
    return m


@router.get(
    "/redfish/v1/StorageServices/{storage_service_id}/FileSystems/{file_system_id}/CapacitySources",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/StorageServices/{storage_service_id}/FileSystems/{file_system_id}/CapacitySources",
    response_model_exclude_none=True,
)
async def get3(
    storage_service_id: str, file_system_id: str, request: Request, response: Response
) -> CapacitySourceCollection:
    s: Service = get_service(CapacitySourceCollection, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "file_system_id": file_system_id,
        "request": request,
        "response": response,
    }
    m = cast(CapacitySourceCollection, s.get(**b))
    set_link_header(m, response)
    return m


@router.get(
    "/redfish/v1/Storage/{storage_id}/StoragePools/{storage_pool_id}/CapacitySources",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Storage/{storage_id}/StoragePools/{storage_pool_id}/CapacitySources",
    response_model_exclude_none=True,
)
async def get4(
    storage_id: str, storage_pool_id: str, request: Request, response: Response
) -> CapacitySourceCollection:
    s: Service = get_service(CapacitySourceCollection, request)
    b: dict[str, Any] = {
        "storage_id": storage_id,
        "storage_pool_id": storage_pool_id,
        "request": request,
        "response": response,
    }
    m = cast(CapacitySourceCollection, s.get(**b))
    set_link_header(m, response)
    return m


@router.get(
    "/redfish/v1/Storage/{storage_id}/Volumes/{volume_id}/CapacitySources",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Storage/{storage_id}/Volumes/{volume_id}/CapacitySources",
    response_model_exclude_none=True,
)
async def get5(
    storage_id: str, volume_id: str, request: Request, response: Response
) -> CapacitySourceCollection:
    s: Service = get_service(CapacitySourceCollection, request)
    b: dict[str, Any] = {
        "storage_id": storage_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
    }
    m = cast(CapacitySourceCollection, s.get(**b))
    set_link_header(m, response)
    return m


@router.get(
    "/redfish/v1/Storage/{storage_id}/FileSystems/{file_system_id}/CapacitySources",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Storage/{storage_id}/FileSystems/{file_system_id}/CapacitySources",
    response_model_exclude_none=True,
)
async def get6(
    storage_id: str, file_system_id: str, request: Request, response: Response
) -> CapacitySourceCollection:
    s: Service = get_service(CapacitySourceCollection, request)
    b: dict[str, Any] = {
        "storage_id": storage_id,
        "file_system_id": file_system_id,
        "request": request,
        "response": response,
    }
    m = cast(CapacitySourceCollection, s.get(**b))
    set_link_header(m, response)
    return m


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/StoragePools/{storage_pool_id}/CapacitySources",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/StoragePools/{storage_pool_id}/CapacitySources",
    response_model_exclude_none=True,
)
async def get7(
    computer_system_id: str,
    storage_id: str,
    storage_pool_id: str,
    request: Request,
    response: Response,
) -> CapacitySourceCollection:
    s: Service = get_service(CapacitySourceCollection, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "storage_pool_id": storage_pool_id,
        "request": request,
        "response": response,
    }
    m = cast(CapacitySourceCollection, s.get(**b))
    set_link_header(m, response)
    return m


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/Volumes/{volume_id}/CapacitySources",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/Volumes/{volume_id}/CapacitySources",
    response_model_exclude_none=True,
)
async def get8(
    computer_system_id: str, storage_id: str, volume_id: str, request: Request, response: Response
) -> CapacitySourceCollection:
    s: Service = get_service(CapacitySourceCollection, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
    }
    m = cast(CapacitySourceCollection, s.get(**b))
    set_link_header(m, response)
    return m


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/FileSystems/{file_system_id}/CapacitySources",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/FileSystems/{file_system_id}/CapacitySources",
    response_model_exclude_none=True,
)
async def get9(
    computer_system_id: str,
    storage_id: str,
    file_system_id: str,
    request: Request,
    response: Response,
) -> CapacitySourceCollection:
    s: Service = get_service(CapacitySourceCollection, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "file_system_id": file_system_id,
        "request": request,
        "response": response,
    }
    m = cast(CapacitySourceCollection, s.get(**b))
    set_link_header(m, response)
    return m
