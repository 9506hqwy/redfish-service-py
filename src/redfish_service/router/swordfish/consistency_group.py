from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ...authenticate import authenticate
from ...model.redfish_error import RedfishError
from ...model.swordfish.consistency_group import (
    AssignReplicaTargetRequest,
    ConsistencyGroup,
    ConsistencyGroupOnUpdate,
    CreateReplicaTargetRequest,
    RemoveReplicaRelationshipRequest,
    ResumeReplicationRequest,
    ReverseReplicationRelationshipRequest,
    SplitReplicationRequest,
    SuspendReplicationRequest,
)
from ...service import Service
from ...util import get_service, set_link_header

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
    m = cast(ConsistencyGroup, s.get(**b))
    set_link_header(m, response)
    return m


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


@router.post(
    "/redfish/v1/Storage/{storage_id}/ConsistencyGroups/{consistency_group_id}/Actions/ConsistencyGroup.AssignReplicaTarget",
    response_model_exclude_none=True,
)
@authenticate
async def assign_replica_target1(
    storage_id: str,
    consistency_group_id: str,
    request: Request,
    response: Response,
    body: AssignReplicaTargetRequest,
) -> RedfishError:
    s: Service = get_service(ConsistencyGroup, request)
    b: dict[str, Any] = {
        "storage_id": storage_id,
        "consistency_group_id": consistency_group_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "AssignReplicaTarget",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Storage/{storage_id}/ConsistencyGroups/{consistency_group_id}/Actions/ConsistencyGroup.CreateReplicaTarget",
    response_model_exclude_none=True,
)
@authenticate
async def create_replica_target1(
    storage_id: str,
    consistency_group_id: str,
    request: Request,
    response: Response,
    body: CreateReplicaTargetRequest,
) -> RedfishError:
    s: Service = get_service(ConsistencyGroup, request)
    b: dict[str, Any] = {
        "storage_id": storage_id,
        "consistency_group_id": consistency_group_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "CreateReplicaTarget",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Storage/{storage_id}/ConsistencyGroups/{consistency_group_id}/Actions/ConsistencyGroup.RemoveReplicaRelationship",
    response_model_exclude_none=True,
)
@authenticate
async def remove_replica_relationship1(
    storage_id: str,
    consistency_group_id: str,
    request: Request,
    response: Response,
    body: RemoveReplicaRelationshipRequest,
) -> RedfishError:
    s: Service = get_service(ConsistencyGroup, request)
    b: dict[str, Any] = {
        "storage_id": storage_id,
        "consistency_group_id": consistency_group_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "RemoveReplicaRelationship",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Storage/{storage_id}/ConsistencyGroups/{consistency_group_id}/Actions/ConsistencyGroup.ResumeReplication",
    response_model_exclude_none=True,
)
@authenticate
async def resume_replication1(
    storage_id: str,
    consistency_group_id: str,
    request: Request,
    response: Response,
    body: ResumeReplicationRequest,
) -> RedfishError:
    s: Service = get_service(ConsistencyGroup, request)
    b: dict[str, Any] = {
        "storage_id": storage_id,
        "consistency_group_id": consistency_group_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "ResumeReplication",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Storage/{storage_id}/ConsistencyGroups/{consistency_group_id}/Actions/ConsistencyGroup.ReverseReplicationRelationship",
    response_model_exclude_none=True,
)
@authenticate
async def reverse_replication_relationship1(
    storage_id: str,
    consistency_group_id: str,
    request: Request,
    response: Response,
    body: ReverseReplicationRelationshipRequest,
) -> RedfishError:
    s: Service = get_service(ConsistencyGroup, request)
    b: dict[str, Any] = {
        "storage_id": storage_id,
        "consistency_group_id": consistency_group_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "ReverseReplicationRelationship",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Storage/{storage_id}/ConsistencyGroups/{consistency_group_id}/Actions/ConsistencyGroup.SplitReplication",
    response_model_exclude_none=True,
)
@authenticate
async def split_replication1(
    storage_id: str,
    consistency_group_id: str,
    request: Request,
    response: Response,
    body: SplitReplicationRequest,
) -> RedfishError:
    s: Service = get_service(ConsistencyGroup, request)
    b: dict[str, Any] = {
        "storage_id": storage_id,
        "consistency_group_id": consistency_group_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "SplitReplication",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Storage/{storage_id}/ConsistencyGroups/{consistency_group_id}/Actions/ConsistencyGroup.SuspendReplication",
    response_model_exclude_none=True,
)
@authenticate
async def suspend_replication1(
    storage_id: str,
    consistency_group_id: str,
    request: Request,
    response: Response,
    body: SuspendReplicationRequest,
) -> RedfishError:
    s: Service = get_service(ConsistencyGroup, request)
    b: dict[str, Any] = {
        "storage_id": storage_id,
        "consistency_group_id": consistency_group_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "SuspendReplication",
    }
    return s.action(**b)


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
    m = cast(ConsistencyGroup, s.get(**b))
    set_link_header(m, response)
    return m


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


@router.post(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/ConsistencyGroups/{consistency_group_id}/Actions/ConsistencyGroup.AssignReplicaTarget",
    response_model_exclude_none=True,
)
@authenticate
async def assign_replica_target2(
    computer_system_id: str,
    storage_id: str,
    consistency_group_id: str,
    request: Request,
    response: Response,
    body: AssignReplicaTargetRequest,
) -> RedfishError:
    s: Service = get_service(ConsistencyGroup, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "consistency_group_id": consistency_group_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "AssignReplicaTarget",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/ConsistencyGroups/{consistency_group_id}/Actions/ConsistencyGroup.CreateReplicaTarget",
    response_model_exclude_none=True,
)
@authenticate
async def create_replica_target2(
    computer_system_id: str,
    storage_id: str,
    consistency_group_id: str,
    request: Request,
    response: Response,
    body: CreateReplicaTargetRequest,
) -> RedfishError:
    s: Service = get_service(ConsistencyGroup, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "consistency_group_id": consistency_group_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "CreateReplicaTarget",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/ConsistencyGroups/{consistency_group_id}/Actions/ConsistencyGroup.RemoveReplicaRelationship",
    response_model_exclude_none=True,
)
@authenticate
async def remove_replica_relationship2(
    computer_system_id: str,
    storage_id: str,
    consistency_group_id: str,
    request: Request,
    response: Response,
    body: RemoveReplicaRelationshipRequest,
) -> RedfishError:
    s: Service = get_service(ConsistencyGroup, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "consistency_group_id": consistency_group_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "RemoveReplicaRelationship",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/ConsistencyGroups/{consistency_group_id}/Actions/ConsistencyGroup.ResumeReplication",
    response_model_exclude_none=True,
)
@authenticate
async def resume_replication2(
    computer_system_id: str,
    storage_id: str,
    consistency_group_id: str,
    request: Request,
    response: Response,
    body: ResumeReplicationRequest,
) -> RedfishError:
    s: Service = get_service(ConsistencyGroup, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "consistency_group_id": consistency_group_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "ResumeReplication",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/ConsistencyGroups/{consistency_group_id}/Actions/ConsistencyGroup.ReverseReplicationRelationship",
    response_model_exclude_none=True,
)
@authenticate
async def reverse_replication_relationship2(
    computer_system_id: str,
    storage_id: str,
    consistency_group_id: str,
    request: Request,
    response: Response,
    body: ReverseReplicationRelationshipRequest,
) -> RedfishError:
    s: Service = get_service(ConsistencyGroup, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "consistency_group_id": consistency_group_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "ReverseReplicationRelationship",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/ConsistencyGroups/{consistency_group_id}/Actions/ConsistencyGroup.SplitReplication",
    response_model_exclude_none=True,
)
@authenticate
async def split_replication2(
    computer_system_id: str,
    storage_id: str,
    consistency_group_id: str,
    request: Request,
    response: Response,
    body: SplitReplicationRequest,
) -> RedfishError:
    s: Service = get_service(ConsistencyGroup, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "consistency_group_id": consistency_group_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "SplitReplication",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/ConsistencyGroups/{consistency_group_id}/Actions/ConsistencyGroup.SuspendReplication",
    response_model_exclude_none=True,
)
@authenticate
async def suspend_replication2(
    computer_system_id: str,
    storage_id: str,
    consistency_group_id: str,
    request: Request,
    response: Response,
    body: SuspendReplicationRequest,
) -> RedfishError:
    s: Service = get_service(ConsistencyGroup, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "consistency_group_id": consistency_group_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "SuspendReplication",
    }
    return s.action(**b)


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
    m = cast(ConsistencyGroup, s.get(**b))
    set_link_header(m, response)
    return m


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


@router.post(
    "/redfish/v1/StorageServices/{storage_service_id}/ConsistencyGroups/{consistency_group_id}/Actions/ConsistencyGroup.AssignReplicaTarget",
    response_model_exclude_none=True,
)
@authenticate
async def assign_replica_target3(
    storage_service_id: str,
    consistency_group_id: str,
    request: Request,
    response: Response,
    body: AssignReplicaTargetRequest,
) -> RedfishError:
    s: Service = get_service(ConsistencyGroup, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "consistency_group_id": consistency_group_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "AssignReplicaTarget",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/StorageServices/{storage_service_id}/ConsistencyGroups/{consistency_group_id}/Actions/ConsistencyGroup.CreateReplicaTarget",
    response_model_exclude_none=True,
)
@authenticate
async def create_replica_target3(
    storage_service_id: str,
    consistency_group_id: str,
    request: Request,
    response: Response,
    body: CreateReplicaTargetRequest,
) -> RedfishError:
    s: Service = get_service(ConsistencyGroup, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "consistency_group_id": consistency_group_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "CreateReplicaTarget",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/StorageServices/{storage_service_id}/ConsistencyGroups/{consistency_group_id}/Actions/ConsistencyGroup.RemoveReplicaRelationship",
    response_model_exclude_none=True,
)
@authenticate
async def remove_replica_relationship3(
    storage_service_id: str,
    consistency_group_id: str,
    request: Request,
    response: Response,
    body: RemoveReplicaRelationshipRequest,
) -> RedfishError:
    s: Service = get_service(ConsistencyGroup, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "consistency_group_id": consistency_group_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "RemoveReplicaRelationship",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/StorageServices/{storage_service_id}/ConsistencyGroups/{consistency_group_id}/Actions/ConsistencyGroup.ResumeReplication",
    response_model_exclude_none=True,
)
@authenticate
async def resume_replication3(
    storage_service_id: str,
    consistency_group_id: str,
    request: Request,
    response: Response,
    body: ResumeReplicationRequest,
) -> RedfishError:
    s: Service = get_service(ConsistencyGroup, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "consistency_group_id": consistency_group_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "ResumeReplication",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/StorageServices/{storage_service_id}/ConsistencyGroups/{consistency_group_id}/Actions/ConsistencyGroup.ReverseReplicationRelationship",
    response_model_exclude_none=True,
)
@authenticate
async def reverse_replication_relationship3(
    storage_service_id: str,
    consistency_group_id: str,
    request: Request,
    response: Response,
    body: ReverseReplicationRelationshipRequest,
) -> RedfishError:
    s: Service = get_service(ConsistencyGroup, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "consistency_group_id": consistency_group_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "ReverseReplicationRelationship",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/StorageServices/{storage_service_id}/ConsistencyGroups/{consistency_group_id}/Actions/ConsistencyGroup.SplitReplication",
    response_model_exclude_none=True,
)
@authenticate
async def split_replication3(
    storage_service_id: str,
    consistency_group_id: str,
    request: Request,
    response: Response,
    body: SplitReplicationRequest,
) -> RedfishError:
    s: Service = get_service(ConsistencyGroup, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "consistency_group_id": consistency_group_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "SplitReplication",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/StorageServices/{storage_service_id}/ConsistencyGroups/{consistency_group_id}/Actions/ConsistencyGroup.SuspendReplication",
    response_model_exclude_none=True,
)
@authenticate
async def suspend_replication3(
    storage_service_id: str,
    consistency_group_id: str,
    request: Request,
    response: Response,
    body: SuspendReplicationRequest,
) -> RedfishError:
    s: Service = get_service(ConsistencyGroup, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "consistency_group_id": consistency_group_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "SuspendReplication",
    }
    return s.action(**b)


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
    m = cast(ConsistencyGroup, s.get(**b))
    set_link_header(m, response)
    return m


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


@router.post(
    "/redfish/v1/StorageServices/{storage_service_id}/Volumes/{volume_id}/ConsistencyGroups/{consistency_group_id}/Actions/ConsistencyGroup.AssignReplicaTarget",
    response_model_exclude_none=True,
)
@authenticate
async def assign_replica_target4(
    storage_service_id: str,
    volume_id: str,
    consistency_group_id: str,
    request: Request,
    response: Response,
    body: AssignReplicaTargetRequest,
) -> RedfishError:
    s: Service = get_service(ConsistencyGroup, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "volume_id": volume_id,
        "consistency_group_id": consistency_group_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "AssignReplicaTarget",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/StorageServices/{storage_service_id}/Volumes/{volume_id}/ConsistencyGroups/{consistency_group_id}/Actions/ConsistencyGroup.CreateReplicaTarget",
    response_model_exclude_none=True,
)
@authenticate
async def create_replica_target4(
    storage_service_id: str,
    volume_id: str,
    consistency_group_id: str,
    request: Request,
    response: Response,
    body: CreateReplicaTargetRequest,
) -> RedfishError:
    s: Service = get_service(ConsistencyGroup, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "volume_id": volume_id,
        "consistency_group_id": consistency_group_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "CreateReplicaTarget",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/StorageServices/{storage_service_id}/Volumes/{volume_id}/ConsistencyGroups/{consistency_group_id}/Actions/ConsistencyGroup.RemoveReplicaRelationship",
    response_model_exclude_none=True,
)
@authenticate
async def remove_replica_relationship4(
    storage_service_id: str,
    volume_id: str,
    consistency_group_id: str,
    request: Request,
    response: Response,
    body: RemoveReplicaRelationshipRequest,
) -> RedfishError:
    s: Service = get_service(ConsistencyGroup, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "volume_id": volume_id,
        "consistency_group_id": consistency_group_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "RemoveReplicaRelationship",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/StorageServices/{storage_service_id}/Volumes/{volume_id}/ConsistencyGroups/{consistency_group_id}/Actions/ConsistencyGroup.ResumeReplication",
    response_model_exclude_none=True,
)
@authenticate
async def resume_replication4(
    storage_service_id: str,
    volume_id: str,
    consistency_group_id: str,
    request: Request,
    response: Response,
    body: ResumeReplicationRequest,
) -> RedfishError:
    s: Service = get_service(ConsistencyGroup, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "volume_id": volume_id,
        "consistency_group_id": consistency_group_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "ResumeReplication",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/StorageServices/{storage_service_id}/Volumes/{volume_id}/ConsistencyGroups/{consistency_group_id}/Actions/ConsistencyGroup.ReverseReplicationRelationship",
    response_model_exclude_none=True,
)
@authenticate
async def reverse_replication_relationship4(
    storage_service_id: str,
    volume_id: str,
    consistency_group_id: str,
    request: Request,
    response: Response,
    body: ReverseReplicationRelationshipRequest,
) -> RedfishError:
    s: Service = get_service(ConsistencyGroup, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "volume_id": volume_id,
        "consistency_group_id": consistency_group_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "ReverseReplicationRelationship",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/StorageServices/{storage_service_id}/Volumes/{volume_id}/ConsistencyGroups/{consistency_group_id}/Actions/ConsistencyGroup.SplitReplication",
    response_model_exclude_none=True,
)
@authenticate
async def split_replication4(
    storage_service_id: str,
    volume_id: str,
    consistency_group_id: str,
    request: Request,
    response: Response,
    body: SplitReplicationRequest,
) -> RedfishError:
    s: Service = get_service(ConsistencyGroup, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "volume_id": volume_id,
        "consistency_group_id": consistency_group_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "SplitReplication",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/StorageServices/{storage_service_id}/Volumes/{volume_id}/ConsistencyGroups/{consistency_group_id}/Actions/ConsistencyGroup.SuspendReplication",
    response_model_exclude_none=True,
)
@authenticate
async def suspend_replication4(
    storage_service_id: str,
    volume_id: str,
    consistency_group_id: str,
    request: Request,
    response: Response,
    body: SuspendReplicationRequest,
) -> RedfishError:
    s: Service = get_service(ConsistencyGroup, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "volume_id": volume_id,
        "consistency_group_id": consistency_group_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "SuspendReplication",
    }
    return s.action(**b)
