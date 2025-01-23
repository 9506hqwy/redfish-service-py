from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..model.drive_collection import DriveCollection
from ..service import Service
from ..util import get_service, set_link_header

router = APIRouter()


@router.get("/redfish/v1/Chassis/{chassis_id}/Drives", response_model_exclude_none=True)
@router.head("/redfish/v1/Chassis/{chassis_id}/Drives", response_model_exclude_none=True)
async def get1(chassis_id: str, request: Request, response: Response) -> DriveCollection:
    s: Service = get_service(DriveCollection, request)
    b: dict[str, Any] = {"chassis_id": chassis_id, "request": request, "response": response}
    m = cast(DriveCollection, s.get(**b))
    set_link_header(m, response)
    return m


@router.get(
    "/redfish/v1/Storage/{storage_id}/FileSystems/{file_system_id}/CapacitySources/{capacity_source_id}/ProvidingDrives",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Storage/{storage_id}/FileSystems/{file_system_id}/CapacitySources/{capacity_source_id}/ProvidingDrives",
    response_model_exclude_none=True,
)
async def get2(
    storage_id: str,
    file_system_id: str,
    capacity_source_id: str,
    request: Request,
    response: Response,
) -> DriveCollection:
    s: Service = get_service(DriveCollection, request)
    b: dict[str, Any] = {
        "storage_id": storage_id,
        "file_system_id": file_system_id,
        "capacity_source_id": capacity_source_id,
        "request": request,
        "response": response,
    }
    m = cast(DriveCollection, s.get(**b))
    set_link_header(m, response)
    return m


@router.get(
    "/redfish/v1/Storage/{storage_id}/StoragePools/{storage_pool_id}/CapacitySources/{capacity_source_id}/ProvidingDrives",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Storage/{storage_id}/StoragePools/{storage_pool_id}/CapacitySources/{capacity_source_id}/ProvidingDrives",
    response_model_exclude_none=True,
)
async def get3(
    storage_id: str,
    storage_pool_id: str,
    capacity_source_id: str,
    request: Request,
    response: Response,
) -> DriveCollection:
    s: Service = get_service(DriveCollection, request)
    b: dict[str, Any] = {
        "storage_id": storage_id,
        "storage_pool_id": storage_pool_id,
        "capacity_source_id": capacity_source_id,
        "request": request,
        "response": response,
    }
    m = cast(DriveCollection, s.get(**b))
    set_link_header(m, response)
    return m


@router.get(
    "/redfish/v1/Storage/{storage_id}/Volumes/{volume_id}/CapacitySources/{capacity_source_id}/ProvidingDrives",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Storage/{storage_id}/Volumes/{volume_id}/CapacitySources/{capacity_source_id}/ProvidingDrives",
    response_model_exclude_none=True,
)
async def get4(
    storage_id: str, volume_id: str, capacity_source_id: str, request: Request, response: Response
) -> DriveCollection:
    s: Service = get_service(DriveCollection, request)
    b: dict[str, Any] = {
        "storage_id": storage_id,
        "volume_id": volume_id,
        "capacity_source_id": capacity_source_id,
        "request": request,
        "response": response,
    }
    m = cast(DriveCollection, s.get(**b))
    set_link_header(m, response)
    return m


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/FileSystems/{file_system_id}/CapacitySources/{capacity_source_id}/ProvidingDrives",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/FileSystems/{file_system_id}/CapacitySources/{capacity_source_id}/ProvidingDrives",
    response_model_exclude_none=True,
)
async def get5(
    computer_system_id: str,
    storage_id: str,
    file_system_id: str,
    capacity_source_id: str,
    request: Request,
    response: Response,
) -> DriveCollection:
    s: Service = get_service(DriveCollection, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "file_system_id": file_system_id,
        "capacity_source_id": capacity_source_id,
        "request": request,
        "response": response,
    }
    m = cast(DriveCollection, s.get(**b))
    set_link_header(m, response)
    return m


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/StoragePools/{storage_pool_id}/CapacitySources/{capacity_source_id}/ProvidingDrives",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/StoragePools/{storage_pool_id}/CapacitySources/{capacity_source_id}/ProvidingDrives",
    response_model_exclude_none=True,
)
async def get6(
    computer_system_id: str,
    storage_id: str,
    storage_pool_id: str,
    capacity_source_id: str,
    request: Request,
    response: Response,
) -> DriveCollection:
    s: Service = get_service(DriveCollection, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "storage_pool_id": storage_pool_id,
        "capacity_source_id": capacity_source_id,
        "request": request,
        "response": response,
    }
    m = cast(DriveCollection, s.get(**b))
    set_link_header(m, response)
    return m


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/Volumes/{volume_id}/CapacitySources/{capacity_source_id}/ProvidingDrives",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/Volumes/{volume_id}/CapacitySources/{capacity_source_id}/ProvidingDrives",
    response_model_exclude_none=True,
)
async def get7(
    computer_system_id: str,
    storage_id: str,
    volume_id: str,
    capacity_source_id: str,
    request: Request,
    response: Response,
) -> DriveCollection:
    s: Service = get_service(DriveCollection, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "volume_id": volume_id,
        "capacity_source_id": capacity_source_id,
        "request": request,
        "response": response,
    }
    m = cast(DriveCollection, s.get(**b))
    set_link_header(m, response)
    return m


@router.get(
    "/redfish/v1/StorageServices/{storage_service_id}/Drives", response_model_exclude_none=True
)
@router.head(
    "/redfish/v1/StorageServices/{storage_service_id}/Drives", response_model_exclude_none=True
)
async def get8(storage_service_id: str, request: Request, response: Response) -> DriveCollection:
    s: Service = get_service(DriveCollection, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "request": request,
        "response": response,
    }
    m = cast(DriveCollection, s.get(**b))
    set_link_header(m, response)
    return m


@router.get(
    "/redfish/v1/StorageServices/{storage_service_id}/FileSystems/{file_system_id}/CapacitySources/{capacity_source_id}/ProvidingDrives",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/StorageServices/{storage_service_id}/FileSystems/{file_system_id}/CapacitySources/{capacity_source_id}/ProvidingDrives",
    response_model_exclude_none=True,
)
async def get9(
    storage_service_id: str,
    file_system_id: str,
    capacity_source_id: str,
    request: Request,
    response: Response,
) -> DriveCollection:
    s: Service = get_service(DriveCollection, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "file_system_id": file_system_id,
        "capacity_source_id": capacity_source_id,
        "request": request,
        "response": response,
    }
    m = cast(DriveCollection, s.get(**b))
    set_link_header(m, response)
    return m


@router.get(
    "/redfish/v1/StorageServices/{storage_service_id}/StoragePools/{storage_pool_id}/CapacitySources/{capacity_source_id}/ProvidingDrives",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/StorageServices/{storage_service_id}/StoragePools/{storage_pool_id}/CapacitySources/{capacity_source_id}/ProvidingDrives",
    response_model_exclude_none=True,
)
async def get10(
    storage_service_id: str,
    storage_pool_id: str,
    capacity_source_id: str,
    request: Request,
    response: Response,
) -> DriveCollection:
    s: Service = get_service(DriveCollection, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "storage_pool_id": storage_pool_id,
        "capacity_source_id": capacity_source_id,
        "request": request,
        "response": response,
    }
    m = cast(DriveCollection, s.get(**b))
    set_link_header(m, response)
    return m


@router.get(
    "/redfish/v1/StorageServices/{storage_service_id}/Volumes/{volume_id}/CapacitySources/{capacity_source_id}/ProvidingDrives",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/StorageServices/{storage_service_id}/Volumes/{volume_id}/CapacitySources/{capacity_source_id}/ProvidingDrives",
    response_model_exclude_none=True,
)
async def get11(
    storage_service_id: str,
    volume_id: str,
    capacity_source_id: str,
    request: Request,
    response: Response,
) -> DriveCollection:
    s: Service = get_service(DriveCollection, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "volume_id": volume_id,
        "capacity_source_id": capacity_source_id,
        "request": request,
        "response": response,
    }
    m = cast(DriveCollection, s.get(**b))
    set_link_header(m, response)
    return m
