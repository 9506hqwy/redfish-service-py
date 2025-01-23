from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ...authenticate import authenticate
from ...model.redfish_error import RedfishError
from ...model.swordfish.volume import (
    AssignReplicaTargetRequest,
    ChangeRaidLayoutRequest,
    CreateReplicaTargetRequest,
    InitializeRequest,
    RemoveReplicaRelationshipRequest,
    ResumeReplicationRequest,
    ReverseReplicationRelationshipRequest,
    SplitReplicationRequest,
    SuspendReplicationRequest,
    Volume,
    VolumeOnUpdate,
)
from ...service import Service
from ...util import get_service, set_link_header

router = APIRouter()


@router.delete(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Storage/{storage_id}/Volumes/{volume_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete1(
    resource_block_id: str, storage_id: str, volume_id: str, request: Request, response: Response
) -> None:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "storage_id": storage_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
    }
    return s.delete(**b)


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Storage/{storage_id}/Volumes/{volume_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Storage/{storage_id}/Volumes/{volume_id}",
    response_model_exclude_none=True,
)
async def get1(
    resource_block_id: str, storage_id: str, volume_id: str, request: Request, response: Response
) -> Volume:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "storage_id": storage_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
    }
    m = cast(Volume, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Storage/{storage_id}/Volumes/{volume_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch1(
    resource_block_id: str,
    storage_id: str,
    volume_id: str,
    request: Request,
    response: Response,
    body: VolumeOnUpdate,
) -> Volume:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "storage_id": storage_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Volume, s.patch(**b))


@router.post(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Storage/{storage_id}/Volumes/{volume_id}/Actions/Volume.AssignReplicaTarget",
    response_model_exclude_none=True,
)
@authenticate
async def assign_replica_target1(
    resource_block_id: str,
    storage_id: str,
    volume_id: str,
    request: Request,
    response: Response,
    body: AssignReplicaTargetRequest,
) -> RedfishError:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "storage_id": storage_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "AssignReplicaTarget",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Storage/{storage_id}/Volumes/{volume_id}/Actions/Volume.ChangeRAIDLayout",
    response_model_exclude_none=True,
)
@authenticate
async def change_raid_layout1(
    resource_block_id: str,
    storage_id: str,
    volume_id: str,
    request: Request,
    response: Response,
    body: ChangeRaidLayoutRequest,
) -> RedfishError:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "storage_id": storage_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "ChangeRAIDLayout",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Storage/{storage_id}/Volumes/{volume_id}/Actions/Volume.CreateReplicaTarget",
    response_model_exclude_none=True,
)
@authenticate
async def create_replica_target1(
    resource_block_id: str,
    storage_id: str,
    volume_id: str,
    request: Request,
    response: Response,
    body: CreateReplicaTargetRequest,
) -> RedfishError:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "storage_id": storage_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "CreateReplicaTarget",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Storage/{storage_id}/Volumes/{volume_id}/Actions/Volume.Initialize",
    response_model_exclude_none=True,
)
@authenticate
async def initialize1(
    resource_block_id: str,
    storage_id: str,
    volume_id: str,
    request: Request,
    response: Response,
    body: InitializeRequest,
) -> RedfishError:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "storage_id": storage_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Initialize",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Storage/{storage_id}/Volumes/{volume_id}/Actions/Volume.RemoveReplicaRelationship",
    response_model_exclude_none=True,
)
@authenticate
async def remove_replica_relationship1(
    resource_block_id: str,
    storage_id: str,
    volume_id: str,
    request: Request,
    response: Response,
    body: RemoveReplicaRelationshipRequest,
) -> RedfishError:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "storage_id": storage_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "RemoveReplicaRelationship",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Storage/{storage_id}/Volumes/{volume_id}/Actions/Volume.ResumeReplication",
    response_model_exclude_none=True,
)
@authenticate
async def resume_replication1(
    resource_block_id: str,
    storage_id: str,
    volume_id: str,
    request: Request,
    response: Response,
    body: ResumeReplicationRequest,
) -> RedfishError:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "storage_id": storage_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "ResumeReplication",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Storage/{storage_id}/Volumes/{volume_id}/Actions/Volume.ReverseReplicationRelationship",
    response_model_exclude_none=True,
)
@authenticate
async def reverse_replication_relationship1(
    resource_block_id: str,
    storage_id: str,
    volume_id: str,
    request: Request,
    response: Response,
    body: ReverseReplicationRelationshipRequest,
) -> RedfishError:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "storage_id": storage_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "ReverseReplicationRelationship",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Storage/{storage_id}/Volumes/{volume_id}/Actions/Volume.SplitReplication",
    response_model_exclude_none=True,
)
@authenticate
async def split_replication1(
    resource_block_id: str,
    storage_id: str,
    volume_id: str,
    request: Request,
    response: Response,
    body: SplitReplicationRequest,
) -> RedfishError:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "storage_id": storage_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "SplitReplication",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Storage/{storage_id}/Volumes/{volume_id}/Actions/Volume.SuspendReplication",
    response_model_exclude_none=True,
)
@authenticate
async def suspend_replication1(
    resource_block_id: str,
    storage_id: str,
    volume_id: str,
    request: Request,
    response: Response,
    body: SuspendReplicationRequest,
) -> RedfishError:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "storage_id": storage_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "SuspendReplication",
    }
    return s.action(**b)


@router.delete(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Storage/{storage_id}/Volumes/{volume_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete2(
    resource_block_id: str,
    computer_system_id: str,
    storage_id: str,
    volume_id: str,
    request: Request,
    response: Response,
) -> None:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
    }
    return s.delete(**b)


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Storage/{storage_id}/Volumes/{volume_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Storage/{storage_id}/Volumes/{volume_id}",
    response_model_exclude_none=True,
)
async def get2(
    resource_block_id: str,
    computer_system_id: str,
    storage_id: str,
    volume_id: str,
    request: Request,
    response: Response,
) -> Volume:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
    }
    m = cast(Volume, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Storage/{storage_id}/Volumes/{volume_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch2(
    resource_block_id: str,
    computer_system_id: str,
    storage_id: str,
    volume_id: str,
    request: Request,
    response: Response,
    body: VolumeOnUpdate,
) -> Volume:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Volume, s.patch(**b))


@router.post(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Storage/{storage_id}/Volumes/{volume_id}/Actions/Volume.AssignReplicaTarget",
    response_model_exclude_none=True,
)
@authenticate
async def assign_replica_target2(
    resource_block_id: str,
    computer_system_id: str,
    storage_id: str,
    volume_id: str,
    request: Request,
    response: Response,
    body: AssignReplicaTargetRequest,
) -> RedfishError:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "AssignReplicaTarget",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Storage/{storage_id}/Volumes/{volume_id}/Actions/Volume.ChangeRAIDLayout",
    response_model_exclude_none=True,
)
@authenticate
async def change_raid_layout2(
    resource_block_id: str,
    computer_system_id: str,
    storage_id: str,
    volume_id: str,
    request: Request,
    response: Response,
    body: ChangeRaidLayoutRequest,
) -> RedfishError:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "ChangeRAIDLayout",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Storage/{storage_id}/Volumes/{volume_id}/Actions/Volume.CreateReplicaTarget",
    response_model_exclude_none=True,
)
@authenticate
async def create_replica_target2(
    resource_block_id: str,
    computer_system_id: str,
    storage_id: str,
    volume_id: str,
    request: Request,
    response: Response,
    body: CreateReplicaTargetRequest,
) -> RedfishError:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "CreateReplicaTarget",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Storage/{storage_id}/Volumes/{volume_id}/Actions/Volume.Initialize",
    response_model_exclude_none=True,
)
@authenticate
async def initialize2(
    resource_block_id: str,
    computer_system_id: str,
    storage_id: str,
    volume_id: str,
    request: Request,
    response: Response,
    body: InitializeRequest,
) -> RedfishError:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Initialize",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Storage/{storage_id}/Volumes/{volume_id}/Actions/Volume.RemoveReplicaRelationship",
    response_model_exclude_none=True,
)
@authenticate
async def remove_replica_relationship2(
    resource_block_id: str,
    computer_system_id: str,
    storage_id: str,
    volume_id: str,
    request: Request,
    response: Response,
    body: RemoveReplicaRelationshipRequest,
) -> RedfishError:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "RemoveReplicaRelationship",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Storage/{storage_id}/Volumes/{volume_id}/Actions/Volume.ResumeReplication",
    response_model_exclude_none=True,
)
@authenticate
async def resume_replication2(
    resource_block_id: str,
    computer_system_id: str,
    storage_id: str,
    volume_id: str,
    request: Request,
    response: Response,
    body: ResumeReplicationRequest,
) -> RedfishError:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "ResumeReplication",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Storage/{storage_id}/Volumes/{volume_id}/Actions/Volume.ReverseReplicationRelationship",
    response_model_exclude_none=True,
)
@authenticate
async def reverse_replication_relationship2(
    resource_block_id: str,
    computer_system_id: str,
    storage_id: str,
    volume_id: str,
    request: Request,
    response: Response,
    body: ReverseReplicationRelationshipRequest,
) -> RedfishError:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "ReverseReplicationRelationship",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Storage/{storage_id}/Volumes/{volume_id}/Actions/Volume.SplitReplication",
    response_model_exclude_none=True,
)
@authenticate
async def split_replication2(
    resource_block_id: str,
    computer_system_id: str,
    storage_id: str,
    volume_id: str,
    request: Request,
    response: Response,
    body: SplitReplicationRequest,
) -> RedfishError:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "SplitReplication",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Storage/{storage_id}/Volumes/{volume_id}/Actions/Volume.SuspendReplication",
    response_model_exclude_none=True,
)
@authenticate
async def suspend_replication2(
    resource_block_id: str,
    computer_system_id: str,
    storage_id: str,
    volume_id: str,
    request: Request,
    response: Response,
    body: SuspendReplicationRequest,
) -> RedfishError:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "SuspendReplication",
    }
    return s.action(**b)


@router.delete(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Storage/{storage_id}/Volumes/{volume_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete3(
    resource_block_id: str, storage_id: str, volume_id: str, request: Request, response: Response
) -> None:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "storage_id": storage_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
    }
    return s.delete(**b)


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Storage/{storage_id}/Volumes/{volume_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Storage/{storage_id}/Volumes/{volume_id}",
    response_model_exclude_none=True,
)
async def get3(
    resource_block_id: str, storage_id: str, volume_id: str, request: Request, response: Response
) -> Volume:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "storage_id": storage_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
    }
    m = cast(Volume, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Storage/{storage_id}/Volumes/{volume_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch3(
    resource_block_id: str,
    storage_id: str,
    volume_id: str,
    request: Request,
    response: Response,
    body: VolumeOnUpdate,
) -> Volume:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "storage_id": storage_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Volume, s.patch(**b))


@router.post(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Storage/{storage_id}/Volumes/{volume_id}/Actions/Volume.AssignReplicaTarget",
    response_model_exclude_none=True,
)
@authenticate
async def assign_replica_target3(
    resource_block_id: str,
    storage_id: str,
    volume_id: str,
    request: Request,
    response: Response,
    body: AssignReplicaTargetRequest,
) -> RedfishError:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "storage_id": storage_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "AssignReplicaTarget",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Storage/{storage_id}/Volumes/{volume_id}/Actions/Volume.ChangeRAIDLayout",
    response_model_exclude_none=True,
)
@authenticate
async def change_raid_layout3(
    resource_block_id: str,
    storage_id: str,
    volume_id: str,
    request: Request,
    response: Response,
    body: ChangeRaidLayoutRequest,
) -> RedfishError:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "storage_id": storage_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "ChangeRAIDLayout",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Storage/{storage_id}/Volumes/{volume_id}/Actions/Volume.CreateReplicaTarget",
    response_model_exclude_none=True,
)
@authenticate
async def create_replica_target3(
    resource_block_id: str,
    storage_id: str,
    volume_id: str,
    request: Request,
    response: Response,
    body: CreateReplicaTargetRequest,
) -> RedfishError:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "storage_id": storage_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "CreateReplicaTarget",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Storage/{storage_id}/Volumes/{volume_id}/Actions/Volume.Initialize",
    response_model_exclude_none=True,
)
@authenticate
async def initialize3(
    resource_block_id: str,
    storage_id: str,
    volume_id: str,
    request: Request,
    response: Response,
    body: InitializeRequest,
) -> RedfishError:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "storage_id": storage_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Initialize",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Storage/{storage_id}/Volumes/{volume_id}/Actions/Volume.RemoveReplicaRelationship",
    response_model_exclude_none=True,
)
@authenticate
async def remove_replica_relationship3(
    resource_block_id: str,
    storage_id: str,
    volume_id: str,
    request: Request,
    response: Response,
    body: RemoveReplicaRelationshipRequest,
) -> RedfishError:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "storage_id": storage_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "RemoveReplicaRelationship",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Storage/{storage_id}/Volumes/{volume_id}/Actions/Volume.ResumeReplication",
    response_model_exclude_none=True,
)
@authenticate
async def resume_replication3(
    resource_block_id: str,
    storage_id: str,
    volume_id: str,
    request: Request,
    response: Response,
    body: ResumeReplicationRequest,
) -> RedfishError:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "storage_id": storage_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "ResumeReplication",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Storage/{storage_id}/Volumes/{volume_id}/Actions/Volume.ReverseReplicationRelationship",
    response_model_exclude_none=True,
)
@authenticate
async def reverse_replication_relationship3(
    resource_block_id: str,
    storage_id: str,
    volume_id: str,
    request: Request,
    response: Response,
    body: ReverseReplicationRelationshipRequest,
) -> RedfishError:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "storage_id": storage_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "ReverseReplicationRelationship",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Storage/{storage_id}/Volumes/{volume_id}/Actions/Volume.SplitReplication",
    response_model_exclude_none=True,
)
@authenticate
async def split_replication3(
    resource_block_id: str,
    storage_id: str,
    volume_id: str,
    request: Request,
    response: Response,
    body: SplitReplicationRequest,
) -> RedfishError:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "storage_id": storage_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "SplitReplication",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Storage/{storage_id}/Volumes/{volume_id}/Actions/Volume.SuspendReplication",
    response_model_exclude_none=True,
)
@authenticate
async def suspend_replication3(
    resource_block_id: str,
    storage_id: str,
    volume_id: str,
    request: Request,
    response: Response,
    body: SuspendReplicationRequest,
) -> RedfishError:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "storage_id": storage_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "SuspendReplication",
    }
    return s.action(**b)


@router.delete(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Storage/{storage_id}/Volumes/{volume_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete4(
    resource_block_id: str,
    computer_system_id: str,
    storage_id: str,
    volume_id: str,
    request: Request,
    response: Response,
) -> None:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
    }
    return s.delete(**b)


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Storage/{storage_id}/Volumes/{volume_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Storage/{storage_id}/Volumes/{volume_id}",
    response_model_exclude_none=True,
)
async def get4(
    resource_block_id: str,
    computer_system_id: str,
    storage_id: str,
    volume_id: str,
    request: Request,
    response: Response,
) -> Volume:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
    }
    m = cast(Volume, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Storage/{storage_id}/Volumes/{volume_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch4(
    resource_block_id: str,
    computer_system_id: str,
    storage_id: str,
    volume_id: str,
    request: Request,
    response: Response,
    body: VolumeOnUpdate,
) -> Volume:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Volume, s.patch(**b))


@router.post(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Storage/{storage_id}/Volumes/{volume_id}/Actions/Volume.AssignReplicaTarget",
    response_model_exclude_none=True,
)
@authenticate
async def assign_replica_target4(
    resource_block_id: str,
    computer_system_id: str,
    storage_id: str,
    volume_id: str,
    request: Request,
    response: Response,
    body: AssignReplicaTargetRequest,
) -> RedfishError:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "AssignReplicaTarget",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Storage/{storage_id}/Volumes/{volume_id}/Actions/Volume.ChangeRAIDLayout",
    response_model_exclude_none=True,
)
@authenticate
async def change_raid_layout4(
    resource_block_id: str,
    computer_system_id: str,
    storage_id: str,
    volume_id: str,
    request: Request,
    response: Response,
    body: ChangeRaidLayoutRequest,
) -> RedfishError:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "ChangeRAIDLayout",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Storage/{storage_id}/Volumes/{volume_id}/Actions/Volume.CreateReplicaTarget",
    response_model_exclude_none=True,
)
@authenticate
async def create_replica_target4(
    resource_block_id: str,
    computer_system_id: str,
    storage_id: str,
    volume_id: str,
    request: Request,
    response: Response,
    body: CreateReplicaTargetRequest,
) -> RedfishError:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "CreateReplicaTarget",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Storage/{storage_id}/Volumes/{volume_id}/Actions/Volume.Initialize",
    response_model_exclude_none=True,
)
@authenticate
async def initialize4(
    resource_block_id: str,
    computer_system_id: str,
    storage_id: str,
    volume_id: str,
    request: Request,
    response: Response,
    body: InitializeRequest,
) -> RedfishError:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Initialize",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Storage/{storage_id}/Volumes/{volume_id}/Actions/Volume.RemoveReplicaRelationship",
    response_model_exclude_none=True,
)
@authenticate
async def remove_replica_relationship4(
    resource_block_id: str,
    computer_system_id: str,
    storage_id: str,
    volume_id: str,
    request: Request,
    response: Response,
    body: RemoveReplicaRelationshipRequest,
) -> RedfishError:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "RemoveReplicaRelationship",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Storage/{storage_id}/Volumes/{volume_id}/Actions/Volume.ResumeReplication",
    response_model_exclude_none=True,
)
@authenticate
async def resume_replication4(
    resource_block_id: str,
    computer_system_id: str,
    storage_id: str,
    volume_id: str,
    request: Request,
    response: Response,
    body: ResumeReplicationRequest,
) -> RedfishError:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "ResumeReplication",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Storage/{storage_id}/Volumes/{volume_id}/Actions/Volume.ReverseReplicationRelationship",
    response_model_exclude_none=True,
)
@authenticate
async def reverse_replication_relationship4(
    resource_block_id: str,
    computer_system_id: str,
    storage_id: str,
    volume_id: str,
    request: Request,
    response: Response,
    body: ReverseReplicationRelationshipRequest,
) -> RedfishError:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "ReverseReplicationRelationship",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Storage/{storage_id}/Volumes/{volume_id}/Actions/Volume.SplitReplication",
    response_model_exclude_none=True,
)
@authenticate
async def split_replication4(
    resource_block_id: str,
    computer_system_id: str,
    storage_id: str,
    volume_id: str,
    request: Request,
    response: Response,
    body: SplitReplicationRequest,
) -> RedfishError:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "SplitReplication",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Storage/{storage_id}/Volumes/{volume_id}/Actions/Volume.SuspendReplication",
    response_model_exclude_none=True,
)
@authenticate
async def suspend_replication4(
    resource_block_id: str,
    computer_system_id: str,
    storage_id: str,
    volume_id: str,
    request: Request,
    response: Response,
    body: SuspendReplicationRequest,
) -> RedfishError:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "SuspendReplication",
    }
    return s.action(**b)


@router.delete(
    "/redfish/v1/Storage/{storage_id}/ConsistencyGroups/{consistency_group_id}/Volumes/{volume_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete5(
    storage_id: str,
    consistency_group_id: str,
    volume_id: str,
    request: Request,
    response: Response,
) -> None:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "storage_id": storage_id,
        "consistency_group_id": consistency_group_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
    }
    return s.delete(**b)


@router.get(
    "/redfish/v1/Storage/{storage_id}/ConsistencyGroups/{consistency_group_id}/Volumes/{volume_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Storage/{storage_id}/ConsistencyGroups/{consistency_group_id}/Volumes/{volume_id}",
    response_model_exclude_none=True,
)
async def get5(
    storage_id: str,
    consistency_group_id: str,
    volume_id: str,
    request: Request,
    response: Response,
) -> Volume:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "storage_id": storage_id,
        "consistency_group_id": consistency_group_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
    }
    m = cast(Volume, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/Storage/{storage_id}/ConsistencyGroups/{consistency_group_id}/Volumes/{volume_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch5(
    storage_id: str,
    consistency_group_id: str,
    volume_id: str,
    request: Request,
    response: Response,
    body: VolumeOnUpdate,
) -> Volume:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "storage_id": storage_id,
        "consistency_group_id": consistency_group_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Volume, s.patch(**b))


@router.post(
    "/redfish/v1/Storage/{storage_id}/ConsistencyGroups/{consistency_group_id}/Volumes/{volume_id}/Actions/Volume.AssignReplicaTarget",
    response_model_exclude_none=True,
)
@authenticate
async def assign_replica_target5(
    storage_id: str,
    consistency_group_id: str,
    volume_id: str,
    request: Request,
    response: Response,
    body: AssignReplicaTargetRequest,
) -> RedfishError:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "storage_id": storage_id,
        "consistency_group_id": consistency_group_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "AssignReplicaTarget",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Storage/{storage_id}/ConsistencyGroups/{consistency_group_id}/Volumes/{volume_id}/Actions/Volume.ChangeRAIDLayout",
    response_model_exclude_none=True,
)
@authenticate
async def change_raid_layout5(
    storage_id: str,
    consistency_group_id: str,
    volume_id: str,
    request: Request,
    response: Response,
    body: ChangeRaidLayoutRequest,
) -> RedfishError:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "storage_id": storage_id,
        "consistency_group_id": consistency_group_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "ChangeRAIDLayout",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Storage/{storage_id}/ConsistencyGroups/{consistency_group_id}/Volumes/{volume_id}/Actions/Volume.CreateReplicaTarget",
    response_model_exclude_none=True,
)
@authenticate
async def create_replica_target5(
    storage_id: str,
    consistency_group_id: str,
    volume_id: str,
    request: Request,
    response: Response,
    body: CreateReplicaTargetRequest,
) -> RedfishError:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "storage_id": storage_id,
        "consistency_group_id": consistency_group_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "CreateReplicaTarget",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Storage/{storage_id}/ConsistencyGroups/{consistency_group_id}/Volumes/{volume_id}/Actions/Volume.Initialize",
    response_model_exclude_none=True,
)
@authenticate
async def initialize5(
    storage_id: str,
    consistency_group_id: str,
    volume_id: str,
    request: Request,
    response: Response,
    body: InitializeRequest,
) -> RedfishError:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "storage_id": storage_id,
        "consistency_group_id": consistency_group_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Initialize",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Storage/{storage_id}/ConsistencyGroups/{consistency_group_id}/Volumes/{volume_id}/Actions/Volume.RemoveReplicaRelationship",
    response_model_exclude_none=True,
)
@authenticate
async def remove_replica_relationship5(
    storage_id: str,
    consistency_group_id: str,
    volume_id: str,
    request: Request,
    response: Response,
    body: RemoveReplicaRelationshipRequest,
) -> RedfishError:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "storage_id": storage_id,
        "consistency_group_id": consistency_group_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "RemoveReplicaRelationship",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Storage/{storage_id}/ConsistencyGroups/{consistency_group_id}/Volumes/{volume_id}/Actions/Volume.ResumeReplication",
    response_model_exclude_none=True,
)
@authenticate
async def resume_replication5(
    storage_id: str,
    consistency_group_id: str,
    volume_id: str,
    request: Request,
    response: Response,
    body: ResumeReplicationRequest,
) -> RedfishError:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "storage_id": storage_id,
        "consistency_group_id": consistency_group_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "ResumeReplication",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Storage/{storage_id}/ConsistencyGroups/{consistency_group_id}/Volumes/{volume_id}/Actions/Volume.ReverseReplicationRelationship",
    response_model_exclude_none=True,
)
@authenticate
async def reverse_replication_relationship5(
    storage_id: str,
    consistency_group_id: str,
    volume_id: str,
    request: Request,
    response: Response,
    body: ReverseReplicationRelationshipRequest,
) -> RedfishError:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "storage_id": storage_id,
        "consistency_group_id": consistency_group_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "ReverseReplicationRelationship",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Storage/{storage_id}/ConsistencyGroups/{consistency_group_id}/Volumes/{volume_id}/Actions/Volume.SplitReplication",
    response_model_exclude_none=True,
)
@authenticate
async def split_replication5(
    storage_id: str,
    consistency_group_id: str,
    volume_id: str,
    request: Request,
    response: Response,
    body: SplitReplicationRequest,
) -> RedfishError:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "storage_id": storage_id,
        "consistency_group_id": consistency_group_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "SplitReplication",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Storage/{storage_id}/ConsistencyGroups/{consistency_group_id}/Volumes/{volume_id}/Actions/Volume.SuspendReplication",
    response_model_exclude_none=True,
)
@authenticate
async def suspend_replication5(
    storage_id: str,
    consistency_group_id: str,
    volume_id: str,
    request: Request,
    response: Response,
    body: SuspendReplicationRequest,
) -> RedfishError:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "storage_id": storage_id,
        "consistency_group_id": consistency_group_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "SuspendReplication",
    }
    return s.action(**b)


@router.delete(
    "/redfish/v1/Storage/{storage_id}/FileSystems/{file_system_id}/CapacitySources/{capacity_source_id}/ProvidingVolumes/{volume_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete6(
    storage_id: str,
    file_system_id: str,
    capacity_source_id: str,
    volume_id: str,
    request: Request,
    response: Response,
) -> None:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "storage_id": storage_id,
        "file_system_id": file_system_id,
        "capacity_source_id": capacity_source_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
    }
    return s.delete(**b)


@router.get(
    "/redfish/v1/Storage/{storage_id}/FileSystems/{file_system_id}/CapacitySources/{capacity_source_id}/ProvidingVolumes/{volume_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Storage/{storage_id}/FileSystems/{file_system_id}/CapacitySources/{capacity_source_id}/ProvidingVolumes/{volume_id}",
    response_model_exclude_none=True,
)
async def get6(
    storage_id: str,
    file_system_id: str,
    capacity_source_id: str,
    volume_id: str,
    request: Request,
    response: Response,
) -> Volume:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "storage_id": storage_id,
        "file_system_id": file_system_id,
        "capacity_source_id": capacity_source_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
    }
    m = cast(Volume, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/Storage/{storage_id}/FileSystems/{file_system_id}/CapacitySources/{capacity_source_id}/ProvidingVolumes/{volume_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch6(
    storage_id: str,
    file_system_id: str,
    capacity_source_id: str,
    volume_id: str,
    request: Request,
    response: Response,
    body: VolumeOnUpdate,
) -> Volume:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "storage_id": storage_id,
        "file_system_id": file_system_id,
        "capacity_source_id": capacity_source_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Volume, s.patch(**b))


@router.post(
    "/redfish/v1/Storage/{storage_id}/FileSystems/{file_system_id}/CapacitySources/{capacity_source_id}/ProvidingVolumes/{volume_id}/Actions/Volume.AssignReplicaTarget",
    response_model_exclude_none=True,
)
@authenticate
async def assign_replica_target6(
    storage_id: str,
    file_system_id: str,
    capacity_source_id: str,
    volume_id: str,
    request: Request,
    response: Response,
    body: AssignReplicaTargetRequest,
) -> RedfishError:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "storage_id": storage_id,
        "file_system_id": file_system_id,
        "capacity_source_id": capacity_source_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "AssignReplicaTarget",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Storage/{storage_id}/FileSystems/{file_system_id}/CapacitySources/{capacity_source_id}/ProvidingVolumes/{volume_id}/Actions/Volume.ChangeRAIDLayout",
    response_model_exclude_none=True,
)
@authenticate
async def change_raid_layout6(
    storage_id: str,
    file_system_id: str,
    capacity_source_id: str,
    volume_id: str,
    request: Request,
    response: Response,
    body: ChangeRaidLayoutRequest,
) -> RedfishError:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "storage_id": storage_id,
        "file_system_id": file_system_id,
        "capacity_source_id": capacity_source_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "ChangeRAIDLayout",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Storage/{storage_id}/FileSystems/{file_system_id}/CapacitySources/{capacity_source_id}/ProvidingVolumes/{volume_id}/Actions/Volume.CreateReplicaTarget",
    response_model_exclude_none=True,
)
@authenticate
async def create_replica_target6(
    storage_id: str,
    file_system_id: str,
    capacity_source_id: str,
    volume_id: str,
    request: Request,
    response: Response,
    body: CreateReplicaTargetRequest,
) -> RedfishError:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "storage_id": storage_id,
        "file_system_id": file_system_id,
        "capacity_source_id": capacity_source_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "CreateReplicaTarget",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Storage/{storage_id}/FileSystems/{file_system_id}/CapacitySources/{capacity_source_id}/ProvidingVolumes/{volume_id}/Actions/Volume.Initialize",
    response_model_exclude_none=True,
)
@authenticate
async def initialize6(
    storage_id: str,
    file_system_id: str,
    capacity_source_id: str,
    volume_id: str,
    request: Request,
    response: Response,
    body: InitializeRequest,
) -> RedfishError:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "storage_id": storage_id,
        "file_system_id": file_system_id,
        "capacity_source_id": capacity_source_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Initialize",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Storage/{storage_id}/FileSystems/{file_system_id}/CapacitySources/{capacity_source_id}/ProvidingVolumes/{volume_id}/Actions/Volume.RemoveReplicaRelationship",
    response_model_exclude_none=True,
)
@authenticate
async def remove_replica_relationship6(
    storage_id: str,
    file_system_id: str,
    capacity_source_id: str,
    volume_id: str,
    request: Request,
    response: Response,
    body: RemoveReplicaRelationshipRequest,
) -> RedfishError:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "storage_id": storage_id,
        "file_system_id": file_system_id,
        "capacity_source_id": capacity_source_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "RemoveReplicaRelationship",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Storage/{storage_id}/FileSystems/{file_system_id}/CapacitySources/{capacity_source_id}/ProvidingVolumes/{volume_id}/Actions/Volume.ResumeReplication",
    response_model_exclude_none=True,
)
@authenticate
async def resume_replication6(
    storage_id: str,
    file_system_id: str,
    capacity_source_id: str,
    volume_id: str,
    request: Request,
    response: Response,
    body: ResumeReplicationRequest,
) -> RedfishError:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "storage_id": storage_id,
        "file_system_id": file_system_id,
        "capacity_source_id": capacity_source_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "ResumeReplication",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Storage/{storage_id}/FileSystems/{file_system_id}/CapacitySources/{capacity_source_id}/ProvidingVolumes/{volume_id}/Actions/Volume.ReverseReplicationRelationship",
    response_model_exclude_none=True,
)
@authenticate
async def reverse_replication_relationship6(
    storage_id: str,
    file_system_id: str,
    capacity_source_id: str,
    volume_id: str,
    request: Request,
    response: Response,
    body: ReverseReplicationRelationshipRequest,
) -> RedfishError:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "storage_id": storage_id,
        "file_system_id": file_system_id,
        "capacity_source_id": capacity_source_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "ReverseReplicationRelationship",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Storage/{storage_id}/FileSystems/{file_system_id}/CapacitySources/{capacity_source_id}/ProvidingVolumes/{volume_id}/Actions/Volume.SplitReplication",
    response_model_exclude_none=True,
)
@authenticate
async def split_replication6(
    storage_id: str,
    file_system_id: str,
    capacity_source_id: str,
    volume_id: str,
    request: Request,
    response: Response,
    body: SplitReplicationRequest,
) -> RedfishError:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "storage_id": storage_id,
        "file_system_id": file_system_id,
        "capacity_source_id": capacity_source_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "SplitReplication",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Storage/{storage_id}/FileSystems/{file_system_id}/CapacitySources/{capacity_source_id}/ProvidingVolumes/{volume_id}/Actions/Volume.SuspendReplication",
    response_model_exclude_none=True,
)
@authenticate
async def suspend_replication6(
    storage_id: str,
    file_system_id: str,
    capacity_source_id: str,
    volume_id: str,
    request: Request,
    response: Response,
    body: SuspendReplicationRequest,
) -> RedfishError:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "storage_id": storage_id,
        "file_system_id": file_system_id,
        "capacity_source_id": capacity_source_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "SuspendReplication",
    }
    return s.action(**b)


@router.delete(
    "/redfish/v1/Storage/{storage_id}/StoragePools/{storage_pool_id}/AllocatedVolumes/{volume_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete7(
    storage_id: str, storage_pool_id: str, volume_id: str, request: Request, response: Response
) -> None:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "storage_id": storage_id,
        "storage_pool_id": storage_pool_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
    }
    return s.delete(**b)


@router.get(
    "/redfish/v1/Storage/{storage_id}/StoragePools/{storage_pool_id}/AllocatedVolumes/{volume_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Storage/{storage_id}/StoragePools/{storage_pool_id}/AllocatedVolumes/{volume_id}",
    response_model_exclude_none=True,
)
async def get7(
    storage_id: str, storage_pool_id: str, volume_id: str, request: Request, response: Response
) -> Volume:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "storage_id": storage_id,
        "storage_pool_id": storage_pool_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
    }
    m = cast(Volume, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/Storage/{storage_id}/StoragePools/{storage_pool_id}/AllocatedVolumes/{volume_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch7(
    storage_id: str,
    storage_pool_id: str,
    volume_id: str,
    request: Request,
    response: Response,
    body: VolumeOnUpdate,
) -> Volume:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "storage_id": storage_id,
        "storage_pool_id": storage_pool_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Volume, s.patch(**b))


@router.post(
    "/redfish/v1/Storage/{storage_id}/StoragePools/{storage_pool_id}/AllocatedVolumes/{volume_id}/Actions/Volume.AssignReplicaTarget",
    response_model_exclude_none=True,
)
@authenticate
async def assign_replica_target7(
    storage_id: str,
    storage_pool_id: str,
    volume_id: str,
    request: Request,
    response: Response,
    body: AssignReplicaTargetRequest,
) -> RedfishError:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "storage_id": storage_id,
        "storage_pool_id": storage_pool_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "AssignReplicaTarget",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Storage/{storage_id}/StoragePools/{storage_pool_id}/AllocatedVolumes/{volume_id}/Actions/Volume.ChangeRAIDLayout",
    response_model_exclude_none=True,
)
@authenticate
async def change_raid_layout7(
    storage_id: str,
    storage_pool_id: str,
    volume_id: str,
    request: Request,
    response: Response,
    body: ChangeRaidLayoutRequest,
) -> RedfishError:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "storage_id": storage_id,
        "storage_pool_id": storage_pool_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "ChangeRAIDLayout",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Storage/{storage_id}/StoragePools/{storage_pool_id}/AllocatedVolumes/{volume_id}/Actions/Volume.CreateReplicaTarget",
    response_model_exclude_none=True,
)
@authenticate
async def create_replica_target7(
    storage_id: str,
    storage_pool_id: str,
    volume_id: str,
    request: Request,
    response: Response,
    body: CreateReplicaTargetRequest,
) -> RedfishError:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "storage_id": storage_id,
        "storage_pool_id": storage_pool_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "CreateReplicaTarget",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Storage/{storage_id}/StoragePools/{storage_pool_id}/AllocatedVolumes/{volume_id}/Actions/Volume.Initialize",
    response_model_exclude_none=True,
)
@authenticate
async def initialize7(
    storage_id: str,
    storage_pool_id: str,
    volume_id: str,
    request: Request,
    response: Response,
    body: InitializeRequest,
) -> RedfishError:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "storage_id": storage_id,
        "storage_pool_id": storage_pool_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Initialize",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Storage/{storage_id}/StoragePools/{storage_pool_id}/AllocatedVolumes/{volume_id}/Actions/Volume.RemoveReplicaRelationship",
    response_model_exclude_none=True,
)
@authenticate
async def remove_replica_relationship7(
    storage_id: str,
    storage_pool_id: str,
    volume_id: str,
    request: Request,
    response: Response,
    body: RemoveReplicaRelationshipRequest,
) -> RedfishError:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "storage_id": storage_id,
        "storage_pool_id": storage_pool_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "RemoveReplicaRelationship",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Storage/{storage_id}/StoragePools/{storage_pool_id}/AllocatedVolumes/{volume_id}/Actions/Volume.ResumeReplication",
    response_model_exclude_none=True,
)
@authenticate
async def resume_replication7(
    storage_id: str,
    storage_pool_id: str,
    volume_id: str,
    request: Request,
    response: Response,
    body: ResumeReplicationRequest,
) -> RedfishError:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "storage_id": storage_id,
        "storage_pool_id": storage_pool_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "ResumeReplication",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Storage/{storage_id}/StoragePools/{storage_pool_id}/AllocatedVolumes/{volume_id}/Actions/Volume.ReverseReplicationRelationship",
    response_model_exclude_none=True,
)
@authenticate
async def reverse_replication_relationship7(
    storage_id: str,
    storage_pool_id: str,
    volume_id: str,
    request: Request,
    response: Response,
    body: ReverseReplicationRelationshipRequest,
) -> RedfishError:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "storage_id": storage_id,
        "storage_pool_id": storage_pool_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "ReverseReplicationRelationship",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Storage/{storage_id}/StoragePools/{storage_pool_id}/AllocatedVolumes/{volume_id}/Actions/Volume.SplitReplication",
    response_model_exclude_none=True,
)
@authenticate
async def split_replication7(
    storage_id: str,
    storage_pool_id: str,
    volume_id: str,
    request: Request,
    response: Response,
    body: SplitReplicationRequest,
) -> RedfishError:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "storage_id": storage_id,
        "storage_pool_id": storage_pool_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "SplitReplication",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Storage/{storage_id}/StoragePools/{storage_pool_id}/AllocatedVolumes/{volume_id}/Actions/Volume.SuspendReplication",
    response_model_exclude_none=True,
)
@authenticate
async def suspend_replication7(
    storage_id: str,
    storage_pool_id: str,
    volume_id: str,
    request: Request,
    response: Response,
    body: SuspendReplicationRequest,
) -> RedfishError:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "storage_id": storage_id,
        "storage_pool_id": storage_pool_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "SuspendReplication",
    }
    return s.action(**b)


@router.delete(
    "/redfish/v1/Storage/{storage_id}/StoragePools/{storage_pool_id}/CapacitySources/{capacity_source_id}/ProvidingVolumes/{volume_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete8(
    storage_id: str,
    storage_pool_id: str,
    capacity_source_id: str,
    volume_id: str,
    request: Request,
    response: Response,
) -> None:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "storage_id": storage_id,
        "storage_pool_id": storage_pool_id,
        "capacity_source_id": capacity_source_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
    }
    return s.delete(**b)


@router.get(
    "/redfish/v1/Storage/{storage_id}/StoragePools/{storage_pool_id}/CapacitySources/{capacity_source_id}/ProvidingVolumes/{volume_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Storage/{storage_id}/StoragePools/{storage_pool_id}/CapacitySources/{capacity_source_id}/ProvidingVolumes/{volume_id}",
    response_model_exclude_none=True,
)
async def get8(
    storage_id: str,
    storage_pool_id: str,
    capacity_source_id: str,
    volume_id: str,
    request: Request,
    response: Response,
) -> Volume:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "storage_id": storage_id,
        "storage_pool_id": storage_pool_id,
        "capacity_source_id": capacity_source_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
    }
    m = cast(Volume, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/Storage/{storage_id}/StoragePools/{storage_pool_id}/CapacitySources/{capacity_source_id}/ProvidingVolumes/{volume_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch8(
    storage_id: str,
    storage_pool_id: str,
    capacity_source_id: str,
    volume_id: str,
    request: Request,
    response: Response,
    body: VolumeOnUpdate,
) -> Volume:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "storage_id": storage_id,
        "storage_pool_id": storage_pool_id,
        "capacity_source_id": capacity_source_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Volume, s.patch(**b))


@router.post(
    "/redfish/v1/Storage/{storage_id}/StoragePools/{storage_pool_id}/CapacitySources/{capacity_source_id}/ProvidingVolumes/{volume_id}/Actions/Volume.AssignReplicaTarget",
    response_model_exclude_none=True,
)
@authenticate
async def assign_replica_target8(
    storage_id: str,
    storage_pool_id: str,
    capacity_source_id: str,
    volume_id: str,
    request: Request,
    response: Response,
    body: AssignReplicaTargetRequest,
) -> RedfishError:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "storage_id": storage_id,
        "storage_pool_id": storage_pool_id,
        "capacity_source_id": capacity_source_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "AssignReplicaTarget",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Storage/{storage_id}/StoragePools/{storage_pool_id}/CapacitySources/{capacity_source_id}/ProvidingVolumes/{volume_id}/Actions/Volume.ChangeRAIDLayout",
    response_model_exclude_none=True,
)
@authenticate
async def change_raid_layout8(
    storage_id: str,
    storage_pool_id: str,
    capacity_source_id: str,
    volume_id: str,
    request: Request,
    response: Response,
    body: ChangeRaidLayoutRequest,
) -> RedfishError:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "storage_id": storage_id,
        "storage_pool_id": storage_pool_id,
        "capacity_source_id": capacity_source_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "ChangeRAIDLayout",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Storage/{storage_id}/StoragePools/{storage_pool_id}/CapacitySources/{capacity_source_id}/ProvidingVolumes/{volume_id}/Actions/Volume.CreateReplicaTarget",
    response_model_exclude_none=True,
)
@authenticate
async def create_replica_target8(
    storage_id: str,
    storage_pool_id: str,
    capacity_source_id: str,
    volume_id: str,
    request: Request,
    response: Response,
    body: CreateReplicaTargetRequest,
) -> RedfishError:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "storage_id": storage_id,
        "storage_pool_id": storage_pool_id,
        "capacity_source_id": capacity_source_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "CreateReplicaTarget",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Storage/{storage_id}/StoragePools/{storage_pool_id}/CapacitySources/{capacity_source_id}/ProvidingVolumes/{volume_id}/Actions/Volume.Initialize",
    response_model_exclude_none=True,
)
@authenticate
async def initialize8(
    storage_id: str,
    storage_pool_id: str,
    capacity_source_id: str,
    volume_id: str,
    request: Request,
    response: Response,
    body: InitializeRequest,
) -> RedfishError:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "storage_id": storage_id,
        "storage_pool_id": storage_pool_id,
        "capacity_source_id": capacity_source_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Initialize",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Storage/{storage_id}/StoragePools/{storage_pool_id}/CapacitySources/{capacity_source_id}/ProvidingVolumes/{volume_id}/Actions/Volume.RemoveReplicaRelationship",
    response_model_exclude_none=True,
)
@authenticate
async def remove_replica_relationship8(
    storage_id: str,
    storage_pool_id: str,
    capacity_source_id: str,
    volume_id: str,
    request: Request,
    response: Response,
    body: RemoveReplicaRelationshipRequest,
) -> RedfishError:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "storage_id": storage_id,
        "storage_pool_id": storage_pool_id,
        "capacity_source_id": capacity_source_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "RemoveReplicaRelationship",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Storage/{storage_id}/StoragePools/{storage_pool_id}/CapacitySources/{capacity_source_id}/ProvidingVolumes/{volume_id}/Actions/Volume.ResumeReplication",
    response_model_exclude_none=True,
)
@authenticate
async def resume_replication8(
    storage_id: str,
    storage_pool_id: str,
    capacity_source_id: str,
    volume_id: str,
    request: Request,
    response: Response,
    body: ResumeReplicationRequest,
) -> RedfishError:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "storage_id": storage_id,
        "storage_pool_id": storage_pool_id,
        "capacity_source_id": capacity_source_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "ResumeReplication",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Storage/{storage_id}/StoragePools/{storage_pool_id}/CapacitySources/{capacity_source_id}/ProvidingVolumes/{volume_id}/Actions/Volume.ReverseReplicationRelationship",
    response_model_exclude_none=True,
)
@authenticate
async def reverse_replication_relationship8(
    storage_id: str,
    storage_pool_id: str,
    capacity_source_id: str,
    volume_id: str,
    request: Request,
    response: Response,
    body: ReverseReplicationRelationshipRequest,
) -> RedfishError:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "storage_id": storage_id,
        "storage_pool_id": storage_pool_id,
        "capacity_source_id": capacity_source_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "ReverseReplicationRelationship",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Storage/{storage_id}/StoragePools/{storage_pool_id}/CapacitySources/{capacity_source_id}/ProvidingVolumes/{volume_id}/Actions/Volume.SplitReplication",
    response_model_exclude_none=True,
)
@authenticate
async def split_replication8(
    storage_id: str,
    storage_pool_id: str,
    capacity_source_id: str,
    volume_id: str,
    request: Request,
    response: Response,
    body: SplitReplicationRequest,
) -> RedfishError:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "storage_id": storage_id,
        "storage_pool_id": storage_pool_id,
        "capacity_source_id": capacity_source_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "SplitReplication",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Storage/{storage_id}/StoragePools/{storage_pool_id}/CapacitySources/{capacity_source_id}/ProvidingVolumes/{volume_id}/Actions/Volume.SuspendReplication",
    response_model_exclude_none=True,
)
@authenticate
async def suspend_replication8(
    storage_id: str,
    storage_pool_id: str,
    capacity_source_id: str,
    volume_id: str,
    request: Request,
    response: Response,
    body: SuspendReplicationRequest,
) -> RedfishError:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "storage_id": storage_id,
        "storage_pool_id": storage_pool_id,
        "capacity_source_id": capacity_source_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "SuspendReplication",
    }
    return s.action(**b)


@router.delete(
    "/redfish/v1/Storage/{storage_id}/Volumes/{volume_id}", response_model_exclude_none=True
)
@authenticate
async def delete9(storage_id: str, volume_id: str, request: Request, response: Response) -> None:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "storage_id": storage_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
    }
    return s.delete(**b)


@router.get(
    "/redfish/v1/Storage/{storage_id}/Volumes/{volume_id}", response_model_exclude_none=True
)
@router.head(
    "/redfish/v1/Storage/{storage_id}/Volumes/{volume_id}", response_model_exclude_none=True
)
async def get9(storage_id: str, volume_id: str, request: Request, response: Response) -> Volume:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "storage_id": storage_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
    }
    m = cast(Volume, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/Storage/{storage_id}/Volumes/{volume_id}", response_model_exclude_none=True
)
@authenticate
async def patch9(
    storage_id: str, volume_id: str, request: Request, response: Response, body: VolumeOnUpdate
) -> Volume:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "storage_id": storage_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Volume, s.patch(**b))


@router.post(
    "/redfish/v1/Storage/{storage_id}/Volumes/{volume_id}/Actions/Volume.AssignReplicaTarget",
    response_model_exclude_none=True,
)
@authenticate
async def assign_replica_target9(
    storage_id: str,
    volume_id: str,
    request: Request,
    response: Response,
    body: AssignReplicaTargetRequest,
) -> RedfishError:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "storage_id": storage_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "AssignReplicaTarget",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Storage/{storage_id}/Volumes/{volume_id}/Actions/Volume.ChangeRAIDLayout",
    response_model_exclude_none=True,
)
@authenticate
async def change_raid_layout9(
    storage_id: str,
    volume_id: str,
    request: Request,
    response: Response,
    body: ChangeRaidLayoutRequest,
) -> RedfishError:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "storage_id": storage_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "ChangeRAIDLayout",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Storage/{storage_id}/Volumes/{volume_id}/Actions/Volume.CreateReplicaTarget",
    response_model_exclude_none=True,
)
@authenticate
async def create_replica_target9(
    storage_id: str,
    volume_id: str,
    request: Request,
    response: Response,
    body: CreateReplicaTargetRequest,
) -> RedfishError:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "storage_id": storage_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "CreateReplicaTarget",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Storage/{storage_id}/Volumes/{volume_id}/Actions/Volume.Initialize",
    response_model_exclude_none=True,
)
@authenticate
async def initialize9(
    storage_id: str, volume_id: str, request: Request, response: Response, body: InitializeRequest
) -> RedfishError:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "storage_id": storage_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Initialize",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Storage/{storage_id}/Volumes/{volume_id}/Actions/Volume.RemoveReplicaRelationship",
    response_model_exclude_none=True,
)
@authenticate
async def remove_replica_relationship9(
    storage_id: str,
    volume_id: str,
    request: Request,
    response: Response,
    body: RemoveReplicaRelationshipRequest,
) -> RedfishError:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "storage_id": storage_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "RemoveReplicaRelationship",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Storage/{storage_id}/Volumes/{volume_id}/Actions/Volume.ResumeReplication",
    response_model_exclude_none=True,
)
@authenticate
async def resume_replication9(
    storage_id: str,
    volume_id: str,
    request: Request,
    response: Response,
    body: ResumeReplicationRequest,
) -> RedfishError:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "storage_id": storage_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "ResumeReplication",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Storage/{storage_id}/Volumes/{volume_id}/Actions/Volume.ReverseReplicationRelationship",
    response_model_exclude_none=True,
)
@authenticate
async def reverse_replication_relationship9(
    storage_id: str,
    volume_id: str,
    request: Request,
    response: Response,
    body: ReverseReplicationRelationshipRequest,
) -> RedfishError:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "storage_id": storage_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "ReverseReplicationRelationship",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Storage/{storage_id}/Volumes/{volume_id}/Actions/Volume.SplitReplication",
    response_model_exclude_none=True,
)
@authenticate
async def split_replication9(
    storage_id: str,
    volume_id: str,
    request: Request,
    response: Response,
    body: SplitReplicationRequest,
) -> RedfishError:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "storage_id": storage_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "SplitReplication",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Storage/{storage_id}/Volumes/{volume_id}/Actions/Volume.SuspendReplication",
    response_model_exclude_none=True,
)
@authenticate
async def suspend_replication9(
    storage_id: str,
    volume_id: str,
    request: Request,
    response: Response,
    body: SuspendReplicationRequest,
) -> RedfishError:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "storage_id": storage_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "SuspendReplication",
    }
    return s.action(**b)


@router.delete(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/ConsistencyGroups/{consistency_group_id}/Volumes/{volume_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete10(
    computer_system_id: str,
    storage_id: str,
    consistency_group_id: str,
    volume_id: str,
    request: Request,
    response: Response,
) -> None:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "consistency_group_id": consistency_group_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
    }
    return s.delete(**b)


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/ConsistencyGroups/{consistency_group_id}/Volumes/{volume_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/ConsistencyGroups/{consistency_group_id}/Volumes/{volume_id}",
    response_model_exclude_none=True,
)
async def get10(
    computer_system_id: str,
    storage_id: str,
    consistency_group_id: str,
    volume_id: str,
    request: Request,
    response: Response,
) -> Volume:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "consistency_group_id": consistency_group_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
    }
    m = cast(Volume, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/ConsistencyGroups/{consistency_group_id}/Volumes/{volume_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch10(
    computer_system_id: str,
    storage_id: str,
    consistency_group_id: str,
    volume_id: str,
    request: Request,
    response: Response,
    body: VolumeOnUpdate,
) -> Volume:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "consistency_group_id": consistency_group_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Volume, s.patch(**b))


@router.post(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/ConsistencyGroups/{consistency_group_id}/Volumes/{volume_id}/Actions/Volume.AssignReplicaTarget",
    response_model_exclude_none=True,
)
@authenticate
async def assign_replica_target10(
    computer_system_id: str,
    storage_id: str,
    consistency_group_id: str,
    volume_id: str,
    request: Request,
    response: Response,
    body: AssignReplicaTargetRequest,
) -> RedfishError:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "consistency_group_id": consistency_group_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "AssignReplicaTarget",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/ConsistencyGroups/{consistency_group_id}/Volumes/{volume_id}/Actions/Volume.ChangeRAIDLayout",
    response_model_exclude_none=True,
)
@authenticate
async def change_raid_layout10(
    computer_system_id: str,
    storage_id: str,
    consistency_group_id: str,
    volume_id: str,
    request: Request,
    response: Response,
    body: ChangeRaidLayoutRequest,
) -> RedfishError:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "consistency_group_id": consistency_group_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "ChangeRAIDLayout",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/ConsistencyGroups/{consistency_group_id}/Volumes/{volume_id}/Actions/Volume.CreateReplicaTarget",
    response_model_exclude_none=True,
)
@authenticate
async def create_replica_target10(
    computer_system_id: str,
    storage_id: str,
    consistency_group_id: str,
    volume_id: str,
    request: Request,
    response: Response,
    body: CreateReplicaTargetRequest,
) -> RedfishError:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "consistency_group_id": consistency_group_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "CreateReplicaTarget",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/ConsistencyGroups/{consistency_group_id}/Volumes/{volume_id}/Actions/Volume.Initialize",
    response_model_exclude_none=True,
)
@authenticate
async def initialize10(
    computer_system_id: str,
    storage_id: str,
    consistency_group_id: str,
    volume_id: str,
    request: Request,
    response: Response,
    body: InitializeRequest,
) -> RedfishError:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "consistency_group_id": consistency_group_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Initialize",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/ConsistencyGroups/{consistency_group_id}/Volumes/{volume_id}/Actions/Volume.RemoveReplicaRelationship",
    response_model_exclude_none=True,
)
@authenticate
async def remove_replica_relationship10(
    computer_system_id: str,
    storage_id: str,
    consistency_group_id: str,
    volume_id: str,
    request: Request,
    response: Response,
    body: RemoveReplicaRelationshipRequest,
) -> RedfishError:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "consistency_group_id": consistency_group_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "RemoveReplicaRelationship",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/ConsistencyGroups/{consistency_group_id}/Volumes/{volume_id}/Actions/Volume.ResumeReplication",
    response_model_exclude_none=True,
)
@authenticate
async def resume_replication10(
    computer_system_id: str,
    storage_id: str,
    consistency_group_id: str,
    volume_id: str,
    request: Request,
    response: Response,
    body: ResumeReplicationRequest,
) -> RedfishError:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "consistency_group_id": consistency_group_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "ResumeReplication",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/ConsistencyGroups/{consistency_group_id}/Volumes/{volume_id}/Actions/Volume.ReverseReplicationRelationship",
    response_model_exclude_none=True,
)
@authenticate
async def reverse_replication_relationship10(
    computer_system_id: str,
    storage_id: str,
    consistency_group_id: str,
    volume_id: str,
    request: Request,
    response: Response,
    body: ReverseReplicationRelationshipRequest,
) -> RedfishError:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "consistency_group_id": consistency_group_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "ReverseReplicationRelationship",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/ConsistencyGroups/{consistency_group_id}/Volumes/{volume_id}/Actions/Volume.SplitReplication",
    response_model_exclude_none=True,
)
@authenticate
async def split_replication10(
    computer_system_id: str,
    storage_id: str,
    consistency_group_id: str,
    volume_id: str,
    request: Request,
    response: Response,
    body: SplitReplicationRequest,
) -> RedfishError:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "consistency_group_id": consistency_group_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "SplitReplication",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/ConsistencyGroups/{consistency_group_id}/Volumes/{volume_id}/Actions/Volume.SuspendReplication",
    response_model_exclude_none=True,
)
@authenticate
async def suspend_replication10(
    computer_system_id: str,
    storage_id: str,
    consistency_group_id: str,
    volume_id: str,
    request: Request,
    response: Response,
    body: SuspendReplicationRequest,
) -> RedfishError:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "consistency_group_id": consistency_group_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "SuspendReplication",
    }
    return s.action(**b)


@router.delete(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/FileSystems/{file_system_id}/CapacitySources/{capacity_source_id}/ProvidingVolumes/{volume_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete11(
    computer_system_id: str,
    storage_id: str,
    file_system_id: str,
    capacity_source_id: str,
    volume_id: str,
    request: Request,
    response: Response,
) -> None:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "file_system_id": file_system_id,
        "capacity_source_id": capacity_source_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
    }
    return s.delete(**b)


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/FileSystems/{file_system_id}/CapacitySources/{capacity_source_id}/ProvidingVolumes/{volume_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/FileSystems/{file_system_id}/CapacitySources/{capacity_source_id}/ProvidingVolumes/{volume_id}",
    response_model_exclude_none=True,
)
async def get11(
    computer_system_id: str,
    storage_id: str,
    file_system_id: str,
    capacity_source_id: str,
    volume_id: str,
    request: Request,
    response: Response,
) -> Volume:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "file_system_id": file_system_id,
        "capacity_source_id": capacity_source_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
    }
    m = cast(Volume, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/FileSystems/{file_system_id}/CapacitySources/{capacity_source_id}/ProvidingVolumes/{volume_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch11(
    computer_system_id: str,
    storage_id: str,
    file_system_id: str,
    capacity_source_id: str,
    volume_id: str,
    request: Request,
    response: Response,
    body: VolumeOnUpdate,
) -> Volume:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "file_system_id": file_system_id,
        "capacity_source_id": capacity_source_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Volume, s.patch(**b))


@router.post(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/FileSystems/{file_system_id}/CapacitySources/{capacity_source_id}/ProvidingVolumes/{volume_id}/Actions/Volume.AssignReplicaTarget",
    response_model_exclude_none=True,
)
@authenticate
async def assign_replica_target11(
    computer_system_id: str,
    storage_id: str,
    file_system_id: str,
    capacity_source_id: str,
    volume_id: str,
    request: Request,
    response: Response,
    body: AssignReplicaTargetRequest,
) -> RedfishError:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "file_system_id": file_system_id,
        "capacity_source_id": capacity_source_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "AssignReplicaTarget",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/FileSystems/{file_system_id}/CapacitySources/{capacity_source_id}/ProvidingVolumes/{volume_id}/Actions/Volume.ChangeRAIDLayout",
    response_model_exclude_none=True,
)
@authenticate
async def change_raid_layout11(
    computer_system_id: str,
    storage_id: str,
    file_system_id: str,
    capacity_source_id: str,
    volume_id: str,
    request: Request,
    response: Response,
    body: ChangeRaidLayoutRequest,
) -> RedfishError:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "file_system_id": file_system_id,
        "capacity_source_id": capacity_source_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "ChangeRAIDLayout",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/FileSystems/{file_system_id}/CapacitySources/{capacity_source_id}/ProvidingVolumes/{volume_id}/Actions/Volume.CreateReplicaTarget",
    response_model_exclude_none=True,
)
@authenticate
async def create_replica_target11(
    computer_system_id: str,
    storage_id: str,
    file_system_id: str,
    capacity_source_id: str,
    volume_id: str,
    request: Request,
    response: Response,
    body: CreateReplicaTargetRequest,
) -> RedfishError:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "file_system_id": file_system_id,
        "capacity_source_id": capacity_source_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "CreateReplicaTarget",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/FileSystems/{file_system_id}/CapacitySources/{capacity_source_id}/ProvidingVolumes/{volume_id}/Actions/Volume.Initialize",
    response_model_exclude_none=True,
)
@authenticate
async def initialize11(
    computer_system_id: str,
    storage_id: str,
    file_system_id: str,
    capacity_source_id: str,
    volume_id: str,
    request: Request,
    response: Response,
    body: InitializeRequest,
) -> RedfishError:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "file_system_id": file_system_id,
        "capacity_source_id": capacity_source_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Initialize",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/FileSystems/{file_system_id}/CapacitySources/{capacity_source_id}/ProvidingVolumes/{volume_id}/Actions/Volume.RemoveReplicaRelationship",
    response_model_exclude_none=True,
)
@authenticate
async def remove_replica_relationship11(
    computer_system_id: str,
    storage_id: str,
    file_system_id: str,
    capacity_source_id: str,
    volume_id: str,
    request: Request,
    response: Response,
    body: RemoveReplicaRelationshipRequest,
) -> RedfishError:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "file_system_id": file_system_id,
        "capacity_source_id": capacity_source_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "RemoveReplicaRelationship",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/FileSystems/{file_system_id}/CapacitySources/{capacity_source_id}/ProvidingVolumes/{volume_id}/Actions/Volume.ResumeReplication",
    response_model_exclude_none=True,
)
@authenticate
async def resume_replication11(
    computer_system_id: str,
    storage_id: str,
    file_system_id: str,
    capacity_source_id: str,
    volume_id: str,
    request: Request,
    response: Response,
    body: ResumeReplicationRequest,
) -> RedfishError:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "file_system_id": file_system_id,
        "capacity_source_id": capacity_source_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "ResumeReplication",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/FileSystems/{file_system_id}/CapacitySources/{capacity_source_id}/ProvidingVolumes/{volume_id}/Actions/Volume.ReverseReplicationRelationship",
    response_model_exclude_none=True,
)
@authenticate
async def reverse_replication_relationship11(
    computer_system_id: str,
    storage_id: str,
    file_system_id: str,
    capacity_source_id: str,
    volume_id: str,
    request: Request,
    response: Response,
    body: ReverseReplicationRelationshipRequest,
) -> RedfishError:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "file_system_id": file_system_id,
        "capacity_source_id": capacity_source_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "ReverseReplicationRelationship",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/FileSystems/{file_system_id}/CapacitySources/{capacity_source_id}/ProvidingVolumes/{volume_id}/Actions/Volume.SplitReplication",
    response_model_exclude_none=True,
)
@authenticate
async def split_replication11(
    computer_system_id: str,
    storage_id: str,
    file_system_id: str,
    capacity_source_id: str,
    volume_id: str,
    request: Request,
    response: Response,
    body: SplitReplicationRequest,
) -> RedfishError:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "file_system_id": file_system_id,
        "capacity_source_id": capacity_source_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "SplitReplication",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/FileSystems/{file_system_id}/CapacitySources/{capacity_source_id}/ProvidingVolumes/{volume_id}/Actions/Volume.SuspendReplication",
    response_model_exclude_none=True,
)
@authenticate
async def suspend_replication11(
    computer_system_id: str,
    storage_id: str,
    file_system_id: str,
    capacity_source_id: str,
    volume_id: str,
    request: Request,
    response: Response,
    body: SuspendReplicationRequest,
) -> RedfishError:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "file_system_id": file_system_id,
        "capacity_source_id": capacity_source_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "SuspendReplication",
    }
    return s.action(**b)


@router.delete(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/StoragePools/{storage_pool_id}/AllocatedVolumes/{volume_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete12(
    computer_system_id: str,
    storage_id: str,
    storage_pool_id: str,
    volume_id: str,
    request: Request,
    response: Response,
) -> None:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "storage_pool_id": storage_pool_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
    }
    return s.delete(**b)


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/StoragePools/{storage_pool_id}/AllocatedVolumes/{volume_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/StoragePools/{storage_pool_id}/AllocatedVolumes/{volume_id}",
    response_model_exclude_none=True,
)
async def get12(
    computer_system_id: str,
    storage_id: str,
    storage_pool_id: str,
    volume_id: str,
    request: Request,
    response: Response,
) -> Volume:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "storage_pool_id": storage_pool_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
    }
    m = cast(Volume, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/StoragePools/{storage_pool_id}/AllocatedVolumes/{volume_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch12(
    computer_system_id: str,
    storage_id: str,
    storage_pool_id: str,
    volume_id: str,
    request: Request,
    response: Response,
    body: VolumeOnUpdate,
) -> Volume:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "storage_pool_id": storage_pool_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Volume, s.patch(**b))


@router.post(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/StoragePools/{storage_pool_id}/AllocatedVolumes/{volume_id}/Actions/Volume.AssignReplicaTarget",
    response_model_exclude_none=True,
)
@authenticate
async def assign_replica_target12(
    computer_system_id: str,
    storage_id: str,
    storage_pool_id: str,
    volume_id: str,
    request: Request,
    response: Response,
    body: AssignReplicaTargetRequest,
) -> RedfishError:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "storage_pool_id": storage_pool_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "AssignReplicaTarget",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/StoragePools/{storage_pool_id}/AllocatedVolumes/{volume_id}/Actions/Volume.ChangeRAIDLayout",
    response_model_exclude_none=True,
)
@authenticate
async def change_raid_layout12(
    computer_system_id: str,
    storage_id: str,
    storage_pool_id: str,
    volume_id: str,
    request: Request,
    response: Response,
    body: ChangeRaidLayoutRequest,
) -> RedfishError:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "storage_pool_id": storage_pool_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "ChangeRAIDLayout",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/StoragePools/{storage_pool_id}/AllocatedVolumes/{volume_id}/Actions/Volume.CreateReplicaTarget",
    response_model_exclude_none=True,
)
@authenticate
async def create_replica_target12(
    computer_system_id: str,
    storage_id: str,
    storage_pool_id: str,
    volume_id: str,
    request: Request,
    response: Response,
    body: CreateReplicaTargetRequest,
) -> RedfishError:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "storage_pool_id": storage_pool_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "CreateReplicaTarget",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/StoragePools/{storage_pool_id}/AllocatedVolumes/{volume_id}/Actions/Volume.Initialize",
    response_model_exclude_none=True,
)
@authenticate
async def initialize12(
    computer_system_id: str,
    storage_id: str,
    storage_pool_id: str,
    volume_id: str,
    request: Request,
    response: Response,
    body: InitializeRequest,
) -> RedfishError:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "storage_pool_id": storage_pool_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Initialize",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/StoragePools/{storage_pool_id}/AllocatedVolumes/{volume_id}/Actions/Volume.RemoveReplicaRelationship",
    response_model_exclude_none=True,
)
@authenticate
async def remove_replica_relationship12(
    computer_system_id: str,
    storage_id: str,
    storage_pool_id: str,
    volume_id: str,
    request: Request,
    response: Response,
    body: RemoveReplicaRelationshipRequest,
) -> RedfishError:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "storage_pool_id": storage_pool_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "RemoveReplicaRelationship",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/StoragePools/{storage_pool_id}/AllocatedVolumes/{volume_id}/Actions/Volume.ResumeReplication",
    response_model_exclude_none=True,
)
@authenticate
async def resume_replication12(
    computer_system_id: str,
    storage_id: str,
    storage_pool_id: str,
    volume_id: str,
    request: Request,
    response: Response,
    body: ResumeReplicationRequest,
) -> RedfishError:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "storage_pool_id": storage_pool_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "ResumeReplication",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/StoragePools/{storage_pool_id}/AllocatedVolumes/{volume_id}/Actions/Volume.ReverseReplicationRelationship",
    response_model_exclude_none=True,
)
@authenticate
async def reverse_replication_relationship12(
    computer_system_id: str,
    storage_id: str,
    storage_pool_id: str,
    volume_id: str,
    request: Request,
    response: Response,
    body: ReverseReplicationRelationshipRequest,
) -> RedfishError:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "storage_pool_id": storage_pool_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "ReverseReplicationRelationship",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/StoragePools/{storage_pool_id}/AllocatedVolumes/{volume_id}/Actions/Volume.SplitReplication",
    response_model_exclude_none=True,
)
@authenticate
async def split_replication12(
    computer_system_id: str,
    storage_id: str,
    storage_pool_id: str,
    volume_id: str,
    request: Request,
    response: Response,
    body: SplitReplicationRequest,
) -> RedfishError:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "storage_pool_id": storage_pool_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "SplitReplication",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/StoragePools/{storage_pool_id}/AllocatedVolumes/{volume_id}/Actions/Volume.SuspendReplication",
    response_model_exclude_none=True,
)
@authenticate
async def suspend_replication12(
    computer_system_id: str,
    storage_id: str,
    storage_pool_id: str,
    volume_id: str,
    request: Request,
    response: Response,
    body: SuspendReplicationRequest,
) -> RedfishError:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "storage_pool_id": storage_pool_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "SuspendReplication",
    }
    return s.action(**b)


@router.delete(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/StoragePools/{storage_pool_id}/CapacitySources/{capacity_source_id}/ProvidingVolumes/{volume_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete13(
    computer_system_id: str,
    storage_id: str,
    storage_pool_id: str,
    capacity_source_id: str,
    volume_id: str,
    request: Request,
    response: Response,
) -> None:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "storage_pool_id": storage_pool_id,
        "capacity_source_id": capacity_source_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
    }
    return s.delete(**b)


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/StoragePools/{storage_pool_id}/CapacitySources/{capacity_source_id}/ProvidingVolumes/{volume_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/StoragePools/{storage_pool_id}/CapacitySources/{capacity_source_id}/ProvidingVolumes/{volume_id}",
    response_model_exclude_none=True,
)
async def get13(
    computer_system_id: str,
    storage_id: str,
    storage_pool_id: str,
    capacity_source_id: str,
    volume_id: str,
    request: Request,
    response: Response,
) -> Volume:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "storage_pool_id": storage_pool_id,
        "capacity_source_id": capacity_source_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
    }
    m = cast(Volume, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/StoragePools/{storage_pool_id}/CapacitySources/{capacity_source_id}/ProvidingVolumes/{volume_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch13(
    computer_system_id: str,
    storage_id: str,
    storage_pool_id: str,
    capacity_source_id: str,
    volume_id: str,
    request: Request,
    response: Response,
    body: VolumeOnUpdate,
) -> Volume:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "storage_pool_id": storage_pool_id,
        "capacity_source_id": capacity_source_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Volume, s.patch(**b))


@router.post(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/StoragePools/{storage_pool_id}/CapacitySources/{capacity_source_id}/ProvidingVolumes/{volume_id}/Actions/Volume.AssignReplicaTarget",
    response_model_exclude_none=True,
)
@authenticate
async def assign_replica_target13(
    computer_system_id: str,
    storage_id: str,
    storage_pool_id: str,
    capacity_source_id: str,
    volume_id: str,
    request: Request,
    response: Response,
    body: AssignReplicaTargetRequest,
) -> RedfishError:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "storage_pool_id": storage_pool_id,
        "capacity_source_id": capacity_source_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "AssignReplicaTarget",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/StoragePools/{storage_pool_id}/CapacitySources/{capacity_source_id}/ProvidingVolumes/{volume_id}/Actions/Volume.ChangeRAIDLayout",
    response_model_exclude_none=True,
)
@authenticate
async def change_raid_layout13(
    computer_system_id: str,
    storage_id: str,
    storage_pool_id: str,
    capacity_source_id: str,
    volume_id: str,
    request: Request,
    response: Response,
    body: ChangeRaidLayoutRequest,
) -> RedfishError:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "storage_pool_id": storage_pool_id,
        "capacity_source_id": capacity_source_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "ChangeRAIDLayout",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/StoragePools/{storage_pool_id}/CapacitySources/{capacity_source_id}/ProvidingVolumes/{volume_id}/Actions/Volume.CreateReplicaTarget",
    response_model_exclude_none=True,
)
@authenticate
async def create_replica_target13(
    computer_system_id: str,
    storage_id: str,
    storage_pool_id: str,
    capacity_source_id: str,
    volume_id: str,
    request: Request,
    response: Response,
    body: CreateReplicaTargetRequest,
) -> RedfishError:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "storage_pool_id": storage_pool_id,
        "capacity_source_id": capacity_source_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "CreateReplicaTarget",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/StoragePools/{storage_pool_id}/CapacitySources/{capacity_source_id}/ProvidingVolumes/{volume_id}/Actions/Volume.Initialize",
    response_model_exclude_none=True,
)
@authenticate
async def initialize13(
    computer_system_id: str,
    storage_id: str,
    storage_pool_id: str,
    capacity_source_id: str,
    volume_id: str,
    request: Request,
    response: Response,
    body: InitializeRequest,
) -> RedfishError:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "storage_pool_id": storage_pool_id,
        "capacity_source_id": capacity_source_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Initialize",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/StoragePools/{storage_pool_id}/CapacitySources/{capacity_source_id}/ProvidingVolumes/{volume_id}/Actions/Volume.RemoveReplicaRelationship",
    response_model_exclude_none=True,
)
@authenticate
async def remove_replica_relationship13(
    computer_system_id: str,
    storage_id: str,
    storage_pool_id: str,
    capacity_source_id: str,
    volume_id: str,
    request: Request,
    response: Response,
    body: RemoveReplicaRelationshipRequest,
) -> RedfishError:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "storage_pool_id": storage_pool_id,
        "capacity_source_id": capacity_source_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "RemoveReplicaRelationship",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/StoragePools/{storage_pool_id}/CapacitySources/{capacity_source_id}/ProvidingVolumes/{volume_id}/Actions/Volume.ResumeReplication",
    response_model_exclude_none=True,
)
@authenticate
async def resume_replication13(
    computer_system_id: str,
    storage_id: str,
    storage_pool_id: str,
    capacity_source_id: str,
    volume_id: str,
    request: Request,
    response: Response,
    body: ResumeReplicationRequest,
) -> RedfishError:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "storage_pool_id": storage_pool_id,
        "capacity_source_id": capacity_source_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "ResumeReplication",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/StoragePools/{storage_pool_id}/CapacitySources/{capacity_source_id}/ProvidingVolumes/{volume_id}/Actions/Volume.ReverseReplicationRelationship",
    response_model_exclude_none=True,
)
@authenticate
async def reverse_replication_relationship13(
    computer_system_id: str,
    storage_id: str,
    storage_pool_id: str,
    capacity_source_id: str,
    volume_id: str,
    request: Request,
    response: Response,
    body: ReverseReplicationRelationshipRequest,
) -> RedfishError:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "storage_pool_id": storage_pool_id,
        "capacity_source_id": capacity_source_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "ReverseReplicationRelationship",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/StoragePools/{storage_pool_id}/CapacitySources/{capacity_source_id}/ProvidingVolumes/{volume_id}/Actions/Volume.SplitReplication",
    response_model_exclude_none=True,
)
@authenticate
async def split_replication13(
    computer_system_id: str,
    storage_id: str,
    storage_pool_id: str,
    capacity_source_id: str,
    volume_id: str,
    request: Request,
    response: Response,
    body: SplitReplicationRequest,
) -> RedfishError:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "storage_pool_id": storage_pool_id,
        "capacity_source_id": capacity_source_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "SplitReplication",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/StoragePools/{storage_pool_id}/CapacitySources/{capacity_source_id}/ProvidingVolumes/{volume_id}/Actions/Volume.SuspendReplication",
    response_model_exclude_none=True,
)
@authenticate
async def suspend_replication13(
    computer_system_id: str,
    storage_id: str,
    storage_pool_id: str,
    capacity_source_id: str,
    volume_id: str,
    request: Request,
    response: Response,
    body: SuspendReplicationRequest,
) -> RedfishError:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "storage_pool_id": storage_pool_id,
        "capacity_source_id": capacity_source_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "SuspendReplication",
    }
    return s.action(**b)


@router.delete(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/Volumes/{volume_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete14(
    computer_system_id: str, storage_id: str, volume_id: str, request: Request, response: Response
) -> None:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
    }
    return s.delete(**b)


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/Volumes/{volume_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/Volumes/{volume_id}",
    response_model_exclude_none=True,
)
async def get14(
    computer_system_id: str, storage_id: str, volume_id: str, request: Request, response: Response
) -> Volume:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
    }
    m = cast(Volume, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/Volumes/{volume_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch14(
    computer_system_id: str,
    storage_id: str,
    volume_id: str,
    request: Request,
    response: Response,
    body: VolumeOnUpdate,
) -> Volume:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Volume, s.patch(**b))


@router.post(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/Volumes/{volume_id}/Actions/Volume.AssignReplicaTarget",
    response_model_exclude_none=True,
)
@authenticate
async def assign_replica_target14(
    computer_system_id: str,
    storage_id: str,
    volume_id: str,
    request: Request,
    response: Response,
    body: AssignReplicaTargetRequest,
) -> RedfishError:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "AssignReplicaTarget",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/Volumes/{volume_id}/Actions/Volume.ChangeRAIDLayout",
    response_model_exclude_none=True,
)
@authenticate
async def change_raid_layout14(
    computer_system_id: str,
    storage_id: str,
    volume_id: str,
    request: Request,
    response: Response,
    body: ChangeRaidLayoutRequest,
) -> RedfishError:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "ChangeRAIDLayout",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/Volumes/{volume_id}/Actions/Volume.CreateReplicaTarget",
    response_model_exclude_none=True,
)
@authenticate
async def create_replica_target14(
    computer_system_id: str,
    storage_id: str,
    volume_id: str,
    request: Request,
    response: Response,
    body: CreateReplicaTargetRequest,
) -> RedfishError:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "CreateReplicaTarget",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/Volumes/{volume_id}/Actions/Volume.Initialize",
    response_model_exclude_none=True,
)
@authenticate
async def initialize14(
    computer_system_id: str,
    storage_id: str,
    volume_id: str,
    request: Request,
    response: Response,
    body: InitializeRequest,
) -> RedfishError:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Initialize",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/Volumes/{volume_id}/Actions/Volume.RemoveReplicaRelationship",
    response_model_exclude_none=True,
)
@authenticate
async def remove_replica_relationship14(
    computer_system_id: str,
    storage_id: str,
    volume_id: str,
    request: Request,
    response: Response,
    body: RemoveReplicaRelationshipRequest,
) -> RedfishError:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "RemoveReplicaRelationship",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/Volumes/{volume_id}/Actions/Volume.ResumeReplication",
    response_model_exclude_none=True,
)
@authenticate
async def resume_replication14(
    computer_system_id: str,
    storage_id: str,
    volume_id: str,
    request: Request,
    response: Response,
    body: ResumeReplicationRequest,
) -> RedfishError:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "ResumeReplication",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/Volumes/{volume_id}/Actions/Volume.ReverseReplicationRelationship",
    response_model_exclude_none=True,
)
@authenticate
async def reverse_replication_relationship14(
    computer_system_id: str,
    storage_id: str,
    volume_id: str,
    request: Request,
    response: Response,
    body: ReverseReplicationRelationshipRequest,
) -> RedfishError:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "ReverseReplicationRelationship",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/Volumes/{volume_id}/Actions/Volume.SplitReplication",
    response_model_exclude_none=True,
)
@authenticate
async def split_replication14(
    computer_system_id: str,
    storage_id: str,
    volume_id: str,
    request: Request,
    response: Response,
    body: SplitReplicationRequest,
) -> RedfishError:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "SplitReplication",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/Volumes/{volume_id}/Actions/Volume.SuspendReplication",
    response_model_exclude_none=True,
)
@authenticate
async def suspend_replication14(
    computer_system_id: str,
    storage_id: str,
    volume_id: str,
    request: Request,
    response: Response,
    body: SuspendReplicationRequest,
) -> RedfishError:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "SuspendReplication",
    }
    return s.action(**b)


@router.delete(
    "/redfish/v1/StorageServices/{storage_service_id}/ConsistencyGroups/{consistency_group_id}/Volumes/{volume_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete15(
    storage_service_id: str,
    consistency_group_id: str,
    volume_id: str,
    request: Request,
    response: Response,
) -> None:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "consistency_group_id": consistency_group_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
    }
    return s.delete(**b)


@router.get(
    "/redfish/v1/StorageServices/{storage_service_id}/ConsistencyGroups/{consistency_group_id}/Volumes/{volume_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/StorageServices/{storage_service_id}/ConsistencyGroups/{consistency_group_id}/Volumes/{volume_id}",
    response_model_exclude_none=True,
)
async def get15(
    storage_service_id: str,
    consistency_group_id: str,
    volume_id: str,
    request: Request,
    response: Response,
) -> Volume:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "consistency_group_id": consistency_group_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
    }
    m = cast(Volume, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/StorageServices/{storage_service_id}/ConsistencyGroups/{consistency_group_id}/Volumes/{volume_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch15(
    storage_service_id: str,
    consistency_group_id: str,
    volume_id: str,
    request: Request,
    response: Response,
    body: VolumeOnUpdate,
) -> Volume:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "consistency_group_id": consistency_group_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Volume, s.patch(**b))


@router.post(
    "/redfish/v1/StorageServices/{storage_service_id}/ConsistencyGroups/{consistency_group_id}/Volumes/{volume_id}/Actions/Volume.AssignReplicaTarget",
    response_model_exclude_none=True,
)
@authenticate
async def assign_replica_target15(
    storage_service_id: str,
    consistency_group_id: str,
    volume_id: str,
    request: Request,
    response: Response,
    body: AssignReplicaTargetRequest,
) -> RedfishError:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "consistency_group_id": consistency_group_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "AssignReplicaTarget",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/StorageServices/{storage_service_id}/ConsistencyGroups/{consistency_group_id}/Volumes/{volume_id}/Actions/Volume.ChangeRAIDLayout",
    response_model_exclude_none=True,
)
@authenticate
async def change_raid_layout15(
    storage_service_id: str,
    consistency_group_id: str,
    volume_id: str,
    request: Request,
    response: Response,
    body: ChangeRaidLayoutRequest,
) -> RedfishError:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "consistency_group_id": consistency_group_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "ChangeRAIDLayout",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/StorageServices/{storage_service_id}/ConsistencyGroups/{consistency_group_id}/Volumes/{volume_id}/Actions/Volume.CreateReplicaTarget",
    response_model_exclude_none=True,
)
@authenticate
async def create_replica_target15(
    storage_service_id: str,
    consistency_group_id: str,
    volume_id: str,
    request: Request,
    response: Response,
    body: CreateReplicaTargetRequest,
) -> RedfishError:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "consistency_group_id": consistency_group_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "CreateReplicaTarget",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/StorageServices/{storage_service_id}/ConsistencyGroups/{consistency_group_id}/Volumes/{volume_id}/Actions/Volume.Initialize",
    response_model_exclude_none=True,
)
@authenticate
async def initialize15(
    storage_service_id: str,
    consistency_group_id: str,
    volume_id: str,
    request: Request,
    response: Response,
    body: InitializeRequest,
) -> RedfishError:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "consistency_group_id": consistency_group_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Initialize",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/StorageServices/{storage_service_id}/ConsistencyGroups/{consistency_group_id}/Volumes/{volume_id}/Actions/Volume.RemoveReplicaRelationship",
    response_model_exclude_none=True,
)
@authenticate
async def remove_replica_relationship15(
    storage_service_id: str,
    consistency_group_id: str,
    volume_id: str,
    request: Request,
    response: Response,
    body: RemoveReplicaRelationshipRequest,
) -> RedfishError:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "consistency_group_id": consistency_group_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "RemoveReplicaRelationship",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/StorageServices/{storage_service_id}/ConsistencyGroups/{consistency_group_id}/Volumes/{volume_id}/Actions/Volume.ResumeReplication",
    response_model_exclude_none=True,
)
@authenticate
async def resume_replication15(
    storage_service_id: str,
    consistency_group_id: str,
    volume_id: str,
    request: Request,
    response: Response,
    body: ResumeReplicationRequest,
) -> RedfishError:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "consistency_group_id": consistency_group_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "ResumeReplication",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/StorageServices/{storage_service_id}/ConsistencyGroups/{consistency_group_id}/Volumes/{volume_id}/Actions/Volume.ReverseReplicationRelationship",
    response_model_exclude_none=True,
)
@authenticate
async def reverse_replication_relationship15(
    storage_service_id: str,
    consistency_group_id: str,
    volume_id: str,
    request: Request,
    response: Response,
    body: ReverseReplicationRelationshipRequest,
) -> RedfishError:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "consistency_group_id": consistency_group_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "ReverseReplicationRelationship",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/StorageServices/{storage_service_id}/ConsistencyGroups/{consistency_group_id}/Volumes/{volume_id}/Actions/Volume.SplitReplication",
    response_model_exclude_none=True,
)
@authenticate
async def split_replication15(
    storage_service_id: str,
    consistency_group_id: str,
    volume_id: str,
    request: Request,
    response: Response,
    body: SplitReplicationRequest,
) -> RedfishError:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "consistency_group_id": consistency_group_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "SplitReplication",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/StorageServices/{storage_service_id}/ConsistencyGroups/{consistency_group_id}/Volumes/{volume_id}/Actions/Volume.SuspendReplication",
    response_model_exclude_none=True,
)
@authenticate
async def suspend_replication15(
    storage_service_id: str,
    consistency_group_id: str,
    volume_id: str,
    request: Request,
    response: Response,
    body: SuspendReplicationRequest,
) -> RedfishError:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "consistency_group_id": consistency_group_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "SuspendReplication",
    }
    return s.action(**b)


@router.delete(
    "/redfish/v1/StorageServices/{storage_service_id}/FileSystems/{file_system_id}/CapacitySources/{capacity_source_id}/ProvidingVolumes/{volume_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete16(
    storage_service_id: str,
    file_system_id: str,
    capacity_source_id: str,
    volume_id: str,
    request: Request,
    response: Response,
) -> None:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "file_system_id": file_system_id,
        "capacity_source_id": capacity_source_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
    }
    return s.delete(**b)


@router.get(
    "/redfish/v1/StorageServices/{storage_service_id}/FileSystems/{file_system_id}/CapacitySources/{capacity_source_id}/ProvidingVolumes/{volume_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/StorageServices/{storage_service_id}/FileSystems/{file_system_id}/CapacitySources/{capacity_source_id}/ProvidingVolumes/{volume_id}",
    response_model_exclude_none=True,
)
async def get16(
    storage_service_id: str,
    file_system_id: str,
    capacity_source_id: str,
    volume_id: str,
    request: Request,
    response: Response,
) -> Volume:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "file_system_id": file_system_id,
        "capacity_source_id": capacity_source_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
    }
    m = cast(Volume, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/StorageServices/{storage_service_id}/FileSystems/{file_system_id}/CapacitySources/{capacity_source_id}/ProvidingVolumes/{volume_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch16(
    storage_service_id: str,
    file_system_id: str,
    capacity_source_id: str,
    volume_id: str,
    request: Request,
    response: Response,
    body: VolumeOnUpdate,
) -> Volume:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "file_system_id": file_system_id,
        "capacity_source_id": capacity_source_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Volume, s.patch(**b))


@router.post(
    "/redfish/v1/StorageServices/{storage_service_id}/FileSystems/{file_system_id}/CapacitySources/{capacity_source_id}/ProvidingVolumes/{volume_id}/Actions/Volume.AssignReplicaTarget",
    response_model_exclude_none=True,
)
@authenticate
async def assign_replica_target16(
    storage_service_id: str,
    file_system_id: str,
    capacity_source_id: str,
    volume_id: str,
    request: Request,
    response: Response,
    body: AssignReplicaTargetRequest,
) -> RedfishError:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "file_system_id": file_system_id,
        "capacity_source_id": capacity_source_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "AssignReplicaTarget",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/StorageServices/{storage_service_id}/FileSystems/{file_system_id}/CapacitySources/{capacity_source_id}/ProvidingVolumes/{volume_id}/Actions/Volume.ChangeRAIDLayout",
    response_model_exclude_none=True,
)
@authenticate
async def change_raid_layout16(
    storage_service_id: str,
    file_system_id: str,
    capacity_source_id: str,
    volume_id: str,
    request: Request,
    response: Response,
    body: ChangeRaidLayoutRequest,
) -> RedfishError:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "file_system_id": file_system_id,
        "capacity_source_id": capacity_source_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "ChangeRAIDLayout",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/StorageServices/{storage_service_id}/FileSystems/{file_system_id}/CapacitySources/{capacity_source_id}/ProvidingVolumes/{volume_id}/Actions/Volume.CreateReplicaTarget",
    response_model_exclude_none=True,
)
@authenticate
async def create_replica_target16(
    storage_service_id: str,
    file_system_id: str,
    capacity_source_id: str,
    volume_id: str,
    request: Request,
    response: Response,
    body: CreateReplicaTargetRequest,
) -> RedfishError:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "file_system_id": file_system_id,
        "capacity_source_id": capacity_source_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "CreateReplicaTarget",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/StorageServices/{storage_service_id}/FileSystems/{file_system_id}/CapacitySources/{capacity_source_id}/ProvidingVolumes/{volume_id}/Actions/Volume.Initialize",
    response_model_exclude_none=True,
)
@authenticate
async def initialize16(
    storage_service_id: str,
    file_system_id: str,
    capacity_source_id: str,
    volume_id: str,
    request: Request,
    response: Response,
    body: InitializeRequest,
) -> RedfishError:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "file_system_id": file_system_id,
        "capacity_source_id": capacity_source_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Initialize",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/StorageServices/{storage_service_id}/FileSystems/{file_system_id}/CapacitySources/{capacity_source_id}/ProvidingVolumes/{volume_id}/Actions/Volume.RemoveReplicaRelationship",
    response_model_exclude_none=True,
)
@authenticate
async def remove_replica_relationship16(
    storage_service_id: str,
    file_system_id: str,
    capacity_source_id: str,
    volume_id: str,
    request: Request,
    response: Response,
    body: RemoveReplicaRelationshipRequest,
) -> RedfishError:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "file_system_id": file_system_id,
        "capacity_source_id": capacity_source_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "RemoveReplicaRelationship",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/StorageServices/{storage_service_id}/FileSystems/{file_system_id}/CapacitySources/{capacity_source_id}/ProvidingVolumes/{volume_id}/Actions/Volume.ResumeReplication",
    response_model_exclude_none=True,
)
@authenticate
async def resume_replication16(
    storage_service_id: str,
    file_system_id: str,
    capacity_source_id: str,
    volume_id: str,
    request: Request,
    response: Response,
    body: ResumeReplicationRequest,
) -> RedfishError:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "file_system_id": file_system_id,
        "capacity_source_id": capacity_source_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "ResumeReplication",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/StorageServices/{storage_service_id}/FileSystems/{file_system_id}/CapacitySources/{capacity_source_id}/ProvidingVolumes/{volume_id}/Actions/Volume.ReverseReplicationRelationship",
    response_model_exclude_none=True,
)
@authenticate
async def reverse_replication_relationship16(
    storage_service_id: str,
    file_system_id: str,
    capacity_source_id: str,
    volume_id: str,
    request: Request,
    response: Response,
    body: ReverseReplicationRelationshipRequest,
) -> RedfishError:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "file_system_id": file_system_id,
        "capacity_source_id": capacity_source_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "ReverseReplicationRelationship",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/StorageServices/{storage_service_id}/FileSystems/{file_system_id}/CapacitySources/{capacity_source_id}/ProvidingVolumes/{volume_id}/Actions/Volume.SplitReplication",
    response_model_exclude_none=True,
)
@authenticate
async def split_replication16(
    storage_service_id: str,
    file_system_id: str,
    capacity_source_id: str,
    volume_id: str,
    request: Request,
    response: Response,
    body: SplitReplicationRequest,
) -> RedfishError:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "file_system_id": file_system_id,
        "capacity_source_id": capacity_source_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "SplitReplication",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/StorageServices/{storage_service_id}/FileSystems/{file_system_id}/CapacitySources/{capacity_source_id}/ProvidingVolumes/{volume_id}/Actions/Volume.SuspendReplication",
    response_model_exclude_none=True,
)
@authenticate
async def suspend_replication16(
    storage_service_id: str,
    file_system_id: str,
    capacity_source_id: str,
    volume_id: str,
    request: Request,
    response: Response,
    body: SuspendReplicationRequest,
) -> RedfishError:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "file_system_id": file_system_id,
        "capacity_source_id": capacity_source_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "SuspendReplication",
    }
    return s.action(**b)


@router.delete(
    "/redfish/v1/StorageServices/{storage_service_id}/StoragePools/{storage_pool_id}/AllocatedVolumes/{volume_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete17(
    storage_service_id: str,
    storage_pool_id: str,
    volume_id: str,
    request: Request,
    response: Response,
) -> None:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "storage_pool_id": storage_pool_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
    }
    return s.delete(**b)


@router.get(
    "/redfish/v1/StorageServices/{storage_service_id}/StoragePools/{storage_pool_id}/AllocatedVolumes/{volume_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/StorageServices/{storage_service_id}/StoragePools/{storage_pool_id}/AllocatedVolumes/{volume_id}",
    response_model_exclude_none=True,
)
async def get17(
    storage_service_id: str,
    storage_pool_id: str,
    volume_id: str,
    request: Request,
    response: Response,
) -> Volume:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "storage_pool_id": storage_pool_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
    }
    m = cast(Volume, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/StorageServices/{storage_service_id}/StoragePools/{storage_pool_id}/AllocatedVolumes/{volume_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch17(
    storage_service_id: str,
    storage_pool_id: str,
    volume_id: str,
    request: Request,
    response: Response,
    body: VolumeOnUpdate,
) -> Volume:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "storage_pool_id": storage_pool_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Volume, s.patch(**b))


@router.post(
    "/redfish/v1/StorageServices/{storage_service_id}/StoragePools/{storage_pool_id}/AllocatedVolumes/{volume_id}/Actions/Volume.AssignReplicaTarget",
    response_model_exclude_none=True,
)
@authenticate
async def assign_replica_target17(
    storage_service_id: str,
    storage_pool_id: str,
    volume_id: str,
    request: Request,
    response: Response,
    body: AssignReplicaTargetRequest,
) -> RedfishError:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "storage_pool_id": storage_pool_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "AssignReplicaTarget",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/StorageServices/{storage_service_id}/StoragePools/{storage_pool_id}/AllocatedVolumes/{volume_id}/Actions/Volume.ChangeRAIDLayout",
    response_model_exclude_none=True,
)
@authenticate
async def change_raid_layout17(
    storage_service_id: str,
    storage_pool_id: str,
    volume_id: str,
    request: Request,
    response: Response,
    body: ChangeRaidLayoutRequest,
) -> RedfishError:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "storage_pool_id": storage_pool_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "ChangeRAIDLayout",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/StorageServices/{storage_service_id}/StoragePools/{storage_pool_id}/AllocatedVolumes/{volume_id}/Actions/Volume.CreateReplicaTarget",
    response_model_exclude_none=True,
)
@authenticate
async def create_replica_target17(
    storage_service_id: str,
    storage_pool_id: str,
    volume_id: str,
    request: Request,
    response: Response,
    body: CreateReplicaTargetRequest,
) -> RedfishError:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "storage_pool_id": storage_pool_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "CreateReplicaTarget",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/StorageServices/{storage_service_id}/StoragePools/{storage_pool_id}/AllocatedVolumes/{volume_id}/Actions/Volume.Initialize",
    response_model_exclude_none=True,
)
@authenticate
async def initialize17(
    storage_service_id: str,
    storage_pool_id: str,
    volume_id: str,
    request: Request,
    response: Response,
    body: InitializeRequest,
) -> RedfishError:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "storage_pool_id": storage_pool_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Initialize",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/StorageServices/{storage_service_id}/StoragePools/{storage_pool_id}/AllocatedVolumes/{volume_id}/Actions/Volume.RemoveReplicaRelationship",
    response_model_exclude_none=True,
)
@authenticate
async def remove_replica_relationship17(
    storage_service_id: str,
    storage_pool_id: str,
    volume_id: str,
    request: Request,
    response: Response,
    body: RemoveReplicaRelationshipRequest,
) -> RedfishError:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "storage_pool_id": storage_pool_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "RemoveReplicaRelationship",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/StorageServices/{storage_service_id}/StoragePools/{storage_pool_id}/AllocatedVolumes/{volume_id}/Actions/Volume.ResumeReplication",
    response_model_exclude_none=True,
)
@authenticate
async def resume_replication17(
    storage_service_id: str,
    storage_pool_id: str,
    volume_id: str,
    request: Request,
    response: Response,
    body: ResumeReplicationRequest,
) -> RedfishError:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "storage_pool_id": storage_pool_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "ResumeReplication",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/StorageServices/{storage_service_id}/StoragePools/{storage_pool_id}/AllocatedVolumes/{volume_id}/Actions/Volume.ReverseReplicationRelationship",
    response_model_exclude_none=True,
)
@authenticate
async def reverse_replication_relationship17(
    storage_service_id: str,
    storage_pool_id: str,
    volume_id: str,
    request: Request,
    response: Response,
    body: ReverseReplicationRelationshipRequest,
) -> RedfishError:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "storage_pool_id": storage_pool_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "ReverseReplicationRelationship",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/StorageServices/{storage_service_id}/StoragePools/{storage_pool_id}/AllocatedVolumes/{volume_id}/Actions/Volume.SplitReplication",
    response_model_exclude_none=True,
)
@authenticate
async def split_replication17(
    storage_service_id: str,
    storage_pool_id: str,
    volume_id: str,
    request: Request,
    response: Response,
    body: SplitReplicationRequest,
) -> RedfishError:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "storage_pool_id": storage_pool_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "SplitReplication",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/StorageServices/{storage_service_id}/StoragePools/{storage_pool_id}/AllocatedVolumes/{volume_id}/Actions/Volume.SuspendReplication",
    response_model_exclude_none=True,
)
@authenticate
async def suspend_replication17(
    storage_service_id: str,
    storage_pool_id: str,
    volume_id: str,
    request: Request,
    response: Response,
    body: SuspendReplicationRequest,
) -> RedfishError:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "storage_pool_id": storage_pool_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "SuspendReplication",
    }
    return s.action(**b)


@router.delete(
    "/redfish/v1/StorageServices/{storage_service_id}/StoragePools/{storage_pool_id}/CapacitySources/{capacity_source_id}/ProvidingVolumes/{volume_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete18(
    storage_service_id: str,
    storage_pool_id: str,
    capacity_source_id: str,
    volume_id: str,
    request: Request,
    response: Response,
) -> None:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "storage_pool_id": storage_pool_id,
        "capacity_source_id": capacity_source_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
    }
    return s.delete(**b)


@router.get(
    "/redfish/v1/StorageServices/{storage_service_id}/StoragePools/{storage_pool_id}/CapacitySources/{capacity_source_id}/ProvidingVolumes/{volume_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/StorageServices/{storage_service_id}/StoragePools/{storage_pool_id}/CapacitySources/{capacity_source_id}/ProvidingVolumes/{volume_id}",
    response_model_exclude_none=True,
)
async def get18(
    storage_service_id: str,
    storage_pool_id: str,
    capacity_source_id: str,
    volume_id: str,
    request: Request,
    response: Response,
) -> Volume:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "storage_pool_id": storage_pool_id,
        "capacity_source_id": capacity_source_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
    }
    m = cast(Volume, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/StorageServices/{storage_service_id}/StoragePools/{storage_pool_id}/CapacitySources/{capacity_source_id}/ProvidingVolumes/{volume_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch18(
    storage_service_id: str,
    storage_pool_id: str,
    capacity_source_id: str,
    volume_id: str,
    request: Request,
    response: Response,
    body: VolumeOnUpdate,
) -> Volume:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "storage_pool_id": storage_pool_id,
        "capacity_source_id": capacity_source_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Volume, s.patch(**b))


@router.post(
    "/redfish/v1/StorageServices/{storage_service_id}/StoragePools/{storage_pool_id}/CapacitySources/{capacity_source_id}/ProvidingVolumes/{volume_id}/Actions/Volume.AssignReplicaTarget",
    response_model_exclude_none=True,
)
@authenticate
async def assign_replica_target18(
    storage_service_id: str,
    storage_pool_id: str,
    capacity_source_id: str,
    volume_id: str,
    request: Request,
    response: Response,
    body: AssignReplicaTargetRequest,
) -> RedfishError:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "storage_pool_id": storage_pool_id,
        "capacity_source_id": capacity_source_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "AssignReplicaTarget",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/StorageServices/{storage_service_id}/StoragePools/{storage_pool_id}/CapacitySources/{capacity_source_id}/ProvidingVolumes/{volume_id}/Actions/Volume.ChangeRAIDLayout",
    response_model_exclude_none=True,
)
@authenticate
async def change_raid_layout18(
    storage_service_id: str,
    storage_pool_id: str,
    capacity_source_id: str,
    volume_id: str,
    request: Request,
    response: Response,
    body: ChangeRaidLayoutRequest,
) -> RedfishError:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "storage_pool_id": storage_pool_id,
        "capacity_source_id": capacity_source_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "ChangeRAIDLayout",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/StorageServices/{storage_service_id}/StoragePools/{storage_pool_id}/CapacitySources/{capacity_source_id}/ProvidingVolumes/{volume_id}/Actions/Volume.CreateReplicaTarget",
    response_model_exclude_none=True,
)
@authenticate
async def create_replica_target18(
    storage_service_id: str,
    storage_pool_id: str,
    capacity_source_id: str,
    volume_id: str,
    request: Request,
    response: Response,
    body: CreateReplicaTargetRequest,
) -> RedfishError:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "storage_pool_id": storage_pool_id,
        "capacity_source_id": capacity_source_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "CreateReplicaTarget",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/StorageServices/{storage_service_id}/StoragePools/{storage_pool_id}/CapacitySources/{capacity_source_id}/ProvidingVolumes/{volume_id}/Actions/Volume.Initialize",
    response_model_exclude_none=True,
)
@authenticate
async def initialize18(
    storage_service_id: str,
    storage_pool_id: str,
    capacity_source_id: str,
    volume_id: str,
    request: Request,
    response: Response,
    body: InitializeRequest,
) -> RedfishError:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "storage_pool_id": storage_pool_id,
        "capacity_source_id": capacity_source_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Initialize",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/StorageServices/{storage_service_id}/StoragePools/{storage_pool_id}/CapacitySources/{capacity_source_id}/ProvidingVolumes/{volume_id}/Actions/Volume.RemoveReplicaRelationship",
    response_model_exclude_none=True,
)
@authenticate
async def remove_replica_relationship18(
    storage_service_id: str,
    storage_pool_id: str,
    capacity_source_id: str,
    volume_id: str,
    request: Request,
    response: Response,
    body: RemoveReplicaRelationshipRequest,
) -> RedfishError:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "storage_pool_id": storage_pool_id,
        "capacity_source_id": capacity_source_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "RemoveReplicaRelationship",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/StorageServices/{storage_service_id}/StoragePools/{storage_pool_id}/CapacitySources/{capacity_source_id}/ProvidingVolumes/{volume_id}/Actions/Volume.ResumeReplication",
    response_model_exclude_none=True,
)
@authenticate
async def resume_replication18(
    storage_service_id: str,
    storage_pool_id: str,
    capacity_source_id: str,
    volume_id: str,
    request: Request,
    response: Response,
    body: ResumeReplicationRequest,
) -> RedfishError:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "storage_pool_id": storage_pool_id,
        "capacity_source_id": capacity_source_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "ResumeReplication",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/StorageServices/{storage_service_id}/StoragePools/{storage_pool_id}/CapacitySources/{capacity_source_id}/ProvidingVolumes/{volume_id}/Actions/Volume.ReverseReplicationRelationship",
    response_model_exclude_none=True,
)
@authenticate
async def reverse_replication_relationship18(
    storage_service_id: str,
    storage_pool_id: str,
    capacity_source_id: str,
    volume_id: str,
    request: Request,
    response: Response,
    body: ReverseReplicationRelationshipRequest,
) -> RedfishError:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "storage_pool_id": storage_pool_id,
        "capacity_source_id": capacity_source_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "ReverseReplicationRelationship",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/StorageServices/{storage_service_id}/StoragePools/{storage_pool_id}/CapacitySources/{capacity_source_id}/ProvidingVolumes/{volume_id}/Actions/Volume.SplitReplication",
    response_model_exclude_none=True,
)
@authenticate
async def split_replication18(
    storage_service_id: str,
    storage_pool_id: str,
    capacity_source_id: str,
    volume_id: str,
    request: Request,
    response: Response,
    body: SplitReplicationRequest,
) -> RedfishError:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "storage_pool_id": storage_pool_id,
        "capacity_source_id": capacity_source_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "SplitReplication",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/StorageServices/{storage_service_id}/StoragePools/{storage_pool_id}/CapacitySources/{capacity_source_id}/ProvidingVolumes/{volume_id}/Actions/Volume.SuspendReplication",
    response_model_exclude_none=True,
)
@authenticate
async def suspend_replication18(
    storage_service_id: str,
    storage_pool_id: str,
    capacity_source_id: str,
    volume_id: str,
    request: Request,
    response: Response,
    body: SuspendReplicationRequest,
) -> RedfishError:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "storage_pool_id": storage_pool_id,
        "capacity_source_id": capacity_source_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "SuspendReplication",
    }
    return s.action(**b)


@router.delete(
    "/redfish/v1/StorageServices/{storage_service_id}/Volumes/{volume_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete19(
    storage_service_id: str, volume_id: str, request: Request, response: Response
) -> None:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
    }
    return s.delete(**b)


@router.get(
    "/redfish/v1/StorageServices/{storage_service_id}/Volumes/{volume_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/StorageServices/{storage_service_id}/Volumes/{volume_id}",
    response_model_exclude_none=True,
)
async def get19(
    storage_service_id: str, volume_id: str, request: Request, response: Response
) -> Volume:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
    }
    m = cast(Volume, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/StorageServices/{storage_service_id}/Volumes/{volume_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch19(
    storage_service_id: str,
    volume_id: str,
    request: Request,
    response: Response,
    body: VolumeOnUpdate,
) -> Volume:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Volume, s.patch(**b))


@router.post(
    "/redfish/v1/StorageServices/{storage_service_id}/Volumes/{volume_id}/Actions/Volume.AssignReplicaTarget",
    response_model_exclude_none=True,
)
@authenticate
async def assign_replica_target19(
    storage_service_id: str,
    volume_id: str,
    request: Request,
    response: Response,
    body: AssignReplicaTargetRequest,
) -> RedfishError:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "AssignReplicaTarget",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/StorageServices/{storage_service_id}/Volumes/{volume_id}/Actions/Volume.ChangeRAIDLayout",
    response_model_exclude_none=True,
)
@authenticate
async def change_raid_layout19(
    storage_service_id: str,
    volume_id: str,
    request: Request,
    response: Response,
    body: ChangeRaidLayoutRequest,
) -> RedfishError:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "ChangeRAIDLayout",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/StorageServices/{storage_service_id}/Volumes/{volume_id}/Actions/Volume.CreateReplicaTarget",
    response_model_exclude_none=True,
)
@authenticate
async def create_replica_target19(
    storage_service_id: str,
    volume_id: str,
    request: Request,
    response: Response,
    body: CreateReplicaTargetRequest,
) -> RedfishError:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "CreateReplicaTarget",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/StorageServices/{storage_service_id}/Volumes/{volume_id}/Actions/Volume.Initialize",
    response_model_exclude_none=True,
)
@authenticate
async def initialize19(
    storage_service_id: str,
    volume_id: str,
    request: Request,
    response: Response,
    body: InitializeRequest,
) -> RedfishError:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Initialize",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/StorageServices/{storage_service_id}/Volumes/{volume_id}/Actions/Volume.RemoveReplicaRelationship",
    response_model_exclude_none=True,
)
@authenticate
async def remove_replica_relationship19(
    storage_service_id: str,
    volume_id: str,
    request: Request,
    response: Response,
    body: RemoveReplicaRelationshipRequest,
) -> RedfishError:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "RemoveReplicaRelationship",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/StorageServices/{storage_service_id}/Volumes/{volume_id}/Actions/Volume.ResumeReplication",
    response_model_exclude_none=True,
)
@authenticate
async def resume_replication19(
    storage_service_id: str,
    volume_id: str,
    request: Request,
    response: Response,
    body: ResumeReplicationRequest,
) -> RedfishError:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "ResumeReplication",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/StorageServices/{storage_service_id}/Volumes/{volume_id}/Actions/Volume.ReverseReplicationRelationship",
    response_model_exclude_none=True,
)
@authenticate
async def reverse_replication_relationship19(
    storage_service_id: str,
    volume_id: str,
    request: Request,
    response: Response,
    body: ReverseReplicationRelationshipRequest,
) -> RedfishError:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "ReverseReplicationRelationship",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/StorageServices/{storage_service_id}/Volumes/{volume_id}/Actions/Volume.SplitReplication",
    response_model_exclude_none=True,
)
@authenticate
async def split_replication19(
    storage_service_id: str,
    volume_id: str,
    request: Request,
    response: Response,
    body: SplitReplicationRequest,
) -> RedfishError:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "SplitReplication",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/StorageServices/{storage_service_id}/Volumes/{volume_id}/Actions/Volume.SuspendReplication",
    response_model_exclude_none=True,
)
@authenticate
async def suspend_replication19(
    storage_service_id: str,
    volume_id: str,
    request: Request,
    response: Response,
    body: SuspendReplicationRequest,
) -> RedfishError:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "SuspendReplication",
    }
    return s.action(**b)


@router.delete(
    "/redfish/v1/StorageServices/{storage_service_id}/Volumes/{volume_id}/CapacitySources/{capacity_source_id}/ProvidingVolumes/{providing_volume_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete20(
    storage_service_id: str,
    volume_id: str,
    capacity_source_id: str,
    providing_volume_id: str,
    request: Request,
    response: Response,
) -> None:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "volume_id": volume_id,
        "capacity_source_id": capacity_source_id,
        "providing_volume_id": providing_volume_id,
        "request": request,
        "response": response,
    }
    return s.delete(**b)


@router.get(
    "/redfish/v1/StorageServices/{storage_service_id}/Volumes/{volume_id}/CapacitySources/{capacity_source_id}/ProvidingVolumes/{providing_volume_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/StorageServices/{storage_service_id}/Volumes/{volume_id}/CapacitySources/{capacity_source_id}/ProvidingVolumes/{providing_volume_id}",
    response_model_exclude_none=True,
)
async def get20(
    storage_service_id: str,
    volume_id: str,
    capacity_source_id: str,
    providing_volume_id: str,
    request: Request,
    response: Response,
) -> Volume:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "volume_id": volume_id,
        "capacity_source_id": capacity_source_id,
        "providing_volume_id": providing_volume_id,
        "request": request,
        "response": response,
    }
    m = cast(Volume, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/StorageServices/{storage_service_id}/Volumes/{volume_id}/CapacitySources/{capacity_source_id}/ProvidingVolumes/{providing_volume_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch20(
    storage_service_id: str,
    volume_id: str,
    capacity_source_id: str,
    providing_volume_id: str,
    request: Request,
    response: Response,
    body: VolumeOnUpdate,
) -> Volume:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "volume_id": volume_id,
        "capacity_source_id": capacity_source_id,
        "providing_volume_id": providing_volume_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Volume, s.patch(**b))


@router.post(
    "/redfish/v1/StorageServices/{storage_service_id}/Volumes/{volume_id}/CapacitySources/{capacity_source_id}/ProvidingVolumes/{providing_volume_id}/Actions/Volume.AssignReplicaTarget",
    response_model_exclude_none=True,
)
@authenticate
async def assign_replica_target20(
    storage_service_id: str,
    volume_id: str,
    capacity_source_id: str,
    providing_volume_id: str,
    request: Request,
    response: Response,
    body: AssignReplicaTargetRequest,
) -> RedfishError:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "volume_id": volume_id,
        "capacity_source_id": capacity_source_id,
        "providing_volume_id": providing_volume_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "AssignReplicaTarget",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/StorageServices/{storage_service_id}/Volumes/{volume_id}/CapacitySources/{capacity_source_id}/ProvidingVolumes/{providing_volume_id}/Actions/Volume.ChangeRAIDLayout",
    response_model_exclude_none=True,
)
@authenticate
async def change_raid_layout20(
    storage_service_id: str,
    volume_id: str,
    capacity_source_id: str,
    providing_volume_id: str,
    request: Request,
    response: Response,
    body: ChangeRaidLayoutRequest,
) -> RedfishError:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "volume_id": volume_id,
        "capacity_source_id": capacity_source_id,
        "providing_volume_id": providing_volume_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "ChangeRAIDLayout",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/StorageServices/{storage_service_id}/Volumes/{volume_id}/CapacitySources/{capacity_source_id}/ProvidingVolumes/{providing_volume_id}/Actions/Volume.CreateReplicaTarget",
    response_model_exclude_none=True,
)
@authenticate
async def create_replica_target20(
    storage_service_id: str,
    volume_id: str,
    capacity_source_id: str,
    providing_volume_id: str,
    request: Request,
    response: Response,
    body: CreateReplicaTargetRequest,
) -> RedfishError:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "volume_id": volume_id,
        "capacity_source_id": capacity_source_id,
        "providing_volume_id": providing_volume_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "CreateReplicaTarget",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/StorageServices/{storage_service_id}/Volumes/{volume_id}/CapacitySources/{capacity_source_id}/ProvidingVolumes/{providing_volume_id}/Actions/Volume.Initialize",
    response_model_exclude_none=True,
)
@authenticate
async def initialize20(
    storage_service_id: str,
    volume_id: str,
    capacity_source_id: str,
    providing_volume_id: str,
    request: Request,
    response: Response,
    body: InitializeRequest,
) -> RedfishError:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "volume_id": volume_id,
        "capacity_source_id": capacity_source_id,
        "providing_volume_id": providing_volume_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Initialize",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/StorageServices/{storage_service_id}/Volumes/{volume_id}/CapacitySources/{capacity_source_id}/ProvidingVolumes/{providing_volume_id}/Actions/Volume.RemoveReplicaRelationship",
    response_model_exclude_none=True,
)
@authenticate
async def remove_replica_relationship20(
    storage_service_id: str,
    volume_id: str,
    capacity_source_id: str,
    providing_volume_id: str,
    request: Request,
    response: Response,
    body: RemoveReplicaRelationshipRequest,
) -> RedfishError:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "volume_id": volume_id,
        "capacity_source_id": capacity_source_id,
        "providing_volume_id": providing_volume_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "RemoveReplicaRelationship",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/StorageServices/{storage_service_id}/Volumes/{volume_id}/CapacitySources/{capacity_source_id}/ProvidingVolumes/{providing_volume_id}/Actions/Volume.ResumeReplication",
    response_model_exclude_none=True,
)
@authenticate
async def resume_replication20(
    storage_service_id: str,
    volume_id: str,
    capacity_source_id: str,
    providing_volume_id: str,
    request: Request,
    response: Response,
    body: ResumeReplicationRequest,
) -> RedfishError:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "volume_id": volume_id,
        "capacity_source_id": capacity_source_id,
        "providing_volume_id": providing_volume_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "ResumeReplication",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/StorageServices/{storage_service_id}/Volumes/{volume_id}/CapacitySources/{capacity_source_id}/ProvidingVolumes/{providing_volume_id}/Actions/Volume.ReverseReplicationRelationship",
    response_model_exclude_none=True,
)
@authenticate
async def reverse_replication_relationship20(
    storage_service_id: str,
    volume_id: str,
    capacity_source_id: str,
    providing_volume_id: str,
    request: Request,
    response: Response,
    body: ReverseReplicationRelationshipRequest,
) -> RedfishError:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "volume_id": volume_id,
        "capacity_source_id": capacity_source_id,
        "providing_volume_id": providing_volume_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "ReverseReplicationRelationship",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/StorageServices/{storage_service_id}/Volumes/{volume_id}/CapacitySources/{capacity_source_id}/ProvidingVolumes/{providing_volume_id}/Actions/Volume.SplitReplication",
    response_model_exclude_none=True,
)
@authenticate
async def split_replication20(
    storage_service_id: str,
    volume_id: str,
    capacity_source_id: str,
    providing_volume_id: str,
    request: Request,
    response: Response,
    body: SplitReplicationRequest,
) -> RedfishError:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "volume_id": volume_id,
        "capacity_source_id": capacity_source_id,
        "providing_volume_id": providing_volume_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "SplitReplication",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/StorageServices/{storage_service_id}/Volumes/{volume_id}/CapacitySources/{capacity_source_id}/ProvidingVolumes/{providing_volume_id}/Actions/Volume.SuspendReplication",
    response_model_exclude_none=True,
)
@authenticate
async def suspend_replication20(
    storage_service_id: str,
    volume_id: str,
    capacity_source_id: str,
    providing_volume_id: str,
    request: Request,
    response: Response,
    body: SuspendReplicationRequest,
) -> RedfishError:
    s: Service = get_service(Volume, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "volume_id": volume_id,
        "capacity_source_id": capacity_source_id,
        "providing_volume_id": providing_volume_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "SuspendReplication",
    }
    return s.action(**b)
