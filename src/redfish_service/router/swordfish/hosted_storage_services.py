from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ...authenticate import authenticate
from ...model.swordfish.hosted_storage_services import HostedStorageServices
from ...model.swordfish.storage_service import StorageService, StorageServiceOnCreate
from ...service import Service, ServiceCollection
from ...util import get_service, get_service_collection, set_link_header

router = APIRouter()


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/HostedServices", response_model_exclude_none=True
)
@router.head(
    "/redfish/v1/Systems/{computer_system_id}/HostedServices", response_model_exclude_none=True
)
async def get1(
    computer_system_id: str, request: Request, response: Response
) -> HostedStorageServices:
    s: Service = get_service(HostedStorageServices, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "request": request,
        "response": response,
    }
    m = cast(HostedStorageServices, s.get(**b))
    set_link_header(m, response)
    return m


@router.post(
    "/redfish/v1/Systems/{computer_system_id}/HostedServices", response_model_exclude_none=True
)
@router.post(
    "/redfish/v1/Systems/{computer_system_id}/HostedServices/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post1(
    computer_system_id: str, request: Request, response: Response, body: StorageServiceOnCreate
) -> StorageService:
    s: ServiceCollection = get_service_collection(HostedStorageServices, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(StorageService, s.post(**b))
