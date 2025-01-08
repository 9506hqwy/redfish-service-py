from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.signature import Signature, SignatureOnCreate
from ..model.signature_collection import SignatureCollection
from ..service import Service, ServiceCollection, find_service, find_service_collection

router = APIRouter()


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/SecureBoot/SecureBootDatabases/{database_id}/Signatures",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Systems/{computer_system_id}/SecureBoot/SecureBootDatabases/{database_id}/Signatures",
    response_model_exclude_none=True,
)
async def get1(
    computer_system_id: str, database_id: str, request: Request, response: Response
) -> SignatureCollection:
    s: Service = find_service(SignatureCollection)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "database_id": database_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(SignatureCollection, s.get(**b))


@router.post(
    "/redfish/v1/Systems/{computer_system_id}/SecureBoot/SecureBootDatabases/{database_id}/Signatures",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/Systems/{computer_system_id}/SecureBoot/SecureBootDatabases/{database_id}/Signatures/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post1(
    computer_system_id: str,
    database_id: str,
    request: Request,
    response: Response,
    body: SignatureOnCreate,
) -> Signature:
    s: ServiceCollection = find_service_collection(SignatureCollection)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "database_id": database_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(Signature, s.post(**b))


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/SecureBoot/SecureBootDatabases/{database_id}/Signatures",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/SecureBoot/SecureBootDatabases/{database_id}/Signatures",
    response_model_exclude_none=True,
)
async def get2(
    resource_block_id: str,
    computer_system_id: str,
    database_id: str,
    request: Request,
    response: Response,
) -> SignatureCollection:
    s: Service = find_service(SignatureCollection)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "database_id": database_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(SignatureCollection, s.get(**b))


@router.post(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/SecureBoot/SecureBootDatabases/{database_id}/Signatures",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/SecureBoot/SecureBootDatabases/{database_id}/Signatures/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post2(
    resource_block_id: str,
    computer_system_id: str,
    database_id: str,
    request: Request,
    response: Response,
    body: SignatureOnCreate,
) -> Signature:
    s: ServiceCollection = find_service_collection(SignatureCollection)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "database_id": database_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(Signature, s.post(**b))


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/SecureBoot/SecureBootDatabases/{database_id}/Signatures",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/SecureBoot/SecureBootDatabases/{database_id}/Signatures",
    response_model_exclude_none=True,
)
async def get3(
    resource_block_id: str,
    computer_system_id: str,
    database_id: str,
    request: Request,
    response: Response,
) -> SignatureCollection:
    s: Service = find_service(SignatureCollection)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "database_id": database_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(SignatureCollection, s.get(**b))


@router.post(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/SecureBoot/SecureBootDatabases/{database_id}/Signatures",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/SecureBoot/SecureBootDatabases/{database_id}/Signatures/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post3(
    resource_block_id: str,
    computer_system_id: str,
    database_id: str,
    request: Request,
    response: Response,
    body: SignatureOnCreate,
) -> Signature:
    s: ServiceCollection = find_service_collection(SignatureCollection)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "database_id": database_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(Signature, s.post(**b))
