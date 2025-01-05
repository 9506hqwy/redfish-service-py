from typing import Any, cast

from fastapi import APIRouter

from ..model.secure_boot_database import SecureBootDatabase
from ..service import Service, find_service
from . import authenticate

router = APIRouter()


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/SecureBoot/SecureBootDatabases/{database_id}",
    response_model_exclude_none=True,
)
@authenticate
async def get1(computer_system_id: str, database_id: str) -> SecureBootDatabase:
    s: Service = find_service(SecureBootDatabase)
    b: dict[str, Any] = {"computer_system_id": computer_system_id, "database_id": database_id}
    return cast(SecureBootDatabase, s.get(**b))


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/SecureBoot/SecureBootDatabases/{database_id}",
    response_model_exclude_none=True,
)
@authenticate
async def get2(
    resource_block_id: str, computer_system_id: str, database_id: str
) -> SecureBootDatabase:
    s: Service = find_service(SecureBootDatabase)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "database_id": database_id,
    }
    return cast(SecureBootDatabase, s.get(**b))


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/SecureBoot/SecureBootDatabases/{database_id}",
    response_model_exclude_none=True,
)
@authenticate
async def get3(
    resource_block_id: str, computer_system_id: str, database_id: str
) -> SecureBootDatabase:
    s: Service = find_service(SecureBootDatabase)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "database_id": database_id,
    }
    return cast(SecureBootDatabase, s.get(**b))
