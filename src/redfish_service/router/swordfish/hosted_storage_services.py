from typing import Any, cast

from fastapi import APIRouter

from ...authenticate import authenticate
from ...model.swordfish.hosted_storage_services import HostedStorageServices
from ...service import Service, find_service

router = APIRouter()


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/HostedServices", response_model_exclude_none=True
)
@authenticate
async def get1(computer_system_id: str) -> HostedStorageServices:
    s: Service = find_service(HostedStorageServices)
    b: dict[str, Any] = {"computer_system_id": computer_system_id}
    return cast(HostedStorageServices, s.get(**b))
