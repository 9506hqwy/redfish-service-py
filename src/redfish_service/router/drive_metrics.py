from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..model.drive_metrics import DriveMetrics
from ..service import Service, find_service

router = APIRouter()


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/Drives/{drive_id}/Metrics",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/Drives/{drive_id}/Metrics",
    response_model_exclude_none=True,
)
async def get1(
    computer_system_id: str, storage_id: str, drive_id: str, request: Request, response: Response
) -> DriveMetrics:
    s: Service = find_service(DriveMetrics)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "drive_id": drive_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(DriveMetrics, s.get(**b))


@router.get(
    "/redfish/v1/Chassis/{chassis_id}/Drives/{drive_id}/Metrics", response_model_exclude_none=True
)
@router.head(
    "/redfish/v1/Chassis/{chassis_id}/Drives/{drive_id}/Metrics", response_model_exclude_none=True
)
async def get2(
    chassis_id: str, drive_id: str, request: Request, response: Response
) -> DriveMetrics:
    s: Service = find_service(DriveMetrics)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "drive_id": drive_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(DriveMetrics, s.get(**b))


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Storage/{storage_id}/Drives/{drive_id}/Metrics",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Storage/{storage_id}/Drives/{drive_id}/Metrics",
    response_model_exclude_none=True,
)
async def get3(
    resource_block_id: str, storage_id: str, drive_id: str, request: Request, response: Response
) -> DriveMetrics:
    s: Service = find_service(DriveMetrics)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "storage_id": storage_id,
        "drive_id": drive_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(DriveMetrics, s.get(**b))


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Drives/{drive_id}/Metrics",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Drives/{drive_id}/Metrics",
    response_model_exclude_none=True,
)
async def get4(
    resource_block_id: str, drive_id: str, request: Request, response: Response
) -> DriveMetrics:
    s: Service = find_service(DriveMetrics)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "drive_id": drive_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(DriveMetrics, s.get(**b))


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Storage/{storage_id}/Drives/{drive_id}/Metrics",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Storage/{storage_id}/Drives/{drive_id}/Metrics",
    response_model_exclude_none=True,
)
async def get5(
    resource_block_id: str,
    computer_system_id: str,
    storage_id: str,
    drive_id: str,
    request: Request,
    response: Response,
) -> DriveMetrics:
    s: Service = find_service(DriveMetrics)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "drive_id": drive_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(DriveMetrics, s.get(**b))


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Storage/{storage_id}/Drives/{drive_id}/Metrics",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Storage/{storage_id}/Drives/{drive_id}/Metrics",
    response_model_exclude_none=True,
)
async def get6(
    resource_block_id: str, storage_id: str, drive_id: str, request: Request, response: Response
) -> DriveMetrics:
    s: Service = find_service(DriveMetrics)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "storage_id": storage_id,
        "drive_id": drive_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(DriveMetrics, s.get(**b))


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Drives/{drive_id}/Metrics",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Drives/{drive_id}/Metrics",
    response_model_exclude_none=True,
)
async def get7(
    resource_block_id: str, drive_id: str, request: Request, response: Response
) -> DriveMetrics:
    s: Service = find_service(DriveMetrics)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "drive_id": drive_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(DriveMetrics, s.get(**b))


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Storage/{storage_id}/Drives/{drive_id}/Metrics",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Storage/{storage_id}/Drives/{drive_id}/Metrics",
    response_model_exclude_none=True,
)
async def get8(
    resource_block_id: str,
    computer_system_id: str,
    storage_id: str,
    drive_id: str,
    request: Request,
    response: Response,
) -> DriveMetrics:
    s: Service = find_service(DriveMetrics)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "drive_id": drive_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(DriveMetrics, s.get(**b))
