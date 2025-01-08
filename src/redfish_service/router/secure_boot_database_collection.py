from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..model.secure_boot_database_collection import SecureBootDatabaseCollection
from ..service import Service, find_service

router = APIRouter()


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/SecureBoot/SecureBootDatabases",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Systems/{computer_system_id}/SecureBoot/SecureBootDatabases",
    response_model_exclude_none=True,
)
async def get1(
    computer_system_id: str, request: Request, response: Response
) -> SecureBootDatabaseCollection:
    s: Service = find_service(SecureBootDatabaseCollection)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(SecureBootDatabaseCollection, s.get(**b))


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/SecureBoot/SecureBootDatabases",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/SecureBoot/SecureBootDatabases",
    response_model_exclude_none=True,
)
async def get2(
    resource_block_id: str, computer_system_id: str, request: Request, response: Response
) -> SecureBootDatabaseCollection:
    s: Service = find_service(SecureBootDatabaseCollection)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(SecureBootDatabaseCollection, s.get(**b))


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/SecureBoot/SecureBootDatabases",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/SecureBoot/SecureBootDatabases",
    response_model_exclude_none=True,
)
async def get3(
    resource_block_id: str, computer_system_id: str, request: Request, response: Response
) -> SecureBootDatabaseCollection:
    s: Service = find_service(SecureBootDatabaseCollection)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(SecureBootDatabaseCollection, s.get(**b))
