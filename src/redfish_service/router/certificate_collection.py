from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.certificate_collection import CertificateCollection
from ..service import Service, find_service

router = APIRouter()


@router.get(
    "/redfish/v1/AccountService/Accounts/{manager_account_id}/Certificates",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/AccountService/Accounts/{manager_account_id}/Certificates",
    response_model_exclude_none=True,
)
@authenticate
async def get1(
    manager_account_id: str, request: Request, response: Response
) -> CertificateCollection:
    s: Service = find_service(CertificateCollection)
    b: dict[str, Any] = {
        "manager_account_id": manager_account_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(CertificateCollection, s.get(**b))


@router.get(
    "/redfish/v1/AccountService/ActiveDirectory/Certificates", response_model_exclude_none=True
)
@router.head(
    "/redfish/v1/AccountService/ActiveDirectory/Certificates", response_model_exclude_none=True
)
@authenticate
async def get2(request: Request, response: Response) -> CertificateCollection:
    s: Service = find_service(CertificateCollection)
    b: dict[str, Any] = {"request": request, "response": response}

    response.headers["OData-Version"] = "4.0"

    return cast(CertificateCollection, s.get(**b))


@router.get("/redfish/v1/AccountService/LDAP/Certificates", response_model_exclude_none=True)
@router.head("/redfish/v1/AccountService/LDAP/Certificates", response_model_exclude_none=True)
@authenticate
async def get3(request: Request, response: Response) -> CertificateCollection:
    s: Service = find_service(CertificateCollection)
    b: dict[str, Any] = {"request": request, "response": response}

    response.headers["OData-Version"] = "4.0"

    return cast(CertificateCollection, s.get(**b))


@router.get(
    "/redfish/v1/AccountService/ExternalAccountProviders/{external_account_provider_id}/Certificates",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/AccountService/ExternalAccountProviders/{external_account_provider_id}/Certificates",
    response_model_exclude_none=True,
)
@authenticate
async def get4(
    external_account_provider_id: str, request: Request, response: Response
) -> CertificateCollection:
    s: Service = find_service(CertificateCollection)
    b: dict[str, Any] = {
        "external_account_provider_id": external_account_provider_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(CertificateCollection, s.get(**b))


@router.get(
    "/redfish/v1/AccountService/MultiFactorAuth/ClientCertificate/Certificates",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/AccountService/MultiFactorAuth/ClientCertificate/Certificates",
    response_model_exclude_none=True,
)
@authenticate
async def get5(request: Request, response: Response) -> CertificateCollection:
    s: Service = find_service(CertificateCollection)
    b: dict[str, Any] = {"request": request, "response": response}

    response.headers["OData-Version"] = "4.0"

    return cast(CertificateCollection, s.get(**b))


@router.get(
    "/redfish/v1/AccountService/MultiFactorAuth/SecurID/Certificates",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/AccountService/MultiFactorAuth/SecurID/Certificates",
    response_model_exclude_none=True,
)
@authenticate
async def get6(request: Request, response: Response) -> CertificateCollection:
    s: Service = find_service(CertificateCollection)
    b: dict[str, Any] = {"request": request, "response": response}

    response.headers["OData-Version"] = "4.0"

    return cast(CertificateCollection, s.get(**b))


@router.get(
    "/redfish/v1/Managers/{manager_id}/RemoteAccountService/Accounts/{manager_account_id}/Certificates",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Managers/{manager_id}/RemoteAccountService/Accounts/{manager_account_id}/Certificates",
    response_model_exclude_none=True,
)
@authenticate
async def get7(
    manager_id: str, manager_account_id: str, request: Request, response: Response
) -> CertificateCollection:
    s: Service = find_service(CertificateCollection)
    b: dict[str, Any] = {
        "manager_id": manager_id,
        "manager_account_id": manager_account_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(CertificateCollection, s.get(**b))


@router.get(
    "/redfish/v1/Managers/{manager_id}/RemoteAccountService/ActiveDirectory/Certificates",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Managers/{manager_id}/RemoteAccountService/ActiveDirectory/Certificates",
    response_model_exclude_none=True,
)
@authenticate
async def get8(manager_id: str, request: Request, response: Response) -> CertificateCollection:
    s: Service = find_service(CertificateCollection)
    b: dict[str, Any] = {"manager_id": manager_id, "request": request, "response": response}

    response.headers["OData-Version"] = "4.0"

    return cast(CertificateCollection, s.get(**b))


@router.get(
    "/redfish/v1/Managers/{manager_id}/RemoteAccountService/LDAP/Certificates",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Managers/{manager_id}/RemoteAccountService/LDAP/Certificates",
    response_model_exclude_none=True,
)
@authenticate
async def get9(manager_id: str, request: Request, response: Response) -> CertificateCollection:
    s: Service = find_service(CertificateCollection)
    b: dict[str, Any] = {"manager_id": manager_id, "request": request, "response": response}

    response.headers["OData-Version"] = "4.0"

    return cast(CertificateCollection, s.get(**b))


@router.get(
    "/redfish/v1/Managers/{manager_id}/RemoteAccountService/ExternalAccountProviders/{external_account_provider_id}/Certificates",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Managers/{manager_id}/RemoteAccountService/ExternalAccountProviders/{external_account_provider_id}/Certificates",
    response_model_exclude_none=True,
)
@authenticate
async def get10(
    manager_id: str, external_account_provider_id: str, request: Request, response: Response
) -> CertificateCollection:
    s: Service = find_service(CertificateCollection)
    b: dict[str, Any] = {
        "manager_id": manager_id,
        "external_account_provider_id": external_account_provider_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(CertificateCollection, s.get(**b))


@router.get(
    "/redfish/v1/Managers/{manager_id}/RemoteAccountService/MultiFactorAuth/ClientCertificate/Certificates",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Managers/{manager_id}/RemoteAccountService/MultiFactorAuth/ClientCertificate/Certificates",
    response_model_exclude_none=True,
)
@authenticate
async def get11(manager_id: str, request: Request, response: Response) -> CertificateCollection:
    s: Service = find_service(CertificateCollection)
    b: dict[str, Any] = {"manager_id": manager_id, "request": request, "response": response}

    response.headers["OData-Version"] = "4.0"

    return cast(CertificateCollection, s.get(**b))


@router.get(
    "/redfish/v1/Managers/{manager_id}/RemoteAccountService/MultiFactorAuth/SecurID/Certificates",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Managers/{manager_id}/RemoteAccountService/MultiFactorAuth/SecurID/Certificates",
    response_model_exclude_none=True,
)
@authenticate
async def get12(manager_id: str, request: Request, response: Response) -> CertificateCollection:
    s: Service = find_service(CertificateCollection)
    b: dict[str, Any] = {"manager_id": manager_id, "request": request, "response": response}

    response.headers["OData-Version"] = "4.0"

    return cast(CertificateCollection, s.get(**b))


@router.get(
    "/redfish/v1/Managers/{manager_id}/NetworkProtocol/HTTPS/Certificates",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Managers/{manager_id}/NetworkProtocol/HTTPS/Certificates",
    response_model_exclude_none=True,
)
@authenticate
async def get13(manager_id: str, request: Request, response: Response) -> CertificateCollection:
    s: Service = find_service(CertificateCollection)
    b: dict[str, Any] = {"manager_id": manager_id, "request": request, "response": response}

    response.headers["OData-Version"] = "4.0"

    return cast(CertificateCollection, s.get(**b))


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/Boot/Certificates", response_model_exclude_none=True
)
@router.head(
    "/redfish/v1/Systems/{computer_system_id}/Boot/Certificates", response_model_exclude_none=True
)
@authenticate
async def get14(
    computer_system_id: str, request: Request, response: Response
) -> CertificateCollection:
    s: Service = find_service(CertificateCollection)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(CertificateCollection, s.get(**b))


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Boot/Certificates",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Boot/Certificates",
    response_model_exclude_none=True,
)
@authenticate
async def get15(
    resource_block_id: str, computer_system_id: str, request: Request, response: Response
) -> CertificateCollection:
    s: Service = find_service(CertificateCollection)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(CertificateCollection, s.get(**b))


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Boot/Certificates",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Boot/Certificates",
    response_model_exclude_none=True,
)
@authenticate
async def get16(
    resource_block_id: str, computer_system_id: str, request: Request, response: Response
) -> CertificateCollection:
    s: Service = find_service(CertificateCollection)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(CertificateCollection, s.get(**b))


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/SecureBoot/SecureBootDatabases/{database_id}/Certificates",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Systems/{computer_system_id}/SecureBoot/SecureBootDatabases/{database_id}/Certificates",
    response_model_exclude_none=True,
)
@authenticate
async def get17(
    computer_system_id: str, database_id: str, request: Request, response: Response
) -> CertificateCollection:
    s: Service = find_service(CertificateCollection)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "database_id": database_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(CertificateCollection, s.get(**b))


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/SecureBoot/SecureBootDatabases/{database_id}/Certificates",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/SecureBoot/SecureBootDatabases/{database_id}/Certificates",
    response_model_exclude_none=True,
)
@authenticate
async def get18(
    resource_block_id: str,
    computer_system_id: str,
    database_id: str,
    request: Request,
    response: Response,
) -> CertificateCollection:
    s: Service = find_service(CertificateCollection)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "database_id": database_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(CertificateCollection, s.get(**b))


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/SecureBoot/SecureBootDatabases/{database_id}/Certificates",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/SecureBoot/SecureBootDatabases/{database_id}/Certificates",
    response_model_exclude_none=True,
)
@authenticate
async def get19(
    resource_block_id: str,
    computer_system_id: str,
    database_id: str,
    request: Request,
    response: Response,
) -> CertificateCollection:
    s: Service = find_service(CertificateCollection)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "database_id": database_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(CertificateCollection, s.get(**b))


@router.get(
    "/redfish/v1/EventService/Subscriptions/{event_destination_id}/Certificates",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/EventService/Subscriptions/{event_destination_id}/Certificates",
    response_model_exclude_none=True,
)
@authenticate
async def get20(
    event_destination_id: str, request: Request, response: Response
) -> CertificateCollection:
    s: Service = find_service(CertificateCollection)
    b: dict[str, Any] = {
        "event_destination_id": event_destination_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(CertificateCollection, s.get(**b))


@router.get(
    "/redfish/v1/EventService/Subscriptions/{event_destination_id}/ClientCertificates",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/EventService/Subscriptions/{event_destination_id}/ClientCertificates",
    response_model_exclude_none=True,
)
@authenticate
async def get21(
    event_destination_id: str, request: Request, response: Response
) -> CertificateCollection:
    s: Service = find_service(CertificateCollection)
    b: dict[str, Any] = {
        "event_destination_id": event_destination_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(CertificateCollection, s.get(**b))


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/Certificates", response_model_exclude_none=True
)
@router.head(
    "/redfish/v1/Systems/{computer_system_id}/Certificates", response_model_exclude_none=True
)
@authenticate
async def get22(
    computer_system_id: str, request: Request, response: Response
) -> CertificateCollection:
    s: Service = find_service(CertificateCollection)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(CertificateCollection, s.get(**b))


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Certificates",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Certificates",
    response_model_exclude_none=True,
)
@authenticate
async def get23(
    resource_block_id: str, computer_system_id: str, request: Request, response: Response
) -> CertificateCollection:
    s: Service = find_service(CertificateCollection)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(CertificateCollection, s.get(**b))


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Certificates",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Certificates",
    response_model_exclude_none=True,
)
@authenticate
async def get24(
    resource_block_id: str, computer_system_id: str, request: Request, response: Response
) -> CertificateCollection:
    s: Service = find_service(CertificateCollection)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(CertificateCollection, s.get(**b))


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/Memory/{memory_id}/Certificates",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Systems/{computer_system_id}/Memory/{memory_id}/Certificates",
    response_model_exclude_none=True,
)
@authenticate
async def get25(
    computer_system_id: str, memory_id: str, request: Request, response: Response
) -> CertificateCollection:
    s: Service = find_service(CertificateCollection)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "memory_id": memory_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(CertificateCollection, s.get(**b))


@router.get(
    "/redfish/v1/Chassis/{chassis_id}/Memory/{memory_id}/Certificates",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Chassis/{chassis_id}/Memory/{memory_id}/Certificates",
    response_model_exclude_none=True,
)
@authenticate
async def get26(
    chassis_id: str, memory_id: str, request: Request, response: Response
) -> CertificateCollection:
    s: Service = find_service(CertificateCollection)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "memory_id": memory_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(CertificateCollection, s.get(**b))


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Memory/{memory_id}/Certificates",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Memory/{memory_id}/Certificates",
    response_model_exclude_none=True,
)
@authenticate
async def get27(
    resource_block_id: str, memory_id: str, request: Request, response: Response
) -> CertificateCollection:
    s: Service = find_service(CertificateCollection)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "memory_id": memory_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(CertificateCollection, s.get(**b))


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Memory/{memory_id}/Certificates",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Memory/{memory_id}/Certificates",
    response_model_exclude_none=True,
)
@authenticate
async def get28(
    resource_block_id: str,
    computer_system_id: str,
    memory_id: str,
    request: Request,
    response: Response,
) -> CertificateCollection:
    s: Service = find_service(CertificateCollection)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "memory_id": memory_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(CertificateCollection, s.get(**b))


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Memory/{memory_id}/Certificates",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Memory/{memory_id}/Certificates",
    response_model_exclude_none=True,
)
@authenticate
async def get29(
    resource_block_id: str, memory_id: str, request: Request, response: Response
) -> CertificateCollection:
    s: Service = find_service(CertificateCollection)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "memory_id": memory_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(CertificateCollection, s.get(**b))


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Memory/{memory_id}/Certificates",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Memory/{memory_id}/Certificates",
    response_model_exclude_none=True,
)
@authenticate
async def get30(
    resource_block_id: str,
    computer_system_id: str,
    memory_id: str,
    request: Request,
    response: Response,
) -> CertificateCollection:
    s: Service = find_service(CertificateCollection)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "memory_id": memory_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(CertificateCollection, s.get(**b))


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/Processors/{processor_id}/Certificates",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Systems/{computer_system_id}/Processors/{processor_id}/Certificates",
    response_model_exclude_none=True,
)
@authenticate
async def get31(
    computer_system_id: str, processor_id: str, request: Request, response: Response
) -> CertificateCollection:
    s: Service = find_service(CertificateCollection)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "processor_id": processor_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(CertificateCollection, s.get(**b))


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Processors/{processor_id}/Certificates",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Processors/{processor_id}/Certificates",
    response_model_exclude_none=True,
)
@authenticate
async def get32(
    resource_block_id: str, processor_id: str, request: Request, response: Response
) -> CertificateCollection:
    s: Service = find_service(CertificateCollection)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "processor_id": processor_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(CertificateCollection, s.get(**b))


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Processors/{processor_id}/Certificates",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Processors/{processor_id}/Certificates",
    response_model_exclude_none=True,
)
@authenticate
async def get33(
    resource_block_id: str,
    computer_system_id: str,
    processor_id: str,
    request: Request,
    response: Response,
) -> CertificateCollection:
    s: Service = find_service(CertificateCollection)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "processor_id": processor_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(CertificateCollection, s.get(**b))


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Processors/{processor_id}/Certificates",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Processors/{processor_id}/Certificates",
    response_model_exclude_none=True,
)
@authenticate
async def get34(
    resource_block_id: str, processor_id: str, request: Request, response: Response
) -> CertificateCollection:
    s: Service = find_service(CertificateCollection)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "processor_id": processor_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(CertificateCollection, s.get(**b))


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Processors/{processor_id}/Certificates",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Processors/{processor_id}/Certificates",
    response_model_exclude_none=True,
)
@authenticate
async def get35(
    resource_block_id: str,
    computer_system_id: str,
    processor_id: str,
    request: Request,
    response: Response,
) -> CertificateCollection:
    s: Service = find_service(CertificateCollection)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "processor_id": processor_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(CertificateCollection, s.get(**b))


@router.get(
    "/redfish/v1/Storage/{storage_id}/StorageControllers/{storage_controller_id}/Certificates",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Storage/{storage_id}/StorageControllers/{storage_controller_id}/Certificates",
    response_model_exclude_none=True,
)
@authenticate
async def get36(
    storage_id: str, storage_controller_id: str, request: Request, response: Response
) -> CertificateCollection:
    s: Service = find_service(CertificateCollection)
    b: dict[str, Any] = {
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(CertificateCollection, s.get(**b))


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/StorageControllers/{storage_controller_id}/Certificates",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/StorageControllers/{storage_controller_id}/Certificates",
    response_model_exclude_none=True,
)
@authenticate
async def get37(
    computer_system_id: str,
    storage_id: str,
    storage_controller_id: str,
    request: Request,
    response: Response,
) -> CertificateCollection:
    s: Service = find_service(CertificateCollection)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(CertificateCollection, s.get(**b))


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Storage/{storage_id}/StorageControllers/{storage_controller_id}/Certificates",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Storage/{storage_id}/StorageControllers/{storage_controller_id}/Certificates",
    response_model_exclude_none=True,
)
@authenticate
async def get38(
    resource_block_id: str,
    storage_id: str,
    storage_controller_id: str,
    request: Request,
    response: Response,
) -> CertificateCollection:
    s: Service = find_service(CertificateCollection)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(CertificateCollection, s.get(**b))


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Storage/{storage_id}/StorageControllers/{storage_controller_id}/Certificates",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Storage/{storage_id}/StorageControllers/{storage_controller_id}/Certificates",
    response_model_exclude_none=True,
)
@authenticate
async def get39(
    resource_block_id: str,
    computer_system_id: str,
    storage_id: str,
    storage_controller_id: str,
    request: Request,
    response: Response,
) -> CertificateCollection:
    s: Service = find_service(CertificateCollection)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(CertificateCollection, s.get(**b))


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Storage/{storage_id}/StorageControllers/{storage_controller_id}/Certificates",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Storage/{storage_id}/StorageControllers/{storage_controller_id}/Certificates",
    response_model_exclude_none=True,
)
@authenticate
async def get40(
    resource_block_id: str,
    storage_id: str,
    storage_controller_id: str,
    request: Request,
    response: Response,
) -> CertificateCollection:
    s: Service = find_service(CertificateCollection)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(CertificateCollection, s.get(**b))


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Storage/{storage_id}/StorageControllers/{storage_controller_id}/Certificates",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Storage/{storage_id}/StorageControllers/{storage_controller_id}/Certificates",
    response_model_exclude_none=True,
)
@authenticate
async def get41(
    resource_block_id: str,
    computer_system_id: str,
    storage_id: str,
    storage_controller_id: str,
    request: Request,
    response: Response,
) -> CertificateCollection:
    s: Service = find_service(CertificateCollection)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(CertificateCollection, s.get(**b))


@router.get(
    "/redfish/v1/Storage/{storage_id}/Controllers/{storage_controller_id}/Certificates",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Storage/{storage_id}/Controllers/{storage_controller_id}/Certificates",
    response_model_exclude_none=True,
)
@authenticate
async def get42(
    storage_id: str, storage_controller_id: str, request: Request, response: Response
) -> CertificateCollection:
    s: Service = find_service(CertificateCollection)
    b: dict[str, Any] = {
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(CertificateCollection, s.get(**b))


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/Controllers/{storage_controller_id}/Certificates",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/Controllers/{storage_controller_id}/Certificates",
    response_model_exclude_none=True,
)
@authenticate
async def get43(
    computer_system_id: str,
    storage_id: str,
    storage_controller_id: str,
    request: Request,
    response: Response,
) -> CertificateCollection:
    s: Service = find_service(CertificateCollection)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(CertificateCollection, s.get(**b))


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Storage/{storage_id}/Controllers/{storage_controller_id}/Certificates",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Storage/{storage_id}/Controllers/{storage_controller_id}/Certificates",
    response_model_exclude_none=True,
)
@authenticate
async def get44(
    resource_block_id: str,
    storage_id: str,
    storage_controller_id: str,
    request: Request,
    response: Response,
) -> CertificateCollection:
    s: Service = find_service(CertificateCollection)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(CertificateCollection, s.get(**b))


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Storage/{storage_id}/Controllers/{storage_controller_id}/Certificates",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Storage/{storage_id}/Controllers/{storage_controller_id}/Certificates",
    response_model_exclude_none=True,
)
@authenticate
async def get45(
    resource_block_id: str,
    computer_system_id: str,
    storage_id: str,
    storage_controller_id: str,
    request: Request,
    response: Response,
) -> CertificateCollection:
    s: Service = find_service(CertificateCollection)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(CertificateCollection, s.get(**b))


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Storage/{storage_id}/Controllers/{storage_controller_id}/Certificates",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Storage/{storage_id}/Controllers/{storage_controller_id}/Certificates",
    response_model_exclude_none=True,
)
@authenticate
async def get46(
    resource_block_id: str,
    storage_id: str,
    storage_controller_id: str,
    request: Request,
    response: Response,
) -> CertificateCollection:
    s: Service = find_service(CertificateCollection)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(CertificateCollection, s.get(**b))


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Storage/{storage_id}/Controllers/{storage_controller_id}/Certificates",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Storage/{storage_id}/Controllers/{storage_controller_id}/Certificates",
    response_model_exclude_none=True,
)
@authenticate
async def get47(
    resource_block_id: str,
    computer_system_id: str,
    storage_id: str,
    storage_controller_id: str,
    request: Request,
    response: Response,
) -> CertificateCollection:
    s: Service = find_service(CertificateCollection)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(CertificateCollection, s.get(**b))


@router.get(
    "/redfish/v1/Fabrics/{fabric_id}/Switches/{switch_id}/Certificates",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Fabrics/{fabric_id}/Switches/{switch_id}/Certificates",
    response_model_exclude_none=True,
)
@authenticate
async def get48(
    fabric_id: str, switch_id: str, request: Request, response: Response
) -> CertificateCollection:
    s: Service = find_service(CertificateCollection)
    b: dict[str, Any] = {
        "fabric_id": fabric_id,
        "switch_id": switch_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(CertificateCollection, s.get(**b))


@router.get("/redfish/v1/Chassis/{chassis_id}/Certificates", response_model_exclude_none=True)
@router.head("/redfish/v1/Chassis/{chassis_id}/Certificates", response_model_exclude_none=True)
@authenticate
async def get49(chassis_id: str, request: Request, response: Response) -> CertificateCollection:
    s: Service = find_service(CertificateCollection)
    b: dict[str, Any] = {"chassis_id": chassis_id, "request": request, "response": response}

    response.headers["OData-Version"] = "4.0"

    return cast(CertificateCollection, s.get(**b))


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/Drives/{drive_id}/Certificates",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/Drives/{drive_id}/Certificates",
    response_model_exclude_none=True,
)
@authenticate
async def get50(
    computer_system_id: str, storage_id: str, drive_id: str, request: Request, response: Response
) -> CertificateCollection:
    s: Service = find_service(CertificateCollection)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "drive_id": drive_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(CertificateCollection, s.get(**b))


@router.get(
    "/redfish/v1/Chassis/{chassis_id}/Drives/{drive_id}/Certificates",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Chassis/{chassis_id}/Drives/{drive_id}/Certificates",
    response_model_exclude_none=True,
)
@authenticate
async def get51(
    chassis_id: str, drive_id: str, request: Request, response: Response
) -> CertificateCollection:
    s: Service = find_service(CertificateCollection)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "drive_id": drive_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(CertificateCollection, s.get(**b))


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Storage/{storage_id}/Drives/{drive_id}/Certificates",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Storage/{storage_id}/Drives/{drive_id}/Certificates",
    response_model_exclude_none=True,
)
@authenticate
async def get52(
    resource_block_id: str, storage_id: str, drive_id: str, request: Request, response: Response
) -> CertificateCollection:
    s: Service = find_service(CertificateCollection)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "storage_id": storage_id,
        "drive_id": drive_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(CertificateCollection, s.get(**b))


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Drives/{drive_id}/Certificates",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Drives/{drive_id}/Certificates",
    response_model_exclude_none=True,
)
@authenticate
async def get53(
    resource_block_id: str, drive_id: str, request: Request, response: Response
) -> CertificateCollection:
    s: Service = find_service(CertificateCollection)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "drive_id": drive_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(CertificateCollection, s.get(**b))


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Storage/{storage_id}/Drives/{drive_id}/Certificates",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Storage/{storage_id}/Drives/{drive_id}/Certificates",
    response_model_exclude_none=True,
)
@authenticate
async def get54(
    resource_block_id: str,
    computer_system_id: str,
    storage_id: str,
    drive_id: str,
    request: Request,
    response: Response,
) -> CertificateCollection:
    s: Service = find_service(CertificateCollection)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "drive_id": drive_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(CertificateCollection, s.get(**b))


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Storage/{storage_id}/Drives/{drive_id}/Certificates",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Storage/{storage_id}/Drives/{drive_id}/Certificates",
    response_model_exclude_none=True,
)
@authenticate
async def get55(
    resource_block_id: str, storage_id: str, drive_id: str, request: Request, response: Response
) -> CertificateCollection:
    s: Service = find_service(CertificateCollection)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "storage_id": storage_id,
        "drive_id": drive_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(CertificateCollection, s.get(**b))


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Drives/{drive_id}/Certificates",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Drives/{drive_id}/Certificates",
    response_model_exclude_none=True,
)
@authenticate
async def get56(
    resource_block_id: str, drive_id: str, request: Request, response: Response
) -> CertificateCollection:
    s: Service = find_service(CertificateCollection)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "drive_id": drive_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(CertificateCollection, s.get(**b))


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Storage/{storage_id}/Drives/{drive_id}/Certificates",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Storage/{storage_id}/Drives/{drive_id}/Certificates",
    response_model_exclude_none=True,
)
@authenticate
async def get57(
    resource_block_id: str,
    computer_system_id: str,
    storage_id: str,
    drive_id: str,
    request: Request,
    response: Response,
) -> CertificateCollection:
    s: Service = find_service(CertificateCollection)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "drive_id": drive_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(CertificateCollection, s.get(**b))


@router.get(
    "/redfish/v1/Chassis/{chassis_id}/NetworkAdapters/{network_adapter_id}/Certificates",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Chassis/{chassis_id}/NetworkAdapters/{network_adapter_id}/Certificates",
    response_model_exclude_none=True,
)
@authenticate
async def get58(
    chassis_id: str, network_adapter_id: str, request: Request, response: Response
) -> CertificateCollection:
    s: Service = find_service(CertificateCollection)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "network_adapter_id": network_adapter_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(CertificateCollection, s.get(**b))


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/VirtualMedia/{virtual_media_id}/Certificates",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Systems/{computer_system_id}/VirtualMedia/{virtual_media_id}/Certificates",
    response_model_exclude_none=True,
)
@authenticate
async def get59(
    computer_system_id: str, virtual_media_id: str, request: Request, response: Response
) -> CertificateCollection:
    s: Service = find_service(CertificateCollection)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "virtual_media_id": virtual_media_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(CertificateCollection, s.get(**b))


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/VirtualMedia/{virtual_media_id}/ClientCertificates",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Systems/{computer_system_id}/VirtualMedia/{virtual_media_id}/ClientCertificates",
    response_model_exclude_none=True,
)
@authenticate
async def get60(
    computer_system_id: str, virtual_media_id: str, request: Request, response: Response
) -> CertificateCollection:
    s: Service = find_service(CertificateCollection)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "virtual_media_id": virtual_media_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(CertificateCollection, s.get(**b))


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/VirtualMedia/{virtual_media_id}/Certificates",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/VirtualMedia/{virtual_media_id}/Certificates",
    response_model_exclude_none=True,
)
@authenticate
async def get61(
    resource_block_id: str,
    computer_system_id: str,
    virtual_media_id: str,
    request: Request,
    response: Response,
) -> CertificateCollection:
    s: Service = find_service(CertificateCollection)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "virtual_media_id": virtual_media_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(CertificateCollection, s.get(**b))


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/VirtualMedia/{virtual_media_id}/ClientCertificates",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/VirtualMedia/{virtual_media_id}/ClientCertificates",
    response_model_exclude_none=True,
)
@authenticate
async def get62(
    resource_block_id: str,
    computer_system_id: str,
    virtual_media_id: str,
    request: Request,
    response: Response,
) -> CertificateCollection:
    s: Service = find_service(CertificateCollection)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "virtual_media_id": virtual_media_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(CertificateCollection, s.get(**b))


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/VirtualMedia/{virtual_media_id}/Certificates",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/VirtualMedia/{virtual_media_id}/Certificates",
    response_model_exclude_none=True,
)
@authenticate
async def get63(
    resource_block_id: str,
    computer_system_id: str,
    virtual_media_id: str,
    request: Request,
    response: Response,
) -> CertificateCollection:
    s: Service = find_service(CertificateCollection)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "virtual_media_id": virtual_media_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(CertificateCollection, s.get(**b))


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/VirtualMedia/{virtual_media_id}/ClientCertificates",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/VirtualMedia/{virtual_media_id}/ClientCertificates",
    response_model_exclude_none=True,
)
@authenticate
async def get64(
    resource_block_id: str,
    computer_system_id: str,
    virtual_media_id: str,
    request: Request,
    response: Response,
) -> CertificateCollection:
    s: Service = find_service(CertificateCollection)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "virtual_media_id": virtual_media_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(CertificateCollection, s.get(**b))


@router.get("/redfish/v1/UpdateService/RemoteServerCertificates", response_model_exclude_none=True)
@router.head(
    "/redfish/v1/UpdateService/RemoteServerCertificates", response_model_exclude_none=True
)
@authenticate
async def get65(request: Request, response: Response) -> CertificateCollection:
    s: Service = find_service(CertificateCollection)
    b: dict[str, Any] = {"request": request, "response": response}

    response.headers["OData-Version"] = "4.0"

    return cast(CertificateCollection, s.get(**b))


@router.get("/redfish/v1/UpdateService/ClientCertificates", response_model_exclude_none=True)
@router.head("/redfish/v1/UpdateService/ClientCertificates", response_model_exclude_none=True)
@authenticate
async def get66(request: Request, response: Response) -> CertificateCollection:
    s: Service = find_service(CertificateCollection)
    b: dict[str, Any] = {"request": request, "response": response}

    response.headers["OData-Version"] = "4.0"

    return cast(CertificateCollection, s.get(**b))


@router.get("/redfish/v1/Managers/{manager_id}/Certificates", response_model_exclude_none=True)
@router.head("/redfish/v1/Managers/{manager_id}/Certificates", response_model_exclude_none=True)
@authenticate
async def get67(manager_id: str, request: Request, response: Response) -> CertificateCollection:
    s: Service = find_service(CertificateCollection)
    b: dict[str, Any] = {"manager_id": manager_id, "request": request, "response": response}

    response.headers["OData-Version"] = "4.0"

    return cast(CertificateCollection, s.get(**b))


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/KeyManagement/KMIPCertificates",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Systems/{computer_system_id}/KeyManagement/KMIPCertificates",
    response_model_exclude_none=True,
)
@authenticate
async def get68(
    computer_system_id: str, request: Request, response: Response
) -> CertificateCollection:
    s: Service = find_service(CertificateCollection)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(CertificateCollection, s.get(**b))


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/KeyManagement/KMIPCertificates",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/KeyManagement/KMIPCertificates",
    response_model_exclude_none=True,
)
@authenticate
async def get69(
    resource_block_id: str, computer_system_id: str, request: Request, response: Response
) -> CertificateCollection:
    s: Service = find_service(CertificateCollection)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(CertificateCollection, s.get(**b))


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/KeyManagement/KMIPCertificates",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/KeyManagement/KMIPCertificates",
    response_model_exclude_none=True,
)
@authenticate
async def get70(
    resource_block_id: str, computer_system_id: str, request: Request, response: Response
) -> CertificateCollection:
    s: Service = find_service(CertificateCollection)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(CertificateCollection, s.get(**b))


@router.get(
    "/redfish/v1/Managers/{manager_id}/SecurityPolicy/SPDM/TrustedCertificates",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Managers/{manager_id}/SecurityPolicy/SPDM/TrustedCertificates",
    response_model_exclude_none=True,
)
@authenticate
async def get71(manager_id: str, request: Request, response: Response) -> CertificateCollection:
    s: Service = find_service(CertificateCollection)
    b: dict[str, Any] = {"manager_id": manager_id, "request": request, "response": response}

    response.headers["OData-Version"] = "4.0"

    return cast(CertificateCollection, s.get(**b))


@router.get(
    "/redfish/v1/Managers/{manager_id}/SecurityPolicy/SPDM/RevokedCertificates",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Managers/{manager_id}/SecurityPolicy/SPDM/RevokedCertificates",
    response_model_exclude_none=True,
)
@authenticate
async def get72(manager_id: str, request: Request, response: Response) -> CertificateCollection:
    s: Service = find_service(CertificateCollection)
    b: dict[str, Any] = {"manager_id": manager_id, "request": request, "response": response}

    response.headers["OData-Version"] = "4.0"

    return cast(CertificateCollection, s.get(**b))


@router.get(
    "/redfish/v1/Managers/{manager_id}/SecurityPolicy/TLS/Client/TrustedCertificates",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Managers/{manager_id}/SecurityPolicy/TLS/Client/TrustedCertificates",
    response_model_exclude_none=True,
)
@authenticate
async def get73(manager_id: str, request: Request, response: Response) -> CertificateCollection:
    s: Service = find_service(CertificateCollection)
    b: dict[str, Any] = {"manager_id": manager_id, "request": request, "response": response}

    response.headers["OData-Version"] = "4.0"

    return cast(CertificateCollection, s.get(**b))


@router.get(
    "/redfish/v1/Managers/{manager_id}/SecurityPolicy/TLS/Client/RevokedCertificates",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Managers/{manager_id}/SecurityPolicy/TLS/Client/RevokedCertificates",
    response_model_exclude_none=True,
)
@authenticate
async def get74(manager_id: str, request: Request, response: Response) -> CertificateCollection:
    s: Service = find_service(CertificateCollection)
    b: dict[str, Any] = {"manager_id": manager_id, "request": request, "response": response}

    response.headers["OData-Version"] = "4.0"

    return cast(CertificateCollection, s.get(**b))


@router.get(
    "/redfish/v1/Managers/{manager_id}/SecurityPolicy/TLS/Server/TrustedCertificates",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Managers/{manager_id}/SecurityPolicy/TLS/Server/TrustedCertificates",
    response_model_exclude_none=True,
)
@authenticate
async def get75(manager_id: str, request: Request, response: Response) -> CertificateCollection:
    s: Service = find_service(CertificateCollection)
    b: dict[str, Any] = {"manager_id": manager_id, "request": request, "response": response}

    response.headers["OData-Version"] = "4.0"

    return cast(CertificateCollection, s.get(**b))


@router.get(
    "/redfish/v1/Managers/{manager_id}/SecurityPolicy/TLS/Server/RevokedCertificates",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Managers/{manager_id}/SecurityPolicy/TLS/Server/RevokedCertificates",
    response_model_exclude_none=True,
)
@authenticate
async def get76(manager_id: str, request: Request, response: Response) -> CertificateCollection:
    s: Service = find_service(CertificateCollection)
    b: dict[str, Any] = {"manager_id": manager_id, "request": request, "response": response}

    response.headers["OData-Version"] = "4.0"

    return cast(CertificateCollection, s.get(**b))


@router.get(
    "/redfish/v1/Chassis/{chassis_id}/TrustedComponents/{trusted_component_id}/Certificates",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Chassis/{chassis_id}/TrustedComponents/{trusted_component_id}/Certificates",
    response_model_exclude_none=True,
)
@authenticate
async def get77(
    chassis_id: str, trusted_component_id: str, request: Request, response: Response
) -> CertificateCollection:
    s: Service = find_service(CertificateCollection)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "trusted_component_id": trusted_component_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(CertificateCollection, s.get(**b))


@router.get(
    "/redfish/v1/AccountService/OutboundConnections/{outbound_connection_id}/Certificates",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/AccountService/OutboundConnections/{outbound_connection_id}/Certificates",
    response_model_exclude_none=True,
)
@authenticate
async def get78(
    outbound_connection_id: str, request: Request, response: Response
) -> CertificateCollection:
    s: Service = find_service(CertificateCollection)
    b: dict[str, Any] = {
        "outbound_connection_id": outbound_connection_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(CertificateCollection, s.get(**b))


@router.get(
    "/redfish/v1/AccountService/OutboundConnections/{outbound_connection_id}/ClientCertificates",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/AccountService/OutboundConnections/{outbound_connection_id}/ClientCertificates",
    response_model_exclude_none=True,
)
@authenticate
async def get79(
    outbound_connection_id: str, request: Request, response: Response
) -> CertificateCollection:
    s: Service = find_service(CertificateCollection)
    b: dict[str, Any] = {
        "outbound_connection_id": outbound_connection_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(CertificateCollection, s.get(**b))


@router.get(
    "/redfish/v1/Chassis/{chassis_id}/PowerSubsystem/PowerSupplies/{power_supply_id}/Certificates",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Chassis/{chassis_id}/PowerSubsystem/PowerSupplies/{power_supply_id}/Certificates",
    response_model_exclude_none=True,
)
@authenticate
async def get80(
    chassis_id: str, power_supply_id: str, request: Request, response: Response
) -> CertificateCollection:
    s: Service = find_service(CertificateCollection)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "power_supply_id": power_supply_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(CertificateCollection, s.get(**b))
