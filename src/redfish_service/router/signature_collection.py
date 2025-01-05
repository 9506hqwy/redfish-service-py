from typing import Any, cast

from fastapi import APIRouter

from ..model.signature_collection import SignatureCollection
from ..service import Service, find_service
from . import authenticate

router = APIRouter()


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/SecureBoot/SecureBootDatabases/{database_id}/Signatures",
    response_model_exclude_none=True,
)
@authenticate
async def get1(computer_system_id: str, database_id: str) -> SignatureCollection:
    s: Service = find_service(SignatureCollection)
    b: dict[str, Any] = {"computer_system_id": computer_system_id, "database_id": database_id}
    return cast(SignatureCollection, s.get(**b))


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/SecureBoot/SecureBootDatabases/{database_id}/Signatures",
    response_model_exclude_none=True,
)
@authenticate
async def get2(
    resource_block_id: str, computer_system_id: str, database_id: str
) -> SignatureCollection:
    s: Service = find_service(SignatureCollection)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "database_id": database_id,
    }
    return cast(SignatureCollection, s.get(**b))


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/SecureBoot/SecureBootDatabases/{database_id}/Signatures",
    response_model_exclude_none=True,
)
@authenticate
async def get3(
    resource_block_id: str, computer_system_id: str, database_id: str
) -> SignatureCollection:
    s: Service = find_service(SignatureCollection)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "database_id": database_id,
    }
    return cast(SignatureCollection, s.get(**b))
