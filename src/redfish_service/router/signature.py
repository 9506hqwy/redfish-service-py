from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.signature import Signature
from ..service import Service
from ..util import get_service

router = APIRouter()


@router.delete(
    "/redfish/v1/Systems/{computer_system_id}/SecureBoot/SecureBootDatabases/{database_id}/Signatures/{signature_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete1(
    computer_system_id: str,
    database_id: str,
    signature_id: str,
    request: Request,
    response: Response,
) -> None:
    s: Service = get_service(Signature, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "database_id": database_id,
        "signature_id": signature_id,
        "request": request,
        "response": response,
    }
    return s.delete(**b)


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/SecureBoot/SecureBootDatabases/{database_id}/Signatures/{signature_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Systems/{computer_system_id}/SecureBoot/SecureBootDatabases/{database_id}/Signatures/{signature_id}",
    response_model_exclude_none=True,
)
async def get1(
    computer_system_id: str,
    database_id: str,
    signature_id: str,
    request: Request,
    response: Response,
) -> Signature:
    s: Service = get_service(Signature, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "database_id": database_id,
        "signature_id": signature_id,
        "request": request,
        "response": response,
    }
    return cast(Signature, s.get(**b))


@router.delete(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/SecureBoot/SecureBootDatabases/{database_id}/Signatures/{signature_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete2(
    resource_block_id: str,
    computer_system_id: str,
    database_id: str,
    signature_id: str,
    request: Request,
    response: Response,
) -> None:
    s: Service = get_service(Signature, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "database_id": database_id,
        "signature_id": signature_id,
        "request": request,
        "response": response,
    }
    return s.delete(**b)


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/SecureBoot/SecureBootDatabases/{database_id}/Signatures/{signature_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/SecureBoot/SecureBootDatabases/{database_id}/Signatures/{signature_id}",
    response_model_exclude_none=True,
)
async def get2(
    resource_block_id: str,
    computer_system_id: str,
    database_id: str,
    signature_id: str,
    request: Request,
    response: Response,
) -> Signature:
    s: Service = get_service(Signature, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "database_id": database_id,
        "signature_id": signature_id,
        "request": request,
        "response": response,
    }
    return cast(Signature, s.get(**b))


@router.delete(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/SecureBoot/SecureBootDatabases/{database_id}/Signatures/{signature_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete3(
    resource_block_id: str,
    computer_system_id: str,
    database_id: str,
    signature_id: str,
    request: Request,
    response: Response,
) -> None:
    s: Service = get_service(Signature, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "database_id": database_id,
        "signature_id": signature_id,
        "request": request,
        "response": response,
    }
    return s.delete(**b)


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/SecureBoot/SecureBootDatabases/{database_id}/Signatures/{signature_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/SecureBoot/SecureBootDatabases/{database_id}/Signatures/{signature_id}",
    response_model_exclude_none=True,
)
async def get3(
    resource_block_id: str,
    computer_system_id: str,
    database_id: str,
    signature_id: str,
    request: Request,
    response: Response,
) -> Signature:
    s: Service = get_service(Signature, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "database_id": database_id,
        "signature_id": signature_id,
        "request": request,
        "response": response,
    }
    return cast(Signature, s.get(**b))
