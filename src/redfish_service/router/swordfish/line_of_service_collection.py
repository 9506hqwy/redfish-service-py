from typing import Any, cast

from fastapi import APIRouter

from ...authenticate import authenticate
from ...model.swordfish.line_of_service_collection import LineOfServiceCollection
from ...service import Service, find_service

router = APIRouter()


@router.get(
    "/redfish/v1/StorageServices/{storage_service_id}/LinesOfService",
    response_model_exclude_none=True,
)
@authenticate
async def get1(storage_service_id: str) -> LineOfServiceCollection:
    s: Service = find_service(LineOfServiceCollection)
    b: dict[str, Any] = {"storage_service_id": storage_service_id}
    return cast(LineOfServiceCollection, s.get(**b))


@router.get(
    "/redfish/v1/StorageServices/{storage_service_id}/LinesOfService/DataProtectionLinesOfService",
    response_model_exclude_none=True,
)
@authenticate
async def get2(storage_service_id: str) -> LineOfServiceCollection:
    s: Service = find_service(LineOfServiceCollection)
    b: dict[str, Any] = {"storage_service_id": storage_service_id}
    return cast(LineOfServiceCollection, s.get(**b))


@router.get(
    "/redfish/v1/StorageServices/{storage_service_id}/LinesOfService/DataSecurityLinesOfService",
    response_model_exclude_none=True,
)
@authenticate
async def get3(storage_service_id: str) -> LineOfServiceCollection:
    s: Service = find_service(LineOfServiceCollection)
    b: dict[str, Any] = {"storage_service_id": storage_service_id}
    return cast(LineOfServiceCollection, s.get(**b))


@router.get(
    "/redfish/v1/StorageServices/{storage_service_id}/LinesOfService/DataStorageLinesOfService",
    response_model_exclude_none=True,
)
@authenticate
async def get4(storage_service_id: str) -> LineOfServiceCollection:
    s: Service = find_service(LineOfServiceCollection)
    b: dict[str, Any] = {"storage_service_id": storage_service_id}
    return cast(LineOfServiceCollection, s.get(**b))


@router.get(
    "/redfish/v1/StorageServices/{storage_service_id}/LinesOfService/IOConnectivityLinesOfService",
    response_model_exclude_none=True,
)
@authenticate
async def get5(storage_service_id: str) -> LineOfServiceCollection:
    s: Service = find_service(LineOfServiceCollection)
    b: dict[str, Any] = {"storage_service_id": storage_service_id}
    return cast(LineOfServiceCollection, s.get(**b))


@router.get(
    "/redfish/v1/StorageServices/{storage_service_id}/LinesOfService/IOPerformanceLinesOfService",
    response_model_exclude_none=True,
)
@authenticate
async def get6(storage_service_id: str) -> LineOfServiceCollection:
    s: Service = find_service(LineOfServiceCollection)
    b: dict[str, Any] = {"storage_service_id": storage_service_id}
    return cast(LineOfServiceCollection, s.get(**b))


@router.get(
    "/redfish/v1/StorageServices/{storage_service_id}/ClassesOfService/{class_of_service_id}/DataProtectionLinesOfService",
    response_model_exclude_none=True,
)
@authenticate
async def get7(storage_service_id: str, class_of_service_id: str) -> LineOfServiceCollection:
    s: Service = find_service(LineOfServiceCollection)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "class_of_service_id": class_of_service_id,
    }
    return cast(LineOfServiceCollection, s.get(**b))


@router.get(
    "/redfish/v1/StorageServices/{storage_service_id}/ClassesOfService/{class_of_service_id}/DataSecurityLinesOfService",
    response_model_exclude_none=True,
)
@authenticate
async def get8(storage_service_id: str, class_of_service_id: str) -> LineOfServiceCollection:
    s: Service = find_service(LineOfServiceCollection)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "class_of_service_id": class_of_service_id,
    }
    return cast(LineOfServiceCollection, s.get(**b))


@router.get(
    "/redfish/v1/StorageServices/{storage_service_id}/ClassesOfService/{class_of_service_id}/DataStorageLinesOfService",
    response_model_exclude_none=True,
)
@authenticate
async def get9(storage_service_id: str, class_of_service_id: str) -> LineOfServiceCollection:
    s: Service = find_service(LineOfServiceCollection)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "class_of_service_id": class_of_service_id,
    }
    return cast(LineOfServiceCollection, s.get(**b))


@router.get(
    "/redfish/v1/StorageServices/{storage_service_id}/ClassesOfService/{class_of_service_id}/IOConnectivityLinesOfService",
    response_model_exclude_none=True,
)
@authenticate
async def get10(storage_service_id: str, class_of_service_id: str) -> LineOfServiceCollection:
    s: Service = find_service(LineOfServiceCollection)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "class_of_service_id": class_of_service_id,
    }
    return cast(LineOfServiceCollection, s.get(**b))


@router.get(
    "/redfish/v1/StorageServices/{storage_service_id}/ClassesOfService/{class_of_service_id}/IOPerformanceLinesOfService",
    response_model_exclude_none=True,
)
@authenticate
async def get11(storage_service_id: str, class_of_service_id: str) -> LineOfServiceCollection:
    s: Service = find_service(LineOfServiceCollection)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "class_of_service_id": class_of_service_id,
    }
    return cast(LineOfServiceCollection, s.get(**b))
