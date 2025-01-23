from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.certificate import Certificate, CertificateOnCreate
from ..model.certificate_collection import CertificateCollection
from ..service import Service, ServiceCollection
from ..util import get_service, get_service_collection, set_link_header

router = APIRouter()


@router.get(
    "/redfish/v1/AccountService/Accounts/{manager_account_id}/Certificates",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/AccountService/Accounts/{manager_account_id}/Certificates",
    response_model_exclude_none=True,
)
async def get1(
    manager_account_id: str, request: Request, response: Response
) -> CertificateCollection:
    s: Service = get_service(CertificateCollection, request)
    b: dict[str, Any] = {
        "manager_account_id": manager_account_id,
        "request": request,
        "response": response,
    }
    m = cast(CertificateCollection, s.get(**b))
    set_link_header(m, response)
    return m


@router.post(
    "/redfish/v1/AccountService/Accounts/{manager_account_id}/Certificates",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/AccountService/Accounts/{manager_account_id}/Certificates/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post1(
    manager_account_id: str, request: Request, response: Response, body: CertificateOnCreate
) -> Certificate:
    s: ServiceCollection = get_service_collection(CertificateCollection, request)
    b: dict[str, Any] = {
        "manager_account_id": manager_account_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Certificate, s.post(**b))


@router.get(
    "/redfish/v1/AccountService/ActiveDirectory/Certificates", response_model_exclude_none=True
)
@router.head(
    "/redfish/v1/AccountService/ActiveDirectory/Certificates", response_model_exclude_none=True
)
async def get2(request: Request, response: Response) -> CertificateCollection:
    s: Service = get_service(CertificateCollection, request)
    b: dict[str, Any] = {"request": request, "response": response}
    m = cast(CertificateCollection, s.get(**b))
    set_link_header(m, response)
    return m


@router.post(
    "/redfish/v1/AccountService/ActiveDirectory/Certificates", response_model_exclude_none=True
)
@router.post(
    "/redfish/v1/AccountService/ActiveDirectory/Certificates/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post2(request: Request, response: Response, body: CertificateOnCreate) -> Certificate:
    s: ServiceCollection = get_service_collection(CertificateCollection, request)
    b: dict[str, Any] = {"request": request, "response": response, "body": body}
    return cast(Certificate, s.post(**b))


@router.get("/redfish/v1/AccountService/LDAP/Certificates", response_model_exclude_none=True)
@router.head("/redfish/v1/AccountService/LDAP/Certificates", response_model_exclude_none=True)
async def get3(request: Request, response: Response) -> CertificateCollection:
    s: Service = get_service(CertificateCollection, request)
    b: dict[str, Any] = {"request": request, "response": response}
    m = cast(CertificateCollection, s.get(**b))
    set_link_header(m, response)
    return m


@router.post("/redfish/v1/AccountService/LDAP/Certificates", response_model_exclude_none=True)
@router.post(
    "/redfish/v1/AccountService/LDAP/Certificates/Members", response_model_exclude_none=True
)
@authenticate
async def post3(request: Request, response: Response, body: CertificateOnCreate) -> Certificate:
    s: ServiceCollection = get_service_collection(CertificateCollection, request)
    b: dict[str, Any] = {"request": request, "response": response, "body": body}
    return cast(Certificate, s.post(**b))


@router.get(
    "/redfish/v1/AccountService/ExternalAccountProviders/{external_account_provider_id}/Certificates",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/AccountService/ExternalAccountProviders/{external_account_provider_id}/Certificates",
    response_model_exclude_none=True,
)
async def get4(
    external_account_provider_id: str, request: Request, response: Response
) -> CertificateCollection:
    s: Service = get_service(CertificateCollection, request)
    b: dict[str, Any] = {
        "external_account_provider_id": external_account_provider_id,
        "request": request,
        "response": response,
    }
    m = cast(CertificateCollection, s.get(**b))
    set_link_header(m, response)
    return m


@router.post(
    "/redfish/v1/AccountService/ExternalAccountProviders/{external_account_provider_id}/Certificates",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/AccountService/ExternalAccountProviders/{external_account_provider_id}/Certificates/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post4(
    external_account_provider_id: str,
    request: Request,
    response: Response,
    body: CertificateOnCreate,
) -> Certificate:
    s: ServiceCollection = get_service_collection(CertificateCollection, request)
    b: dict[str, Any] = {
        "external_account_provider_id": external_account_provider_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Certificate, s.post(**b))


@router.get(
    "/redfish/v1/AccountService/MultiFactorAuth/ClientCertificate/Certificates",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/AccountService/MultiFactorAuth/ClientCertificate/Certificates",
    response_model_exclude_none=True,
)
async def get5(request: Request, response: Response) -> CertificateCollection:
    s: Service = get_service(CertificateCollection, request)
    b: dict[str, Any] = {"request": request, "response": response}
    m = cast(CertificateCollection, s.get(**b))
    set_link_header(m, response)
    return m


@router.post(
    "/redfish/v1/AccountService/MultiFactorAuth/ClientCertificate/Certificates",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/AccountService/MultiFactorAuth/ClientCertificate/Certificates/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post5(request: Request, response: Response, body: CertificateOnCreate) -> Certificate:
    s: ServiceCollection = get_service_collection(CertificateCollection, request)
    b: dict[str, Any] = {"request": request, "response": response, "body": body}
    return cast(Certificate, s.post(**b))


@router.get(
    "/redfish/v1/AccountService/MultiFactorAuth/SecurID/Certificates",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/AccountService/MultiFactorAuth/SecurID/Certificates",
    response_model_exclude_none=True,
)
async def get6(request: Request, response: Response) -> CertificateCollection:
    s: Service = get_service(CertificateCollection, request)
    b: dict[str, Any] = {"request": request, "response": response}
    m = cast(CertificateCollection, s.get(**b))
    set_link_header(m, response)
    return m


@router.post(
    "/redfish/v1/AccountService/MultiFactorAuth/SecurID/Certificates",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/AccountService/MultiFactorAuth/SecurID/Certificates/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post6(request: Request, response: Response, body: CertificateOnCreate) -> Certificate:
    s: ServiceCollection = get_service_collection(CertificateCollection, request)
    b: dict[str, Any] = {"request": request, "response": response, "body": body}
    return cast(Certificate, s.post(**b))


@router.get(
    "/redfish/v1/Managers/{manager_id}/RemoteAccountService/Accounts/{manager_account_id}/Certificates",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Managers/{manager_id}/RemoteAccountService/Accounts/{manager_account_id}/Certificates",
    response_model_exclude_none=True,
)
async def get7(
    manager_id: str, manager_account_id: str, request: Request, response: Response
) -> CertificateCollection:
    s: Service = get_service(CertificateCollection, request)
    b: dict[str, Any] = {
        "manager_id": manager_id,
        "manager_account_id": manager_account_id,
        "request": request,
        "response": response,
    }
    m = cast(CertificateCollection, s.get(**b))
    set_link_header(m, response)
    return m


@router.post(
    "/redfish/v1/Managers/{manager_id}/RemoteAccountService/Accounts/{manager_account_id}/Certificates",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/Managers/{manager_id}/RemoteAccountService/Accounts/{manager_account_id}/Certificates/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post7(
    manager_id: str,
    manager_account_id: str,
    request: Request,
    response: Response,
    body: CertificateOnCreate,
) -> Certificate:
    s: ServiceCollection = get_service_collection(CertificateCollection, request)
    b: dict[str, Any] = {
        "manager_id": manager_id,
        "manager_account_id": manager_account_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Certificate, s.post(**b))


@router.get(
    "/redfish/v1/Managers/{manager_id}/RemoteAccountService/ActiveDirectory/Certificates",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Managers/{manager_id}/RemoteAccountService/ActiveDirectory/Certificates",
    response_model_exclude_none=True,
)
async def get8(manager_id: str, request: Request, response: Response) -> CertificateCollection:
    s: Service = get_service(CertificateCollection, request)
    b: dict[str, Any] = {"manager_id": manager_id, "request": request, "response": response}
    m = cast(CertificateCollection, s.get(**b))
    set_link_header(m, response)
    return m


@router.post(
    "/redfish/v1/Managers/{manager_id}/RemoteAccountService/ActiveDirectory/Certificates",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/Managers/{manager_id}/RemoteAccountService/ActiveDirectory/Certificates/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post8(
    manager_id: str, request: Request, response: Response, body: CertificateOnCreate
) -> Certificate:
    s: ServiceCollection = get_service_collection(CertificateCollection, request)
    b: dict[str, Any] = {
        "manager_id": manager_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Certificate, s.post(**b))


@router.get(
    "/redfish/v1/Managers/{manager_id}/RemoteAccountService/LDAP/Certificates",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Managers/{manager_id}/RemoteAccountService/LDAP/Certificates",
    response_model_exclude_none=True,
)
async def get9(manager_id: str, request: Request, response: Response) -> CertificateCollection:
    s: Service = get_service(CertificateCollection, request)
    b: dict[str, Any] = {"manager_id": manager_id, "request": request, "response": response}
    m = cast(CertificateCollection, s.get(**b))
    set_link_header(m, response)
    return m


@router.post(
    "/redfish/v1/Managers/{manager_id}/RemoteAccountService/LDAP/Certificates",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/Managers/{manager_id}/RemoteAccountService/LDAP/Certificates/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post9(
    manager_id: str, request: Request, response: Response, body: CertificateOnCreate
) -> Certificate:
    s: ServiceCollection = get_service_collection(CertificateCollection, request)
    b: dict[str, Any] = {
        "manager_id": manager_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Certificate, s.post(**b))


@router.get(
    "/redfish/v1/Managers/{manager_id}/RemoteAccountService/ExternalAccountProviders/{external_account_provider_id}/Certificates",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Managers/{manager_id}/RemoteAccountService/ExternalAccountProviders/{external_account_provider_id}/Certificates",
    response_model_exclude_none=True,
)
async def get10(
    manager_id: str, external_account_provider_id: str, request: Request, response: Response
) -> CertificateCollection:
    s: Service = get_service(CertificateCollection, request)
    b: dict[str, Any] = {
        "manager_id": manager_id,
        "external_account_provider_id": external_account_provider_id,
        "request": request,
        "response": response,
    }
    m = cast(CertificateCollection, s.get(**b))
    set_link_header(m, response)
    return m


@router.post(
    "/redfish/v1/Managers/{manager_id}/RemoteAccountService/ExternalAccountProviders/{external_account_provider_id}/Certificates",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/Managers/{manager_id}/RemoteAccountService/ExternalAccountProviders/{external_account_provider_id}/Certificates/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post10(
    manager_id: str,
    external_account_provider_id: str,
    request: Request,
    response: Response,
    body: CertificateOnCreate,
) -> Certificate:
    s: ServiceCollection = get_service_collection(CertificateCollection, request)
    b: dict[str, Any] = {
        "manager_id": manager_id,
        "external_account_provider_id": external_account_provider_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Certificate, s.post(**b))


@router.get(
    "/redfish/v1/Managers/{manager_id}/RemoteAccountService/MultiFactorAuth/ClientCertificate/Certificates",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Managers/{manager_id}/RemoteAccountService/MultiFactorAuth/ClientCertificate/Certificates",
    response_model_exclude_none=True,
)
async def get11(manager_id: str, request: Request, response: Response) -> CertificateCollection:
    s: Service = get_service(CertificateCollection, request)
    b: dict[str, Any] = {"manager_id": manager_id, "request": request, "response": response}
    m = cast(CertificateCollection, s.get(**b))
    set_link_header(m, response)
    return m


@router.post(
    "/redfish/v1/Managers/{manager_id}/RemoteAccountService/MultiFactorAuth/ClientCertificate/Certificates",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/Managers/{manager_id}/RemoteAccountService/MultiFactorAuth/ClientCertificate/Certificates/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post11(
    manager_id: str, request: Request, response: Response, body: CertificateOnCreate
) -> Certificate:
    s: ServiceCollection = get_service_collection(CertificateCollection, request)
    b: dict[str, Any] = {
        "manager_id": manager_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Certificate, s.post(**b))


@router.get(
    "/redfish/v1/Managers/{manager_id}/RemoteAccountService/MultiFactorAuth/SecurID/Certificates",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Managers/{manager_id}/RemoteAccountService/MultiFactorAuth/SecurID/Certificates",
    response_model_exclude_none=True,
)
async def get12(manager_id: str, request: Request, response: Response) -> CertificateCollection:
    s: Service = get_service(CertificateCollection, request)
    b: dict[str, Any] = {"manager_id": manager_id, "request": request, "response": response}
    m = cast(CertificateCollection, s.get(**b))
    set_link_header(m, response)
    return m


@router.post(
    "/redfish/v1/Managers/{manager_id}/RemoteAccountService/MultiFactorAuth/SecurID/Certificates",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/Managers/{manager_id}/RemoteAccountService/MultiFactorAuth/SecurID/Certificates/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post12(
    manager_id: str, request: Request, response: Response, body: CertificateOnCreate
) -> Certificate:
    s: ServiceCollection = get_service_collection(CertificateCollection, request)
    b: dict[str, Any] = {
        "manager_id": manager_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Certificate, s.post(**b))


@router.get(
    "/redfish/v1/Managers/{manager_id}/NetworkProtocol/HTTPS/Certificates",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Managers/{manager_id}/NetworkProtocol/HTTPS/Certificates",
    response_model_exclude_none=True,
)
async def get13(manager_id: str, request: Request, response: Response) -> CertificateCollection:
    s: Service = get_service(CertificateCollection, request)
    b: dict[str, Any] = {"manager_id": manager_id, "request": request, "response": response}
    m = cast(CertificateCollection, s.get(**b))
    set_link_header(m, response)
    return m


@router.post(
    "/redfish/v1/Managers/{manager_id}/NetworkProtocol/HTTPS/Certificates",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/Managers/{manager_id}/NetworkProtocol/HTTPS/Certificates/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post13(
    manager_id: str, request: Request, response: Response, body: CertificateOnCreate
) -> Certificate:
    s: ServiceCollection = get_service_collection(CertificateCollection, request)
    b: dict[str, Any] = {
        "manager_id": manager_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Certificate, s.post(**b))


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/Boot/Certificates", response_model_exclude_none=True
)
@router.head(
    "/redfish/v1/Systems/{computer_system_id}/Boot/Certificates", response_model_exclude_none=True
)
async def get14(
    computer_system_id: str, request: Request, response: Response
) -> CertificateCollection:
    s: Service = get_service(CertificateCollection, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "request": request,
        "response": response,
    }
    m = cast(CertificateCollection, s.get(**b))
    set_link_header(m, response)
    return m


@router.post(
    "/redfish/v1/Systems/{computer_system_id}/Boot/Certificates", response_model_exclude_none=True
)
@router.post(
    "/redfish/v1/Systems/{computer_system_id}/Boot/Certificates/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post14(
    computer_system_id: str, request: Request, response: Response, body: CertificateOnCreate
) -> Certificate:
    s: ServiceCollection = get_service_collection(CertificateCollection, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Certificate, s.post(**b))


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Boot/Certificates",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Boot/Certificates",
    response_model_exclude_none=True,
)
async def get15(
    resource_block_id: str, computer_system_id: str, request: Request, response: Response
) -> CertificateCollection:
    s: Service = get_service(CertificateCollection, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "request": request,
        "response": response,
    }
    m = cast(CertificateCollection, s.get(**b))
    set_link_header(m, response)
    return m


@router.post(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Boot/Certificates",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Boot/Certificates/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post15(
    resource_block_id: str,
    computer_system_id: str,
    request: Request,
    response: Response,
    body: CertificateOnCreate,
) -> Certificate:
    s: ServiceCollection = get_service_collection(CertificateCollection, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Certificate, s.post(**b))


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Boot/Certificates",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Boot/Certificates",
    response_model_exclude_none=True,
)
async def get16(
    resource_block_id: str, computer_system_id: str, request: Request, response: Response
) -> CertificateCollection:
    s: Service = get_service(CertificateCollection, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "request": request,
        "response": response,
    }
    m = cast(CertificateCollection, s.get(**b))
    set_link_header(m, response)
    return m


@router.post(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Boot/Certificates",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Boot/Certificates/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post16(
    resource_block_id: str,
    computer_system_id: str,
    request: Request,
    response: Response,
    body: CertificateOnCreate,
) -> Certificate:
    s: ServiceCollection = get_service_collection(CertificateCollection, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Certificate, s.post(**b))


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/SecureBoot/SecureBootDatabases/{database_id}/Certificates",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Systems/{computer_system_id}/SecureBoot/SecureBootDatabases/{database_id}/Certificates",
    response_model_exclude_none=True,
)
async def get17(
    computer_system_id: str, database_id: str, request: Request, response: Response
) -> CertificateCollection:
    s: Service = get_service(CertificateCollection, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "database_id": database_id,
        "request": request,
        "response": response,
    }
    m = cast(CertificateCollection, s.get(**b))
    set_link_header(m, response)
    return m


@router.post(
    "/redfish/v1/Systems/{computer_system_id}/SecureBoot/SecureBootDatabases/{database_id}/Certificates",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/Systems/{computer_system_id}/SecureBoot/SecureBootDatabases/{database_id}/Certificates/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post17(
    computer_system_id: str,
    database_id: str,
    request: Request,
    response: Response,
    body: CertificateOnCreate,
) -> Certificate:
    s: ServiceCollection = get_service_collection(CertificateCollection, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "database_id": database_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Certificate, s.post(**b))


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/SecureBoot/SecureBootDatabases/{database_id}/Certificates",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/SecureBoot/SecureBootDatabases/{database_id}/Certificates",
    response_model_exclude_none=True,
)
async def get18(
    resource_block_id: str,
    computer_system_id: str,
    database_id: str,
    request: Request,
    response: Response,
) -> CertificateCollection:
    s: Service = get_service(CertificateCollection, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "database_id": database_id,
        "request": request,
        "response": response,
    }
    m = cast(CertificateCollection, s.get(**b))
    set_link_header(m, response)
    return m


@router.post(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/SecureBoot/SecureBootDatabases/{database_id}/Certificates",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/SecureBoot/SecureBootDatabases/{database_id}/Certificates/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post18(
    resource_block_id: str,
    computer_system_id: str,
    database_id: str,
    request: Request,
    response: Response,
    body: CertificateOnCreate,
) -> Certificate:
    s: ServiceCollection = get_service_collection(CertificateCollection, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "database_id": database_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Certificate, s.post(**b))


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/SecureBoot/SecureBootDatabases/{database_id}/Certificates",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/SecureBoot/SecureBootDatabases/{database_id}/Certificates",
    response_model_exclude_none=True,
)
async def get19(
    resource_block_id: str,
    computer_system_id: str,
    database_id: str,
    request: Request,
    response: Response,
) -> CertificateCollection:
    s: Service = get_service(CertificateCollection, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "database_id": database_id,
        "request": request,
        "response": response,
    }
    m = cast(CertificateCollection, s.get(**b))
    set_link_header(m, response)
    return m


@router.post(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/SecureBoot/SecureBootDatabases/{database_id}/Certificates",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/SecureBoot/SecureBootDatabases/{database_id}/Certificates/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post19(
    resource_block_id: str,
    computer_system_id: str,
    database_id: str,
    request: Request,
    response: Response,
    body: CertificateOnCreate,
) -> Certificate:
    s: ServiceCollection = get_service_collection(CertificateCollection, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "database_id": database_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Certificate, s.post(**b))


@router.get(
    "/redfish/v1/EventService/Subscriptions/{event_destination_id}/Certificates",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/EventService/Subscriptions/{event_destination_id}/Certificates",
    response_model_exclude_none=True,
)
async def get20(
    event_destination_id: str, request: Request, response: Response
) -> CertificateCollection:
    s: Service = get_service(CertificateCollection, request)
    b: dict[str, Any] = {
        "event_destination_id": event_destination_id,
        "request": request,
        "response": response,
    }
    m = cast(CertificateCollection, s.get(**b))
    set_link_header(m, response)
    return m


@router.post(
    "/redfish/v1/EventService/Subscriptions/{event_destination_id}/Certificates",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/EventService/Subscriptions/{event_destination_id}/Certificates/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post20(
    event_destination_id: str, request: Request, response: Response, body: CertificateOnCreate
) -> Certificate:
    s: ServiceCollection = get_service_collection(CertificateCollection, request)
    b: dict[str, Any] = {
        "event_destination_id": event_destination_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Certificate, s.post(**b))


@router.get(
    "/redfish/v1/EventService/Subscriptions/{event_destination_id}/ClientCertificates",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/EventService/Subscriptions/{event_destination_id}/ClientCertificates",
    response_model_exclude_none=True,
)
async def get21(
    event_destination_id: str, request: Request, response: Response
) -> CertificateCollection:
    s: Service = get_service(CertificateCollection, request)
    b: dict[str, Any] = {
        "event_destination_id": event_destination_id,
        "request": request,
        "response": response,
    }
    m = cast(CertificateCollection, s.get(**b))
    set_link_header(m, response)
    return m


@router.post(
    "/redfish/v1/EventService/Subscriptions/{event_destination_id}/ClientCertificates",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/EventService/Subscriptions/{event_destination_id}/ClientCertificates/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post21(
    event_destination_id: str, request: Request, response: Response, body: CertificateOnCreate
) -> Certificate:
    s: ServiceCollection = get_service_collection(CertificateCollection, request)
    b: dict[str, Any] = {
        "event_destination_id": event_destination_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Certificate, s.post(**b))


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/Certificates", response_model_exclude_none=True
)
@router.head(
    "/redfish/v1/Systems/{computer_system_id}/Certificates", response_model_exclude_none=True
)
async def get22(
    computer_system_id: str, request: Request, response: Response
) -> CertificateCollection:
    s: Service = get_service(CertificateCollection, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "request": request,
        "response": response,
    }
    m = cast(CertificateCollection, s.get(**b))
    set_link_header(m, response)
    return m


@router.post(
    "/redfish/v1/Systems/{computer_system_id}/Certificates", response_model_exclude_none=True
)
@router.post(
    "/redfish/v1/Systems/{computer_system_id}/Certificates/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post22(
    computer_system_id: str, request: Request, response: Response, body: CertificateOnCreate
) -> Certificate:
    s: ServiceCollection = get_service_collection(CertificateCollection, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Certificate, s.post(**b))


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Certificates",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Certificates",
    response_model_exclude_none=True,
)
async def get23(
    resource_block_id: str, computer_system_id: str, request: Request, response: Response
) -> CertificateCollection:
    s: Service = get_service(CertificateCollection, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "request": request,
        "response": response,
    }
    m = cast(CertificateCollection, s.get(**b))
    set_link_header(m, response)
    return m


@router.post(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Certificates",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Certificates/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post23(
    resource_block_id: str,
    computer_system_id: str,
    request: Request,
    response: Response,
    body: CertificateOnCreate,
) -> Certificate:
    s: ServiceCollection = get_service_collection(CertificateCollection, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Certificate, s.post(**b))


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Certificates",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Certificates",
    response_model_exclude_none=True,
)
async def get24(
    resource_block_id: str, computer_system_id: str, request: Request, response: Response
) -> CertificateCollection:
    s: Service = get_service(CertificateCollection, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "request": request,
        "response": response,
    }
    m = cast(CertificateCollection, s.get(**b))
    set_link_header(m, response)
    return m


@router.post(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Certificates",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Certificates/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post24(
    resource_block_id: str,
    computer_system_id: str,
    request: Request,
    response: Response,
    body: CertificateOnCreate,
) -> Certificate:
    s: ServiceCollection = get_service_collection(CertificateCollection, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Certificate, s.post(**b))


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/Memory/{memory_id}/Certificates",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Systems/{computer_system_id}/Memory/{memory_id}/Certificates",
    response_model_exclude_none=True,
)
async def get25(
    computer_system_id: str, memory_id: str, request: Request, response: Response
) -> CertificateCollection:
    s: Service = get_service(CertificateCollection, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "memory_id": memory_id,
        "request": request,
        "response": response,
    }
    m = cast(CertificateCollection, s.get(**b))
    set_link_header(m, response)
    return m


@router.post(
    "/redfish/v1/Systems/{computer_system_id}/Memory/{memory_id}/Certificates",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/Systems/{computer_system_id}/Memory/{memory_id}/Certificates/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post25(
    computer_system_id: str,
    memory_id: str,
    request: Request,
    response: Response,
    body: CertificateOnCreate,
) -> Certificate:
    s: ServiceCollection = get_service_collection(CertificateCollection, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "memory_id": memory_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Certificate, s.post(**b))


@router.get(
    "/redfish/v1/Chassis/{chassis_id}/Memory/{memory_id}/Certificates",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Chassis/{chassis_id}/Memory/{memory_id}/Certificates",
    response_model_exclude_none=True,
)
async def get26(
    chassis_id: str, memory_id: str, request: Request, response: Response
) -> CertificateCollection:
    s: Service = get_service(CertificateCollection, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "memory_id": memory_id,
        "request": request,
        "response": response,
    }
    m = cast(CertificateCollection, s.get(**b))
    set_link_header(m, response)
    return m


@router.post(
    "/redfish/v1/Chassis/{chassis_id}/Memory/{memory_id}/Certificates",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/Chassis/{chassis_id}/Memory/{memory_id}/Certificates/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post26(
    chassis_id: str,
    memory_id: str,
    request: Request,
    response: Response,
    body: CertificateOnCreate,
) -> Certificate:
    s: ServiceCollection = get_service_collection(CertificateCollection, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "memory_id": memory_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Certificate, s.post(**b))


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Memory/{memory_id}/Certificates",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Memory/{memory_id}/Certificates",
    response_model_exclude_none=True,
)
async def get27(
    resource_block_id: str, memory_id: str, request: Request, response: Response
) -> CertificateCollection:
    s: Service = get_service(CertificateCollection, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "memory_id": memory_id,
        "request": request,
        "response": response,
    }
    m = cast(CertificateCollection, s.get(**b))
    set_link_header(m, response)
    return m


@router.post(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Memory/{memory_id}/Certificates",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Memory/{memory_id}/Certificates/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post27(
    resource_block_id: str,
    memory_id: str,
    request: Request,
    response: Response,
    body: CertificateOnCreate,
) -> Certificate:
    s: ServiceCollection = get_service_collection(CertificateCollection, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "memory_id": memory_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Certificate, s.post(**b))


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Memory/{memory_id}/Certificates",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Memory/{memory_id}/Certificates",
    response_model_exclude_none=True,
)
async def get28(
    resource_block_id: str,
    computer_system_id: str,
    memory_id: str,
    request: Request,
    response: Response,
) -> CertificateCollection:
    s: Service = get_service(CertificateCollection, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "memory_id": memory_id,
        "request": request,
        "response": response,
    }
    m = cast(CertificateCollection, s.get(**b))
    set_link_header(m, response)
    return m


@router.post(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Memory/{memory_id}/Certificates",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Memory/{memory_id}/Certificates/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post28(
    resource_block_id: str,
    computer_system_id: str,
    memory_id: str,
    request: Request,
    response: Response,
    body: CertificateOnCreate,
) -> Certificate:
    s: ServiceCollection = get_service_collection(CertificateCollection, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "memory_id": memory_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Certificate, s.post(**b))


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Memory/{memory_id}/Certificates",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Memory/{memory_id}/Certificates",
    response_model_exclude_none=True,
)
async def get29(
    resource_block_id: str, memory_id: str, request: Request, response: Response
) -> CertificateCollection:
    s: Service = get_service(CertificateCollection, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "memory_id": memory_id,
        "request": request,
        "response": response,
    }
    m = cast(CertificateCollection, s.get(**b))
    set_link_header(m, response)
    return m


@router.post(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Memory/{memory_id}/Certificates",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Memory/{memory_id}/Certificates/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post29(
    resource_block_id: str,
    memory_id: str,
    request: Request,
    response: Response,
    body: CertificateOnCreate,
) -> Certificate:
    s: ServiceCollection = get_service_collection(CertificateCollection, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "memory_id": memory_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Certificate, s.post(**b))


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Memory/{memory_id}/Certificates",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Memory/{memory_id}/Certificates",
    response_model_exclude_none=True,
)
async def get30(
    resource_block_id: str,
    computer_system_id: str,
    memory_id: str,
    request: Request,
    response: Response,
) -> CertificateCollection:
    s: Service = get_service(CertificateCollection, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "memory_id": memory_id,
        "request": request,
        "response": response,
    }
    m = cast(CertificateCollection, s.get(**b))
    set_link_header(m, response)
    return m


@router.post(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Memory/{memory_id}/Certificates",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Memory/{memory_id}/Certificates/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post30(
    resource_block_id: str,
    computer_system_id: str,
    memory_id: str,
    request: Request,
    response: Response,
    body: CertificateOnCreate,
) -> Certificate:
    s: ServiceCollection = get_service_collection(CertificateCollection, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "memory_id": memory_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Certificate, s.post(**b))


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/Processors/{processor_id}/Certificates",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Systems/{computer_system_id}/Processors/{processor_id}/Certificates",
    response_model_exclude_none=True,
)
async def get31(
    computer_system_id: str, processor_id: str, request: Request, response: Response
) -> CertificateCollection:
    s: Service = get_service(CertificateCollection, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "processor_id": processor_id,
        "request": request,
        "response": response,
    }
    m = cast(CertificateCollection, s.get(**b))
    set_link_header(m, response)
    return m


@router.post(
    "/redfish/v1/Systems/{computer_system_id}/Processors/{processor_id}/Certificates",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/Systems/{computer_system_id}/Processors/{processor_id}/Certificates/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post31(
    computer_system_id: str,
    processor_id: str,
    request: Request,
    response: Response,
    body: CertificateOnCreate,
) -> Certificate:
    s: ServiceCollection = get_service_collection(CertificateCollection, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "processor_id": processor_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Certificate, s.post(**b))


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Processors/{processor_id}/Certificates",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Processors/{processor_id}/Certificates",
    response_model_exclude_none=True,
)
async def get32(
    resource_block_id: str, processor_id: str, request: Request, response: Response
) -> CertificateCollection:
    s: Service = get_service(CertificateCollection, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "processor_id": processor_id,
        "request": request,
        "response": response,
    }
    m = cast(CertificateCollection, s.get(**b))
    set_link_header(m, response)
    return m


@router.post(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Processors/{processor_id}/Certificates",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Processors/{processor_id}/Certificates/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post32(
    resource_block_id: str,
    processor_id: str,
    request: Request,
    response: Response,
    body: CertificateOnCreate,
) -> Certificate:
    s: ServiceCollection = get_service_collection(CertificateCollection, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "processor_id": processor_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Certificate, s.post(**b))


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Processors/{processor_id}/Certificates",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Processors/{processor_id}/Certificates",
    response_model_exclude_none=True,
)
async def get33(
    resource_block_id: str,
    computer_system_id: str,
    processor_id: str,
    request: Request,
    response: Response,
) -> CertificateCollection:
    s: Service = get_service(CertificateCollection, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "processor_id": processor_id,
        "request": request,
        "response": response,
    }
    m = cast(CertificateCollection, s.get(**b))
    set_link_header(m, response)
    return m


@router.post(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Processors/{processor_id}/Certificates",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Processors/{processor_id}/Certificates/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post33(
    resource_block_id: str,
    computer_system_id: str,
    processor_id: str,
    request: Request,
    response: Response,
    body: CertificateOnCreate,
) -> Certificate:
    s: ServiceCollection = get_service_collection(CertificateCollection, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "processor_id": processor_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Certificate, s.post(**b))


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Processors/{processor_id}/Certificates",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Processors/{processor_id}/Certificates",
    response_model_exclude_none=True,
)
async def get34(
    resource_block_id: str, processor_id: str, request: Request, response: Response
) -> CertificateCollection:
    s: Service = get_service(CertificateCollection, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "processor_id": processor_id,
        "request": request,
        "response": response,
    }
    m = cast(CertificateCollection, s.get(**b))
    set_link_header(m, response)
    return m


@router.post(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Processors/{processor_id}/Certificates",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Processors/{processor_id}/Certificates/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post34(
    resource_block_id: str,
    processor_id: str,
    request: Request,
    response: Response,
    body: CertificateOnCreate,
) -> Certificate:
    s: ServiceCollection = get_service_collection(CertificateCollection, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "processor_id": processor_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Certificate, s.post(**b))


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Processors/{processor_id}/Certificates",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Processors/{processor_id}/Certificates",
    response_model_exclude_none=True,
)
async def get35(
    resource_block_id: str,
    computer_system_id: str,
    processor_id: str,
    request: Request,
    response: Response,
) -> CertificateCollection:
    s: Service = get_service(CertificateCollection, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "processor_id": processor_id,
        "request": request,
        "response": response,
    }
    m = cast(CertificateCollection, s.get(**b))
    set_link_header(m, response)
    return m


@router.post(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Processors/{processor_id}/Certificates",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Processors/{processor_id}/Certificates/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post35(
    resource_block_id: str,
    computer_system_id: str,
    processor_id: str,
    request: Request,
    response: Response,
    body: CertificateOnCreate,
) -> Certificate:
    s: ServiceCollection = get_service_collection(CertificateCollection, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "processor_id": processor_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Certificate, s.post(**b))


@router.get(
    "/redfish/v1/Storage/{storage_id}/StorageControllers/{storage_controller_id}/Certificates",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Storage/{storage_id}/StorageControllers/{storage_controller_id}/Certificates",
    response_model_exclude_none=True,
)
async def get36(
    storage_id: str, storage_controller_id: str, request: Request, response: Response
) -> CertificateCollection:
    s: Service = get_service(CertificateCollection, request)
    b: dict[str, Any] = {
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
        "request": request,
        "response": response,
    }
    m = cast(CertificateCollection, s.get(**b))
    set_link_header(m, response)
    return m


@router.post(
    "/redfish/v1/Storage/{storage_id}/StorageControllers/{storage_controller_id}/Certificates",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/Storage/{storage_id}/StorageControllers/{storage_controller_id}/Certificates/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post36(
    storage_id: str,
    storage_controller_id: str,
    request: Request,
    response: Response,
    body: CertificateOnCreate,
) -> Certificate:
    s: ServiceCollection = get_service_collection(CertificateCollection, request)
    b: dict[str, Any] = {
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Certificate, s.post(**b))


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/StorageControllers/{storage_controller_id}/Certificates",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/StorageControllers/{storage_controller_id}/Certificates",
    response_model_exclude_none=True,
)
async def get37(
    computer_system_id: str,
    storage_id: str,
    storage_controller_id: str,
    request: Request,
    response: Response,
) -> CertificateCollection:
    s: Service = get_service(CertificateCollection, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
        "request": request,
        "response": response,
    }
    m = cast(CertificateCollection, s.get(**b))
    set_link_header(m, response)
    return m


@router.post(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/StorageControllers/{storage_controller_id}/Certificates",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/StorageControllers/{storage_controller_id}/Certificates/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post37(
    computer_system_id: str,
    storage_id: str,
    storage_controller_id: str,
    request: Request,
    response: Response,
    body: CertificateOnCreate,
) -> Certificate:
    s: ServiceCollection = get_service_collection(CertificateCollection, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Certificate, s.post(**b))


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Storage/{storage_id}/StorageControllers/{storage_controller_id}/Certificates",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Storage/{storage_id}/StorageControllers/{storage_controller_id}/Certificates",
    response_model_exclude_none=True,
)
async def get38(
    resource_block_id: str,
    storage_id: str,
    storage_controller_id: str,
    request: Request,
    response: Response,
) -> CertificateCollection:
    s: Service = get_service(CertificateCollection, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
        "request": request,
        "response": response,
    }
    m = cast(CertificateCollection, s.get(**b))
    set_link_header(m, response)
    return m


@router.post(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Storage/{storage_id}/StorageControllers/{storage_controller_id}/Certificates",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Storage/{storage_id}/StorageControllers/{storage_controller_id}/Certificates/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post38(
    resource_block_id: str,
    storage_id: str,
    storage_controller_id: str,
    request: Request,
    response: Response,
    body: CertificateOnCreate,
) -> Certificate:
    s: ServiceCollection = get_service_collection(CertificateCollection, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Certificate, s.post(**b))


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Storage/{storage_id}/StorageControllers/{storage_controller_id}/Certificates",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Storage/{storage_id}/StorageControllers/{storage_controller_id}/Certificates",
    response_model_exclude_none=True,
)
async def get39(
    resource_block_id: str,
    computer_system_id: str,
    storage_id: str,
    storage_controller_id: str,
    request: Request,
    response: Response,
) -> CertificateCollection:
    s: Service = get_service(CertificateCollection, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
        "request": request,
        "response": response,
    }
    m = cast(CertificateCollection, s.get(**b))
    set_link_header(m, response)
    return m


@router.post(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Storage/{storage_id}/StorageControllers/{storage_controller_id}/Certificates",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Storage/{storage_id}/StorageControllers/{storage_controller_id}/Certificates/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post39(
    resource_block_id: str,
    computer_system_id: str,
    storage_id: str,
    storage_controller_id: str,
    request: Request,
    response: Response,
    body: CertificateOnCreate,
) -> Certificate:
    s: ServiceCollection = get_service_collection(CertificateCollection, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Certificate, s.post(**b))


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Storage/{storage_id}/StorageControllers/{storage_controller_id}/Certificates",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Storage/{storage_id}/StorageControllers/{storage_controller_id}/Certificates",
    response_model_exclude_none=True,
)
async def get40(
    resource_block_id: str,
    storage_id: str,
    storage_controller_id: str,
    request: Request,
    response: Response,
) -> CertificateCollection:
    s: Service = get_service(CertificateCollection, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
        "request": request,
        "response": response,
    }
    m = cast(CertificateCollection, s.get(**b))
    set_link_header(m, response)
    return m


@router.post(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Storage/{storage_id}/StorageControllers/{storage_controller_id}/Certificates",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Storage/{storage_id}/StorageControllers/{storage_controller_id}/Certificates/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post40(
    resource_block_id: str,
    storage_id: str,
    storage_controller_id: str,
    request: Request,
    response: Response,
    body: CertificateOnCreate,
) -> Certificate:
    s: ServiceCollection = get_service_collection(CertificateCollection, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Certificate, s.post(**b))


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Storage/{storage_id}/StorageControllers/{storage_controller_id}/Certificates",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Storage/{storage_id}/StorageControllers/{storage_controller_id}/Certificates",
    response_model_exclude_none=True,
)
async def get41(
    resource_block_id: str,
    computer_system_id: str,
    storage_id: str,
    storage_controller_id: str,
    request: Request,
    response: Response,
) -> CertificateCollection:
    s: Service = get_service(CertificateCollection, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
        "request": request,
        "response": response,
    }
    m = cast(CertificateCollection, s.get(**b))
    set_link_header(m, response)
    return m


@router.post(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Storage/{storage_id}/StorageControllers/{storage_controller_id}/Certificates",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Storage/{storage_id}/StorageControllers/{storage_controller_id}/Certificates/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post41(
    resource_block_id: str,
    computer_system_id: str,
    storage_id: str,
    storage_controller_id: str,
    request: Request,
    response: Response,
    body: CertificateOnCreate,
) -> Certificate:
    s: ServiceCollection = get_service_collection(CertificateCollection, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Certificate, s.post(**b))


@router.get(
    "/redfish/v1/Storage/{storage_id}/Controllers/{storage_controller_id}/Certificates",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Storage/{storage_id}/Controllers/{storage_controller_id}/Certificates",
    response_model_exclude_none=True,
)
async def get42(
    storage_id: str, storage_controller_id: str, request: Request, response: Response
) -> CertificateCollection:
    s: Service = get_service(CertificateCollection, request)
    b: dict[str, Any] = {
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
        "request": request,
        "response": response,
    }
    m = cast(CertificateCollection, s.get(**b))
    set_link_header(m, response)
    return m


@router.post(
    "/redfish/v1/Storage/{storage_id}/Controllers/{storage_controller_id}/Certificates",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/Storage/{storage_id}/Controllers/{storage_controller_id}/Certificates/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post42(
    storage_id: str,
    storage_controller_id: str,
    request: Request,
    response: Response,
    body: CertificateOnCreate,
) -> Certificate:
    s: ServiceCollection = get_service_collection(CertificateCollection, request)
    b: dict[str, Any] = {
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Certificate, s.post(**b))


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/Controllers/{storage_controller_id}/Certificates",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/Controllers/{storage_controller_id}/Certificates",
    response_model_exclude_none=True,
)
async def get43(
    computer_system_id: str,
    storage_id: str,
    storage_controller_id: str,
    request: Request,
    response: Response,
) -> CertificateCollection:
    s: Service = get_service(CertificateCollection, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
        "request": request,
        "response": response,
    }
    m = cast(CertificateCollection, s.get(**b))
    set_link_header(m, response)
    return m


@router.post(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/Controllers/{storage_controller_id}/Certificates",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/Controllers/{storage_controller_id}/Certificates/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post43(
    computer_system_id: str,
    storage_id: str,
    storage_controller_id: str,
    request: Request,
    response: Response,
    body: CertificateOnCreate,
) -> Certificate:
    s: ServiceCollection = get_service_collection(CertificateCollection, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Certificate, s.post(**b))


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Storage/{storage_id}/Controllers/{storage_controller_id}/Certificates",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Storage/{storage_id}/Controllers/{storage_controller_id}/Certificates",
    response_model_exclude_none=True,
)
async def get44(
    resource_block_id: str,
    storage_id: str,
    storage_controller_id: str,
    request: Request,
    response: Response,
) -> CertificateCollection:
    s: Service = get_service(CertificateCollection, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
        "request": request,
        "response": response,
    }
    m = cast(CertificateCollection, s.get(**b))
    set_link_header(m, response)
    return m


@router.post(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Storage/{storage_id}/Controllers/{storage_controller_id}/Certificates",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Storage/{storage_id}/Controllers/{storage_controller_id}/Certificates/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post44(
    resource_block_id: str,
    storage_id: str,
    storage_controller_id: str,
    request: Request,
    response: Response,
    body: CertificateOnCreate,
) -> Certificate:
    s: ServiceCollection = get_service_collection(CertificateCollection, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Certificate, s.post(**b))


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Storage/{storage_id}/Controllers/{storage_controller_id}/Certificates",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Storage/{storage_id}/Controllers/{storage_controller_id}/Certificates",
    response_model_exclude_none=True,
)
async def get45(
    resource_block_id: str,
    computer_system_id: str,
    storage_id: str,
    storage_controller_id: str,
    request: Request,
    response: Response,
) -> CertificateCollection:
    s: Service = get_service(CertificateCollection, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
        "request": request,
        "response": response,
    }
    m = cast(CertificateCollection, s.get(**b))
    set_link_header(m, response)
    return m


@router.post(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Storage/{storage_id}/Controllers/{storage_controller_id}/Certificates",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Storage/{storage_id}/Controllers/{storage_controller_id}/Certificates/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post45(
    resource_block_id: str,
    computer_system_id: str,
    storage_id: str,
    storage_controller_id: str,
    request: Request,
    response: Response,
    body: CertificateOnCreate,
) -> Certificate:
    s: ServiceCollection = get_service_collection(CertificateCollection, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Certificate, s.post(**b))


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Storage/{storage_id}/Controllers/{storage_controller_id}/Certificates",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Storage/{storage_id}/Controllers/{storage_controller_id}/Certificates",
    response_model_exclude_none=True,
)
async def get46(
    resource_block_id: str,
    storage_id: str,
    storage_controller_id: str,
    request: Request,
    response: Response,
) -> CertificateCollection:
    s: Service = get_service(CertificateCollection, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
        "request": request,
        "response": response,
    }
    m = cast(CertificateCollection, s.get(**b))
    set_link_header(m, response)
    return m


@router.post(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Storage/{storage_id}/Controllers/{storage_controller_id}/Certificates",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Storage/{storage_id}/Controllers/{storage_controller_id}/Certificates/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post46(
    resource_block_id: str,
    storage_id: str,
    storage_controller_id: str,
    request: Request,
    response: Response,
    body: CertificateOnCreate,
) -> Certificate:
    s: ServiceCollection = get_service_collection(CertificateCollection, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Certificate, s.post(**b))


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Storage/{storage_id}/Controllers/{storage_controller_id}/Certificates",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Storage/{storage_id}/Controllers/{storage_controller_id}/Certificates",
    response_model_exclude_none=True,
)
async def get47(
    resource_block_id: str,
    computer_system_id: str,
    storage_id: str,
    storage_controller_id: str,
    request: Request,
    response: Response,
) -> CertificateCollection:
    s: Service = get_service(CertificateCollection, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
        "request": request,
        "response": response,
    }
    m = cast(CertificateCollection, s.get(**b))
    set_link_header(m, response)
    return m


@router.post(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Storage/{storage_id}/Controllers/{storage_controller_id}/Certificates",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Storage/{storage_id}/Controllers/{storage_controller_id}/Certificates/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post47(
    resource_block_id: str,
    computer_system_id: str,
    storage_id: str,
    storage_controller_id: str,
    request: Request,
    response: Response,
    body: CertificateOnCreate,
) -> Certificate:
    s: ServiceCollection = get_service_collection(CertificateCollection, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Certificate, s.post(**b))


@router.get(
    "/redfish/v1/Fabrics/{fabric_id}/Switches/{switch_id}/Certificates",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Fabrics/{fabric_id}/Switches/{switch_id}/Certificates",
    response_model_exclude_none=True,
)
async def get48(
    fabric_id: str, switch_id: str, request: Request, response: Response
) -> CertificateCollection:
    s: Service = get_service(CertificateCollection, request)
    b: dict[str, Any] = {
        "fabric_id": fabric_id,
        "switch_id": switch_id,
        "request": request,
        "response": response,
    }
    m = cast(CertificateCollection, s.get(**b))
    set_link_header(m, response)
    return m


@router.post(
    "/redfish/v1/Fabrics/{fabric_id}/Switches/{switch_id}/Certificates",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/Fabrics/{fabric_id}/Switches/{switch_id}/Certificates/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post48(
    fabric_id: str, switch_id: str, request: Request, response: Response, body: CertificateOnCreate
) -> Certificate:
    s: ServiceCollection = get_service_collection(CertificateCollection, request)
    b: dict[str, Any] = {
        "fabric_id": fabric_id,
        "switch_id": switch_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Certificate, s.post(**b))


@router.get("/redfish/v1/Chassis/{chassis_id}/Certificates", response_model_exclude_none=True)
@router.head("/redfish/v1/Chassis/{chassis_id}/Certificates", response_model_exclude_none=True)
async def get49(chassis_id: str, request: Request, response: Response) -> CertificateCollection:
    s: Service = get_service(CertificateCollection, request)
    b: dict[str, Any] = {"chassis_id": chassis_id, "request": request, "response": response}
    m = cast(CertificateCollection, s.get(**b))
    set_link_header(m, response)
    return m


@router.post("/redfish/v1/Chassis/{chassis_id}/Certificates", response_model_exclude_none=True)
@router.post(
    "/redfish/v1/Chassis/{chassis_id}/Certificates/Members", response_model_exclude_none=True
)
@authenticate
async def post49(
    chassis_id: str, request: Request, response: Response, body: CertificateOnCreate
) -> Certificate:
    s: ServiceCollection = get_service_collection(CertificateCollection, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Certificate, s.post(**b))


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/Drives/{drive_id}/Certificates",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/Drives/{drive_id}/Certificates",
    response_model_exclude_none=True,
)
async def get50(
    computer_system_id: str, storage_id: str, drive_id: str, request: Request, response: Response
) -> CertificateCollection:
    s: Service = get_service(CertificateCollection, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "drive_id": drive_id,
        "request": request,
        "response": response,
    }
    m = cast(CertificateCollection, s.get(**b))
    set_link_header(m, response)
    return m


@router.post(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/Drives/{drive_id}/Certificates",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/Drives/{drive_id}/Certificates/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post50(
    computer_system_id: str,
    storage_id: str,
    drive_id: str,
    request: Request,
    response: Response,
    body: CertificateOnCreate,
) -> Certificate:
    s: ServiceCollection = get_service_collection(CertificateCollection, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "drive_id": drive_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Certificate, s.post(**b))


@router.get(
    "/redfish/v1/Chassis/{chassis_id}/Drives/{drive_id}/Certificates",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Chassis/{chassis_id}/Drives/{drive_id}/Certificates",
    response_model_exclude_none=True,
)
async def get51(
    chassis_id: str, drive_id: str, request: Request, response: Response
) -> CertificateCollection:
    s: Service = get_service(CertificateCollection, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "drive_id": drive_id,
        "request": request,
        "response": response,
    }
    m = cast(CertificateCollection, s.get(**b))
    set_link_header(m, response)
    return m


@router.post(
    "/redfish/v1/Chassis/{chassis_id}/Drives/{drive_id}/Certificates",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/Chassis/{chassis_id}/Drives/{drive_id}/Certificates/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post51(
    chassis_id: str, drive_id: str, request: Request, response: Response, body: CertificateOnCreate
) -> Certificate:
    s: ServiceCollection = get_service_collection(CertificateCollection, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "drive_id": drive_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Certificate, s.post(**b))


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Storage/{storage_id}/Drives/{drive_id}/Certificates",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Storage/{storage_id}/Drives/{drive_id}/Certificates",
    response_model_exclude_none=True,
)
async def get52(
    resource_block_id: str, storage_id: str, drive_id: str, request: Request, response: Response
) -> CertificateCollection:
    s: Service = get_service(CertificateCollection, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "storage_id": storage_id,
        "drive_id": drive_id,
        "request": request,
        "response": response,
    }
    m = cast(CertificateCollection, s.get(**b))
    set_link_header(m, response)
    return m


@router.post(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Storage/{storage_id}/Drives/{drive_id}/Certificates",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Storage/{storage_id}/Drives/{drive_id}/Certificates/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post52(
    resource_block_id: str,
    storage_id: str,
    drive_id: str,
    request: Request,
    response: Response,
    body: CertificateOnCreate,
) -> Certificate:
    s: ServiceCollection = get_service_collection(CertificateCollection, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "storage_id": storage_id,
        "drive_id": drive_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Certificate, s.post(**b))


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Drives/{drive_id}/Certificates",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Drives/{drive_id}/Certificates",
    response_model_exclude_none=True,
)
async def get53(
    resource_block_id: str, drive_id: str, request: Request, response: Response
) -> CertificateCollection:
    s: Service = get_service(CertificateCollection, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "drive_id": drive_id,
        "request": request,
        "response": response,
    }
    m = cast(CertificateCollection, s.get(**b))
    set_link_header(m, response)
    return m


@router.post(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Drives/{drive_id}/Certificates",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Drives/{drive_id}/Certificates/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post53(
    resource_block_id: str,
    drive_id: str,
    request: Request,
    response: Response,
    body: CertificateOnCreate,
) -> Certificate:
    s: ServiceCollection = get_service_collection(CertificateCollection, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "drive_id": drive_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Certificate, s.post(**b))


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Storage/{storage_id}/Drives/{drive_id}/Certificates",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Storage/{storage_id}/Drives/{drive_id}/Certificates",
    response_model_exclude_none=True,
)
async def get54(
    resource_block_id: str,
    computer_system_id: str,
    storage_id: str,
    drive_id: str,
    request: Request,
    response: Response,
) -> CertificateCollection:
    s: Service = get_service(CertificateCollection, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "drive_id": drive_id,
        "request": request,
        "response": response,
    }
    m = cast(CertificateCollection, s.get(**b))
    set_link_header(m, response)
    return m


@router.post(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Storage/{storage_id}/Drives/{drive_id}/Certificates",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Storage/{storage_id}/Drives/{drive_id}/Certificates/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post54(
    resource_block_id: str,
    computer_system_id: str,
    storage_id: str,
    drive_id: str,
    request: Request,
    response: Response,
    body: CertificateOnCreate,
) -> Certificate:
    s: ServiceCollection = get_service_collection(CertificateCollection, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "drive_id": drive_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Certificate, s.post(**b))


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Storage/{storage_id}/Drives/{drive_id}/Certificates",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Storage/{storage_id}/Drives/{drive_id}/Certificates",
    response_model_exclude_none=True,
)
async def get55(
    resource_block_id: str, storage_id: str, drive_id: str, request: Request, response: Response
) -> CertificateCollection:
    s: Service = get_service(CertificateCollection, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "storage_id": storage_id,
        "drive_id": drive_id,
        "request": request,
        "response": response,
    }
    m = cast(CertificateCollection, s.get(**b))
    set_link_header(m, response)
    return m


@router.post(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Storage/{storage_id}/Drives/{drive_id}/Certificates",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Storage/{storage_id}/Drives/{drive_id}/Certificates/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post55(
    resource_block_id: str,
    storage_id: str,
    drive_id: str,
    request: Request,
    response: Response,
    body: CertificateOnCreate,
) -> Certificate:
    s: ServiceCollection = get_service_collection(CertificateCollection, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "storage_id": storage_id,
        "drive_id": drive_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Certificate, s.post(**b))


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Drives/{drive_id}/Certificates",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Drives/{drive_id}/Certificates",
    response_model_exclude_none=True,
)
async def get56(
    resource_block_id: str, drive_id: str, request: Request, response: Response
) -> CertificateCollection:
    s: Service = get_service(CertificateCollection, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "drive_id": drive_id,
        "request": request,
        "response": response,
    }
    m = cast(CertificateCollection, s.get(**b))
    set_link_header(m, response)
    return m


@router.post(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Drives/{drive_id}/Certificates",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Drives/{drive_id}/Certificates/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post56(
    resource_block_id: str,
    drive_id: str,
    request: Request,
    response: Response,
    body: CertificateOnCreate,
) -> Certificate:
    s: ServiceCollection = get_service_collection(CertificateCollection, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "drive_id": drive_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Certificate, s.post(**b))


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Storage/{storage_id}/Drives/{drive_id}/Certificates",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Storage/{storage_id}/Drives/{drive_id}/Certificates",
    response_model_exclude_none=True,
)
async def get57(
    resource_block_id: str,
    computer_system_id: str,
    storage_id: str,
    drive_id: str,
    request: Request,
    response: Response,
) -> CertificateCollection:
    s: Service = get_service(CertificateCollection, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "drive_id": drive_id,
        "request": request,
        "response": response,
    }
    m = cast(CertificateCollection, s.get(**b))
    set_link_header(m, response)
    return m


@router.post(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Storage/{storage_id}/Drives/{drive_id}/Certificates",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Storage/{storage_id}/Drives/{drive_id}/Certificates/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post57(
    resource_block_id: str,
    computer_system_id: str,
    storage_id: str,
    drive_id: str,
    request: Request,
    response: Response,
    body: CertificateOnCreate,
) -> Certificate:
    s: ServiceCollection = get_service_collection(CertificateCollection, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "drive_id": drive_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Certificate, s.post(**b))


@router.get(
    "/redfish/v1/Chassis/{chassis_id}/NetworkAdapters/{network_adapter_id}/Certificates",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Chassis/{chassis_id}/NetworkAdapters/{network_adapter_id}/Certificates",
    response_model_exclude_none=True,
)
async def get58(
    chassis_id: str, network_adapter_id: str, request: Request, response: Response
) -> CertificateCollection:
    s: Service = get_service(CertificateCollection, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "network_adapter_id": network_adapter_id,
        "request": request,
        "response": response,
    }
    m = cast(CertificateCollection, s.get(**b))
    set_link_header(m, response)
    return m


@router.post(
    "/redfish/v1/Chassis/{chassis_id}/NetworkAdapters/{network_adapter_id}/Certificates",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/Chassis/{chassis_id}/NetworkAdapters/{network_adapter_id}/Certificates/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post58(
    chassis_id: str,
    network_adapter_id: str,
    request: Request,
    response: Response,
    body: CertificateOnCreate,
) -> Certificate:
    s: ServiceCollection = get_service_collection(CertificateCollection, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "network_adapter_id": network_adapter_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Certificate, s.post(**b))


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/VirtualMedia/{virtual_media_id}/Certificates",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Systems/{computer_system_id}/VirtualMedia/{virtual_media_id}/Certificates",
    response_model_exclude_none=True,
)
async def get59(
    computer_system_id: str, virtual_media_id: str, request: Request, response: Response
) -> CertificateCollection:
    s: Service = get_service(CertificateCollection, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "virtual_media_id": virtual_media_id,
        "request": request,
        "response": response,
    }
    m = cast(CertificateCollection, s.get(**b))
    set_link_header(m, response)
    return m


@router.post(
    "/redfish/v1/Systems/{computer_system_id}/VirtualMedia/{virtual_media_id}/Certificates",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/Systems/{computer_system_id}/VirtualMedia/{virtual_media_id}/Certificates/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post59(
    computer_system_id: str,
    virtual_media_id: str,
    request: Request,
    response: Response,
    body: CertificateOnCreate,
) -> Certificate:
    s: ServiceCollection = get_service_collection(CertificateCollection, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "virtual_media_id": virtual_media_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Certificate, s.post(**b))


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/VirtualMedia/{virtual_media_id}/ClientCertificates",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Systems/{computer_system_id}/VirtualMedia/{virtual_media_id}/ClientCertificates",
    response_model_exclude_none=True,
)
async def get60(
    computer_system_id: str, virtual_media_id: str, request: Request, response: Response
) -> CertificateCollection:
    s: Service = get_service(CertificateCollection, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "virtual_media_id": virtual_media_id,
        "request": request,
        "response": response,
    }
    m = cast(CertificateCollection, s.get(**b))
    set_link_header(m, response)
    return m


@router.post(
    "/redfish/v1/Systems/{computer_system_id}/VirtualMedia/{virtual_media_id}/ClientCertificates",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/Systems/{computer_system_id}/VirtualMedia/{virtual_media_id}/ClientCertificates/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post60(
    computer_system_id: str,
    virtual_media_id: str,
    request: Request,
    response: Response,
    body: CertificateOnCreate,
) -> Certificate:
    s: ServiceCollection = get_service_collection(CertificateCollection, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "virtual_media_id": virtual_media_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Certificate, s.post(**b))


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/VirtualMedia/{virtual_media_id}/Certificates",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/VirtualMedia/{virtual_media_id}/Certificates",
    response_model_exclude_none=True,
)
async def get61(
    resource_block_id: str,
    computer_system_id: str,
    virtual_media_id: str,
    request: Request,
    response: Response,
) -> CertificateCollection:
    s: Service = get_service(CertificateCollection, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "virtual_media_id": virtual_media_id,
        "request": request,
        "response": response,
    }
    m = cast(CertificateCollection, s.get(**b))
    set_link_header(m, response)
    return m


@router.post(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/VirtualMedia/{virtual_media_id}/Certificates",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/VirtualMedia/{virtual_media_id}/Certificates/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post61(
    resource_block_id: str,
    computer_system_id: str,
    virtual_media_id: str,
    request: Request,
    response: Response,
    body: CertificateOnCreate,
) -> Certificate:
    s: ServiceCollection = get_service_collection(CertificateCollection, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "virtual_media_id": virtual_media_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Certificate, s.post(**b))


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/VirtualMedia/{virtual_media_id}/ClientCertificates",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/VirtualMedia/{virtual_media_id}/ClientCertificates",
    response_model_exclude_none=True,
)
async def get62(
    resource_block_id: str,
    computer_system_id: str,
    virtual_media_id: str,
    request: Request,
    response: Response,
) -> CertificateCollection:
    s: Service = get_service(CertificateCollection, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "virtual_media_id": virtual_media_id,
        "request": request,
        "response": response,
    }
    m = cast(CertificateCollection, s.get(**b))
    set_link_header(m, response)
    return m


@router.post(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/VirtualMedia/{virtual_media_id}/ClientCertificates",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/VirtualMedia/{virtual_media_id}/ClientCertificates/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post62(
    resource_block_id: str,
    computer_system_id: str,
    virtual_media_id: str,
    request: Request,
    response: Response,
    body: CertificateOnCreate,
) -> Certificate:
    s: ServiceCollection = get_service_collection(CertificateCollection, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "virtual_media_id": virtual_media_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Certificate, s.post(**b))


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/VirtualMedia/{virtual_media_id}/Certificates",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/VirtualMedia/{virtual_media_id}/Certificates",
    response_model_exclude_none=True,
)
async def get63(
    resource_block_id: str,
    computer_system_id: str,
    virtual_media_id: str,
    request: Request,
    response: Response,
) -> CertificateCollection:
    s: Service = get_service(CertificateCollection, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "virtual_media_id": virtual_media_id,
        "request": request,
        "response": response,
    }
    m = cast(CertificateCollection, s.get(**b))
    set_link_header(m, response)
    return m


@router.post(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/VirtualMedia/{virtual_media_id}/Certificates",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/VirtualMedia/{virtual_media_id}/Certificates/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post63(
    resource_block_id: str,
    computer_system_id: str,
    virtual_media_id: str,
    request: Request,
    response: Response,
    body: CertificateOnCreate,
) -> Certificate:
    s: ServiceCollection = get_service_collection(CertificateCollection, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "virtual_media_id": virtual_media_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Certificate, s.post(**b))


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/VirtualMedia/{virtual_media_id}/ClientCertificates",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/VirtualMedia/{virtual_media_id}/ClientCertificates",
    response_model_exclude_none=True,
)
async def get64(
    resource_block_id: str,
    computer_system_id: str,
    virtual_media_id: str,
    request: Request,
    response: Response,
) -> CertificateCollection:
    s: Service = get_service(CertificateCollection, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "virtual_media_id": virtual_media_id,
        "request": request,
        "response": response,
    }
    m = cast(CertificateCollection, s.get(**b))
    set_link_header(m, response)
    return m


@router.post(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/VirtualMedia/{virtual_media_id}/ClientCertificates",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/VirtualMedia/{virtual_media_id}/ClientCertificates/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post64(
    resource_block_id: str,
    computer_system_id: str,
    virtual_media_id: str,
    request: Request,
    response: Response,
    body: CertificateOnCreate,
) -> Certificate:
    s: ServiceCollection = get_service_collection(CertificateCollection, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "virtual_media_id": virtual_media_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Certificate, s.post(**b))


@router.get("/redfish/v1/UpdateService/RemoteServerCertificates", response_model_exclude_none=True)
@router.head(
    "/redfish/v1/UpdateService/RemoteServerCertificates", response_model_exclude_none=True
)
async def get65(request: Request, response: Response) -> CertificateCollection:
    s: Service = get_service(CertificateCollection, request)
    b: dict[str, Any] = {"request": request, "response": response}
    m = cast(CertificateCollection, s.get(**b))
    set_link_header(m, response)
    return m


@router.post(
    "/redfish/v1/UpdateService/RemoteServerCertificates", response_model_exclude_none=True
)
@router.post(
    "/redfish/v1/UpdateService/RemoteServerCertificates/Members", response_model_exclude_none=True
)
@authenticate
async def post65(request: Request, response: Response, body: CertificateOnCreate) -> Certificate:
    s: ServiceCollection = get_service_collection(CertificateCollection, request)
    b: dict[str, Any] = {"request": request, "response": response, "body": body}
    return cast(Certificate, s.post(**b))


@router.get("/redfish/v1/UpdateService/ClientCertificates", response_model_exclude_none=True)
@router.head("/redfish/v1/UpdateService/ClientCertificates", response_model_exclude_none=True)
async def get66(request: Request, response: Response) -> CertificateCollection:
    s: Service = get_service(CertificateCollection, request)
    b: dict[str, Any] = {"request": request, "response": response}
    m = cast(CertificateCollection, s.get(**b))
    set_link_header(m, response)
    return m


@router.post("/redfish/v1/UpdateService/ClientCertificates", response_model_exclude_none=True)
@router.post(
    "/redfish/v1/UpdateService/ClientCertificates/Members", response_model_exclude_none=True
)
@authenticate
async def post66(request: Request, response: Response, body: CertificateOnCreate) -> Certificate:
    s: ServiceCollection = get_service_collection(CertificateCollection, request)
    b: dict[str, Any] = {"request": request, "response": response, "body": body}
    return cast(Certificate, s.post(**b))


@router.get("/redfish/v1/Managers/{manager_id}/Certificates", response_model_exclude_none=True)
@router.head("/redfish/v1/Managers/{manager_id}/Certificates", response_model_exclude_none=True)
async def get67(manager_id: str, request: Request, response: Response) -> CertificateCollection:
    s: Service = get_service(CertificateCollection, request)
    b: dict[str, Any] = {"manager_id": manager_id, "request": request, "response": response}
    m = cast(CertificateCollection, s.get(**b))
    set_link_header(m, response)
    return m


@router.post("/redfish/v1/Managers/{manager_id}/Certificates", response_model_exclude_none=True)
@router.post(
    "/redfish/v1/Managers/{manager_id}/Certificates/Members", response_model_exclude_none=True
)
@authenticate
async def post67(
    manager_id: str, request: Request, response: Response, body: CertificateOnCreate
) -> Certificate:
    s: ServiceCollection = get_service_collection(CertificateCollection, request)
    b: dict[str, Any] = {
        "manager_id": manager_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Certificate, s.post(**b))


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/KeyManagement/KMIPCertificates",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Systems/{computer_system_id}/KeyManagement/KMIPCertificates",
    response_model_exclude_none=True,
)
async def get68(
    computer_system_id: str, request: Request, response: Response
) -> CertificateCollection:
    s: Service = get_service(CertificateCollection, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "request": request,
        "response": response,
    }
    m = cast(CertificateCollection, s.get(**b))
    set_link_header(m, response)
    return m


@router.post(
    "/redfish/v1/Systems/{computer_system_id}/KeyManagement/KMIPCertificates",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/Systems/{computer_system_id}/KeyManagement/KMIPCertificates/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post68(
    computer_system_id: str, request: Request, response: Response, body: CertificateOnCreate
) -> Certificate:
    s: ServiceCollection = get_service_collection(CertificateCollection, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Certificate, s.post(**b))


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/KeyManagement/KMIPCertificates",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/KeyManagement/KMIPCertificates",
    response_model_exclude_none=True,
)
async def get69(
    resource_block_id: str, computer_system_id: str, request: Request, response: Response
) -> CertificateCollection:
    s: Service = get_service(CertificateCollection, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "request": request,
        "response": response,
    }
    m = cast(CertificateCollection, s.get(**b))
    set_link_header(m, response)
    return m


@router.post(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/KeyManagement/KMIPCertificates",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/KeyManagement/KMIPCertificates/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post69(
    resource_block_id: str,
    computer_system_id: str,
    request: Request,
    response: Response,
    body: CertificateOnCreate,
) -> Certificate:
    s: ServiceCollection = get_service_collection(CertificateCollection, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Certificate, s.post(**b))


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/KeyManagement/KMIPCertificates",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/KeyManagement/KMIPCertificates",
    response_model_exclude_none=True,
)
async def get70(
    resource_block_id: str, computer_system_id: str, request: Request, response: Response
) -> CertificateCollection:
    s: Service = get_service(CertificateCollection, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "request": request,
        "response": response,
    }
    m = cast(CertificateCollection, s.get(**b))
    set_link_header(m, response)
    return m


@router.post(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/KeyManagement/KMIPCertificates",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/KeyManagement/KMIPCertificates/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post70(
    resource_block_id: str,
    computer_system_id: str,
    request: Request,
    response: Response,
    body: CertificateOnCreate,
) -> Certificate:
    s: ServiceCollection = get_service_collection(CertificateCollection, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Certificate, s.post(**b))


@router.get(
    "/redfish/v1/Managers/{manager_id}/SecurityPolicy/SPDM/TrustedCertificates",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Managers/{manager_id}/SecurityPolicy/SPDM/TrustedCertificates",
    response_model_exclude_none=True,
)
async def get71(manager_id: str, request: Request, response: Response) -> CertificateCollection:
    s: Service = get_service(CertificateCollection, request)
    b: dict[str, Any] = {"manager_id": manager_id, "request": request, "response": response}
    m = cast(CertificateCollection, s.get(**b))
    set_link_header(m, response)
    return m


@router.post(
    "/redfish/v1/Managers/{manager_id}/SecurityPolicy/SPDM/TrustedCertificates",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/Managers/{manager_id}/SecurityPolicy/SPDM/TrustedCertificates/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post71(
    manager_id: str, request: Request, response: Response, body: CertificateOnCreate
) -> Certificate:
    s: ServiceCollection = get_service_collection(CertificateCollection, request)
    b: dict[str, Any] = {
        "manager_id": manager_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Certificate, s.post(**b))


@router.get(
    "/redfish/v1/Managers/{manager_id}/SecurityPolicy/SPDM/RevokedCertificates",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Managers/{manager_id}/SecurityPolicy/SPDM/RevokedCertificates",
    response_model_exclude_none=True,
)
async def get72(manager_id: str, request: Request, response: Response) -> CertificateCollection:
    s: Service = get_service(CertificateCollection, request)
    b: dict[str, Any] = {"manager_id": manager_id, "request": request, "response": response}
    m = cast(CertificateCollection, s.get(**b))
    set_link_header(m, response)
    return m


@router.post(
    "/redfish/v1/Managers/{manager_id}/SecurityPolicy/SPDM/RevokedCertificates",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/Managers/{manager_id}/SecurityPolicy/SPDM/RevokedCertificates/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post72(
    manager_id: str, request: Request, response: Response, body: CertificateOnCreate
) -> Certificate:
    s: ServiceCollection = get_service_collection(CertificateCollection, request)
    b: dict[str, Any] = {
        "manager_id": manager_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Certificate, s.post(**b))


@router.get(
    "/redfish/v1/Managers/{manager_id}/SecurityPolicy/TLS/Client/TrustedCertificates",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Managers/{manager_id}/SecurityPolicy/TLS/Client/TrustedCertificates",
    response_model_exclude_none=True,
)
async def get73(manager_id: str, request: Request, response: Response) -> CertificateCollection:
    s: Service = get_service(CertificateCollection, request)
    b: dict[str, Any] = {"manager_id": manager_id, "request": request, "response": response}
    m = cast(CertificateCollection, s.get(**b))
    set_link_header(m, response)
    return m


@router.post(
    "/redfish/v1/Managers/{manager_id}/SecurityPolicy/TLS/Client/TrustedCertificates",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/Managers/{manager_id}/SecurityPolicy/TLS/Client/TrustedCertificates/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post73(
    manager_id: str, request: Request, response: Response, body: CertificateOnCreate
) -> Certificate:
    s: ServiceCollection = get_service_collection(CertificateCollection, request)
    b: dict[str, Any] = {
        "manager_id": manager_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Certificate, s.post(**b))


@router.get(
    "/redfish/v1/Managers/{manager_id}/SecurityPolicy/TLS/Client/RevokedCertificates",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Managers/{manager_id}/SecurityPolicy/TLS/Client/RevokedCertificates",
    response_model_exclude_none=True,
)
async def get74(manager_id: str, request: Request, response: Response) -> CertificateCollection:
    s: Service = get_service(CertificateCollection, request)
    b: dict[str, Any] = {"manager_id": manager_id, "request": request, "response": response}
    m = cast(CertificateCollection, s.get(**b))
    set_link_header(m, response)
    return m


@router.post(
    "/redfish/v1/Managers/{manager_id}/SecurityPolicy/TLS/Client/RevokedCertificates",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/Managers/{manager_id}/SecurityPolicy/TLS/Client/RevokedCertificates/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post74(
    manager_id: str, request: Request, response: Response, body: CertificateOnCreate
) -> Certificate:
    s: ServiceCollection = get_service_collection(CertificateCollection, request)
    b: dict[str, Any] = {
        "manager_id": manager_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Certificate, s.post(**b))


@router.get(
    "/redfish/v1/Managers/{manager_id}/SecurityPolicy/TLS/Server/TrustedCertificates",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Managers/{manager_id}/SecurityPolicy/TLS/Server/TrustedCertificates",
    response_model_exclude_none=True,
)
async def get75(manager_id: str, request: Request, response: Response) -> CertificateCollection:
    s: Service = get_service(CertificateCollection, request)
    b: dict[str, Any] = {"manager_id": manager_id, "request": request, "response": response}
    m = cast(CertificateCollection, s.get(**b))
    set_link_header(m, response)
    return m


@router.post(
    "/redfish/v1/Managers/{manager_id}/SecurityPolicy/TLS/Server/TrustedCertificates",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/Managers/{manager_id}/SecurityPolicy/TLS/Server/TrustedCertificates/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post75(
    manager_id: str, request: Request, response: Response, body: CertificateOnCreate
) -> Certificate:
    s: ServiceCollection = get_service_collection(CertificateCollection, request)
    b: dict[str, Any] = {
        "manager_id": manager_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Certificate, s.post(**b))


@router.get(
    "/redfish/v1/Managers/{manager_id}/SecurityPolicy/TLS/Server/RevokedCertificates",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Managers/{manager_id}/SecurityPolicy/TLS/Server/RevokedCertificates",
    response_model_exclude_none=True,
)
async def get76(manager_id: str, request: Request, response: Response) -> CertificateCollection:
    s: Service = get_service(CertificateCollection, request)
    b: dict[str, Any] = {"manager_id": manager_id, "request": request, "response": response}
    m = cast(CertificateCollection, s.get(**b))
    set_link_header(m, response)
    return m


@router.post(
    "/redfish/v1/Managers/{manager_id}/SecurityPolicy/TLS/Server/RevokedCertificates",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/Managers/{manager_id}/SecurityPolicy/TLS/Server/RevokedCertificates/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post76(
    manager_id: str, request: Request, response: Response, body: CertificateOnCreate
) -> Certificate:
    s: ServiceCollection = get_service_collection(CertificateCollection, request)
    b: dict[str, Any] = {
        "manager_id": manager_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Certificate, s.post(**b))


@router.get(
    "/redfish/v1/Chassis/{chassis_id}/TrustedComponents/{trusted_component_id}/Certificates",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Chassis/{chassis_id}/TrustedComponents/{trusted_component_id}/Certificates",
    response_model_exclude_none=True,
)
async def get77(
    chassis_id: str, trusted_component_id: str, request: Request, response: Response
) -> CertificateCollection:
    s: Service = get_service(CertificateCollection, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "trusted_component_id": trusted_component_id,
        "request": request,
        "response": response,
    }
    m = cast(CertificateCollection, s.get(**b))
    set_link_header(m, response)
    return m


@router.post(
    "/redfish/v1/Chassis/{chassis_id}/TrustedComponents/{trusted_component_id}/Certificates",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/Chassis/{chassis_id}/TrustedComponents/{trusted_component_id}/Certificates/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post77(
    chassis_id: str,
    trusted_component_id: str,
    request: Request,
    response: Response,
    body: CertificateOnCreate,
) -> Certificate:
    s: ServiceCollection = get_service_collection(CertificateCollection, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "trusted_component_id": trusted_component_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Certificate, s.post(**b))


@router.get(
    "/redfish/v1/AccountService/OutboundConnections/{outbound_connection_id}/Certificates",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/AccountService/OutboundConnections/{outbound_connection_id}/Certificates",
    response_model_exclude_none=True,
)
async def get78(
    outbound_connection_id: str, request: Request, response: Response
) -> CertificateCollection:
    s: Service = get_service(CertificateCollection, request)
    b: dict[str, Any] = {
        "outbound_connection_id": outbound_connection_id,
        "request": request,
        "response": response,
    }
    m = cast(CertificateCollection, s.get(**b))
    set_link_header(m, response)
    return m


@router.post(
    "/redfish/v1/AccountService/OutboundConnections/{outbound_connection_id}/Certificates",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/AccountService/OutboundConnections/{outbound_connection_id}/Certificates/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post78(
    outbound_connection_id: str, request: Request, response: Response, body: CertificateOnCreate
) -> Certificate:
    s: ServiceCollection = get_service_collection(CertificateCollection, request)
    b: dict[str, Any] = {
        "outbound_connection_id": outbound_connection_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Certificate, s.post(**b))


@router.get(
    "/redfish/v1/AccountService/OutboundConnections/{outbound_connection_id}/ClientCertificates",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/AccountService/OutboundConnections/{outbound_connection_id}/ClientCertificates",
    response_model_exclude_none=True,
)
async def get79(
    outbound_connection_id: str, request: Request, response: Response
) -> CertificateCollection:
    s: Service = get_service(CertificateCollection, request)
    b: dict[str, Any] = {
        "outbound_connection_id": outbound_connection_id,
        "request": request,
        "response": response,
    }
    m = cast(CertificateCollection, s.get(**b))
    set_link_header(m, response)
    return m


@router.post(
    "/redfish/v1/AccountService/OutboundConnections/{outbound_connection_id}/ClientCertificates",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/AccountService/OutboundConnections/{outbound_connection_id}/ClientCertificates/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post79(
    outbound_connection_id: str, request: Request, response: Response, body: CertificateOnCreate
) -> Certificate:
    s: ServiceCollection = get_service_collection(CertificateCollection, request)
    b: dict[str, Any] = {
        "outbound_connection_id": outbound_connection_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Certificate, s.post(**b))


@router.get(
    "/redfish/v1/Chassis/{chassis_id}/PowerSubsystem/PowerSupplies/{power_supply_id}/Certificates",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Chassis/{chassis_id}/PowerSubsystem/PowerSupplies/{power_supply_id}/Certificates",
    response_model_exclude_none=True,
)
async def get80(
    chassis_id: str, power_supply_id: str, request: Request, response: Response
) -> CertificateCollection:
    s: Service = get_service(CertificateCollection, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "power_supply_id": power_supply_id,
        "request": request,
        "response": response,
    }
    m = cast(CertificateCollection, s.get(**b))
    set_link_header(m, response)
    return m


@router.post(
    "/redfish/v1/Chassis/{chassis_id}/PowerSubsystem/PowerSupplies/{power_supply_id}/Certificates",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/Chassis/{chassis_id}/PowerSubsystem/PowerSupplies/{power_supply_id}/Certificates/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post80(
    chassis_id: str,
    power_supply_id: str,
    request: Request,
    response: Response,
    body: CertificateOnCreate,
) -> Certificate:
    s: ServiceCollection = get_service_collection(CertificateCollection, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "power_supply_id": power_supply_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Certificate, s.post(**b))
