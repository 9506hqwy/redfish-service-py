from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ...authenticate import authenticate
from ...model.redfish_error import RedfishError
from ...model.swordfish.storage_pool import (
    AddDrivesRequest,
    RemoveDrivesRequest,
    SetCompressionStateRequest,
    SetDeduplicationStateRequest,
    SetEncryptionStateRequest,
    StoragePool,
    StoragePoolOnUpdate,
)
from ...service import Service
from ...util import get_service

router = APIRouter()


@router.delete(
    "/redfish/v1/StorageServices/{storage_service_id}/StoragePools/{storage_pool_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete1(
    storage_service_id: str, storage_pool_id: str, request: Request, response: Response
) -> None:
    s: Service = get_service(StoragePool, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "storage_pool_id": storage_pool_id,
        "request": request,
        "response": response,
    }
    return s.delete(**b)


@router.get(
    "/redfish/v1/StorageServices/{storage_service_id}/StoragePools/{storage_pool_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/StorageServices/{storage_service_id}/StoragePools/{storage_pool_id}",
    response_model_exclude_none=True,
)
async def get1(
    storage_service_id: str, storage_pool_id: str, request: Request, response: Response
) -> StoragePool:
    s: Service = get_service(StoragePool, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "storage_pool_id": storage_pool_id,
        "request": request,
        "response": response,
    }
    return cast(StoragePool, s.get(**b))


@router.patch(
    "/redfish/v1/StorageServices/{storage_service_id}/StoragePools/{storage_pool_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch1(
    storage_service_id: str,
    storage_pool_id: str,
    request: Request,
    response: Response,
    body: StoragePoolOnUpdate,
) -> StoragePool:
    s: Service = get_service(StoragePool, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "storage_pool_id": storage_pool_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(StoragePool, s.patch(**b))


@router.post(
    "/redfish/v1/StorageServices/{storage_service_id}/StoragePools/{storage_pool_id}/Actions/StoragePool.AddDrives",
    response_model_exclude_none=True,
)
@authenticate
async def add_drives1(
    storage_service_id: str,
    storage_pool_id: str,
    request: Request,
    response: Response,
    body: AddDrivesRequest,
) -> RedfishError:
    s: Service = get_service(StoragePool, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "storage_pool_id": storage_pool_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "AddDrives",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/StorageServices/{storage_service_id}/StoragePools/{storage_pool_id}/Actions/StoragePool.RemoveDrives",
    response_model_exclude_none=True,
)
@authenticate
async def remove_drives1(
    storage_service_id: str,
    storage_pool_id: str,
    request: Request,
    response: Response,
    body: RemoveDrivesRequest,
) -> RedfishError:
    s: Service = get_service(StoragePool, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "storage_pool_id": storage_pool_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "RemoveDrives",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/StorageServices/{storage_service_id}/StoragePools/{storage_pool_id}/Actions/StoragePool.SetCompressionState",
    response_model_exclude_none=True,
)
@authenticate
async def set_compression_state1(
    storage_service_id: str,
    storage_pool_id: str,
    request: Request,
    response: Response,
    body: SetCompressionStateRequest,
) -> RedfishError:
    s: Service = get_service(StoragePool, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "storage_pool_id": storage_pool_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "SetCompressionState",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/StorageServices/{storage_service_id}/StoragePools/{storage_pool_id}/Actions/StoragePool.SetDeduplicationState",
    response_model_exclude_none=True,
)
@authenticate
async def set_deduplication_state1(
    storage_service_id: str,
    storage_pool_id: str,
    request: Request,
    response: Response,
    body: SetDeduplicationStateRequest,
) -> RedfishError:
    s: Service = get_service(StoragePool, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "storage_pool_id": storage_pool_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "SetDeduplicationState",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/StorageServices/{storage_service_id}/StoragePools/{storage_pool_id}/Actions/StoragePool.SetEncryptionState",
    response_model_exclude_none=True,
)
@authenticate
async def set_encryption_state1(
    storage_service_id: str,
    storage_pool_id: str,
    request: Request,
    response: Response,
    body: SetEncryptionStateRequest,
) -> RedfishError:
    s: Service = get_service(StoragePool, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "storage_pool_id": storage_pool_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "SetEncryptionState",
    }
    return s.action(**b)


@router.delete(
    "/redfish/v1/StorageServices/{storage_service_id}/StoragePools/{storage_pool_id}/AllocatedPools/{allocated_pool_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete2(
    storage_service_id: str,
    storage_pool_id: str,
    allocated_pool_id: str,
    request: Request,
    response: Response,
) -> None:
    s: Service = get_service(StoragePool, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "storage_pool_id": storage_pool_id,
        "allocated_pool_id": allocated_pool_id,
        "request": request,
        "response": response,
    }
    return s.delete(**b)


@router.get(
    "/redfish/v1/StorageServices/{storage_service_id}/StoragePools/{storage_pool_id}/AllocatedPools/{allocated_pool_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/StorageServices/{storage_service_id}/StoragePools/{storage_pool_id}/AllocatedPools/{allocated_pool_id}",
    response_model_exclude_none=True,
)
async def get2(
    storage_service_id: str,
    storage_pool_id: str,
    allocated_pool_id: str,
    request: Request,
    response: Response,
) -> StoragePool:
    s: Service = get_service(StoragePool, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "storage_pool_id": storage_pool_id,
        "allocated_pool_id": allocated_pool_id,
        "request": request,
        "response": response,
    }
    return cast(StoragePool, s.get(**b))


@router.patch(
    "/redfish/v1/StorageServices/{storage_service_id}/StoragePools/{storage_pool_id}/AllocatedPools/{allocated_pool_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch2(
    storage_service_id: str,
    storage_pool_id: str,
    allocated_pool_id: str,
    request: Request,
    response: Response,
    body: StoragePoolOnUpdate,
) -> StoragePool:
    s: Service = get_service(StoragePool, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "storage_pool_id": storage_pool_id,
        "allocated_pool_id": allocated_pool_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(StoragePool, s.patch(**b))


@router.post(
    "/redfish/v1/StorageServices/{storage_service_id}/StoragePools/{storage_pool_id}/AllocatedPools/{allocated_pool_id}/Actions/StoragePool.AddDrives",
    response_model_exclude_none=True,
)
@authenticate
async def add_drives2(
    storage_service_id: str,
    storage_pool_id: str,
    allocated_pool_id: str,
    request: Request,
    response: Response,
    body: AddDrivesRequest,
) -> RedfishError:
    s: Service = get_service(StoragePool, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "storage_pool_id": storage_pool_id,
        "allocated_pool_id": allocated_pool_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "AddDrives",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/StorageServices/{storage_service_id}/StoragePools/{storage_pool_id}/AllocatedPools/{allocated_pool_id}/Actions/StoragePool.RemoveDrives",
    response_model_exclude_none=True,
)
@authenticate
async def remove_drives2(
    storage_service_id: str,
    storage_pool_id: str,
    allocated_pool_id: str,
    request: Request,
    response: Response,
    body: RemoveDrivesRequest,
) -> RedfishError:
    s: Service = get_service(StoragePool, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "storage_pool_id": storage_pool_id,
        "allocated_pool_id": allocated_pool_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "RemoveDrives",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/StorageServices/{storage_service_id}/StoragePools/{storage_pool_id}/AllocatedPools/{allocated_pool_id}/Actions/StoragePool.SetCompressionState",
    response_model_exclude_none=True,
)
@authenticate
async def set_compression_state2(
    storage_service_id: str,
    storage_pool_id: str,
    allocated_pool_id: str,
    request: Request,
    response: Response,
    body: SetCompressionStateRequest,
) -> RedfishError:
    s: Service = get_service(StoragePool, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "storage_pool_id": storage_pool_id,
        "allocated_pool_id": allocated_pool_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "SetCompressionState",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/StorageServices/{storage_service_id}/StoragePools/{storage_pool_id}/AllocatedPools/{allocated_pool_id}/Actions/StoragePool.SetDeduplicationState",
    response_model_exclude_none=True,
)
@authenticate
async def set_deduplication_state2(
    storage_service_id: str,
    storage_pool_id: str,
    allocated_pool_id: str,
    request: Request,
    response: Response,
    body: SetDeduplicationStateRequest,
) -> RedfishError:
    s: Service = get_service(StoragePool, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "storage_pool_id": storage_pool_id,
        "allocated_pool_id": allocated_pool_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "SetDeduplicationState",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/StorageServices/{storage_service_id}/StoragePools/{storage_pool_id}/AllocatedPools/{allocated_pool_id}/Actions/StoragePool.SetEncryptionState",
    response_model_exclude_none=True,
)
@authenticate
async def set_encryption_state2(
    storage_service_id: str,
    storage_pool_id: str,
    allocated_pool_id: str,
    request: Request,
    response: Response,
    body: SetEncryptionStateRequest,
) -> RedfishError:
    s: Service = get_service(StoragePool, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "storage_pool_id": storage_pool_id,
        "allocated_pool_id": allocated_pool_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "SetEncryptionState",
    }
    return s.action(**b)


@router.delete(
    "/redfish/v1/StorageServices/{storage_service_id}/StoragePools/{storage_pool_id}/CapacitySources/{capacity_source_id}/ProvidingPools/{providing_pool_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete3(
    storage_service_id: str,
    storage_pool_id: str,
    capacity_source_id: str,
    providing_pool_id: str,
    request: Request,
    response: Response,
) -> None:
    s: Service = get_service(StoragePool, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "storage_pool_id": storage_pool_id,
        "capacity_source_id": capacity_source_id,
        "providing_pool_id": providing_pool_id,
        "request": request,
        "response": response,
    }
    return s.delete(**b)


@router.get(
    "/redfish/v1/StorageServices/{storage_service_id}/StoragePools/{storage_pool_id}/CapacitySources/{capacity_source_id}/ProvidingPools/{providing_pool_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/StorageServices/{storage_service_id}/StoragePools/{storage_pool_id}/CapacitySources/{capacity_source_id}/ProvidingPools/{providing_pool_id}",
    response_model_exclude_none=True,
)
async def get3(
    storage_service_id: str,
    storage_pool_id: str,
    capacity_source_id: str,
    providing_pool_id: str,
    request: Request,
    response: Response,
) -> StoragePool:
    s: Service = get_service(StoragePool, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "storage_pool_id": storage_pool_id,
        "capacity_source_id": capacity_source_id,
        "providing_pool_id": providing_pool_id,
        "request": request,
        "response": response,
    }
    return cast(StoragePool, s.get(**b))


@router.patch(
    "/redfish/v1/StorageServices/{storage_service_id}/StoragePools/{storage_pool_id}/CapacitySources/{capacity_source_id}/ProvidingPools/{providing_pool_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch3(
    storage_service_id: str,
    storage_pool_id: str,
    capacity_source_id: str,
    providing_pool_id: str,
    request: Request,
    response: Response,
    body: StoragePoolOnUpdate,
) -> StoragePool:
    s: Service = get_service(StoragePool, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "storage_pool_id": storage_pool_id,
        "capacity_source_id": capacity_source_id,
        "providing_pool_id": providing_pool_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(StoragePool, s.patch(**b))


@router.post(
    "/redfish/v1/StorageServices/{storage_service_id}/StoragePools/{storage_pool_id}/CapacitySources/{capacity_source_id}/ProvidingPools/{providing_pool_id}/Actions/StoragePool.AddDrives",
    response_model_exclude_none=True,
)
@authenticate
async def add_drives3(
    storage_service_id: str,
    storage_pool_id: str,
    capacity_source_id: str,
    providing_pool_id: str,
    request: Request,
    response: Response,
    body: AddDrivesRequest,
) -> RedfishError:
    s: Service = get_service(StoragePool, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "storage_pool_id": storage_pool_id,
        "capacity_source_id": capacity_source_id,
        "providing_pool_id": providing_pool_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "AddDrives",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/StorageServices/{storage_service_id}/StoragePools/{storage_pool_id}/CapacitySources/{capacity_source_id}/ProvidingPools/{providing_pool_id}/Actions/StoragePool.RemoveDrives",
    response_model_exclude_none=True,
)
@authenticate
async def remove_drives3(
    storage_service_id: str,
    storage_pool_id: str,
    capacity_source_id: str,
    providing_pool_id: str,
    request: Request,
    response: Response,
    body: RemoveDrivesRequest,
) -> RedfishError:
    s: Service = get_service(StoragePool, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "storage_pool_id": storage_pool_id,
        "capacity_source_id": capacity_source_id,
        "providing_pool_id": providing_pool_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "RemoveDrives",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/StorageServices/{storage_service_id}/StoragePools/{storage_pool_id}/CapacitySources/{capacity_source_id}/ProvidingPools/{providing_pool_id}/Actions/StoragePool.SetCompressionState",
    response_model_exclude_none=True,
)
@authenticate
async def set_compression_state3(
    storage_service_id: str,
    storage_pool_id: str,
    capacity_source_id: str,
    providing_pool_id: str,
    request: Request,
    response: Response,
    body: SetCompressionStateRequest,
) -> RedfishError:
    s: Service = get_service(StoragePool, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "storage_pool_id": storage_pool_id,
        "capacity_source_id": capacity_source_id,
        "providing_pool_id": providing_pool_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "SetCompressionState",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/StorageServices/{storage_service_id}/StoragePools/{storage_pool_id}/CapacitySources/{capacity_source_id}/ProvidingPools/{providing_pool_id}/Actions/StoragePool.SetDeduplicationState",
    response_model_exclude_none=True,
)
@authenticate
async def set_deduplication_state3(
    storage_service_id: str,
    storage_pool_id: str,
    capacity_source_id: str,
    providing_pool_id: str,
    request: Request,
    response: Response,
    body: SetDeduplicationStateRequest,
) -> RedfishError:
    s: Service = get_service(StoragePool, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "storage_pool_id": storage_pool_id,
        "capacity_source_id": capacity_source_id,
        "providing_pool_id": providing_pool_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "SetDeduplicationState",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/StorageServices/{storage_service_id}/StoragePools/{storage_pool_id}/CapacitySources/{capacity_source_id}/ProvidingPools/{providing_pool_id}/Actions/StoragePool.SetEncryptionState",
    response_model_exclude_none=True,
)
@authenticate
async def set_encryption_state3(
    storage_service_id: str,
    storage_pool_id: str,
    capacity_source_id: str,
    providing_pool_id: str,
    request: Request,
    response: Response,
    body: SetEncryptionStateRequest,
) -> RedfishError:
    s: Service = get_service(StoragePool, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "storage_pool_id": storage_pool_id,
        "capacity_source_id": capacity_source_id,
        "providing_pool_id": providing_pool_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "SetEncryptionState",
    }
    return s.action(**b)


@router.delete(
    "/redfish/v1/StorageServices/{storage_service_id}/Volumes/{volume_id}/CapacitySources/{capacity_source_id}/ProvidingPools/{storage_pool_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete4(
    storage_service_id: str,
    volume_id: str,
    capacity_source_id: str,
    storage_pool_id: str,
    request: Request,
    response: Response,
) -> None:
    s: Service = get_service(StoragePool, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "volume_id": volume_id,
        "capacity_source_id": capacity_source_id,
        "storage_pool_id": storage_pool_id,
        "request": request,
        "response": response,
    }
    return s.delete(**b)


@router.get(
    "/redfish/v1/StorageServices/{storage_service_id}/Volumes/{volume_id}/CapacitySources/{capacity_source_id}/ProvidingPools/{storage_pool_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/StorageServices/{storage_service_id}/Volumes/{volume_id}/CapacitySources/{capacity_source_id}/ProvidingPools/{storage_pool_id}",
    response_model_exclude_none=True,
)
async def get4(
    storage_service_id: str,
    volume_id: str,
    capacity_source_id: str,
    storage_pool_id: str,
    request: Request,
    response: Response,
) -> StoragePool:
    s: Service = get_service(StoragePool, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "volume_id": volume_id,
        "capacity_source_id": capacity_source_id,
        "storage_pool_id": storage_pool_id,
        "request": request,
        "response": response,
    }
    return cast(StoragePool, s.get(**b))


@router.patch(
    "/redfish/v1/StorageServices/{storage_service_id}/Volumes/{volume_id}/CapacitySources/{capacity_source_id}/ProvidingPools/{storage_pool_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch4(
    storage_service_id: str,
    volume_id: str,
    capacity_source_id: str,
    storage_pool_id: str,
    request: Request,
    response: Response,
    body: StoragePoolOnUpdate,
) -> StoragePool:
    s: Service = get_service(StoragePool, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "volume_id": volume_id,
        "capacity_source_id": capacity_source_id,
        "storage_pool_id": storage_pool_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(StoragePool, s.patch(**b))


@router.post(
    "/redfish/v1/StorageServices/{storage_service_id}/Volumes/{volume_id}/CapacitySources/{capacity_source_id}/ProvidingPools/{storage_pool_id}/Actions/StoragePool.AddDrives",
    response_model_exclude_none=True,
)
@authenticate
async def add_drives4(
    storage_service_id: str,
    volume_id: str,
    capacity_source_id: str,
    storage_pool_id: str,
    request: Request,
    response: Response,
    body: AddDrivesRequest,
) -> RedfishError:
    s: Service = get_service(StoragePool, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "volume_id": volume_id,
        "capacity_source_id": capacity_source_id,
        "storage_pool_id": storage_pool_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "AddDrives",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/StorageServices/{storage_service_id}/Volumes/{volume_id}/CapacitySources/{capacity_source_id}/ProvidingPools/{storage_pool_id}/Actions/StoragePool.RemoveDrives",
    response_model_exclude_none=True,
)
@authenticate
async def remove_drives4(
    storage_service_id: str,
    volume_id: str,
    capacity_source_id: str,
    storage_pool_id: str,
    request: Request,
    response: Response,
    body: RemoveDrivesRequest,
) -> RedfishError:
    s: Service = get_service(StoragePool, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "volume_id": volume_id,
        "capacity_source_id": capacity_source_id,
        "storage_pool_id": storage_pool_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "RemoveDrives",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/StorageServices/{storage_service_id}/Volumes/{volume_id}/CapacitySources/{capacity_source_id}/ProvidingPools/{storage_pool_id}/Actions/StoragePool.SetCompressionState",
    response_model_exclude_none=True,
)
@authenticate
async def set_compression_state4(
    storage_service_id: str,
    volume_id: str,
    capacity_source_id: str,
    storage_pool_id: str,
    request: Request,
    response: Response,
    body: SetCompressionStateRequest,
) -> RedfishError:
    s: Service = get_service(StoragePool, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "volume_id": volume_id,
        "capacity_source_id": capacity_source_id,
        "storage_pool_id": storage_pool_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "SetCompressionState",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/StorageServices/{storage_service_id}/Volumes/{volume_id}/CapacitySources/{capacity_source_id}/ProvidingPools/{storage_pool_id}/Actions/StoragePool.SetDeduplicationState",
    response_model_exclude_none=True,
)
@authenticate
async def set_deduplication_state4(
    storage_service_id: str,
    volume_id: str,
    capacity_source_id: str,
    storage_pool_id: str,
    request: Request,
    response: Response,
    body: SetDeduplicationStateRequest,
) -> RedfishError:
    s: Service = get_service(StoragePool, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "volume_id": volume_id,
        "capacity_source_id": capacity_source_id,
        "storage_pool_id": storage_pool_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "SetDeduplicationState",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/StorageServices/{storage_service_id}/Volumes/{volume_id}/CapacitySources/{capacity_source_id}/ProvidingPools/{storage_pool_id}/Actions/StoragePool.SetEncryptionState",
    response_model_exclude_none=True,
)
@authenticate
async def set_encryption_state4(
    storage_service_id: str,
    volume_id: str,
    capacity_source_id: str,
    storage_pool_id: str,
    request: Request,
    response: Response,
    body: SetEncryptionStateRequest,
) -> RedfishError:
    s: Service = get_service(StoragePool, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "volume_id": volume_id,
        "capacity_source_id": capacity_source_id,
        "storage_pool_id": storage_pool_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "SetEncryptionState",
    }
    return s.action(**b)


@router.delete(
    "/redfish/v1/StorageServices/{storage_service_id}/Volumes/{volume_id}/AllocatedPools/{storage_pool_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete5(
    storage_service_id: str,
    volume_id: str,
    storage_pool_id: str,
    request: Request,
    response: Response,
) -> None:
    s: Service = get_service(StoragePool, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "volume_id": volume_id,
        "storage_pool_id": storage_pool_id,
        "request": request,
        "response": response,
    }
    return s.delete(**b)


@router.get(
    "/redfish/v1/StorageServices/{storage_service_id}/Volumes/{volume_id}/AllocatedPools/{storage_pool_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/StorageServices/{storage_service_id}/Volumes/{volume_id}/AllocatedPools/{storage_pool_id}",
    response_model_exclude_none=True,
)
async def get5(
    storage_service_id: str,
    volume_id: str,
    storage_pool_id: str,
    request: Request,
    response: Response,
) -> StoragePool:
    s: Service = get_service(StoragePool, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "volume_id": volume_id,
        "storage_pool_id": storage_pool_id,
        "request": request,
        "response": response,
    }
    return cast(StoragePool, s.get(**b))


@router.patch(
    "/redfish/v1/StorageServices/{storage_service_id}/Volumes/{volume_id}/AllocatedPools/{storage_pool_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch5(
    storage_service_id: str,
    volume_id: str,
    storage_pool_id: str,
    request: Request,
    response: Response,
    body: StoragePoolOnUpdate,
) -> StoragePool:
    s: Service = get_service(StoragePool, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "volume_id": volume_id,
        "storage_pool_id": storage_pool_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(StoragePool, s.patch(**b))


@router.post(
    "/redfish/v1/StorageServices/{storage_service_id}/Volumes/{volume_id}/AllocatedPools/{storage_pool_id}/Actions/StoragePool.AddDrives",
    response_model_exclude_none=True,
)
@authenticate
async def add_drives5(
    storage_service_id: str,
    volume_id: str,
    storage_pool_id: str,
    request: Request,
    response: Response,
    body: AddDrivesRequest,
) -> RedfishError:
    s: Service = get_service(StoragePool, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "volume_id": volume_id,
        "storage_pool_id": storage_pool_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "AddDrives",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/StorageServices/{storage_service_id}/Volumes/{volume_id}/AllocatedPools/{storage_pool_id}/Actions/StoragePool.RemoveDrives",
    response_model_exclude_none=True,
)
@authenticate
async def remove_drives5(
    storage_service_id: str,
    volume_id: str,
    storage_pool_id: str,
    request: Request,
    response: Response,
    body: RemoveDrivesRequest,
) -> RedfishError:
    s: Service = get_service(StoragePool, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "volume_id": volume_id,
        "storage_pool_id": storage_pool_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "RemoveDrives",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/StorageServices/{storage_service_id}/Volumes/{volume_id}/AllocatedPools/{storage_pool_id}/Actions/StoragePool.SetCompressionState",
    response_model_exclude_none=True,
)
@authenticate
async def set_compression_state5(
    storage_service_id: str,
    volume_id: str,
    storage_pool_id: str,
    request: Request,
    response: Response,
    body: SetCompressionStateRequest,
) -> RedfishError:
    s: Service = get_service(StoragePool, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "volume_id": volume_id,
        "storage_pool_id": storage_pool_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "SetCompressionState",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/StorageServices/{storage_service_id}/Volumes/{volume_id}/AllocatedPools/{storage_pool_id}/Actions/StoragePool.SetDeduplicationState",
    response_model_exclude_none=True,
)
@authenticate
async def set_deduplication_state5(
    storage_service_id: str,
    volume_id: str,
    storage_pool_id: str,
    request: Request,
    response: Response,
    body: SetDeduplicationStateRequest,
) -> RedfishError:
    s: Service = get_service(StoragePool, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "volume_id": volume_id,
        "storage_pool_id": storage_pool_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "SetDeduplicationState",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/StorageServices/{storage_service_id}/Volumes/{volume_id}/AllocatedPools/{storage_pool_id}/Actions/StoragePool.SetEncryptionState",
    response_model_exclude_none=True,
)
@authenticate
async def set_encryption_state5(
    storage_service_id: str,
    volume_id: str,
    storage_pool_id: str,
    request: Request,
    response: Response,
    body: SetEncryptionStateRequest,
) -> RedfishError:
    s: Service = get_service(StoragePool, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "volume_id": volume_id,
        "storage_pool_id": storage_pool_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "SetEncryptionState",
    }
    return s.action(**b)


@router.delete(
    "/redfish/v1/StorageServices/{storage_service_id}/FileSystems/{file_system_id}/CapacitySources/{capacity_source_id}/ProvidingPools/{storage_pool_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete6(
    storage_service_id: str,
    file_system_id: str,
    capacity_source_id: str,
    storage_pool_id: str,
    request: Request,
    response: Response,
) -> None:
    s: Service = get_service(StoragePool, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "file_system_id": file_system_id,
        "capacity_source_id": capacity_source_id,
        "storage_pool_id": storage_pool_id,
        "request": request,
        "response": response,
    }
    return s.delete(**b)


@router.get(
    "/redfish/v1/StorageServices/{storage_service_id}/FileSystems/{file_system_id}/CapacitySources/{capacity_source_id}/ProvidingPools/{storage_pool_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/StorageServices/{storage_service_id}/FileSystems/{file_system_id}/CapacitySources/{capacity_source_id}/ProvidingPools/{storage_pool_id}",
    response_model_exclude_none=True,
)
async def get6(
    storage_service_id: str,
    file_system_id: str,
    capacity_source_id: str,
    storage_pool_id: str,
    request: Request,
    response: Response,
) -> StoragePool:
    s: Service = get_service(StoragePool, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "file_system_id": file_system_id,
        "capacity_source_id": capacity_source_id,
        "storage_pool_id": storage_pool_id,
        "request": request,
        "response": response,
    }
    return cast(StoragePool, s.get(**b))


@router.patch(
    "/redfish/v1/StorageServices/{storage_service_id}/FileSystems/{file_system_id}/CapacitySources/{capacity_source_id}/ProvidingPools/{storage_pool_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch6(
    storage_service_id: str,
    file_system_id: str,
    capacity_source_id: str,
    storage_pool_id: str,
    request: Request,
    response: Response,
    body: StoragePoolOnUpdate,
) -> StoragePool:
    s: Service = get_service(StoragePool, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "file_system_id": file_system_id,
        "capacity_source_id": capacity_source_id,
        "storage_pool_id": storage_pool_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(StoragePool, s.patch(**b))


@router.post(
    "/redfish/v1/StorageServices/{storage_service_id}/FileSystems/{file_system_id}/CapacitySources/{capacity_source_id}/ProvidingPools/{storage_pool_id}/Actions/StoragePool.AddDrives",
    response_model_exclude_none=True,
)
@authenticate
async def add_drives6(
    storage_service_id: str,
    file_system_id: str,
    capacity_source_id: str,
    storage_pool_id: str,
    request: Request,
    response: Response,
    body: AddDrivesRequest,
) -> RedfishError:
    s: Service = get_service(StoragePool, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "file_system_id": file_system_id,
        "capacity_source_id": capacity_source_id,
        "storage_pool_id": storage_pool_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "AddDrives",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/StorageServices/{storage_service_id}/FileSystems/{file_system_id}/CapacitySources/{capacity_source_id}/ProvidingPools/{storage_pool_id}/Actions/StoragePool.RemoveDrives",
    response_model_exclude_none=True,
)
@authenticate
async def remove_drives6(
    storage_service_id: str,
    file_system_id: str,
    capacity_source_id: str,
    storage_pool_id: str,
    request: Request,
    response: Response,
    body: RemoveDrivesRequest,
) -> RedfishError:
    s: Service = get_service(StoragePool, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "file_system_id": file_system_id,
        "capacity_source_id": capacity_source_id,
        "storage_pool_id": storage_pool_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "RemoveDrives",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/StorageServices/{storage_service_id}/FileSystems/{file_system_id}/CapacitySources/{capacity_source_id}/ProvidingPools/{storage_pool_id}/Actions/StoragePool.SetCompressionState",
    response_model_exclude_none=True,
)
@authenticate
async def set_compression_state6(
    storage_service_id: str,
    file_system_id: str,
    capacity_source_id: str,
    storage_pool_id: str,
    request: Request,
    response: Response,
    body: SetCompressionStateRequest,
) -> RedfishError:
    s: Service = get_service(StoragePool, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "file_system_id": file_system_id,
        "capacity_source_id": capacity_source_id,
        "storage_pool_id": storage_pool_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "SetCompressionState",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/StorageServices/{storage_service_id}/FileSystems/{file_system_id}/CapacitySources/{capacity_source_id}/ProvidingPools/{storage_pool_id}/Actions/StoragePool.SetDeduplicationState",
    response_model_exclude_none=True,
)
@authenticate
async def set_deduplication_state6(
    storage_service_id: str,
    file_system_id: str,
    capacity_source_id: str,
    storage_pool_id: str,
    request: Request,
    response: Response,
    body: SetDeduplicationStateRequest,
) -> RedfishError:
    s: Service = get_service(StoragePool, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "file_system_id": file_system_id,
        "capacity_source_id": capacity_source_id,
        "storage_pool_id": storage_pool_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "SetDeduplicationState",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/StorageServices/{storage_service_id}/FileSystems/{file_system_id}/CapacitySources/{capacity_source_id}/ProvidingPools/{storage_pool_id}/Actions/StoragePool.SetEncryptionState",
    response_model_exclude_none=True,
)
@authenticate
async def set_encryption_state6(
    storage_service_id: str,
    file_system_id: str,
    capacity_source_id: str,
    storage_pool_id: str,
    request: Request,
    response: Response,
    body: SetEncryptionStateRequest,
) -> RedfishError:
    s: Service = get_service(StoragePool, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "file_system_id": file_system_id,
        "capacity_source_id": capacity_source_id,
        "storage_pool_id": storage_pool_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "SetEncryptionState",
    }
    return s.action(**b)


@router.delete(
    "/redfish/v1/Storage/{storage_id}/StoragePools/{storage_pool_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete7(
    storage_id: str, storage_pool_id: str, request: Request, response: Response
) -> None:
    s: Service = get_service(StoragePool, request)
    b: dict[str, Any] = {
        "storage_id": storage_id,
        "storage_pool_id": storage_pool_id,
        "request": request,
        "response": response,
    }
    return s.delete(**b)


@router.get(
    "/redfish/v1/Storage/{storage_id}/StoragePools/{storage_pool_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Storage/{storage_id}/StoragePools/{storage_pool_id}",
    response_model_exclude_none=True,
)
async def get7(
    storage_id: str, storage_pool_id: str, request: Request, response: Response
) -> StoragePool:
    s: Service = get_service(StoragePool, request)
    b: dict[str, Any] = {
        "storage_id": storage_id,
        "storage_pool_id": storage_pool_id,
        "request": request,
        "response": response,
    }
    return cast(StoragePool, s.get(**b))


@router.patch(
    "/redfish/v1/Storage/{storage_id}/StoragePools/{storage_pool_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch7(
    storage_id: str,
    storage_pool_id: str,
    request: Request,
    response: Response,
    body: StoragePoolOnUpdate,
) -> StoragePool:
    s: Service = get_service(StoragePool, request)
    b: dict[str, Any] = {
        "storage_id": storage_id,
        "storage_pool_id": storage_pool_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(StoragePool, s.patch(**b))


@router.post(
    "/redfish/v1/Storage/{storage_id}/StoragePools/{storage_pool_id}/Actions/StoragePool.AddDrives",
    response_model_exclude_none=True,
)
@authenticate
async def add_drives7(
    storage_id: str,
    storage_pool_id: str,
    request: Request,
    response: Response,
    body: AddDrivesRequest,
) -> RedfishError:
    s: Service = get_service(StoragePool, request)
    b: dict[str, Any] = {
        "storage_id": storage_id,
        "storage_pool_id": storage_pool_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "AddDrives",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Storage/{storage_id}/StoragePools/{storage_pool_id}/Actions/StoragePool.RemoveDrives",
    response_model_exclude_none=True,
)
@authenticate
async def remove_drives7(
    storage_id: str,
    storage_pool_id: str,
    request: Request,
    response: Response,
    body: RemoveDrivesRequest,
) -> RedfishError:
    s: Service = get_service(StoragePool, request)
    b: dict[str, Any] = {
        "storage_id": storage_id,
        "storage_pool_id": storage_pool_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "RemoveDrives",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Storage/{storage_id}/StoragePools/{storage_pool_id}/Actions/StoragePool.SetCompressionState",
    response_model_exclude_none=True,
)
@authenticate
async def set_compression_state7(
    storage_id: str,
    storage_pool_id: str,
    request: Request,
    response: Response,
    body: SetCompressionStateRequest,
) -> RedfishError:
    s: Service = get_service(StoragePool, request)
    b: dict[str, Any] = {
        "storage_id": storage_id,
        "storage_pool_id": storage_pool_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "SetCompressionState",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Storage/{storage_id}/StoragePools/{storage_pool_id}/Actions/StoragePool.SetDeduplicationState",
    response_model_exclude_none=True,
)
@authenticate
async def set_deduplication_state7(
    storage_id: str,
    storage_pool_id: str,
    request: Request,
    response: Response,
    body: SetDeduplicationStateRequest,
) -> RedfishError:
    s: Service = get_service(StoragePool, request)
    b: dict[str, Any] = {
        "storage_id": storage_id,
        "storage_pool_id": storage_pool_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "SetDeduplicationState",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Storage/{storage_id}/StoragePools/{storage_pool_id}/Actions/StoragePool.SetEncryptionState",
    response_model_exclude_none=True,
)
@authenticate
async def set_encryption_state7(
    storage_id: str,
    storage_pool_id: str,
    request: Request,
    response: Response,
    body: SetEncryptionStateRequest,
) -> RedfishError:
    s: Service = get_service(StoragePool, request)
    b: dict[str, Any] = {
        "storage_id": storage_id,
        "storage_pool_id": storage_pool_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "SetEncryptionState",
    }
    return s.action(**b)


@router.delete(
    "/redfish/v1/Storage/{storage_id}/StoragePools/{storage_pool_id}/AllocatedPools/{allocated_pool_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete8(
    storage_id: str,
    storage_pool_id: str,
    allocated_pool_id: str,
    request: Request,
    response: Response,
) -> None:
    s: Service = get_service(StoragePool, request)
    b: dict[str, Any] = {
        "storage_id": storage_id,
        "storage_pool_id": storage_pool_id,
        "allocated_pool_id": allocated_pool_id,
        "request": request,
        "response": response,
    }
    return s.delete(**b)


@router.get(
    "/redfish/v1/Storage/{storage_id}/StoragePools/{storage_pool_id}/AllocatedPools/{allocated_pool_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Storage/{storage_id}/StoragePools/{storage_pool_id}/AllocatedPools/{allocated_pool_id}",
    response_model_exclude_none=True,
)
async def get8(
    storage_id: str,
    storage_pool_id: str,
    allocated_pool_id: str,
    request: Request,
    response: Response,
) -> StoragePool:
    s: Service = get_service(StoragePool, request)
    b: dict[str, Any] = {
        "storage_id": storage_id,
        "storage_pool_id": storage_pool_id,
        "allocated_pool_id": allocated_pool_id,
        "request": request,
        "response": response,
    }
    return cast(StoragePool, s.get(**b))


@router.patch(
    "/redfish/v1/Storage/{storage_id}/StoragePools/{storage_pool_id}/AllocatedPools/{allocated_pool_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch8(
    storage_id: str,
    storage_pool_id: str,
    allocated_pool_id: str,
    request: Request,
    response: Response,
    body: StoragePoolOnUpdate,
) -> StoragePool:
    s: Service = get_service(StoragePool, request)
    b: dict[str, Any] = {
        "storage_id": storage_id,
        "storage_pool_id": storage_pool_id,
        "allocated_pool_id": allocated_pool_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(StoragePool, s.patch(**b))


@router.post(
    "/redfish/v1/Storage/{storage_id}/StoragePools/{storage_pool_id}/AllocatedPools/{allocated_pool_id}/Actions/StoragePool.AddDrives",
    response_model_exclude_none=True,
)
@authenticate
async def add_drives8(
    storage_id: str,
    storage_pool_id: str,
    allocated_pool_id: str,
    request: Request,
    response: Response,
    body: AddDrivesRequest,
) -> RedfishError:
    s: Service = get_service(StoragePool, request)
    b: dict[str, Any] = {
        "storage_id": storage_id,
        "storage_pool_id": storage_pool_id,
        "allocated_pool_id": allocated_pool_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "AddDrives",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Storage/{storage_id}/StoragePools/{storage_pool_id}/AllocatedPools/{allocated_pool_id}/Actions/StoragePool.RemoveDrives",
    response_model_exclude_none=True,
)
@authenticate
async def remove_drives8(
    storage_id: str,
    storage_pool_id: str,
    allocated_pool_id: str,
    request: Request,
    response: Response,
    body: RemoveDrivesRequest,
) -> RedfishError:
    s: Service = get_service(StoragePool, request)
    b: dict[str, Any] = {
        "storage_id": storage_id,
        "storage_pool_id": storage_pool_id,
        "allocated_pool_id": allocated_pool_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "RemoveDrives",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Storage/{storage_id}/StoragePools/{storage_pool_id}/AllocatedPools/{allocated_pool_id}/Actions/StoragePool.SetCompressionState",
    response_model_exclude_none=True,
)
@authenticate
async def set_compression_state8(
    storage_id: str,
    storage_pool_id: str,
    allocated_pool_id: str,
    request: Request,
    response: Response,
    body: SetCompressionStateRequest,
) -> RedfishError:
    s: Service = get_service(StoragePool, request)
    b: dict[str, Any] = {
        "storage_id": storage_id,
        "storage_pool_id": storage_pool_id,
        "allocated_pool_id": allocated_pool_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "SetCompressionState",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Storage/{storage_id}/StoragePools/{storage_pool_id}/AllocatedPools/{allocated_pool_id}/Actions/StoragePool.SetDeduplicationState",
    response_model_exclude_none=True,
)
@authenticate
async def set_deduplication_state8(
    storage_id: str,
    storage_pool_id: str,
    allocated_pool_id: str,
    request: Request,
    response: Response,
    body: SetDeduplicationStateRequest,
) -> RedfishError:
    s: Service = get_service(StoragePool, request)
    b: dict[str, Any] = {
        "storage_id": storage_id,
        "storage_pool_id": storage_pool_id,
        "allocated_pool_id": allocated_pool_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "SetDeduplicationState",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Storage/{storage_id}/StoragePools/{storage_pool_id}/AllocatedPools/{allocated_pool_id}/Actions/StoragePool.SetEncryptionState",
    response_model_exclude_none=True,
)
@authenticate
async def set_encryption_state8(
    storage_id: str,
    storage_pool_id: str,
    allocated_pool_id: str,
    request: Request,
    response: Response,
    body: SetEncryptionStateRequest,
) -> RedfishError:
    s: Service = get_service(StoragePool, request)
    b: dict[str, Any] = {
        "storage_id": storage_id,
        "storage_pool_id": storage_pool_id,
        "allocated_pool_id": allocated_pool_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "SetEncryptionState",
    }
    return s.action(**b)


@router.delete(
    "/redfish/v1/Storage/{storage_id}/StoragePools/{storage_pool_id}/CapacitySources/{capacity_source_id}/ProvidingPools/{providing_pool_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete9(
    storage_id: str,
    storage_pool_id: str,
    capacity_source_id: str,
    providing_pool_id: str,
    request: Request,
    response: Response,
) -> None:
    s: Service = get_service(StoragePool, request)
    b: dict[str, Any] = {
        "storage_id": storage_id,
        "storage_pool_id": storage_pool_id,
        "capacity_source_id": capacity_source_id,
        "providing_pool_id": providing_pool_id,
        "request": request,
        "response": response,
    }
    return s.delete(**b)


@router.get(
    "/redfish/v1/Storage/{storage_id}/StoragePools/{storage_pool_id}/CapacitySources/{capacity_source_id}/ProvidingPools/{providing_pool_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Storage/{storage_id}/StoragePools/{storage_pool_id}/CapacitySources/{capacity_source_id}/ProvidingPools/{providing_pool_id}",
    response_model_exclude_none=True,
)
async def get9(
    storage_id: str,
    storage_pool_id: str,
    capacity_source_id: str,
    providing_pool_id: str,
    request: Request,
    response: Response,
) -> StoragePool:
    s: Service = get_service(StoragePool, request)
    b: dict[str, Any] = {
        "storage_id": storage_id,
        "storage_pool_id": storage_pool_id,
        "capacity_source_id": capacity_source_id,
        "providing_pool_id": providing_pool_id,
        "request": request,
        "response": response,
    }
    return cast(StoragePool, s.get(**b))


@router.patch(
    "/redfish/v1/Storage/{storage_id}/StoragePools/{storage_pool_id}/CapacitySources/{capacity_source_id}/ProvidingPools/{providing_pool_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch9(
    storage_id: str,
    storage_pool_id: str,
    capacity_source_id: str,
    providing_pool_id: str,
    request: Request,
    response: Response,
    body: StoragePoolOnUpdate,
) -> StoragePool:
    s: Service = get_service(StoragePool, request)
    b: dict[str, Any] = {
        "storage_id": storage_id,
        "storage_pool_id": storage_pool_id,
        "capacity_source_id": capacity_source_id,
        "providing_pool_id": providing_pool_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(StoragePool, s.patch(**b))


@router.post(
    "/redfish/v1/Storage/{storage_id}/StoragePools/{storage_pool_id}/CapacitySources/{capacity_source_id}/ProvidingPools/{providing_pool_id}/Actions/StoragePool.AddDrives",
    response_model_exclude_none=True,
)
@authenticate
async def add_drives9(
    storage_id: str,
    storage_pool_id: str,
    capacity_source_id: str,
    providing_pool_id: str,
    request: Request,
    response: Response,
    body: AddDrivesRequest,
) -> RedfishError:
    s: Service = get_service(StoragePool, request)
    b: dict[str, Any] = {
        "storage_id": storage_id,
        "storage_pool_id": storage_pool_id,
        "capacity_source_id": capacity_source_id,
        "providing_pool_id": providing_pool_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "AddDrives",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Storage/{storage_id}/StoragePools/{storage_pool_id}/CapacitySources/{capacity_source_id}/ProvidingPools/{providing_pool_id}/Actions/StoragePool.RemoveDrives",
    response_model_exclude_none=True,
)
@authenticate
async def remove_drives9(
    storage_id: str,
    storage_pool_id: str,
    capacity_source_id: str,
    providing_pool_id: str,
    request: Request,
    response: Response,
    body: RemoveDrivesRequest,
) -> RedfishError:
    s: Service = get_service(StoragePool, request)
    b: dict[str, Any] = {
        "storage_id": storage_id,
        "storage_pool_id": storage_pool_id,
        "capacity_source_id": capacity_source_id,
        "providing_pool_id": providing_pool_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "RemoveDrives",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Storage/{storage_id}/StoragePools/{storage_pool_id}/CapacitySources/{capacity_source_id}/ProvidingPools/{providing_pool_id}/Actions/StoragePool.SetCompressionState",
    response_model_exclude_none=True,
)
@authenticate
async def set_compression_state9(
    storage_id: str,
    storage_pool_id: str,
    capacity_source_id: str,
    providing_pool_id: str,
    request: Request,
    response: Response,
    body: SetCompressionStateRequest,
) -> RedfishError:
    s: Service = get_service(StoragePool, request)
    b: dict[str, Any] = {
        "storage_id": storage_id,
        "storage_pool_id": storage_pool_id,
        "capacity_source_id": capacity_source_id,
        "providing_pool_id": providing_pool_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "SetCompressionState",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Storage/{storage_id}/StoragePools/{storage_pool_id}/CapacitySources/{capacity_source_id}/ProvidingPools/{providing_pool_id}/Actions/StoragePool.SetDeduplicationState",
    response_model_exclude_none=True,
)
@authenticate
async def set_deduplication_state9(
    storage_id: str,
    storage_pool_id: str,
    capacity_source_id: str,
    providing_pool_id: str,
    request: Request,
    response: Response,
    body: SetDeduplicationStateRequest,
) -> RedfishError:
    s: Service = get_service(StoragePool, request)
    b: dict[str, Any] = {
        "storage_id": storage_id,
        "storage_pool_id": storage_pool_id,
        "capacity_source_id": capacity_source_id,
        "providing_pool_id": providing_pool_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "SetDeduplicationState",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Storage/{storage_id}/StoragePools/{storage_pool_id}/CapacitySources/{capacity_source_id}/ProvidingPools/{providing_pool_id}/Actions/StoragePool.SetEncryptionState",
    response_model_exclude_none=True,
)
@authenticate
async def set_encryption_state9(
    storage_id: str,
    storage_pool_id: str,
    capacity_source_id: str,
    providing_pool_id: str,
    request: Request,
    response: Response,
    body: SetEncryptionStateRequest,
) -> RedfishError:
    s: Service = get_service(StoragePool, request)
    b: dict[str, Any] = {
        "storage_id": storage_id,
        "storage_pool_id": storage_pool_id,
        "capacity_source_id": capacity_source_id,
        "providing_pool_id": providing_pool_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "SetEncryptionState",
    }
    return s.action(**b)


@router.delete(
    "/redfish/v1/Storage/{storage_id}/Volumes/{volume_id}/CapacitySources/{capacity_source_id}/ProvidingPools/{storage_pool_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete10(
    storage_id: str,
    volume_id: str,
    capacity_source_id: str,
    storage_pool_id: str,
    request: Request,
    response: Response,
) -> None:
    s: Service = get_service(StoragePool, request)
    b: dict[str, Any] = {
        "storage_id": storage_id,
        "volume_id": volume_id,
        "capacity_source_id": capacity_source_id,
        "storage_pool_id": storage_pool_id,
        "request": request,
        "response": response,
    }
    return s.delete(**b)


@router.get(
    "/redfish/v1/Storage/{storage_id}/Volumes/{volume_id}/CapacitySources/{capacity_source_id}/ProvidingPools/{storage_pool_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Storage/{storage_id}/Volumes/{volume_id}/CapacitySources/{capacity_source_id}/ProvidingPools/{storage_pool_id}",
    response_model_exclude_none=True,
)
async def get10(
    storage_id: str,
    volume_id: str,
    capacity_source_id: str,
    storage_pool_id: str,
    request: Request,
    response: Response,
) -> StoragePool:
    s: Service = get_service(StoragePool, request)
    b: dict[str, Any] = {
        "storage_id": storage_id,
        "volume_id": volume_id,
        "capacity_source_id": capacity_source_id,
        "storage_pool_id": storage_pool_id,
        "request": request,
        "response": response,
    }
    return cast(StoragePool, s.get(**b))


@router.patch(
    "/redfish/v1/Storage/{storage_id}/Volumes/{volume_id}/CapacitySources/{capacity_source_id}/ProvidingPools/{storage_pool_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch10(
    storage_id: str,
    volume_id: str,
    capacity_source_id: str,
    storage_pool_id: str,
    request: Request,
    response: Response,
    body: StoragePoolOnUpdate,
) -> StoragePool:
    s: Service = get_service(StoragePool, request)
    b: dict[str, Any] = {
        "storage_id": storage_id,
        "volume_id": volume_id,
        "capacity_source_id": capacity_source_id,
        "storage_pool_id": storage_pool_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(StoragePool, s.patch(**b))


@router.post(
    "/redfish/v1/Storage/{storage_id}/Volumes/{volume_id}/CapacitySources/{capacity_source_id}/ProvidingPools/{storage_pool_id}/Actions/StoragePool.AddDrives",
    response_model_exclude_none=True,
)
@authenticate
async def add_drives10(
    storage_id: str,
    volume_id: str,
    capacity_source_id: str,
    storage_pool_id: str,
    request: Request,
    response: Response,
    body: AddDrivesRequest,
) -> RedfishError:
    s: Service = get_service(StoragePool, request)
    b: dict[str, Any] = {
        "storage_id": storage_id,
        "volume_id": volume_id,
        "capacity_source_id": capacity_source_id,
        "storage_pool_id": storage_pool_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "AddDrives",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Storage/{storage_id}/Volumes/{volume_id}/CapacitySources/{capacity_source_id}/ProvidingPools/{storage_pool_id}/Actions/StoragePool.RemoveDrives",
    response_model_exclude_none=True,
)
@authenticate
async def remove_drives10(
    storage_id: str,
    volume_id: str,
    capacity_source_id: str,
    storage_pool_id: str,
    request: Request,
    response: Response,
    body: RemoveDrivesRequest,
) -> RedfishError:
    s: Service = get_service(StoragePool, request)
    b: dict[str, Any] = {
        "storage_id": storage_id,
        "volume_id": volume_id,
        "capacity_source_id": capacity_source_id,
        "storage_pool_id": storage_pool_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "RemoveDrives",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Storage/{storage_id}/Volumes/{volume_id}/CapacitySources/{capacity_source_id}/ProvidingPools/{storage_pool_id}/Actions/StoragePool.SetCompressionState",
    response_model_exclude_none=True,
)
@authenticate
async def set_compression_state10(
    storage_id: str,
    volume_id: str,
    capacity_source_id: str,
    storage_pool_id: str,
    request: Request,
    response: Response,
    body: SetCompressionStateRequest,
) -> RedfishError:
    s: Service = get_service(StoragePool, request)
    b: dict[str, Any] = {
        "storage_id": storage_id,
        "volume_id": volume_id,
        "capacity_source_id": capacity_source_id,
        "storage_pool_id": storage_pool_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "SetCompressionState",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Storage/{storage_id}/Volumes/{volume_id}/CapacitySources/{capacity_source_id}/ProvidingPools/{storage_pool_id}/Actions/StoragePool.SetDeduplicationState",
    response_model_exclude_none=True,
)
@authenticate
async def set_deduplication_state10(
    storage_id: str,
    volume_id: str,
    capacity_source_id: str,
    storage_pool_id: str,
    request: Request,
    response: Response,
    body: SetDeduplicationStateRequest,
) -> RedfishError:
    s: Service = get_service(StoragePool, request)
    b: dict[str, Any] = {
        "storage_id": storage_id,
        "volume_id": volume_id,
        "capacity_source_id": capacity_source_id,
        "storage_pool_id": storage_pool_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "SetDeduplicationState",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Storage/{storage_id}/Volumes/{volume_id}/CapacitySources/{capacity_source_id}/ProvidingPools/{storage_pool_id}/Actions/StoragePool.SetEncryptionState",
    response_model_exclude_none=True,
)
@authenticate
async def set_encryption_state10(
    storage_id: str,
    volume_id: str,
    capacity_source_id: str,
    storage_pool_id: str,
    request: Request,
    response: Response,
    body: SetEncryptionStateRequest,
) -> RedfishError:
    s: Service = get_service(StoragePool, request)
    b: dict[str, Any] = {
        "storage_id": storage_id,
        "volume_id": volume_id,
        "capacity_source_id": capacity_source_id,
        "storage_pool_id": storage_pool_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "SetEncryptionState",
    }
    return s.action(**b)


@router.delete(
    "/redfish/v1/Storage/{storage_id}/Volumes/{volume_id}/AllocatedPools/{storage_pool_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete11(
    storage_id: str, volume_id: str, storage_pool_id: str, request: Request, response: Response
) -> None:
    s: Service = get_service(StoragePool, request)
    b: dict[str, Any] = {
        "storage_id": storage_id,
        "volume_id": volume_id,
        "storage_pool_id": storage_pool_id,
        "request": request,
        "response": response,
    }
    return s.delete(**b)


@router.get(
    "/redfish/v1/Storage/{storage_id}/Volumes/{volume_id}/AllocatedPools/{storage_pool_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Storage/{storage_id}/Volumes/{volume_id}/AllocatedPools/{storage_pool_id}",
    response_model_exclude_none=True,
)
async def get11(
    storage_id: str, volume_id: str, storage_pool_id: str, request: Request, response: Response
) -> StoragePool:
    s: Service = get_service(StoragePool, request)
    b: dict[str, Any] = {
        "storage_id": storage_id,
        "volume_id": volume_id,
        "storage_pool_id": storage_pool_id,
        "request": request,
        "response": response,
    }
    return cast(StoragePool, s.get(**b))


@router.patch(
    "/redfish/v1/Storage/{storage_id}/Volumes/{volume_id}/AllocatedPools/{storage_pool_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch11(
    storage_id: str,
    volume_id: str,
    storage_pool_id: str,
    request: Request,
    response: Response,
    body: StoragePoolOnUpdate,
) -> StoragePool:
    s: Service = get_service(StoragePool, request)
    b: dict[str, Any] = {
        "storage_id": storage_id,
        "volume_id": volume_id,
        "storage_pool_id": storage_pool_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(StoragePool, s.patch(**b))


@router.post(
    "/redfish/v1/Storage/{storage_id}/Volumes/{volume_id}/AllocatedPools/{storage_pool_id}/Actions/StoragePool.AddDrives",
    response_model_exclude_none=True,
)
@authenticate
async def add_drives11(
    storage_id: str,
    volume_id: str,
    storage_pool_id: str,
    request: Request,
    response: Response,
    body: AddDrivesRequest,
) -> RedfishError:
    s: Service = get_service(StoragePool, request)
    b: dict[str, Any] = {
        "storage_id": storage_id,
        "volume_id": volume_id,
        "storage_pool_id": storage_pool_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "AddDrives",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Storage/{storage_id}/Volumes/{volume_id}/AllocatedPools/{storage_pool_id}/Actions/StoragePool.RemoveDrives",
    response_model_exclude_none=True,
)
@authenticate
async def remove_drives11(
    storage_id: str,
    volume_id: str,
    storage_pool_id: str,
    request: Request,
    response: Response,
    body: RemoveDrivesRequest,
) -> RedfishError:
    s: Service = get_service(StoragePool, request)
    b: dict[str, Any] = {
        "storage_id": storage_id,
        "volume_id": volume_id,
        "storage_pool_id": storage_pool_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "RemoveDrives",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Storage/{storage_id}/Volumes/{volume_id}/AllocatedPools/{storage_pool_id}/Actions/StoragePool.SetCompressionState",
    response_model_exclude_none=True,
)
@authenticate
async def set_compression_state11(
    storage_id: str,
    volume_id: str,
    storage_pool_id: str,
    request: Request,
    response: Response,
    body: SetCompressionStateRequest,
) -> RedfishError:
    s: Service = get_service(StoragePool, request)
    b: dict[str, Any] = {
        "storage_id": storage_id,
        "volume_id": volume_id,
        "storage_pool_id": storage_pool_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "SetCompressionState",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Storage/{storage_id}/Volumes/{volume_id}/AllocatedPools/{storage_pool_id}/Actions/StoragePool.SetDeduplicationState",
    response_model_exclude_none=True,
)
@authenticate
async def set_deduplication_state11(
    storage_id: str,
    volume_id: str,
    storage_pool_id: str,
    request: Request,
    response: Response,
    body: SetDeduplicationStateRequest,
) -> RedfishError:
    s: Service = get_service(StoragePool, request)
    b: dict[str, Any] = {
        "storage_id": storage_id,
        "volume_id": volume_id,
        "storage_pool_id": storage_pool_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "SetDeduplicationState",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Storage/{storage_id}/Volumes/{volume_id}/AllocatedPools/{storage_pool_id}/Actions/StoragePool.SetEncryptionState",
    response_model_exclude_none=True,
)
@authenticate
async def set_encryption_state11(
    storage_id: str,
    volume_id: str,
    storage_pool_id: str,
    request: Request,
    response: Response,
    body: SetEncryptionStateRequest,
) -> RedfishError:
    s: Service = get_service(StoragePool, request)
    b: dict[str, Any] = {
        "storage_id": storage_id,
        "volume_id": volume_id,
        "storage_pool_id": storage_pool_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "SetEncryptionState",
    }
    return s.action(**b)


@router.delete(
    "/redfish/v1/Storage/{storage_id}/FileSystems/{file_system_id}/CapacitySources/{capacity_source_id}/ProvidingPools/{storage_pool_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete12(
    storage_id: str,
    file_system_id: str,
    capacity_source_id: str,
    storage_pool_id: str,
    request: Request,
    response: Response,
) -> None:
    s: Service = get_service(StoragePool, request)
    b: dict[str, Any] = {
        "storage_id": storage_id,
        "file_system_id": file_system_id,
        "capacity_source_id": capacity_source_id,
        "storage_pool_id": storage_pool_id,
        "request": request,
        "response": response,
    }
    return s.delete(**b)


@router.get(
    "/redfish/v1/Storage/{storage_id}/FileSystems/{file_system_id}/CapacitySources/{capacity_source_id}/ProvidingPools/{storage_pool_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Storage/{storage_id}/FileSystems/{file_system_id}/CapacitySources/{capacity_source_id}/ProvidingPools/{storage_pool_id}",
    response_model_exclude_none=True,
)
async def get12(
    storage_id: str,
    file_system_id: str,
    capacity_source_id: str,
    storage_pool_id: str,
    request: Request,
    response: Response,
) -> StoragePool:
    s: Service = get_service(StoragePool, request)
    b: dict[str, Any] = {
        "storage_id": storage_id,
        "file_system_id": file_system_id,
        "capacity_source_id": capacity_source_id,
        "storage_pool_id": storage_pool_id,
        "request": request,
        "response": response,
    }
    return cast(StoragePool, s.get(**b))


@router.patch(
    "/redfish/v1/Storage/{storage_id}/FileSystems/{file_system_id}/CapacitySources/{capacity_source_id}/ProvidingPools/{storage_pool_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch12(
    storage_id: str,
    file_system_id: str,
    capacity_source_id: str,
    storage_pool_id: str,
    request: Request,
    response: Response,
    body: StoragePoolOnUpdate,
) -> StoragePool:
    s: Service = get_service(StoragePool, request)
    b: dict[str, Any] = {
        "storage_id": storage_id,
        "file_system_id": file_system_id,
        "capacity_source_id": capacity_source_id,
        "storage_pool_id": storage_pool_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(StoragePool, s.patch(**b))


@router.post(
    "/redfish/v1/Storage/{storage_id}/FileSystems/{file_system_id}/CapacitySources/{capacity_source_id}/ProvidingPools/{storage_pool_id}/Actions/StoragePool.AddDrives",
    response_model_exclude_none=True,
)
@authenticate
async def add_drives12(
    storage_id: str,
    file_system_id: str,
    capacity_source_id: str,
    storage_pool_id: str,
    request: Request,
    response: Response,
    body: AddDrivesRequest,
) -> RedfishError:
    s: Service = get_service(StoragePool, request)
    b: dict[str, Any] = {
        "storage_id": storage_id,
        "file_system_id": file_system_id,
        "capacity_source_id": capacity_source_id,
        "storage_pool_id": storage_pool_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "AddDrives",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Storage/{storage_id}/FileSystems/{file_system_id}/CapacitySources/{capacity_source_id}/ProvidingPools/{storage_pool_id}/Actions/StoragePool.RemoveDrives",
    response_model_exclude_none=True,
)
@authenticate
async def remove_drives12(
    storage_id: str,
    file_system_id: str,
    capacity_source_id: str,
    storage_pool_id: str,
    request: Request,
    response: Response,
    body: RemoveDrivesRequest,
) -> RedfishError:
    s: Service = get_service(StoragePool, request)
    b: dict[str, Any] = {
        "storage_id": storage_id,
        "file_system_id": file_system_id,
        "capacity_source_id": capacity_source_id,
        "storage_pool_id": storage_pool_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "RemoveDrives",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Storage/{storage_id}/FileSystems/{file_system_id}/CapacitySources/{capacity_source_id}/ProvidingPools/{storage_pool_id}/Actions/StoragePool.SetCompressionState",
    response_model_exclude_none=True,
)
@authenticate
async def set_compression_state12(
    storage_id: str,
    file_system_id: str,
    capacity_source_id: str,
    storage_pool_id: str,
    request: Request,
    response: Response,
    body: SetCompressionStateRequest,
) -> RedfishError:
    s: Service = get_service(StoragePool, request)
    b: dict[str, Any] = {
        "storage_id": storage_id,
        "file_system_id": file_system_id,
        "capacity_source_id": capacity_source_id,
        "storage_pool_id": storage_pool_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "SetCompressionState",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Storage/{storage_id}/FileSystems/{file_system_id}/CapacitySources/{capacity_source_id}/ProvidingPools/{storage_pool_id}/Actions/StoragePool.SetDeduplicationState",
    response_model_exclude_none=True,
)
@authenticate
async def set_deduplication_state12(
    storage_id: str,
    file_system_id: str,
    capacity_source_id: str,
    storage_pool_id: str,
    request: Request,
    response: Response,
    body: SetDeduplicationStateRequest,
) -> RedfishError:
    s: Service = get_service(StoragePool, request)
    b: dict[str, Any] = {
        "storage_id": storage_id,
        "file_system_id": file_system_id,
        "capacity_source_id": capacity_source_id,
        "storage_pool_id": storage_pool_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "SetDeduplicationState",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Storage/{storage_id}/FileSystems/{file_system_id}/CapacitySources/{capacity_source_id}/ProvidingPools/{storage_pool_id}/Actions/StoragePool.SetEncryptionState",
    response_model_exclude_none=True,
)
@authenticate
async def set_encryption_state12(
    storage_id: str,
    file_system_id: str,
    capacity_source_id: str,
    storage_pool_id: str,
    request: Request,
    response: Response,
    body: SetEncryptionStateRequest,
) -> RedfishError:
    s: Service = get_service(StoragePool, request)
    b: dict[str, Any] = {
        "storage_id": storage_id,
        "file_system_id": file_system_id,
        "capacity_source_id": capacity_source_id,
        "storage_pool_id": storage_pool_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "SetEncryptionState",
    }
    return s.action(**b)


@router.delete(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/StoragePools/{storage_pool_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete13(
    computer_system_id: str,
    storage_id: str,
    storage_pool_id: str,
    request: Request,
    response: Response,
) -> None:
    s: Service = get_service(StoragePool, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "storage_pool_id": storage_pool_id,
        "request": request,
        "response": response,
    }
    return s.delete(**b)


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/StoragePools/{storage_pool_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/StoragePools/{storage_pool_id}",
    response_model_exclude_none=True,
)
async def get13(
    computer_system_id: str,
    storage_id: str,
    storage_pool_id: str,
    request: Request,
    response: Response,
) -> StoragePool:
    s: Service = get_service(StoragePool, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "storage_pool_id": storage_pool_id,
        "request": request,
        "response": response,
    }
    return cast(StoragePool, s.get(**b))


@router.patch(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/StoragePools/{storage_pool_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch13(
    computer_system_id: str,
    storage_id: str,
    storage_pool_id: str,
    request: Request,
    response: Response,
    body: StoragePoolOnUpdate,
) -> StoragePool:
    s: Service = get_service(StoragePool, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "storage_pool_id": storage_pool_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(StoragePool, s.patch(**b))


@router.post(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/StoragePools/{storage_pool_id}/Actions/StoragePool.AddDrives",
    response_model_exclude_none=True,
)
@authenticate
async def add_drives13(
    computer_system_id: str,
    storage_id: str,
    storage_pool_id: str,
    request: Request,
    response: Response,
    body: AddDrivesRequest,
) -> RedfishError:
    s: Service = get_service(StoragePool, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "storage_pool_id": storage_pool_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "AddDrives",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/StoragePools/{storage_pool_id}/Actions/StoragePool.RemoveDrives",
    response_model_exclude_none=True,
)
@authenticate
async def remove_drives13(
    computer_system_id: str,
    storage_id: str,
    storage_pool_id: str,
    request: Request,
    response: Response,
    body: RemoveDrivesRequest,
) -> RedfishError:
    s: Service = get_service(StoragePool, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "storage_pool_id": storage_pool_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "RemoveDrives",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/StoragePools/{storage_pool_id}/Actions/StoragePool.SetCompressionState",
    response_model_exclude_none=True,
)
@authenticate
async def set_compression_state13(
    computer_system_id: str,
    storage_id: str,
    storage_pool_id: str,
    request: Request,
    response: Response,
    body: SetCompressionStateRequest,
) -> RedfishError:
    s: Service = get_service(StoragePool, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "storage_pool_id": storage_pool_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "SetCompressionState",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/StoragePools/{storage_pool_id}/Actions/StoragePool.SetDeduplicationState",
    response_model_exclude_none=True,
)
@authenticate
async def set_deduplication_state13(
    computer_system_id: str,
    storage_id: str,
    storage_pool_id: str,
    request: Request,
    response: Response,
    body: SetDeduplicationStateRequest,
) -> RedfishError:
    s: Service = get_service(StoragePool, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "storage_pool_id": storage_pool_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "SetDeduplicationState",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/StoragePools/{storage_pool_id}/Actions/StoragePool.SetEncryptionState",
    response_model_exclude_none=True,
)
@authenticate
async def set_encryption_state13(
    computer_system_id: str,
    storage_id: str,
    storage_pool_id: str,
    request: Request,
    response: Response,
    body: SetEncryptionStateRequest,
) -> RedfishError:
    s: Service = get_service(StoragePool, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "storage_pool_id": storage_pool_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "SetEncryptionState",
    }
    return s.action(**b)


@router.delete(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/StoragePools/{storage_pool_id}/AllocatedPools/{allocated_pool_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete14(
    computer_system_id: str,
    storage_id: str,
    storage_pool_id: str,
    allocated_pool_id: str,
    request: Request,
    response: Response,
) -> None:
    s: Service = get_service(StoragePool, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "storage_pool_id": storage_pool_id,
        "allocated_pool_id": allocated_pool_id,
        "request": request,
        "response": response,
    }
    return s.delete(**b)


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/StoragePools/{storage_pool_id}/AllocatedPools/{allocated_pool_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/StoragePools/{storage_pool_id}/AllocatedPools/{allocated_pool_id}",
    response_model_exclude_none=True,
)
async def get14(
    computer_system_id: str,
    storage_id: str,
    storage_pool_id: str,
    allocated_pool_id: str,
    request: Request,
    response: Response,
) -> StoragePool:
    s: Service = get_service(StoragePool, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "storage_pool_id": storage_pool_id,
        "allocated_pool_id": allocated_pool_id,
        "request": request,
        "response": response,
    }
    return cast(StoragePool, s.get(**b))


@router.patch(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/StoragePools/{storage_pool_id}/AllocatedPools/{allocated_pool_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch14(
    computer_system_id: str,
    storage_id: str,
    storage_pool_id: str,
    allocated_pool_id: str,
    request: Request,
    response: Response,
    body: StoragePoolOnUpdate,
) -> StoragePool:
    s: Service = get_service(StoragePool, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "storage_pool_id": storage_pool_id,
        "allocated_pool_id": allocated_pool_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(StoragePool, s.patch(**b))


@router.post(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/StoragePools/{storage_pool_id}/AllocatedPools/{allocated_pool_id}/Actions/StoragePool.AddDrives",
    response_model_exclude_none=True,
)
@authenticate
async def add_drives14(
    computer_system_id: str,
    storage_id: str,
    storage_pool_id: str,
    allocated_pool_id: str,
    request: Request,
    response: Response,
    body: AddDrivesRequest,
) -> RedfishError:
    s: Service = get_service(StoragePool, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "storage_pool_id": storage_pool_id,
        "allocated_pool_id": allocated_pool_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "AddDrives",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/StoragePools/{storage_pool_id}/AllocatedPools/{allocated_pool_id}/Actions/StoragePool.RemoveDrives",
    response_model_exclude_none=True,
)
@authenticate
async def remove_drives14(
    computer_system_id: str,
    storage_id: str,
    storage_pool_id: str,
    allocated_pool_id: str,
    request: Request,
    response: Response,
    body: RemoveDrivesRequest,
) -> RedfishError:
    s: Service = get_service(StoragePool, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "storage_pool_id": storage_pool_id,
        "allocated_pool_id": allocated_pool_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "RemoveDrives",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/StoragePools/{storage_pool_id}/AllocatedPools/{allocated_pool_id}/Actions/StoragePool.SetCompressionState",
    response_model_exclude_none=True,
)
@authenticate
async def set_compression_state14(
    computer_system_id: str,
    storage_id: str,
    storage_pool_id: str,
    allocated_pool_id: str,
    request: Request,
    response: Response,
    body: SetCompressionStateRequest,
) -> RedfishError:
    s: Service = get_service(StoragePool, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "storage_pool_id": storage_pool_id,
        "allocated_pool_id": allocated_pool_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "SetCompressionState",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/StoragePools/{storage_pool_id}/AllocatedPools/{allocated_pool_id}/Actions/StoragePool.SetDeduplicationState",
    response_model_exclude_none=True,
)
@authenticate
async def set_deduplication_state14(
    computer_system_id: str,
    storage_id: str,
    storage_pool_id: str,
    allocated_pool_id: str,
    request: Request,
    response: Response,
    body: SetDeduplicationStateRequest,
) -> RedfishError:
    s: Service = get_service(StoragePool, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "storage_pool_id": storage_pool_id,
        "allocated_pool_id": allocated_pool_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "SetDeduplicationState",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/StoragePools/{storage_pool_id}/AllocatedPools/{allocated_pool_id}/Actions/StoragePool.SetEncryptionState",
    response_model_exclude_none=True,
)
@authenticate
async def set_encryption_state14(
    computer_system_id: str,
    storage_id: str,
    storage_pool_id: str,
    allocated_pool_id: str,
    request: Request,
    response: Response,
    body: SetEncryptionStateRequest,
) -> RedfishError:
    s: Service = get_service(StoragePool, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "storage_pool_id": storage_pool_id,
        "allocated_pool_id": allocated_pool_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "SetEncryptionState",
    }
    return s.action(**b)


@router.delete(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/StoragePools/{storage_pool_id}/CapacitySources/{capacity_source_id}/ProvidingPools/{providing_pool_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete15(
    computer_system_id: str,
    storage_id: str,
    storage_pool_id: str,
    capacity_source_id: str,
    providing_pool_id: str,
    request: Request,
    response: Response,
) -> None:
    s: Service = get_service(StoragePool, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "storage_pool_id": storage_pool_id,
        "capacity_source_id": capacity_source_id,
        "providing_pool_id": providing_pool_id,
        "request": request,
        "response": response,
    }
    return s.delete(**b)


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/StoragePools/{storage_pool_id}/CapacitySources/{capacity_source_id}/ProvidingPools/{providing_pool_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/StoragePools/{storage_pool_id}/CapacitySources/{capacity_source_id}/ProvidingPools/{providing_pool_id}",
    response_model_exclude_none=True,
)
async def get15(
    computer_system_id: str,
    storage_id: str,
    storage_pool_id: str,
    capacity_source_id: str,
    providing_pool_id: str,
    request: Request,
    response: Response,
) -> StoragePool:
    s: Service = get_service(StoragePool, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "storage_pool_id": storage_pool_id,
        "capacity_source_id": capacity_source_id,
        "providing_pool_id": providing_pool_id,
        "request": request,
        "response": response,
    }
    return cast(StoragePool, s.get(**b))


@router.patch(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/StoragePools/{storage_pool_id}/CapacitySources/{capacity_source_id}/ProvidingPools/{providing_pool_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch15(
    computer_system_id: str,
    storage_id: str,
    storage_pool_id: str,
    capacity_source_id: str,
    providing_pool_id: str,
    request: Request,
    response: Response,
    body: StoragePoolOnUpdate,
) -> StoragePool:
    s: Service = get_service(StoragePool, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "storage_pool_id": storage_pool_id,
        "capacity_source_id": capacity_source_id,
        "providing_pool_id": providing_pool_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(StoragePool, s.patch(**b))


@router.post(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/StoragePools/{storage_pool_id}/CapacitySources/{capacity_source_id}/ProvidingPools/{providing_pool_id}/Actions/StoragePool.AddDrives",
    response_model_exclude_none=True,
)
@authenticate
async def add_drives15(
    computer_system_id: str,
    storage_id: str,
    storage_pool_id: str,
    capacity_source_id: str,
    providing_pool_id: str,
    request: Request,
    response: Response,
    body: AddDrivesRequest,
) -> RedfishError:
    s: Service = get_service(StoragePool, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "storage_pool_id": storage_pool_id,
        "capacity_source_id": capacity_source_id,
        "providing_pool_id": providing_pool_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "AddDrives",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/StoragePools/{storage_pool_id}/CapacitySources/{capacity_source_id}/ProvidingPools/{providing_pool_id}/Actions/StoragePool.RemoveDrives",
    response_model_exclude_none=True,
)
@authenticate
async def remove_drives15(
    computer_system_id: str,
    storage_id: str,
    storage_pool_id: str,
    capacity_source_id: str,
    providing_pool_id: str,
    request: Request,
    response: Response,
    body: RemoveDrivesRequest,
) -> RedfishError:
    s: Service = get_service(StoragePool, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "storage_pool_id": storage_pool_id,
        "capacity_source_id": capacity_source_id,
        "providing_pool_id": providing_pool_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "RemoveDrives",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/StoragePools/{storage_pool_id}/CapacitySources/{capacity_source_id}/ProvidingPools/{providing_pool_id}/Actions/StoragePool.SetCompressionState",
    response_model_exclude_none=True,
)
@authenticate
async def set_compression_state15(
    computer_system_id: str,
    storage_id: str,
    storage_pool_id: str,
    capacity_source_id: str,
    providing_pool_id: str,
    request: Request,
    response: Response,
    body: SetCompressionStateRequest,
) -> RedfishError:
    s: Service = get_service(StoragePool, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "storage_pool_id": storage_pool_id,
        "capacity_source_id": capacity_source_id,
        "providing_pool_id": providing_pool_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "SetCompressionState",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/StoragePools/{storage_pool_id}/CapacitySources/{capacity_source_id}/ProvidingPools/{providing_pool_id}/Actions/StoragePool.SetDeduplicationState",
    response_model_exclude_none=True,
)
@authenticate
async def set_deduplication_state15(
    computer_system_id: str,
    storage_id: str,
    storage_pool_id: str,
    capacity_source_id: str,
    providing_pool_id: str,
    request: Request,
    response: Response,
    body: SetDeduplicationStateRequest,
) -> RedfishError:
    s: Service = get_service(StoragePool, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "storage_pool_id": storage_pool_id,
        "capacity_source_id": capacity_source_id,
        "providing_pool_id": providing_pool_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "SetDeduplicationState",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/StoragePools/{storage_pool_id}/CapacitySources/{capacity_source_id}/ProvidingPools/{providing_pool_id}/Actions/StoragePool.SetEncryptionState",
    response_model_exclude_none=True,
)
@authenticate
async def set_encryption_state15(
    computer_system_id: str,
    storage_id: str,
    storage_pool_id: str,
    capacity_source_id: str,
    providing_pool_id: str,
    request: Request,
    response: Response,
    body: SetEncryptionStateRequest,
) -> RedfishError:
    s: Service = get_service(StoragePool, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "storage_pool_id": storage_pool_id,
        "capacity_source_id": capacity_source_id,
        "providing_pool_id": providing_pool_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "SetEncryptionState",
    }
    return s.action(**b)


@router.delete(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/Volumes/{volume_id}/CapacitySources/{capacity_source_id}/ProvidingPools/{storage_pool_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete16(
    computer_system_id: str,
    storage_id: str,
    volume_id: str,
    capacity_source_id: str,
    storage_pool_id: str,
    request: Request,
    response: Response,
) -> None:
    s: Service = get_service(StoragePool, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "volume_id": volume_id,
        "capacity_source_id": capacity_source_id,
        "storage_pool_id": storage_pool_id,
        "request": request,
        "response": response,
    }
    return s.delete(**b)


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/Volumes/{volume_id}/CapacitySources/{capacity_source_id}/ProvidingPools/{storage_pool_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/Volumes/{volume_id}/CapacitySources/{capacity_source_id}/ProvidingPools/{storage_pool_id}",
    response_model_exclude_none=True,
)
async def get16(
    computer_system_id: str,
    storage_id: str,
    volume_id: str,
    capacity_source_id: str,
    storage_pool_id: str,
    request: Request,
    response: Response,
) -> StoragePool:
    s: Service = get_service(StoragePool, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "volume_id": volume_id,
        "capacity_source_id": capacity_source_id,
        "storage_pool_id": storage_pool_id,
        "request": request,
        "response": response,
    }
    return cast(StoragePool, s.get(**b))


@router.patch(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/Volumes/{volume_id}/CapacitySources/{capacity_source_id}/ProvidingPools/{storage_pool_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch16(
    computer_system_id: str,
    storage_id: str,
    volume_id: str,
    capacity_source_id: str,
    storage_pool_id: str,
    request: Request,
    response: Response,
    body: StoragePoolOnUpdate,
) -> StoragePool:
    s: Service = get_service(StoragePool, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "volume_id": volume_id,
        "capacity_source_id": capacity_source_id,
        "storage_pool_id": storage_pool_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(StoragePool, s.patch(**b))


@router.post(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/Volumes/{volume_id}/CapacitySources/{capacity_source_id}/ProvidingPools/{storage_pool_id}/Actions/StoragePool.AddDrives",
    response_model_exclude_none=True,
)
@authenticate
async def add_drives16(
    computer_system_id: str,
    storage_id: str,
    volume_id: str,
    capacity_source_id: str,
    storage_pool_id: str,
    request: Request,
    response: Response,
    body: AddDrivesRequest,
) -> RedfishError:
    s: Service = get_service(StoragePool, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "volume_id": volume_id,
        "capacity_source_id": capacity_source_id,
        "storage_pool_id": storage_pool_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "AddDrives",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/Volumes/{volume_id}/CapacitySources/{capacity_source_id}/ProvidingPools/{storage_pool_id}/Actions/StoragePool.RemoveDrives",
    response_model_exclude_none=True,
)
@authenticate
async def remove_drives16(
    computer_system_id: str,
    storage_id: str,
    volume_id: str,
    capacity_source_id: str,
    storage_pool_id: str,
    request: Request,
    response: Response,
    body: RemoveDrivesRequest,
) -> RedfishError:
    s: Service = get_service(StoragePool, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "volume_id": volume_id,
        "capacity_source_id": capacity_source_id,
        "storage_pool_id": storage_pool_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "RemoveDrives",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/Volumes/{volume_id}/CapacitySources/{capacity_source_id}/ProvidingPools/{storage_pool_id}/Actions/StoragePool.SetCompressionState",
    response_model_exclude_none=True,
)
@authenticate
async def set_compression_state16(
    computer_system_id: str,
    storage_id: str,
    volume_id: str,
    capacity_source_id: str,
    storage_pool_id: str,
    request: Request,
    response: Response,
    body: SetCompressionStateRequest,
) -> RedfishError:
    s: Service = get_service(StoragePool, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "volume_id": volume_id,
        "capacity_source_id": capacity_source_id,
        "storage_pool_id": storage_pool_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "SetCompressionState",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/Volumes/{volume_id}/CapacitySources/{capacity_source_id}/ProvidingPools/{storage_pool_id}/Actions/StoragePool.SetDeduplicationState",
    response_model_exclude_none=True,
)
@authenticate
async def set_deduplication_state16(
    computer_system_id: str,
    storage_id: str,
    volume_id: str,
    capacity_source_id: str,
    storage_pool_id: str,
    request: Request,
    response: Response,
    body: SetDeduplicationStateRequest,
) -> RedfishError:
    s: Service = get_service(StoragePool, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "volume_id": volume_id,
        "capacity_source_id": capacity_source_id,
        "storage_pool_id": storage_pool_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "SetDeduplicationState",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/Volumes/{volume_id}/CapacitySources/{capacity_source_id}/ProvidingPools/{storage_pool_id}/Actions/StoragePool.SetEncryptionState",
    response_model_exclude_none=True,
)
@authenticate
async def set_encryption_state16(
    computer_system_id: str,
    storage_id: str,
    volume_id: str,
    capacity_source_id: str,
    storage_pool_id: str,
    request: Request,
    response: Response,
    body: SetEncryptionStateRequest,
) -> RedfishError:
    s: Service = get_service(StoragePool, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "volume_id": volume_id,
        "capacity_source_id": capacity_source_id,
        "storage_pool_id": storage_pool_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "SetEncryptionState",
    }
    return s.action(**b)


@router.delete(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/Volumes/{volume_id}/AllocatedPools/{storage_pool_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete17(
    computer_system_id: str,
    storage_id: str,
    volume_id: str,
    storage_pool_id: str,
    request: Request,
    response: Response,
) -> None:
    s: Service = get_service(StoragePool, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "volume_id": volume_id,
        "storage_pool_id": storage_pool_id,
        "request": request,
        "response": response,
    }
    return s.delete(**b)


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/Volumes/{volume_id}/AllocatedPools/{storage_pool_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/Volumes/{volume_id}/AllocatedPools/{storage_pool_id}",
    response_model_exclude_none=True,
)
async def get17(
    computer_system_id: str,
    storage_id: str,
    volume_id: str,
    storage_pool_id: str,
    request: Request,
    response: Response,
) -> StoragePool:
    s: Service = get_service(StoragePool, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "volume_id": volume_id,
        "storage_pool_id": storage_pool_id,
        "request": request,
        "response": response,
    }
    return cast(StoragePool, s.get(**b))


@router.patch(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/Volumes/{volume_id}/AllocatedPools/{storage_pool_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch17(
    computer_system_id: str,
    storage_id: str,
    volume_id: str,
    storage_pool_id: str,
    request: Request,
    response: Response,
    body: StoragePoolOnUpdate,
) -> StoragePool:
    s: Service = get_service(StoragePool, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "volume_id": volume_id,
        "storage_pool_id": storage_pool_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(StoragePool, s.patch(**b))


@router.post(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/Volumes/{volume_id}/AllocatedPools/{storage_pool_id}/Actions/StoragePool.AddDrives",
    response_model_exclude_none=True,
)
@authenticate
async def add_drives17(
    computer_system_id: str,
    storage_id: str,
    volume_id: str,
    storage_pool_id: str,
    request: Request,
    response: Response,
    body: AddDrivesRequest,
) -> RedfishError:
    s: Service = get_service(StoragePool, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "volume_id": volume_id,
        "storage_pool_id": storage_pool_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "AddDrives",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/Volumes/{volume_id}/AllocatedPools/{storage_pool_id}/Actions/StoragePool.RemoveDrives",
    response_model_exclude_none=True,
)
@authenticate
async def remove_drives17(
    computer_system_id: str,
    storage_id: str,
    volume_id: str,
    storage_pool_id: str,
    request: Request,
    response: Response,
    body: RemoveDrivesRequest,
) -> RedfishError:
    s: Service = get_service(StoragePool, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "volume_id": volume_id,
        "storage_pool_id": storage_pool_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "RemoveDrives",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/Volumes/{volume_id}/AllocatedPools/{storage_pool_id}/Actions/StoragePool.SetCompressionState",
    response_model_exclude_none=True,
)
@authenticate
async def set_compression_state17(
    computer_system_id: str,
    storage_id: str,
    volume_id: str,
    storage_pool_id: str,
    request: Request,
    response: Response,
    body: SetCompressionStateRequest,
) -> RedfishError:
    s: Service = get_service(StoragePool, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "volume_id": volume_id,
        "storage_pool_id": storage_pool_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "SetCompressionState",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/Volumes/{volume_id}/AllocatedPools/{storage_pool_id}/Actions/StoragePool.SetDeduplicationState",
    response_model_exclude_none=True,
)
@authenticate
async def set_deduplication_state17(
    computer_system_id: str,
    storage_id: str,
    volume_id: str,
    storage_pool_id: str,
    request: Request,
    response: Response,
    body: SetDeduplicationStateRequest,
) -> RedfishError:
    s: Service = get_service(StoragePool, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "volume_id": volume_id,
        "storage_pool_id": storage_pool_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "SetDeduplicationState",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/Volumes/{volume_id}/AllocatedPools/{storage_pool_id}/Actions/StoragePool.SetEncryptionState",
    response_model_exclude_none=True,
)
@authenticate
async def set_encryption_state17(
    computer_system_id: str,
    storage_id: str,
    volume_id: str,
    storage_pool_id: str,
    request: Request,
    response: Response,
    body: SetEncryptionStateRequest,
) -> RedfishError:
    s: Service = get_service(StoragePool, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "volume_id": volume_id,
        "storage_pool_id": storage_pool_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "SetEncryptionState",
    }
    return s.action(**b)


@router.delete(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/FileSystems/{file_system_id}/CapacitySources/{capacity_source_id}/ProvidingPools/{storage_pool_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete18(
    computer_system_id: str,
    storage_id: str,
    file_system_id: str,
    capacity_source_id: str,
    storage_pool_id: str,
    request: Request,
    response: Response,
) -> None:
    s: Service = get_service(StoragePool, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "file_system_id": file_system_id,
        "capacity_source_id": capacity_source_id,
        "storage_pool_id": storage_pool_id,
        "request": request,
        "response": response,
    }
    return s.delete(**b)


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/FileSystems/{file_system_id}/CapacitySources/{capacity_source_id}/ProvidingPools/{storage_pool_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/FileSystems/{file_system_id}/CapacitySources/{capacity_source_id}/ProvidingPools/{storage_pool_id}",
    response_model_exclude_none=True,
)
async def get18(
    computer_system_id: str,
    storage_id: str,
    file_system_id: str,
    capacity_source_id: str,
    storage_pool_id: str,
    request: Request,
    response: Response,
) -> StoragePool:
    s: Service = get_service(StoragePool, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "file_system_id": file_system_id,
        "capacity_source_id": capacity_source_id,
        "storage_pool_id": storage_pool_id,
        "request": request,
        "response": response,
    }
    return cast(StoragePool, s.get(**b))


@router.patch(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/FileSystems/{file_system_id}/CapacitySources/{capacity_source_id}/ProvidingPools/{storage_pool_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch18(
    computer_system_id: str,
    storage_id: str,
    file_system_id: str,
    capacity_source_id: str,
    storage_pool_id: str,
    request: Request,
    response: Response,
    body: StoragePoolOnUpdate,
) -> StoragePool:
    s: Service = get_service(StoragePool, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "file_system_id": file_system_id,
        "capacity_source_id": capacity_source_id,
        "storage_pool_id": storage_pool_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(StoragePool, s.patch(**b))


@router.post(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/FileSystems/{file_system_id}/CapacitySources/{capacity_source_id}/ProvidingPools/{storage_pool_id}/Actions/StoragePool.AddDrives",
    response_model_exclude_none=True,
)
@authenticate
async def add_drives18(
    computer_system_id: str,
    storage_id: str,
    file_system_id: str,
    capacity_source_id: str,
    storage_pool_id: str,
    request: Request,
    response: Response,
    body: AddDrivesRequest,
) -> RedfishError:
    s: Service = get_service(StoragePool, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "file_system_id": file_system_id,
        "capacity_source_id": capacity_source_id,
        "storage_pool_id": storage_pool_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "AddDrives",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/FileSystems/{file_system_id}/CapacitySources/{capacity_source_id}/ProvidingPools/{storage_pool_id}/Actions/StoragePool.RemoveDrives",
    response_model_exclude_none=True,
)
@authenticate
async def remove_drives18(
    computer_system_id: str,
    storage_id: str,
    file_system_id: str,
    capacity_source_id: str,
    storage_pool_id: str,
    request: Request,
    response: Response,
    body: RemoveDrivesRequest,
) -> RedfishError:
    s: Service = get_service(StoragePool, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "file_system_id": file_system_id,
        "capacity_source_id": capacity_source_id,
        "storage_pool_id": storage_pool_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "RemoveDrives",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/FileSystems/{file_system_id}/CapacitySources/{capacity_source_id}/ProvidingPools/{storage_pool_id}/Actions/StoragePool.SetCompressionState",
    response_model_exclude_none=True,
)
@authenticate
async def set_compression_state18(
    computer_system_id: str,
    storage_id: str,
    file_system_id: str,
    capacity_source_id: str,
    storage_pool_id: str,
    request: Request,
    response: Response,
    body: SetCompressionStateRequest,
) -> RedfishError:
    s: Service = get_service(StoragePool, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "file_system_id": file_system_id,
        "capacity_source_id": capacity_source_id,
        "storage_pool_id": storage_pool_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "SetCompressionState",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/FileSystems/{file_system_id}/CapacitySources/{capacity_source_id}/ProvidingPools/{storage_pool_id}/Actions/StoragePool.SetDeduplicationState",
    response_model_exclude_none=True,
)
@authenticate
async def set_deduplication_state18(
    computer_system_id: str,
    storage_id: str,
    file_system_id: str,
    capacity_source_id: str,
    storage_pool_id: str,
    request: Request,
    response: Response,
    body: SetDeduplicationStateRequest,
) -> RedfishError:
    s: Service = get_service(StoragePool, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "file_system_id": file_system_id,
        "capacity_source_id": capacity_source_id,
        "storage_pool_id": storage_pool_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "SetDeduplicationState",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/FileSystems/{file_system_id}/CapacitySources/{capacity_source_id}/ProvidingPools/{storage_pool_id}/Actions/StoragePool.SetEncryptionState",
    response_model_exclude_none=True,
)
@authenticate
async def set_encryption_state18(
    computer_system_id: str,
    storage_id: str,
    file_system_id: str,
    capacity_source_id: str,
    storage_pool_id: str,
    request: Request,
    response: Response,
    body: SetEncryptionStateRequest,
) -> RedfishError:
    s: Service = get_service(StoragePool, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "file_system_id": file_system_id,
        "capacity_source_id": capacity_source_id,
        "storage_pool_id": storage_pool_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "SetEncryptionState",
    }
    return s.action(**b)
