from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ...authenticate import authenticate
from ...model.swordfish.hosted_storage_services import HostedStorageServices
from ...model.swordfish.storage_service import StorageService, StorageServiceOnCreate
from ...service import Service, ServiceCollection, find_service, find_service_collection

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
    s: Service = find_service(HostedStorageServices)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(HostedStorageServices, s.get(**b))


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
    s: ServiceCollection = find_service_collection(HostedStorageServices)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(StorageService, s.post(**b))
