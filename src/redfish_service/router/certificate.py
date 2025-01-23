from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.certificate import (
    Certificate,
    CertificateOnUpdate,
    RekeyRequest,
    RenewRequest,
)
from ..model.redfish_error import RedfishError
from ..service import Service
from ..util import get_service, set_link_header

router = APIRouter()


@router.delete(
    "/redfish/v1/AccountService/Accounts/{manager_account_id}/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete1(
    manager_account_id: str, certificate_id: str, request: Request, response: Response
) -> None:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "manager_account_id": manager_account_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
    }
    return s.delete(**b)


@router.get(
    "/redfish/v1/AccountService/Accounts/{manager_account_id}/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/AccountService/Accounts/{manager_account_id}/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
async def get1(
    manager_account_id: str, certificate_id: str, request: Request, response: Response
) -> Certificate:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "manager_account_id": manager_account_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
    }
    m = cast(Certificate, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/AccountService/Accounts/{manager_account_id}/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch1(
    manager_account_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
    body: CertificateOnUpdate,
) -> Certificate:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "manager_account_id": manager_account_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Certificate, s.patch(**b))


@router.post(
    "/redfish/v1/AccountService/Accounts/{manager_account_id}/Certificates/{certificate_id}/Actions/Certificate.Rekey",
    response_model_exclude_none=True,
)
@authenticate
async def rekey1(
    manager_account_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
    body: RekeyRequest,
) -> RedfishError:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "manager_account_id": manager_account_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Rekey",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/AccountService/Accounts/{manager_account_id}/Certificates/{certificate_id}/Actions/Certificate.Renew",
    response_model_exclude_none=True,
)
@authenticate
async def renew1(
    manager_account_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
    body: RenewRequest,
) -> RedfishError:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "manager_account_id": manager_account_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Renew",
    }
    return s.action(**b)


@router.delete(
    "/redfish/v1/AccountService/ActiveDirectory/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete2(certificate_id: str, request: Request, response: Response) -> None:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
    }
    return s.delete(**b)


@router.get(
    "/redfish/v1/AccountService/ActiveDirectory/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/AccountService/ActiveDirectory/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
async def get2(certificate_id: str, request: Request, response: Response) -> Certificate:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
    }
    m = cast(Certificate, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/AccountService/ActiveDirectory/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch2(
    certificate_id: str, request: Request, response: Response, body: CertificateOnUpdate
) -> Certificate:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Certificate, s.patch(**b))


@router.post(
    "/redfish/v1/AccountService/ActiveDirectory/Certificates/{certificate_id}/Actions/Certificate.Rekey",
    response_model_exclude_none=True,
)
@authenticate
async def rekey2(
    certificate_id: str, request: Request, response: Response, body: RekeyRequest
) -> RedfishError:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Rekey",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/AccountService/ActiveDirectory/Certificates/{certificate_id}/Actions/Certificate.Renew",
    response_model_exclude_none=True,
)
@authenticate
async def renew2(
    certificate_id: str, request: Request, response: Response, body: RenewRequest
) -> RedfishError:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Renew",
    }
    return s.action(**b)


@router.delete(
    "/redfish/v1/AccountService/LDAP/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete3(certificate_id: str, request: Request, response: Response) -> None:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
    }
    return s.delete(**b)


@router.get(
    "/redfish/v1/AccountService/LDAP/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/AccountService/LDAP/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
async def get3(certificate_id: str, request: Request, response: Response) -> Certificate:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
    }
    m = cast(Certificate, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/AccountService/LDAP/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch3(
    certificate_id: str, request: Request, response: Response, body: CertificateOnUpdate
) -> Certificate:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Certificate, s.patch(**b))


@router.post(
    "/redfish/v1/AccountService/LDAP/Certificates/{certificate_id}/Actions/Certificate.Rekey",
    response_model_exclude_none=True,
)
@authenticate
async def rekey3(
    certificate_id: str, request: Request, response: Response, body: RekeyRequest
) -> RedfishError:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Rekey",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/AccountService/LDAP/Certificates/{certificate_id}/Actions/Certificate.Renew",
    response_model_exclude_none=True,
)
@authenticate
async def renew3(
    certificate_id: str, request: Request, response: Response, body: RenewRequest
) -> RedfishError:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Renew",
    }
    return s.action(**b)


@router.delete(
    "/redfish/v1/AccountService/ExternalAccountProviders/{external_account_provider_id}/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete4(
    external_account_provider_id: str, certificate_id: str, request: Request, response: Response
) -> None:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "external_account_provider_id": external_account_provider_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
    }
    return s.delete(**b)


@router.get(
    "/redfish/v1/AccountService/ExternalAccountProviders/{external_account_provider_id}/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/AccountService/ExternalAccountProviders/{external_account_provider_id}/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
async def get4(
    external_account_provider_id: str, certificate_id: str, request: Request, response: Response
) -> Certificate:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "external_account_provider_id": external_account_provider_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
    }
    m = cast(Certificate, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/AccountService/ExternalAccountProviders/{external_account_provider_id}/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch4(
    external_account_provider_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
    body: CertificateOnUpdate,
) -> Certificate:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "external_account_provider_id": external_account_provider_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Certificate, s.patch(**b))


@router.post(
    "/redfish/v1/AccountService/ExternalAccountProviders/{external_account_provider_id}/Certificates/{certificate_id}/Actions/Certificate.Rekey",
    response_model_exclude_none=True,
)
@authenticate
async def rekey4(
    external_account_provider_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
    body: RekeyRequest,
) -> RedfishError:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "external_account_provider_id": external_account_provider_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Rekey",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/AccountService/ExternalAccountProviders/{external_account_provider_id}/Certificates/{certificate_id}/Actions/Certificate.Renew",
    response_model_exclude_none=True,
)
@authenticate
async def renew4(
    external_account_provider_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
    body: RenewRequest,
) -> RedfishError:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "external_account_provider_id": external_account_provider_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Renew",
    }
    return s.action(**b)


@router.delete(
    "/redfish/v1/AccountService/MultiFactorAuth/ClientCertificate/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete5(certificate_id: str, request: Request, response: Response) -> None:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
    }
    return s.delete(**b)


@router.get(
    "/redfish/v1/AccountService/MultiFactorAuth/ClientCertificate/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/AccountService/MultiFactorAuth/ClientCertificate/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
async def get5(certificate_id: str, request: Request, response: Response) -> Certificate:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
    }
    m = cast(Certificate, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/AccountService/MultiFactorAuth/ClientCertificate/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch5(
    certificate_id: str, request: Request, response: Response, body: CertificateOnUpdate
) -> Certificate:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Certificate, s.patch(**b))


@router.post(
    "/redfish/v1/AccountService/MultiFactorAuth/ClientCertificate/Certificates/{certificate_id}/Actions/Certificate.Rekey",
    response_model_exclude_none=True,
)
@authenticate
async def rekey5(
    certificate_id: str, request: Request, response: Response, body: RekeyRequest
) -> RedfishError:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Rekey",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/AccountService/MultiFactorAuth/ClientCertificate/Certificates/{certificate_id}/Actions/Certificate.Renew",
    response_model_exclude_none=True,
)
@authenticate
async def renew5(
    certificate_id: str, request: Request, response: Response, body: RenewRequest
) -> RedfishError:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Renew",
    }
    return s.action(**b)


@router.delete(
    "/redfish/v1/AccountService/MultiFactorAuth/SecurID/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete6(certificate_id: str, request: Request, response: Response) -> None:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
    }
    return s.delete(**b)


@router.get(
    "/redfish/v1/AccountService/MultiFactorAuth/SecurID/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/AccountService/MultiFactorAuth/SecurID/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
async def get6(certificate_id: str, request: Request, response: Response) -> Certificate:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
    }
    m = cast(Certificate, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/AccountService/MultiFactorAuth/SecurID/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch6(
    certificate_id: str, request: Request, response: Response, body: CertificateOnUpdate
) -> Certificate:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Certificate, s.patch(**b))


@router.post(
    "/redfish/v1/AccountService/MultiFactorAuth/SecurID/Certificates/{certificate_id}/Actions/Certificate.Rekey",
    response_model_exclude_none=True,
)
@authenticate
async def rekey6(
    certificate_id: str, request: Request, response: Response, body: RekeyRequest
) -> RedfishError:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Rekey",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/AccountService/MultiFactorAuth/SecurID/Certificates/{certificate_id}/Actions/Certificate.Renew",
    response_model_exclude_none=True,
)
@authenticate
async def renew6(
    certificate_id: str, request: Request, response: Response, body: RenewRequest
) -> RedfishError:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Renew",
    }
    return s.action(**b)


@router.delete(
    "/redfish/v1/Managers/{manager_id}/RemoteAccountService/Accounts/{manager_account_id}/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete7(
    manager_id: str,
    manager_account_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
) -> None:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "manager_id": manager_id,
        "manager_account_id": manager_account_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
    }
    return s.delete(**b)


@router.get(
    "/redfish/v1/Managers/{manager_id}/RemoteAccountService/Accounts/{manager_account_id}/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Managers/{manager_id}/RemoteAccountService/Accounts/{manager_account_id}/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
async def get7(
    manager_id: str,
    manager_account_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
) -> Certificate:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "manager_id": manager_id,
        "manager_account_id": manager_account_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
    }
    m = cast(Certificate, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/Managers/{manager_id}/RemoteAccountService/Accounts/{manager_account_id}/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch7(
    manager_id: str,
    manager_account_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
    body: CertificateOnUpdate,
) -> Certificate:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "manager_id": manager_id,
        "manager_account_id": manager_account_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Certificate, s.patch(**b))


@router.post(
    "/redfish/v1/Managers/{manager_id}/RemoteAccountService/Accounts/{manager_account_id}/Certificates/{certificate_id}/Actions/Certificate.Rekey",
    response_model_exclude_none=True,
)
@authenticate
async def rekey7(
    manager_id: str,
    manager_account_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
    body: RekeyRequest,
) -> RedfishError:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "manager_id": manager_id,
        "manager_account_id": manager_account_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Rekey",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Managers/{manager_id}/RemoteAccountService/Accounts/{manager_account_id}/Certificates/{certificate_id}/Actions/Certificate.Renew",
    response_model_exclude_none=True,
)
@authenticate
async def renew7(
    manager_id: str,
    manager_account_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
    body: RenewRequest,
) -> RedfishError:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "manager_id": manager_id,
        "manager_account_id": manager_account_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Renew",
    }
    return s.action(**b)


@router.delete(
    "/redfish/v1/Managers/{manager_id}/RemoteAccountService/ActiveDirectory/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete8(
    manager_id: str, certificate_id: str, request: Request, response: Response
) -> None:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "manager_id": manager_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
    }
    return s.delete(**b)


@router.get(
    "/redfish/v1/Managers/{manager_id}/RemoteAccountService/ActiveDirectory/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Managers/{manager_id}/RemoteAccountService/ActiveDirectory/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
async def get8(
    manager_id: str, certificate_id: str, request: Request, response: Response
) -> Certificate:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "manager_id": manager_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
    }
    m = cast(Certificate, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/Managers/{manager_id}/RemoteAccountService/ActiveDirectory/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch8(
    manager_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
    body: CertificateOnUpdate,
) -> Certificate:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "manager_id": manager_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Certificate, s.patch(**b))


@router.post(
    "/redfish/v1/Managers/{manager_id}/RemoteAccountService/ActiveDirectory/Certificates/{certificate_id}/Actions/Certificate.Rekey",
    response_model_exclude_none=True,
)
@authenticate
async def rekey8(
    manager_id: str, certificate_id: str, request: Request, response: Response, body: RekeyRequest
) -> RedfishError:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "manager_id": manager_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Rekey",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Managers/{manager_id}/RemoteAccountService/ActiveDirectory/Certificates/{certificate_id}/Actions/Certificate.Renew",
    response_model_exclude_none=True,
)
@authenticate
async def renew8(
    manager_id: str, certificate_id: str, request: Request, response: Response, body: RenewRequest
) -> RedfishError:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "manager_id": manager_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Renew",
    }
    return s.action(**b)


@router.delete(
    "/redfish/v1/Managers/{manager_id}/RemoteAccountService/LDAP/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete9(
    manager_id: str, certificate_id: str, request: Request, response: Response
) -> None:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "manager_id": manager_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
    }
    return s.delete(**b)


@router.get(
    "/redfish/v1/Managers/{manager_id}/RemoteAccountService/LDAP/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Managers/{manager_id}/RemoteAccountService/LDAP/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
async def get9(
    manager_id: str, certificate_id: str, request: Request, response: Response
) -> Certificate:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "manager_id": manager_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
    }
    m = cast(Certificate, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/Managers/{manager_id}/RemoteAccountService/LDAP/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch9(
    manager_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
    body: CertificateOnUpdate,
) -> Certificate:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "manager_id": manager_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Certificate, s.patch(**b))


@router.post(
    "/redfish/v1/Managers/{manager_id}/RemoteAccountService/LDAP/Certificates/{certificate_id}/Actions/Certificate.Rekey",
    response_model_exclude_none=True,
)
@authenticate
async def rekey9(
    manager_id: str, certificate_id: str, request: Request, response: Response, body: RekeyRequest
) -> RedfishError:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "manager_id": manager_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Rekey",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Managers/{manager_id}/RemoteAccountService/LDAP/Certificates/{certificate_id}/Actions/Certificate.Renew",
    response_model_exclude_none=True,
)
@authenticate
async def renew9(
    manager_id: str, certificate_id: str, request: Request, response: Response, body: RenewRequest
) -> RedfishError:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "manager_id": manager_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Renew",
    }
    return s.action(**b)


@router.delete(
    "/redfish/v1/Managers/{manager_id}/RemoteAccountService/ExternalAccountProviders/{external_account_provider_id}/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete10(
    manager_id: str,
    external_account_provider_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
) -> None:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "manager_id": manager_id,
        "external_account_provider_id": external_account_provider_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
    }
    return s.delete(**b)


@router.get(
    "/redfish/v1/Managers/{manager_id}/RemoteAccountService/ExternalAccountProviders/{external_account_provider_id}/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Managers/{manager_id}/RemoteAccountService/ExternalAccountProviders/{external_account_provider_id}/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
async def get10(
    manager_id: str,
    external_account_provider_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
) -> Certificate:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "manager_id": manager_id,
        "external_account_provider_id": external_account_provider_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
    }
    m = cast(Certificate, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/Managers/{manager_id}/RemoteAccountService/ExternalAccountProviders/{external_account_provider_id}/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch10(
    manager_id: str,
    external_account_provider_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
    body: CertificateOnUpdate,
) -> Certificate:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "manager_id": manager_id,
        "external_account_provider_id": external_account_provider_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Certificate, s.patch(**b))


@router.post(
    "/redfish/v1/Managers/{manager_id}/RemoteAccountService/ExternalAccountProviders/{external_account_provider_id}/Certificates/{certificate_id}/Actions/Certificate.Rekey",
    response_model_exclude_none=True,
)
@authenticate
async def rekey10(
    manager_id: str,
    external_account_provider_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
    body: RekeyRequest,
) -> RedfishError:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "manager_id": manager_id,
        "external_account_provider_id": external_account_provider_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Rekey",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Managers/{manager_id}/RemoteAccountService/ExternalAccountProviders/{external_account_provider_id}/Certificates/{certificate_id}/Actions/Certificate.Renew",
    response_model_exclude_none=True,
)
@authenticate
async def renew10(
    manager_id: str,
    external_account_provider_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
    body: RenewRequest,
) -> RedfishError:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "manager_id": manager_id,
        "external_account_provider_id": external_account_provider_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Renew",
    }
    return s.action(**b)


@router.delete(
    "/redfish/v1/Managers/{manager_id}/RemoteAccountService/MultiFactorAuth/ClientCertificate/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete11(
    manager_id: str, certificate_id: str, request: Request, response: Response
) -> None:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "manager_id": manager_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
    }
    return s.delete(**b)


@router.get(
    "/redfish/v1/Managers/{manager_id}/RemoteAccountService/MultiFactorAuth/ClientCertificate/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Managers/{manager_id}/RemoteAccountService/MultiFactorAuth/ClientCertificate/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
async def get11(
    manager_id: str, certificate_id: str, request: Request, response: Response
) -> Certificate:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "manager_id": manager_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
    }
    m = cast(Certificate, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/Managers/{manager_id}/RemoteAccountService/MultiFactorAuth/ClientCertificate/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch11(
    manager_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
    body: CertificateOnUpdate,
) -> Certificate:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "manager_id": manager_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Certificate, s.patch(**b))


@router.post(
    "/redfish/v1/Managers/{manager_id}/RemoteAccountService/MultiFactorAuth/ClientCertificate/Certificates/{certificate_id}/Actions/Certificate.Rekey",
    response_model_exclude_none=True,
)
@authenticate
async def rekey11(
    manager_id: str, certificate_id: str, request: Request, response: Response, body: RekeyRequest
) -> RedfishError:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "manager_id": manager_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Rekey",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Managers/{manager_id}/RemoteAccountService/MultiFactorAuth/ClientCertificate/Certificates/{certificate_id}/Actions/Certificate.Renew",
    response_model_exclude_none=True,
)
@authenticate
async def renew11(
    manager_id: str, certificate_id: str, request: Request, response: Response, body: RenewRequest
) -> RedfishError:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "manager_id": manager_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Renew",
    }
    return s.action(**b)


@router.delete(
    "/redfish/v1/Managers/{manager_id}/RemoteAccountService/MultiFactorAuth/SecurID/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete12(
    manager_id: str, certificate_id: str, request: Request, response: Response
) -> None:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "manager_id": manager_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
    }
    return s.delete(**b)


@router.get(
    "/redfish/v1/Managers/{manager_id}/RemoteAccountService/MultiFactorAuth/SecurID/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Managers/{manager_id}/RemoteAccountService/MultiFactorAuth/SecurID/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
async def get12(
    manager_id: str, certificate_id: str, request: Request, response: Response
) -> Certificate:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "manager_id": manager_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
    }
    m = cast(Certificate, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/Managers/{manager_id}/RemoteAccountService/MultiFactorAuth/SecurID/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch12(
    manager_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
    body: CertificateOnUpdate,
) -> Certificate:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "manager_id": manager_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Certificate, s.patch(**b))


@router.post(
    "/redfish/v1/Managers/{manager_id}/RemoteAccountService/MultiFactorAuth/SecurID/Certificates/{certificate_id}/Actions/Certificate.Rekey",
    response_model_exclude_none=True,
)
@authenticate
async def rekey12(
    manager_id: str, certificate_id: str, request: Request, response: Response, body: RekeyRequest
) -> RedfishError:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "manager_id": manager_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Rekey",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Managers/{manager_id}/RemoteAccountService/MultiFactorAuth/SecurID/Certificates/{certificate_id}/Actions/Certificate.Renew",
    response_model_exclude_none=True,
)
@authenticate
async def renew12(
    manager_id: str, certificate_id: str, request: Request, response: Response, body: RenewRequest
) -> RedfishError:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "manager_id": manager_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Renew",
    }
    return s.action(**b)


@router.delete(
    "/redfish/v1/Managers/{manager_id}/NetworkProtocol/HTTPS/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete13(
    manager_id: str, certificate_id: str, request: Request, response: Response
) -> None:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "manager_id": manager_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
    }
    return s.delete(**b)


@router.get(
    "/redfish/v1/Managers/{manager_id}/NetworkProtocol/HTTPS/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Managers/{manager_id}/NetworkProtocol/HTTPS/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
async def get13(
    manager_id: str, certificate_id: str, request: Request, response: Response
) -> Certificate:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "manager_id": manager_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
    }
    m = cast(Certificate, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/Managers/{manager_id}/NetworkProtocol/HTTPS/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch13(
    manager_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
    body: CertificateOnUpdate,
) -> Certificate:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "manager_id": manager_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Certificate, s.patch(**b))


@router.post(
    "/redfish/v1/Managers/{manager_id}/NetworkProtocol/HTTPS/Certificates/{certificate_id}/Actions/Certificate.Rekey",
    response_model_exclude_none=True,
)
@authenticate
async def rekey13(
    manager_id: str, certificate_id: str, request: Request, response: Response, body: RekeyRequest
) -> RedfishError:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "manager_id": manager_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Rekey",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Managers/{manager_id}/NetworkProtocol/HTTPS/Certificates/{certificate_id}/Actions/Certificate.Renew",
    response_model_exclude_none=True,
)
@authenticate
async def renew13(
    manager_id: str, certificate_id: str, request: Request, response: Response, body: RenewRequest
) -> RedfishError:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "manager_id": manager_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Renew",
    }
    return s.action(**b)


@router.delete(
    "/redfish/v1/Systems/{computer_system_id}/Boot/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete14(
    computer_system_id: str, certificate_id: str, request: Request, response: Response
) -> None:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
    }
    return s.delete(**b)


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/Boot/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Systems/{computer_system_id}/Boot/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
async def get14(
    computer_system_id: str, certificate_id: str, request: Request, response: Response
) -> Certificate:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
    }
    m = cast(Certificate, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/Systems/{computer_system_id}/Boot/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch14(
    computer_system_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
    body: CertificateOnUpdate,
) -> Certificate:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Certificate, s.patch(**b))


@router.post(
    "/redfish/v1/Systems/{computer_system_id}/Boot/Certificates/{certificate_id}/Actions/Certificate.Rekey",
    response_model_exclude_none=True,
)
@authenticate
async def rekey14(
    computer_system_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
    body: RekeyRequest,
) -> RedfishError:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Rekey",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Systems/{computer_system_id}/Boot/Certificates/{certificate_id}/Actions/Certificate.Renew",
    response_model_exclude_none=True,
)
@authenticate
async def renew14(
    computer_system_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
    body: RenewRequest,
) -> RedfishError:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Renew",
    }
    return s.action(**b)


@router.delete(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Boot/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete15(
    resource_block_id: str,
    computer_system_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
) -> None:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
    }
    return s.delete(**b)


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Boot/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Boot/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
async def get15(
    resource_block_id: str,
    computer_system_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
) -> Certificate:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
    }
    m = cast(Certificate, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Boot/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch15(
    resource_block_id: str,
    computer_system_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
    body: CertificateOnUpdate,
) -> Certificate:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Certificate, s.patch(**b))


@router.post(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Boot/Certificates/{certificate_id}/Actions/Certificate.Rekey",
    response_model_exclude_none=True,
)
@authenticate
async def rekey15(
    resource_block_id: str,
    computer_system_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
    body: RekeyRequest,
) -> RedfishError:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Rekey",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Boot/Certificates/{certificate_id}/Actions/Certificate.Renew",
    response_model_exclude_none=True,
)
@authenticate
async def renew15(
    resource_block_id: str,
    computer_system_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
    body: RenewRequest,
) -> RedfishError:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Renew",
    }
    return s.action(**b)


@router.delete(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Boot/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete16(
    resource_block_id: str,
    computer_system_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
) -> None:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
    }
    return s.delete(**b)


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Boot/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Boot/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
async def get16(
    resource_block_id: str,
    computer_system_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
) -> Certificate:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
    }
    m = cast(Certificate, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Boot/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch16(
    resource_block_id: str,
    computer_system_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
    body: CertificateOnUpdate,
) -> Certificate:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Certificate, s.patch(**b))


@router.post(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Boot/Certificates/{certificate_id}/Actions/Certificate.Rekey",
    response_model_exclude_none=True,
)
@authenticate
async def rekey16(
    resource_block_id: str,
    computer_system_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
    body: RekeyRequest,
) -> RedfishError:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Rekey",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Boot/Certificates/{certificate_id}/Actions/Certificate.Renew",
    response_model_exclude_none=True,
)
@authenticate
async def renew16(
    resource_block_id: str,
    computer_system_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
    body: RenewRequest,
) -> RedfishError:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Renew",
    }
    return s.action(**b)


@router.delete(
    "/redfish/v1/Systems/{computer_system_id}/SecureBoot/SecureBootDatabases/{database_id}/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete17(
    computer_system_id: str,
    database_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
) -> None:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "database_id": database_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
    }
    return s.delete(**b)


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/SecureBoot/SecureBootDatabases/{database_id}/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Systems/{computer_system_id}/SecureBoot/SecureBootDatabases/{database_id}/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
async def get17(
    computer_system_id: str,
    database_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
) -> Certificate:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "database_id": database_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
    }
    m = cast(Certificate, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/Systems/{computer_system_id}/SecureBoot/SecureBootDatabases/{database_id}/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch17(
    computer_system_id: str,
    database_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
    body: CertificateOnUpdate,
) -> Certificate:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "database_id": database_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Certificate, s.patch(**b))


@router.post(
    "/redfish/v1/Systems/{computer_system_id}/SecureBoot/SecureBootDatabases/{database_id}/Certificates/{certificate_id}/Actions/Certificate.Rekey",
    response_model_exclude_none=True,
)
@authenticate
async def rekey17(
    computer_system_id: str,
    database_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
    body: RekeyRequest,
) -> RedfishError:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "database_id": database_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Rekey",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Systems/{computer_system_id}/SecureBoot/SecureBootDatabases/{database_id}/Certificates/{certificate_id}/Actions/Certificate.Renew",
    response_model_exclude_none=True,
)
@authenticate
async def renew17(
    computer_system_id: str,
    database_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
    body: RenewRequest,
) -> RedfishError:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "database_id": database_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Renew",
    }
    return s.action(**b)


@router.delete(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/SecureBoot/SecureBootDatabases/{database_id}/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete18(
    resource_block_id: str,
    computer_system_id: str,
    database_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
) -> None:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "database_id": database_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
    }
    return s.delete(**b)


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/SecureBoot/SecureBootDatabases/{database_id}/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/SecureBoot/SecureBootDatabases/{database_id}/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
async def get18(
    resource_block_id: str,
    computer_system_id: str,
    database_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
) -> Certificate:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "database_id": database_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
    }
    m = cast(Certificate, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/SecureBoot/SecureBootDatabases/{database_id}/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch18(
    resource_block_id: str,
    computer_system_id: str,
    database_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
    body: CertificateOnUpdate,
) -> Certificate:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "database_id": database_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Certificate, s.patch(**b))


@router.post(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/SecureBoot/SecureBootDatabases/{database_id}/Certificates/{certificate_id}/Actions/Certificate.Rekey",
    response_model_exclude_none=True,
)
@authenticate
async def rekey18(
    resource_block_id: str,
    computer_system_id: str,
    database_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
    body: RekeyRequest,
) -> RedfishError:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "database_id": database_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Rekey",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/SecureBoot/SecureBootDatabases/{database_id}/Certificates/{certificate_id}/Actions/Certificate.Renew",
    response_model_exclude_none=True,
)
@authenticate
async def renew18(
    resource_block_id: str,
    computer_system_id: str,
    database_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
    body: RenewRequest,
) -> RedfishError:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "database_id": database_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Renew",
    }
    return s.action(**b)


@router.delete(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/SecureBoot/SecureBootDatabases/{database_id}/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete19(
    resource_block_id: str,
    computer_system_id: str,
    database_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
) -> None:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "database_id": database_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
    }
    return s.delete(**b)


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/SecureBoot/SecureBootDatabases/{database_id}/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/SecureBoot/SecureBootDatabases/{database_id}/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
async def get19(
    resource_block_id: str,
    computer_system_id: str,
    database_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
) -> Certificate:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "database_id": database_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
    }
    m = cast(Certificate, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/SecureBoot/SecureBootDatabases/{database_id}/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch19(
    resource_block_id: str,
    computer_system_id: str,
    database_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
    body: CertificateOnUpdate,
) -> Certificate:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "database_id": database_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Certificate, s.patch(**b))


@router.post(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/SecureBoot/SecureBootDatabases/{database_id}/Certificates/{certificate_id}/Actions/Certificate.Rekey",
    response_model_exclude_none=True,
)
@authenticate
async def rekey19(
    resource_block_id: str,
    computer_system_id: str,
    database_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
    body: RekeyRequest,
) -> RedfishError:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "database_id": database_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Rekey",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/SecureBoot/SecureBootDatabases/{database_id}/Certificates/{certificate_id}/Actions/Certificate.Renew",
    response_model_exclude_none=True,
)
@authenticate
async def renew19(
    resource_block_id: str,
    computer_system_id: str,
    database_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
    body: RenewRequest,
) -> RedfishError:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "database_id": database_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Renew",
    }
    return s.action(**b)


@router.delete(
    "/redfish/v1/EventService/Subscriptions/{event_destination_id}/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete20(
    event_destination_id: str, certificate_id: str, request: Request, response: Response
) -> None:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "event_destination_id": event_destination_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
    }
    return s.delete(**b)


@router.get(
    "/redfish/v1/EventService/Subscriptions/{event_destination_id}/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/EventService/Subscriptions/{event_destination_id}/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
async def get20(
    event_destination_id: str, certificate_id: str, request: Request, response: Response
) -> Certificate:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "event_destination_id": event_destination_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
    }
    m = cast(Certificate, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/EventService/Subscriptions/{event_destination_id}/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch20(
    event_destination_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
    body: CertificateOnUpdate,
) -> Certificate:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "event_destination_id": event_destination_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Certificate, s.patch(**b))


@router.post(
    "/redfish/v1/EventService/Subscriptions/{event_destination_id}/Certificates/{certificate_id}/Actions/Certificate.Rekey",
    response_model_exclude_none=True,
)
@authenticate
async def rekey20(
    event_destination_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
    body: RekeyRequest,
) -> RedfishError:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "event_destination_id": event_destination_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Rekey",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/EventService/Subscriptions/{event_destination_id}/Certificates/{certificate_id}/Actions/Certificate.Renew",
    response_model_exclude_none=True,
)
@authenticate
async def renew20(
    event_destination_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
    body: RenewRequest,
) -> RedfishError:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "event_destination_id": event_destination_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Renew",
    }
    return s.action(**b)


@router.delete(
    "/redfish/v1/EventService/Subscriptions/{event_destination_id}/ClientCertificates/{certificate_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete21(
    event_destination_id: str, certificate_id: str, request: Request, response: Response
) -> None:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "event_destination_id": event_destination_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
    }
    return s.delete(**b)


@router.get(
    "/redfish/v1/EventService/Subscriptions/{event_destination_id}/ClientCertificates/{certificate_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/EventService/Subscriptions/{event_destination_id}/ClientCertificates/{certificate_id}",
    response_model_exclude_none=True,
)
async def get21(
    event_destination_id: str, certificate_id: str, request: Request, response: Response
) -> Certificate:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "event_destination_id": event_destination_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
    }
    m = cast(Certificate, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/EventService/Subscriptions/{event_destination_id}/ClientCertificates/{certificate_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch21(
    event_destination_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
    body: CertificateOnUpdate,
) -> Certificate:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "event_destination_id": event_destination_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Certificate, s.patch(**b))


@router.post(
    "/redfish/v1/EventService/Subscriptions/{event_destination_id}/ClientCertificates/{certificate_id}/Actions/Certificate.Rekey",
    response_model_exclude_none=True,
)
@authenticate
async def rekey21(
    event_destination_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
    body: RekeyRequest,
) -> RedfishError:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "event_destination_id": event_destination_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Rekey",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/EventService/Subscriptions/{event_destination_id}/ClientCertificates/{certificate_id}/Actions/Certificate.Renew",
    response_model_exclude_none=True,
)
@authenticate
async def renew21(
    event_destination_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
    body: RenewRequest,
) -> RedfishError:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "event_destination_id": event_destination_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Renew",
    }
    return s.action(**b)


@router.delete(
    "/redfish/v1/Systems/{computer_system_id}/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete22(
    computer_system_id: str, certificate_id: str, request: Request, response: Response
) -> None:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
    }
    return s.delete(**b)


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Systems/{computer_system_id}/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
async def get22(
    computer_system_id: str, certificate_id: str, request: Request, response: Response
) -> Certificate:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
    }
    m = cast(Certificate, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/Systems/{computer_system_id}/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch22(
    computer_system_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
    body: CertificateOnUpdate,
) -> Certificate:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Certificate, s.patch(**b))


@router.post(
    "/redfish/v1/Systems/{computer_system_id}/Certificates/{certificate_id}/Actions/Certificate.Rekey",
    response_model_exclude_none=True,
)
@authenticate
async def rekey22(
    computer_system_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
    body: RekeyRequest,
) -> RedfishError:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Rekey",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Systems/{computer_system_id}/Certificates/{certificate_id}/Actions/Certificate.Renew",
    response_model_exclude_none=True,
)
@authenticate
async def renew22(
    computer_system_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
    body: RenewRequest,
) -> RedfishError:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Renew",
    }
    return s.action(**b)


@router.delete(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete23(
    resource_block_id: str,
    computer_system_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
) -> None:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
    }
    return s.delete(**b)


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
async def get23(
    resource_block_id: str,
    computer_system_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
) -> Certificate:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
    }
    m = cast(Certificate, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch23(
    resource_block_id: str,
    computer_system_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
    body: CertificateOnUpdate,
) -> Certificate:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Certificate, s.patch(**b))


@router.post(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Certificates/{certificate_id}/Actions/Certificate.Rekey",
    response_model_exclude_none=True,
)
@authenticate
async def rekey23(
    resource_block_id: str,
    computer_system_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
    body: RekeyRequest,
) -> RedfishError:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Rekey",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Certificates/{certificate_id}/Actions/Certificate.Renew",
    response_model_exclude_none=True,
)
@authenticate
async def renew23(
    resource_block_id: str,
    computer_system_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
    body: RenewRequest,
) -> RedfishError:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Renew",
    }
    return s.action(**b)


@router.delete(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete24(
    resource_block_id: str,
    computer_system_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
) -> None:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
    }
    return s.delete(**b)


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
async def get24(
    resource_block_id: str,
    computer_system_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
) -> Certificate:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
    }
    m = cast(Certificate, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch24(
    resource_block_id: str,
    computer_system_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
    body: CertificateOnUpdate,
) -> Certificate:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Certificate, s.patch(**b))


@router.post(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Certificates/{certificate_id}/Actions/Certificate.Rekey",
    response_model_exclude_none=True,
)
@authenticate
async def rekey24(
    resource_block_id: str,
    computer_system_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
    body: RekeyRequest,
) -> RedfishError:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Rekey",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Certificates/{certificate_id}/Actions/Certificate.Renew",
    response_model_exclude_none=True,
)
@authenticate
async def renew24(
    resource_block_id: str,
    computer_system_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
    body: RenewRequest,
) -> RedfishError:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Renew",
    }
    return s.action(**b)


@router.delete(
    "/redfish/v1/Systems/{computer_system_id}/Memory/{memory_id}/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete25(
    computer_system_id: str,
    memory_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
) -> None:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "memory_id": memory_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
    }
    return s.delete(**b)


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/Memory/{memory_id}/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Systems/{computer_system_id}/Memory/{memory_id}/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
async def get25(
    computer_system_id: str,
    memory_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
) -> Certificate:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "memory_id": memory_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
    }
    m = cast(Certificate, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/Systems/{computer_system_id}/Memory/{memory_id}/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch25(
    computer_system_id: str,
    memory_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
    body: CertificateOnUpdate,
) -> Certificate:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "memory_id": memory_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Certificate, s.patch(**b))


@router.post(
    "/redfish/v1/Systems/{computer_system_id}/Memory/{memory_id}/Certificates/{certificate_id}/Actions/Certificate.Rekey",
    response_model_exclude_none=True,
)
@authenticate
async def rekey25(
    computer_system_id: str,
    memory_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
    body: RekeyRequest,
) -> RedfishError:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "memory_id": memory_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Rekey",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Systems/{computer_system_id}/Memory/{memory_id}/Certificates/{certificate_id}/Actions/Certificate.Renew",
    response_model_exclude_none=True,
)
@authenticate
async def renew25(
    computer_system_id: str,
    memory_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
    body: RenewRequest,
) -> RedfishError:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "memory_id": memory_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Renew",
    }
    return s.action(**b)


@router.delete(
    "/redfish/v1/Chassis/{chassis_id}/Memory/{memory_id}/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete26(
    chassis_id: str, memory_id: str, certificate_id: str, request: Request, response: Response
) -> None:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "memory_id": memory_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
    }
    return s.delete(**b)


@router.get(
    "/redfish/v1/Chassis/{chassis_id}/Memory/{memory_id}/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Chassis/{chassis_id}/Memory/{memory_id}/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
async def get26(
    chassis_id: str, memory_id: str, certificate_id: str, request: Request, response: Response
) -> Certificate:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "memory_id": memory_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
    }
    m = cast(Certificate, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/Chassis/{chassis_id}/Memory/{memory_id}/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch26(
    chassis_id: str,
    memory_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
    body: CertificateOnUpdate,
) -> Certificate:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "memory_id": memory_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Certificate, s.patch(**b))


@router.post(
    "/redfish/v1/Chassis/{chassis_id}/Memory/{memory_id}/Certificates/{certificate_id}/Actions/Certificate.Rekey",
    response_model_exclude_none=True,
)
@authenticate
async def rekey26(
    chassis_id: str,
    memory_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
    body: RekeyRequest,
) -> RedfishError:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "memory_id": memory_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Rekey",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Chassis/{chassis_id}/Memory/{memory_id}/Certificates/{certificate_id}/Actions/Certificate.Renew",
    response_model_exclude_none=True,
)
@authenticate
async def renew26(
    chassis_id: str,
    memory_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
    body: RenewRequest,
) -> RedfishError:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "memory_id": memory_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Renew",
    }
    return s.action(**b)


@router.delete(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Memory/{memory_id}/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete27(
    resource_block_id: str,
    memory_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
) -> None:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "memory_id": memory_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
    }
    return s.delete(**b)


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Memory/{memory_id}/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Memory/{memory_id}/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
async def get27(
    resource_block_id: str,
    memory_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
) -> Certificate:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "memory_id": memory_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
    }
    m = cast(Certificate, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Memory/{memory_id}/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch27(
    resource_block_id: str,
    memory_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
    body: CertificateOnUpdate,
) -> Certificate:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "memory_id": memory_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Certificate, s.patch(**b))


@router.post(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Memory/{memory_id}/Certificates/{certificate_id}/Actions/Certificate.Rekey",
    response_model_exclude_none=True,
)
@authenticate
async def rekey27(
    resource_block_id: str,
    memory_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
    body: RekeyRequest,
) -> RedfishError:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "memory_id": memory_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Rekey",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Memory/{memory_id}/Certificates/{certificate_id}/Actions/Certificate.Renew",
    response_model_exclude_none=True,
)
@authenticate
async def renew27(
    resource_block_id: str,
    memory_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
    body: RenewRequest,
) -> RedfishError:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "memory_id": memory_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Renew",
    }
    return s.action(**b)


@router.delete(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Memory/{memory_id}/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete28(
    resource_block_id: str,
    computer_system_id: str,
    memory_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
) -> None:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "memory_id": memory_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
    }
    return s.delete(**b)


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Memory/{memory_id}/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Memory/{memory_id}/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
async def get28(
    resource_block_id: str,
    computer_system_id: str,
    memory_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
) -> Certificate:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "memory_id": memory_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
    }
    m = cast(Certificate, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Memory/{memory_id}/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch28(
    resource_block_id: str,
    computer_system_id: str,
    memory_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
    body: CertificateOnUpdate,
) -> Certificate:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "memory_id": memory_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Certificate, s.patch(**b))


@router.post(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Memory/{memory_id}/Certificates/{certificate_id}/Actions/Certificate.Rekey",
    response_model_exclude_none=True,
)
@authenticate
async def rekey28(
    resource_block_id: str,
    computer_system_id: str,
    memory_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
    body: RekeyRequest,
) -> RedfishError:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "memory_id": memory_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Rekey",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Memory/{memory_id}/Certificates/{certificate_id}/Actions/Certificate.Renew",
    response_model_exclude_none=True,
)
@authenticate
async def renew28(
    resource_block_id: str,
    computer_system_id: str,
    memory_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
    body: RenewRequest,
) -> RedfishError:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "memory_id": memory_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Renew",
    }
    return s.action(**b)


@router.delete(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Memory/{memory_id}/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete29(
    resource_block_id: str,
    memory_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
) -> None:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "memory_id": memory_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
    }
    return s.delete(**b)


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Memory/{memory_id}/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Memory/{memory_id}/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
async def get29(
    resource_block_id: str,
    memory_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
) -> Certificate:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "memory_id": memory_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
    }
    m = cast(Certificate, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Memory/{memory_id}/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch29(
    resource_block_id: str,
    memory_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
    body: CertificateOnUpdate,
) -> Certificate:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "memory_id": memory_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Certificate, s.patch(**b))


@router.post(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Memory/{memory_id}/Certificates/{certificate_id}/Actions/Certificate.Rekey",
    response_model_exclude_none=True,
)
@authenticate
async def rekey29(
    resource_block_id: str,
    memory_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
    body: RekeyRequest,
) -> RedfishError:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "memory_id": memory_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Rekey",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Memory/{memory_id}/Certificates/{certificate_id}/Actions/Certificate.Renew",
    response_model_exclude_none=True,
)
@authenticate
async def renew29(
    resource_block_id: str,
    memory_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
    body: RenewRequest,
) -> RedfishError:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "memory_id": memory_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Renew",
    }
    return s.action(**b)


@router.delete(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Memory/{memory_id}/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete30(
    resource_block_id: str,
    computer_system_id: str,
    memory_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
) -> None:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "memory_id": memory_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
    }
    return s.delete(**b)


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Memory/{memory_id}/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Memory/{memory_id}/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
async def get30(
    resource_block_id: str,
    computer_system_id: str,
    memory_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
) -> Certificate:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "memory_id": memory_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
    }
    m = cast(Certificate, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Memory/{memory_id}/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch30(
    resource_block_id: str,
    computer_system_id: str,
    memory_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
    body: CertificateOnUpdate,
) -> Certificate:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "memory_id": memory_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Certificate, s.patch(**b))


@router.post(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Memory/{memory_id}/Certificates/{certificate_id}/Actions/Certificate.Rekey",
    response_model_exclude_none=True,
)
@authenticate
async def rekey30(
    resource_block_id: str,
    computer_system_id: str,
    memory_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
    body: RekeyRequest,
) -> RedfishError:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "memory_id": memory_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Rekey",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Memory/{memory_id}/Certificates/{certificate_id}/Actions/Certificate.Renew",
    response_model_exclude_none=True,
)
@authenticate
async def renew30(
    resource_block_id: str,
    computer_system_id: str,
    memory_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
    body: RenewRequest,
) -> RedfishError:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "memory_id": memory_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Renew",
    }
    return s.action(**b)


@router.delete(
    "/redfish/v1/Systems/{computer_system_id}/Processors/{processor_id}/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete31(
    computer_system_id: str,
    processor_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
) -> None:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "processor_id": processor_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
    }
    return s.delete(**b)


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/Processors/{processor_id}/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Systems/{computer_system_id}/Processors/{processor_id}/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
async def get31(
    computer_system_id: str,
    processor_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
) -> Certificate:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "processor_id": processor_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
    }
    m = cast(Certificate, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/Systems/{computer_system_id}/Processors/{processor_id}/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch31(
    computer_system_id: str,
    processor_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
    body: CertificateOnUpdate,
) -> Certificate:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "processor_id": processor_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Certificate, s.patch(**b))


@router.post(
    "/redfish/v1/Systems/{computer_system_id}/Processors/{processor_id}/Certificates/{certificate_id}/Actions/Certificate.Rekey",
    response_model_exclude_none=True,
)
@authenticate
async def rekey31(
    computer_system_id: str,
    processor_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
    body: RekeyRequest,
) -> RedfishError:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "processor_id": processor_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Rekey",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Systems/{computer_system_id}/Processors/{processor_id}/Certificates/{certificate_id}/Actions/Certificate.Renew",
    response_model_exclude_none=True,
)
@authenticate
async def renew31(
    computer_system_id: str,
    processor_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
    body: RenewRequest,
) -> RedfishError:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "processor_id": processor_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Renew",
    }
    return s.action(**b)


@router.delete(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Processors/{processor_id}/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete32(
    resource_block_id: str,
    processor_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
) -> None:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "processor_id": processor_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
    }
    return s.delete(**b)


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Processors/{processor_id}/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Processors/{processor_id}/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
async def get32(
    resource_block_id: str,
    processor_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
) -> Certificate:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "processor_id": processor_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
    }
    m = cast(Certificate, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Processors/{processor_id}/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch32(
    resource_block_id: str,
    processor_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
    body: CertificateOnUpdate,
) -> Certificate:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "processor_id": processor_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Certificate, s.patch(**b))


@router.post(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Processors/{processor_id}/Certificates/{certificate_id}/Actions/Certificate.Rekey",
    response_model_exclude_none=True,
)
@authenticate
async def rekey32(
    resource_block_id: str,
    processor_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
    body: RekeyRequest,
) -> RedfishError:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "processor_id": processor_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Rekey",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Processors/{processor_id}/Certificates/{certificate_id}/Actions/Certificate.Renew",
    response_model_exclude_none=True,
)
@authenticate
async def renew32(
    resource_block_id: str,
    processor_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
    body: RenewRequest,
) -> RedfishError:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "processor_id": processor_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Renew",
    }
    return s.action(**b)


@router.delete(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Processors/{processor_id}/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete33(
    resource_block_id: str,
    computer_system_id: str,
    processor_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
) -> None:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "processor_id": processor_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
    }
    return s.delete(**b)


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Processors/{processor_id}/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Processors/{processor_id}/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
async def get33(
    resource_block_id: str,
    computer_system_id: str,
    processor_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
) -> Certificate:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "processor_id": processor_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
    }
    m = cast(Certificate, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Processors/{processor_id}/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch33(
    resource_block_id: str,
    computer_system_id: str,
    processor_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
    body: CertificateOnUpdate,
) -> Certificate:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "processor_id": processor_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Certificate, s.patch(**b))


@router.post(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Processors/{processor_id}/Certificates/{certificate_id}/Actions/Certificate.Rekey",
    response_model_exclude_none=True,
)
@authenticate
async def rekey33(
    resource_block_id: str,
    computer_system_id: str,
    processor_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
    body: RekeyRequest,
) -> RedfishError:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "processor_id": processor_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Rekey",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Processors/{processor_id}/Certificates/{certificate_id}/Actions/Certificate.Renew",
    response_model_exclude_none=True,
)
@authenticate
async def renew33(
    resource_block_id: str,
    computer_system_id: str,
    processor_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
    body: RenewRequest,
) -> RedfishError:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "processor_id": processor_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Renew",
    }
    return s.action(**b)


@router.delete(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Processors/{processor_id}/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete34(
    resource_block_id: str,
    processor_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
) -> None:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "processor_id": processor_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
    }
    return s.delete(**b)


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Processors/{processor_id}/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Processors/{processor_id}/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
async def get34(
    resource_block_id: str,
    processor_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
) -> Certificate:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "processor_id": processor_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
    }
    m = cast(Certificate, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Processors/{processor_id}/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch34(
    resource_block_id: str,
    processor_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
    body: CertificateOnUpdate,
) -> Certificate:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "processor_id": processor_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Certificate, s.patch(**b))


@router.post(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Processors/{processor_id}/Certificates/{certificate_id}/Actions/Certificate.Rekey",
    response_model_exclude_none=True,
)
@authenticate
async def rekey34(
    resource_block_id: str,
    processor_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
    body: RekeyRequest,
) -> RedfishError:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "processor_id": processor_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Rekey",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Processors/{processor_id}/Certificates/{certificate_id}/Actions/Certificate.Renew",
    response_model_exclude_none=True,
)
@authenticate
async def renew34(
    resource_block_id: str,
    processor_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
    body: RenewRequest,
) -> RedfishError:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "processor_id": processor_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Renew",
    }
    return s.action(**b)


@router.delete(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Processors/{processor_id}/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete35(
    resource_block_id: str,
    computer_system_id: str,
    processor_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
) -> None:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "processor_id": processor_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
    }
    return s.delete(**b)


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Processors/{processor_id}/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Processors/{processor_id}/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
async def get35(
    resource_block_id: str,
    computer_system_id: str,
    processor_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
) -> Certificate:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "processor_id": processor_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
    }
    m = cast(Certificate, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Processors/{processor_id}/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch35(
    resource_block_id: str,
    computer_system_id: str,
    processor_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
    body: CertificateOnUpdate,
) -> Certificate:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "processor_id": processor_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Certificate, s.patch(**b))


@router.post(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Processors/{processor_id}/Certificates/{certificate_id}/Actions/Certificate.Rekey",
    response_model_exclude_none=True,
)
@authenticate
async def rekey35(
    resource_block_id: str,
    computer_system_id: str,
    processor_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
    body: RekeyRequest,
) -> RedfishError:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "processor_id": processor_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Rekey",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Processors/{processor_id}/Certificates/{certificate_id}/Actions/Certificate.Renew",
    response_model_exclude_none=True,
)
@authenticate
async def renew35(
    resource_block_id: str,
    computer_system_id: str,
    processor_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
    body: RenewRequest,
) -> RedfishError:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "processor_id": processor_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Renew",
    }
    return s.action(**b)


@router.delete(
    "/redfish/v1/Storage/{storage_id}/StorageControllers/{storage_controller_id}/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete36(
    storage_id: str,
    storage_controller_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
) -> None:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
    }
    return s.delete(**b)


@router.get(
    "/redfish/v1/Storage/{storage_id}/StorageControllers/{storage_controller_id}/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Storage/{storage_id}/StorageControllers/{storage_controller_id}/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
async def get36(
    storage_id: str,
    storage_controller_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
) -> Certificate:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
    }
    m = cast(Certificate, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/Storage/{storage_id}/StorageControllers/{storage_controller_id}/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch36(
    storage_id: str,
    storage_controller_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
    body: CertificateOnUpdate,
) -> Certificate:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Certificate, s.patch(**b))


@router.post(
    "/redfish/v1/Storage/{storage_id}/StorageControllers/{storage_controller_id}/Certificates/{certificate_id}/Actions/Certificate.Rekey",
    response_model_exclude_none=True,
)
@authenticate
async def rekey36(
    storage_id: str,
    storage_controller_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
    body: RekeyRequest,
) -> RedfishError:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Rekey",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Storage/{storage_id}/StorageControllers/{storage_controller_id}/Certificates/{certificate_id}/Actions/Certificate.Renew",
    response_model_exclude_none=True,
)
@authenticate
async def renew36(
    storage_id: str,
    storage_controller_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
    body: RenewRequest,
) -> RedfishError:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Renew",
    }
    return s.action(**b)


@router.delete(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/StorageControllers/{storage_controller_id}/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete37(
    computer_system_id: str,
    storage_id: str,
    storage_controller_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
) -> None:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
    }
    return s.delete(**b)


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/StorageControllers/{storage_controller_id}/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/StorageControllers/{storage_controller_id}/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
async def get37(
    computer_system_id: str,
    storage_id: str,
    storage_controller_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
) -> Certificate:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
    }
    m = cast(Certificate, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/StorageControllers/{storage_controller_id}/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch37(
    computer_system_id: str,
    storage_id: str,
    storage_controller_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
    body: CertificateOnUpdate,
) -> Certificate:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Certificate, s.patch(**b))


@router.post(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/StorageControllers/{storage_controller_id}/Certificates/{certificate_id}/Actions/Certificate.Rekey",
    response_model_exclude_none=True,
)
@authenticate
async def rekey37(
    computer_system_id: str,
    storage_id: str,
    storage_controller_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
    body: RekeyRequest,
) -> RedfishError:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Rekey",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/StorageControllers/{storage_controller_id}/Certificates/{certificate_id}/Actions/Certificate.Renew",
    response_model_exclude_none=True,
)
@authenticate
async def renew37(
    computer_system_id: str,
    storage_id: str,
    storage_controller_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
    body: RenewRequest,
) -> RedfishError:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Renew",
    }
    return s.action(**b)


@router.delete(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Storage/{storage_id}/StorageControllers/{storage_controller_id}/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete38(
    resource_block_id: str,
    storage_id: str,
    storage_controller_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
) -> None:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
    }
    return s.delete(**b)


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Storage/{storage_id}/StorageControllers/{storage_controller_id}/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Storage/{storage_id}/StorageControllers/{storage_controller_id}/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
async def get38(
    resource_block_id: str,
    storage_id: str,
    storage_controller_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
) -> Certificate:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
    }
    m = cast(Certificate, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Storage/{storage_id}/StorageControllers/{storage_controller_id}/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch38(
    resource_block_id: str,
    storage_id: str,
    storage_controller_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
    body: CertificateOnUpdate,
) -> Certificate:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Certificate, s.patch(**b))


@router.post(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Storage/{storage_id}/StorageControllers/{storage_controller_id}/Certificates/{certificate_id}/Actions/Certificate.Rekey",
    response_model_exclude_none=True,
)
@authenticate
async def rekey38(
    resource_block_id: str,
    storage_id: str,
    storage_controller_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
    body: RekeyRequest,
) -> RedfishError:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Rekey",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Storage/{storage_id}/StorageControllers/{storage_controller_id}/Certificates/{certificate_id}/Actions/Certificate.Renew",
    response_model_exclude_none=True,
)
@authenticate
async def renew38(
    resource_block_id: str,
    storage_id: str,
    storage_controller_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
    body: RenewRequest,
) -> RedfishError:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Renew",
    }
    return s.action(**b)


@router.delete(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Storage/{storage_id}/StorageControllers/{storage_controller_id}/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete39(
    resource_block_id: str,
    computer_system_id: str,
    storage_id: str,
    storage_controller_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
) -> None:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
    }
    return s.delete(**b)


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Storage/{storage_id}/StorageControllers/{storage_controller_id}/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Storage/{storage_id}/StorageControllers/{storage_controller_id}/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
async def get39(
    resource_block_id: str,
    computer_system_id: str,
    storage_id: str,
    storage_controller_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
) -> Certificate:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
    }
    m = cast(Certificate, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Storage/{storage_id}/StorageControllers/{storage_controller_id}/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch39(
    resource_block_id: str,
    computer_system_id: str,
    storage_id: str,
    storage_controller_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
    body: CertificateOnUpdate,
) -> Certificate:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Certificate, s.patch(**b))


@router.post(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Storage/{storage_id}/StorageControllers/{storage_controller_id}/Certificates/{certificate_id}/Actions/Certificate.Rekey",
    response_model_exclude_none=True,
)
@authenticate
async def rekey39(
    resource_block_id: str,
    computer_system_id: str,
    storage_id: str,
    storage_controller_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
    body: RekeyRequest,
) -> RedfishError:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Rekey",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Storage/{storage_id}/StorageControllers/{storage_controller_id}/Certificates/{certificate_id}/Actions/Certificate.Renew",
    response_model_exclude_none=True,
)
@authenticate
async def renew39(
    resource_block_id: str,
    computer_system_id: str,
    storage_id: str,
    storage_controller_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
    body: RenewRequest,
) -> RedfishError:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Renew",
    }
    return s.action(**b)


@router.delete(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Storage/{storage_id}/StorageControllers/{storage_controller_id}/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete40(
    resource_block_id: str,
    storage_id: str,
    storage_controller_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
) -> None:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
    }
    return s.delete(**b)


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Storage/{storage_id}/StorageControllers/{storage_controller_id}/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Storage/{storage_id}/StorageControllers/{storage_controller_id}/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
async def get40(
    resource_block_id: str,
    storage_id: str,
    storage_controller_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
) -> Certificate:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
    }
    m = cast(Certificate, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Storage/{storage_id}/StorageControllers/{storage_controller_id}/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch40(
    resource_block_id: str,
    storage_id: str,
    storage_controller_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
    body: CertificateOnUpdate,
) -> Certificate:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Certificate, s.patch(**b))


@router.post(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Storage/{storage_id}/StorageControllers/{storage_controller_id}/Certificates/{certificate_id}/Actions/Certificate.Rekey",
    response_model_exclude_none=True,
)
@authenticate
async def rekey40(
    resource_block_id: str,
    storage_id: str,
    storage_controller_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
    body: RekeyRequest,
) -> RedfishError:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Rekey",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Storage/{storage_id}/StorageControllers/{storage_controller_id}/Certificates/{certificate_id}/Actions/Certificate.Renew",
    response_model_exclude_none=True,
)
@authenticate
async def renew40(
    resource_block_id: str,
    storage_id: str,
    storage_controller_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
    body: RenewRequest,
) -> RedfishError:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Renew",
    }
    return s.action(**b)


@router.delete(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Storage/{storage_id}/StorageControllers/{storage_controller_id}/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete41(
    resource_block_id: str,
    computer_system_id: str,
    storage_id: str,
    storage_controller_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
) -> None:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
    }
    return s.delete(**b)


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Storage/{storage_id}/StorageControllers/{storage_controller_id}/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Storage/{storage_id}/StorageControllers/{storage_controller_id}/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
async def get41(
    resource_block_id: str,
    computer_system_id: str,
    storage_id: str,
    storage_controller_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
) -> Certificate:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
    }
    m = cast(Certificate, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Storage/{storage_id}/StorageControllers/{storage_controller_id}/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch41(
    resource_block_id: str,
    computer_system_id: str,
    storage_id: str,
    storage_controller_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
    body: CertificateOnUpdate,
) -> Certificate:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Certificate, s.patch(**b))


@router.post(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Storage/{storage_id}/StorageControllers/{storage_controller_id}/Certificates/{certificate_id}/Actions/Certificate.Rekey",
    response_model_exclude_none=True,
)
@authenticate
async def rekey41(
    resource_block_id: str,
    computer_system_id: str,
    storage_id: str,
    storage_controller_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
    body: RekeyRequest,
) -> RedfishError:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Rekey",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Storage/{storage_id}/StorageControllers/{storage_controller_id}/Certificates/{certificate_id}/Actions/Certificate.Renew",
    response_model_exclude_none=True,
)
@authenticate
async def renew41(
    resource_block_id: str,
    computer_system_id: str,
    storage_id: str,
    storage_controller_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
    body: RenewRequest,
) -> RedfishError:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Renew",
    }
    return s.action(**b)


@router.delete(
    "/redfish/v1/Storage/{storage_id}/Controllers/{storage_controller_id}/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete42(
    storage_id: str,
    storage_controller_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
) -> None:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
    }
    return s.delete(**b)


@router.get(
    "/redfish/v1/Storage/{storage_id}/Controllers/{storage_controller_id}/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Storage/{storage_id}/Controllers/{storage_controller_id}/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
async def get42(
    storage_id: str,
    storage_controller_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
) -> Certificate:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
    }
    m = cast(Certificate, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/Storage/{storage_id}/Controllers/{storage_controller_id}/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch42(
    storage_id: str,
    storage_controller_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
    body: CertificateOnUpdate,
) -> Certificate:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Certificate, s.patch(**b))


@router.post(
    "/redfish/v1/Storage/{storage_id}/Controllers/{storage_controller_id}/Certificates/{certificate_id}/Actions/Certificate.Rekey",
    response_model_exclude_none=True,
)
@authenticate
async def rekey42(
    storage_id: str,
    storage_controller_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
    body: RekeyRequest,
) -> RedfishError:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Rekey",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Storage/{storage_id}/Controllers/{storage_controller_id}/Certificates/{certificate_id}/Actions/Certificate.Renew",
    response_model_exclude_none=True,
)
@authenticate
async def renew42(
    storage_id: str,
    storage_controller_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
    body: RenewRequest,
) -> RedfishError:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Renew",
    }
    return s.action(**b)


@router.delete(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/Controllers/{storage_controller_id}/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete43(
    computer_system_id: str,
    storage_id: str,
    storage_controller_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
) -> None:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
    }
    return s.delete(**b)


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/Controllers/{storage_controller_id}/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/Controllers/{storage_controller_id}/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
async def get43(
    computer_system_id: str,
    storage_id: str,
    storage_controller_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
) -> Certificate:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
    }
    m = cast(Certificate, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/Controllers/{storage_controller_id}/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch43(
    computer_system_id: str,
    storage_id: str,
    storage_controller_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
    body: CertificateOnUpdate,
) -> Certificate:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Certificate, s.patch(**b))


@router.post(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/Controllers/{storage_controller_id}/Certificates/{certificate_id}/Actions/Certificate.Rekey",
    response_model_exclude_none=True,
)
@authenticate
async def rekey43(
    computer_system_id: str,
    storage_id: str,
    storage_controller_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
    body: RekeyRequest,
) -> RedfishError:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Rekey",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/Controllers/{storage_controller_id}/Certificates/{certificate_id}/Actions/Certificate.Renew",
    response_model_exclude_none=True,
)
@authenticate
async def renew43(
    computer_system_id: str,
    storage_id: str,
    storage_controller_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
    body: RenewRequest,
) -> RedfishError:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Renew",
    }
    return s.action(**b)


@router.delete(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Storage/{storage_id}/Controllers/{storage_controller_id}/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete44(
    resource_block_id: str,
    storage_id: str,
    storage_controller_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
) -> None:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
    }
    return s.delete(**b)


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Storage/{storage_id}/Controllers/{storage_controller_id}/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Storage/{storage_id}/Controllers/{storage_controller_id}/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
async def get44(
    resource_block_id: str,
    storage_id: str,
    storage_controller_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
) -> Certificate:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
    }
    m = cast(Certificate, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Storage/{storage_id}/Controllers/{storage_controller_id}/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch44(
    resource_block_id: str,
    storage_id: str,
    storage_controller_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
    body: CertificateOnUpdate,
) -> Certificate:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Certificate, s.patch(**b))


@router.post(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Storage/{storage_id}/Controllers/{storage_controller_id}/Certificates/{certificate_id}/Actions/Certificate.Rekey",
    response_model_exclude_none=True,
)
@authenticate
async def rekey44(
    resource_block_id: str,
    storage_id: str,
    storage_controller_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
    body: RekeyRequest,
) -> RedfishError:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Rekey",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Storage/{storage_id}/Controllers/{storage_controller_id}/Certificates/{certificate_id}/Actions/Certificate.Renew",
    response_model_exclude_none=True,
)
@authenticate
async def renew44(
    resource_block_id: str,
    storage_id: str,
    storage_controller_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
    body: RenewRequest,
) -> RedfishError:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Renew",
    }
    return s.action(**b)


@router.delete(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Storage/{storage_id}/Controllers/{storage_controller_id}/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete45(
    resource_block_id: str,
    computer_system_id: str,
    storage_id: str,
    storage_controller_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
) -> None:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
    }
    return s.delete(**b)


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Storage/{storage_id}/Controllers/{storage_controller_id}/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Storage/{storage_id}/Controllers/{storage_controller_id}/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
async def get45(
    resource_block_id: str,
    computer_system_id: str,
    storage_id: str,
    storage_controller_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
) -> Certificate:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
    }
    m = cast(Certificate, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Storage/{storage_id}/Controllers/{storage_controller_id}/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch45(
    resource_block_id: str,
    computer_system_id: str,
    storage_id: str,
    storage_controller_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
    body: CertificateOnUpdate,
) -> Certificate:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Certificate, s.patch(**b))


@router.post(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Storage/{storage_id}/Controllers/{storage_controller_id}/Certificates/{certificate_id}/Actions/Certificate.Rekey",
    response_model_exclude_none=True,
)
@authenticate
async def rekey45(
    resource_block_id: str,
    computer_system_id: str,
    storage_id: str,
    storage_controller_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
    body: RekeyRequest,
) -> RedfishError:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Rekey",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Storage/{storage_id}/Controllers/{storage_controller_id}/Certificates/{certificate_id}/Actions/Certificate.Renew",
    response_model_exclude_none=True,
)
@authenticate
async def renew45(
    resource_block_id: str,
    computer_system_id: str,
    storage_id: str,
    storage_controller_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
    body: RenewRequest,
) -> RedfishError:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Renew",
    }
    return s.action(**b)


@router.delete(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Storage/{storage_id}/Controllers/{storage_controller_id}/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete46(
    resource_block_id: str,
    storage_id: str,
    storage_controller_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
) -> None:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
    }
    return s.delete(**b)


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Storage/{storage_id}/Controllers/{storage_controller_id}/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Storage/{storage_id}/Controllers/{storage_controller_id}/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
async def get46(
    resource_block_id: str,
    storage_id: str,
    storage_controller_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
) -> Certificate:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
    }
    m = cast(Certificate, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Storage/{storage_id}/Controllers/{storage_controller_id}/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch46(
    resource_block_id: str,
    storage_id: str,
    storage_controller_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
    body: CertificateOnUpdate,
) -> Certificate:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Certificate, s.patch(**b))


@router.post(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Storage/{storage_id}/Controllers/{storage_controller_id}/Certificates/{certificate_id}/Actions/Certificate.Rekey",
    response_model_exclude_none=True,
)
@authenticate
async def rekey46(
    resource_block_id: str,
    storage_id: str,
    storage_controller_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
    body: RekeyRequest,
) -> RedfishError:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Rekey",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Storage/{storage_id}/Controllers/{storage_controller_id}/Certificates/{certificate_id}/Actions/Certificate.Renew",
    response_model_exclude_none=True,
)
@authenticate
async def renew46(
    resource_block_id: str,
    storage_id: str,
    storage_controller_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
    body: RenewRequest,
) -> RedfishError:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Renew",
    }
    return s.action(**b)


@router.delete(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Storage/{storage_id}/Controllers/{storage_controller_id}/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete47(
    resource_block_id: str,
    computer_system_id: str,
    storage_id: str,
    storage_controller_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
) -> None:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
    }
    return s.delete(**b)


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Storage/{storage_id}/Controllers/{storage_controller_id}/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Storage/{storage_id}/Controllers/{storage_controller_id}/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
async def get47(
    resource_block_id: str,
    computer_system_id: str,
    storage_id: str,
    storage_controller_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
) -> Certificate:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
    }
    m = cast(Certificate, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Storage/{storage_id}/Controllers/{storage_controller_id}/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch47(
    resource_block_id: str,
    computer_system_id: str,
    storage_id: str,
    storage_controller_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
    body: CertificateOnUpdate,
) -> Certificate:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Certificate, s.patch(**b))


@router.post(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Storage/{storage_id}/Controllers/{storage_controller_id}/Certificates/{certificate_id}/Actions/Certificate.Rekey",
    response_model_exclude_none=True,
)
@authenticate
async def rekey47(
    resource_block_id: str,
    computer_system_id: str,
    storage_id: str,
    storage_controller_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
    body: RekeyRequest,
) -> RedfishError:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Rekey",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Storage/{storage_id}/Controllers/{storage_controller_id}/Certificates/{certificate_id}/Actions/Certificate.Renew",
    response_model_exclude_none=True,
)
@authenticate
async def renew47(
    resource_block_id: str,
    computer_system_id: str,
    storage_id: str,
    storage_controller_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
    body: RenewRequest,
) -> RedfishError:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Renew",
    }
    return s.action(**b)


@router.delete(
    "/redfish/v1/Fabrics/{fabric_id}/Switches/{switch_id}/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete48(
    fabric_id: str, switch_id: str, certificate_id: str, request: Request, response: Response
) -> None:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "fabric_id": fabric_id,
        "switch_id": switch_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
    }
    return s.delete(**b)


@router.get(
    "/redfish/v1/Fabrics/{fabric_id}/Switches/{switch_id}/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Fabrics/{fabric_id}/Switches/{switch_id}/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
async def get48(
    fabric_id: str, switch_id: str, certificate_id: str, request: Request, response: Response
) -> Certificate:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "fabric_id": fabric_id,
        "switch_id": switch_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
    }
    m = cast(Certificate, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/Fabrics/{fabric_id}/Switches/{switch_id}/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch48(
    fabric_id: str,
    switch_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
    body: CertificateOnUpdate,
) -> Certificate:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "fabric_id": fabric_id,
        "switch_id": switch_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Certificate, s.patch(**b))


@router.post(
    "/redfish/v1/Fabrics/{fabric_id}/Switches/{switch_id}/Certificates/{certificate_id}/Actions/Certificate.Rekey",
    response_model_exclude_none=True,
)
@authenticate
async def rekey48(
    fabric_id: str,
    switch_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
    body: RekeyRequest,
) -> RedfishError:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "fabric_id": fabric_id,
        "switch_id": switch_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Rekey",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Fabrics/{fabric_id}/Switches/{switch_id}/Certificates/{certificate_id}/Actions/Certificate.Renew",
    response_model_exclude_none=True,
)
@authenticate
async def renew48(
    fabric_id: str,
    switch_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
    body: RenewRequest,
) -> RedfishError:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "fabric_id": fabric_id,
        "switch_id": switch_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Renew",
    }
    return s.action(**b)


@router.delete(
    "/redfish/v1/Chassis/{chassis_id}/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete49(
    chassis_id: str, certificate_id: str, request: Request, response: Response
) -> None:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
    }
    return s.delete(**b)


@router.get(
    "/redfish/v1/Chassis/{chassis_id}/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Chassis/{chassis_id}/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
async def get49(
    chassis_id: str, certificate_id: str, request: Request, response: Response
) -> Certificate:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
    }
    m = cast(Certificate, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/Chassis/{chassis_id}/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch49(
    chassis_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
    body: CertificateOnUpdate,
) -> Certificate:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Certificate, s.patch(**b))


@router.post(
    "/redfish/v1/Chassis/{chassis_id}/Certificates/{certificate_id}/Actions/Certificate.Rekey",
    response_model_exclude_none=True,
)
@authenticate
async def rekey49(
    chassis_id: str, certificate_id: str, request: Request, response: Response, body: RekeyRequest
) -> RedfishError:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Rekey",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Chassis/{chassis_id}/Certificates/{certificate_id}/Actions/Certificate.Renew",
    response_model_exclude_none=True,
)
@authenticate
async def renew49(
    chassis_id: str, certificate_id: str, request: Request, response: Response, body: RenewRequest
) -> RedfishError:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Renew",
    }
    return s.action(**b)


@router.delete(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/Drives/{drive_id}/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete50(
    computer_system_id: str,
    storage_id: str,
    drive_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
) -> None:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "drive_id": drive_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
    }
    return s.delete(**b)


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/Drives/{drive_id}/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/Drives/{drive_id}/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
async def get50(
    computer_system_id: str,
    storage_id: str,
    drive_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
) -> Certificate:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "drive_id": drive_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
    }
    m = cast(Certificate, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/Drives/{drive_id}/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch50(
    computer_system_id: str,
    storage_id: str,
    drive_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
    body: CertificateOnUpdate,
) -> Certificate:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "drive_id": drive_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Certificate, s.patch(**b))


@router.post(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/Drives/{drive_id}/Certificates/{certificate_id}/Actions/Certificate.Rekey",
    response_model_exclude_none=True,
)
@authenticate
async def rekey50(
    computer_system_id: str,
    storage_id: str,
    drive_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
    body: RekeyRequest,
) -> RedfishError:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "drive_id": drive_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Rekey",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/Drives/{drive_id}/Certificates/{certificate_id}/Actions/Certificate.Renew",
    response_model_exclude_none=True,
)
@authenticate
async def renew50(
    computer_system_id: str,
    storage_id: str,
    drive_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
    body: RenewRequest,
) -> RedfishError:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "drive_id": drive_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Renew",
    }
    return s.action(**b)


@router.delete(
    "/redfish/v1/Chassis/{chassis_id}/Drives/{drive_id}/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete51(
    chassis_id: str, drive_id: str, certificate_id: str, request: Request, response: Response
) -> None:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "drive_id": drive_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
    }
    return s.delete(**b)


@router.get(
    "/redfish/v1/Chassis/{chassis_id}/Drives/{drive_id}/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Chassis/{chassis_id}/Drives/{drive_id}/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
async def get51(
    chassis_id: str, drive_id: str, certificate_id: str, request: Request, response: Response
) -> Certificate:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "drive_id": drive_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
    }
    m = cast(Certificate, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/Chassis/{chassis_id}/Drives/{drive_id}/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch51(
    chassis_id: str,
    drive_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
    body: CertificateOnUpdate,
) -> Certificate:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "drive_id": drive_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Certificate, s.patch(**b))


@router.post(
    "/redfish/v1/Chassis/{chassis_id}/Drives/{drive_id}/Certificates/{certificate_id}/Actions/Certificate.Rekey",
    response_model_exclude_none=True,
)
@authenticate
async def rekey51(
    chassis_id: str,
    drive_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
    body: RekeyRequest,
) -> RedfishError:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "drive_id": drive_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Rekey",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Chassis/{chassis_id}/Drives/{drive_id}/Certificates/{certificate_id}/Actions/Certificate.Renew",
    response_model_exclude_none=True,
)
@authenticate
async def renew51(
    chassis_id: str,
    drive_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
    body: RenewRequest,
) -> RedfishError:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "drive_id": drive_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Renew",
    }
    return s.action(**b)


@router.delete(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Storage/{storage_id}/Drives/{drive_id}/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete52(
    resource_block_id: str,
    storage_id: str,
    drive_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
) -> None:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "storage_id": storage_id,
        "drive_id": drive_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
    }
    return s.delete(**b)


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Storage/{storage_id}/Drives/{drive_id}/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Storage/{storage_id}/Drives/{drive_id}/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
async def get52(
    resource_block_id: str,
    storage_id: str,
    drive_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
) -> Certificate:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "storage_id": storage_id,
        "drive_id": drive_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
    }
    m = cast(Certificate, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Storage/{storage_id}/Drives/{drive_id}/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch52(
    resource_block_id: str,
    storage_id: str,
    drive_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
    body: CertificateOnUpdate,
) -> Certificate:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "storage_id": storage_id,
        "drive_id": drive_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Certificate, s.patch(**b))


@router.post(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Storage/{storage_id}/Drives/{drive_id}/Certificates/{certificate_id}/Actions/Certificate.Rekey",
    response_model_exclude_none=True,
)
@authenticate
async def rekey52(
    resource_block_id: str,
    storage_id: str,
    drive_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
    body: RekeyRequest,
) -> RedfishError:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "storage_id": storage_id,
        "drive_id": drive_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Rekey",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Storage/{storage_id}/Drives/{drive_id}/Certificates/{certificate_id}/Actions/Certificate.Renew",
    response_model_exclude_none=True,
)
@authenticate
async def renew52(
    resource_block_id: str,
    storage_id: str,
    drive_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
    body: RenewRequest,
) -> RedfishError:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "storage_id": storage_id,
        "drive_id": drive_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Renew",
    }
    return s.action(**b)


@router.delete(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Drives/{drive_id}/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete53(
    resource_block_id: str,
    drive_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
) -> None:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "drive_id": drive_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
    }
    return s.delete(**b)


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Drives/{drive_id}/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Drives/{drive_id}/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
async def get53(
    resource_block_id: str,
    drive_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
) -> Certificate:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "drive_id": drive_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
    }
    m = cast(Certificate, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Drives/{drive_id}/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch53(
    resource_block_id: str,
    drive_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
    body: CertificateOnUpdate,
) -> Certificate:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "drive_id": drive_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Certificate, s.patch(**b))


@router.post(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Drives/{drive_id}/Certificates/{certificate_id}/Actions/Certificate.Rekey",
    response_model_exclude_none=True,
)
@authenticate
async def rekey53(
    resource_block_id: str,
    drive_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
    body: RekeyRequest,
) -> RedfishError:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "drive_id": drive_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Rekey",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Drives/{drive_id}/Certificates/{certificate_id}/Actions/Certificate.Renew",
    response_model_exclude_none=True,
)
@authenticate
async def renew53(
    resource_block_id: str,
    drive_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
    body: RenewRequest,
) -> RedfishError:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "drive_id": drive_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Renew",
    }
    return s.action(**b)


@router.delete(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Storage/{storage_id}/Drives/{drive_id}/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete54(
    resource_block_id: str,
    computer_system_id: str,
    storage_id: str,
    drive_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
) -> None:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "drive_id": drive_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
    }
    return s.delete(**b)


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Storage/{storage_id}/Drives/{drive_id}/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Storage/{storage_id}/Drives/{drive_id}/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
async def get54(
    resource_block_id: str,
    computer_system_id: str,
    storage_id: str,
    drive_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
) -> Certificate:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "drive_id": drive_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
    }
    m = cast(Certificate, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Storage/{storage_id}/Drives/{drive_id}/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch54(
    resource_block_id: str,
    computer_system_id: str,
    storage_id: str,
    drive_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
    body: CertificateOnUpdate,
) -> Certificate:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "drive_id": drive_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Certificate, s.patch(**b))


@router.post(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Storage/{storage_id}/Drives/{drive_id}/Certificates/{certificate_id}/Actions/Certificate.Rekey",
    response_model_exclude_none=True,
)
@authenticate
async def rekey54(
    resource_block_id: str,
    computer_system_id: str,
    storage_id: str,
    drive_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
    body: RekeyRequest,
) -> RedfishError:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "drive_id": drive_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Rekey",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Storage/{storage_id}/Drives/{drive_id}/Certificates/{certificate_id}/Actions/Certificate.Renew",
    response_model_exclude_none=True,
)
@authenticate
async def renew54(
    resource_block_id: str,
    computer_system_id: str,
    storage_id: str,
    drive_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
    body: RenewRequest,
) -> RedfishError:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "drive_id": drive_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Renew",
    }
    return s.action(**b)


@router.delete(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Storage/{storage_id}/Drives/{drive_id}/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete55(
    resource_block_id: str,
    storage_id: str,
    drive_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
) -> None:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "storage_id": storage_id,
        "drive_id": drive_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
    }
    return s.delete(**b)


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Storage/{storage_id}/Drives/{drive_id}/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Storage/{storage_id}/Drives/{drive_id}/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
async def get55(
    resource_block_id: str,
    storage_id: str,
    drive_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
) -> Certificate:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "storage_id": storage_id,
        "drive_id": drive_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
    }
    m = cast(Certificate, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Storage/{storage_id}/Drives/{drive_id}/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch55(
    resource_block_id: str,
    storage_id: str,
    drive_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
    body: CertificateOnUpdate,
) -> Certificate:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "storage_id": storage_id,
        "drive_id": drive_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Certificate, s.patch(**b))


@router.post(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Storage/{storage_id}/Drives/{drive_id}/Certificates/{certificate_id}/Actions/Certificate.Rekey",
    response_model_exclude_none=True,
)
@authenticate
async def rekey55(
    resource_block_id: str,
    storage_id: str,
    drive_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
    body: RekeyRequest,
) -> RedfishError:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "storage_id": storage_id,
        "drive_id": drive_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Rekey",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Storage/{storage_id}/Drives/{drive_id}/Certificates/{certificate_id}/Actions/Certificate.Renew",
    response_model_exclude_none=True,
)
@authenticate
async def renew55(
    resource_block_id: str,
    storage_id: str,
    drive_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
    body: RenewRequest,
) -> RedfishError:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "storage_id": storage_id,
        "drive_id": drive_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Renew",
    }
    return s.action(**b)


@router.delete(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Drives/{drive_id}/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete56(
    resource_block_id: str,
    drive_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
) -> None:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "drive_id": drive_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
    }
    return s.delete(**b)


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Drives/{drive_id}/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Drives/{drive_id}/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
async def get56(
    resource_block_id: str,
    drive_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
) -> Certificate:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "drive_id": drive_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
    }
    m = cast(Certificate, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Drives/{drive_id}/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch56(
    resource_block_id: str,
    drive_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
    body: CertificateOnUpdate,
) -> Certificate:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "drive_id": drive_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Certificate, s.patch(**b))


@router.post(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Drives/{drive_id}/Certificates/{certificate_id}/Actions/Certificate.Rekey",
    response_model_exclude_none=True,
)
@authenticate
async def rekey56(
    resource_block_id: str,
    drive_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
    body: RekeyRequest,
) -> RedfishError:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "drive_id": drive_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Rekey",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Drives/{drive_id}/Certificates/{certificate_id}/Actions/Certificate.Renew",
    response_model_exclude_none=True,
)
@authenticate
async def renew56(
    resource_block_id: str,
    drive_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
    body: RenewRequest,
) -> RedfishError:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "drive_id": drive_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Renew",
    }
    return s.action(**b)


@router.delete(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Storage/{storage_id}/Drives/{drive_id}/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete57(
    resource_block_id: str,
    computer_system_id: str,
    storage_id: str,
    drive_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
) -> None:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "drive_id": drive_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
    }
    return s.delete(**b)


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Storage/{storage_id}/Drives/{drive_id}/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Storage/{storage_id}/Drives/{drive_id}/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
async def get57(
    resource_block_id: str,
    computer_system_id: str,
    storage_id: str,
    drive_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
) -> Certificate:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "drive_id": drive_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
    }
    m = cast(Certificate, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Storage/{storage_id}/Drives/{drive_id}/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch57(
    resource_block_id: str,
    computer_system_id: str,
    storage_id: str,
    drive_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
    body: CertificateOnUpdate,
) -> Certificate:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "drive_id": drive_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Certificate, s.patch(**b))


@router.post(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Storage/{storage_id}/Drives/{drive_id}/Certificates/{certificate_id}/Actions/Certificate.Rekey",
    response_model_exclude_none=True,
)
@authenticate
async def rekey57(
    resource_block_id: str,
    computer_system_id: str,
    storage_id: str,
    drive_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
    body: RekeyRequest,
) -> RedfishError:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "drive_id": drive_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Rekey",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Storage/{storage_id}/Drives/{drive_id}/Certificates/{certificate_id}/Actions/Certificate.Renew",
    response_model_exclude_none=True,
)
@authenticate
async def renew57(
    resource_block_id: str,
    computer_system_id: str,
    storage_id: str,
    drive_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
    body: RenewRequest,
) -> RedfishError:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "drive_id": drive_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Renew",
    }
    return s.action(**b)


@router.delete(
    "/redfish/v1/Chassis/{chassis_id}/NetworkAdapters/{network_adapter_id}/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete58(
    chassis_id: str,
    network_adapter_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
) -> None:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "network_adapter_id": network_adapter_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
    }
    return s.delete(**b)


@router.get(
    "/redfish/v1/Chassis/{chassis_id}/NetworkAdapters/{network_adapter_id}/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Chassis/{chassis_id}/NetworkAdapters/{network_adapter_id}/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
async def get58(
    chassis_id: str,
    network_adapter_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
) -> Certificate:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "network_adapter_id": network_adapter_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
    }
    m = cast(Certificate, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/Chassis/{chassis_id}/NetworkAdapters/{network_adapter_id}/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch58(
    chassis_id: str,
    network_adapter_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
    body: CertificateOnUpdate,
) -> Certificate:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "network_adapter_id": network_adapter_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Certificate, s.patch(**b))


@router.post(
    "/redfish/v1/Chassis/{chassis_id}/NetworkAdapters/{network_adapter_id}/Certificates/{certificate_id}/Actions/Certificate.Rekey",
    response_model_exclude_none=True,
)
@authenticate
async def rekey58(
    chassis_id: str,
    network_adapter_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
    body: RekeyRequest,
) -> RedfishError:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "network_adapter_id": network_adapter_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Rekey",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Chassis/{chassis_id}/NetworkAdapters/{network_adapter_id}/Certificates/{certificate_id}/Actions/Certificate.Renew",
    response_model_exclude_none=True,
)
@authenticate
async def renew58(
    chassis_id: str,
    network_adapter_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
    body: RenewRequest,
) -> RedfishError:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "network_adapter_id": network_adapter_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Renew",
    }
    return s.action(**b)


@router.delete(
    "/redfish/v1/Systems/{computer_system_id}/VirtualMedia/{virtual_media_id}/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete59(
    computer_system_id: str,
    virtual_media_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
) -> None:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "virtual_media_id": virtual_media_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
    }
    return s.delete(**b)


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/VirtualMedia/{virtual_media_id}/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Systems/{computer_system_id}/VirtualMedia/{virtual_media_id}/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
async def get59(
    computer_system_id: str,
    virtual_media_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
) -> Certificate:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "virtual_media_id": virtual_media_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
    }
    m = cast(Certificate, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/Systems/{computer_system_id}/VirtualMedia/{virtual_media_id}/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch59(
    computer_system_id: str,
    virtual_media_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
    body: CertificateOnUpdate,
) -> Certificate:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "virtual_media_id": virtual_media_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Certificate, s.patch(**b))


@router.post(
    "/redfish/v1/Systems/{computer_system_id}/VirtualMedia/{virtual_media_id}/Certificates/{certificate_id}/Actions/Certificate.Rekey",
    response_model_exclude_none=True,
)
@authenticate
async def rekey59(
    computer_system_id: str,
    virtual_media_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
    body: RekeyRequest,
) -> RedfishError:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "virtual_media_id": virtual_media_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Rekey",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Systems/{computer_system_id}/VirtualMedia/{virtual_media_id}/Certificates/{certificate_id}/Actions/Certificate.Renew",
    response_model_exclude_none=True,
)
@authenticate
async def renew59(
    computer_system_id: str,
    virtual_media_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
    body: RenewRequest,
) -> RedfishError:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "virtual_media_id": virtual_media_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Renew",
    }
    return s.action(**b)


@router.delete(
    "/redfish/v1/Systems/{computer_system_id}/VirtualMedia/{virtual_media_id}/ClientCertificates/{certificate_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete60(
    computer_system_id: str,
    virtual_media_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
) -> None:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "virtual_media_id": virtual_media_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
    }
    return s.delete(**b)


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/VirtualMedia/{virtual_media_id}/ClientCertificates/{certificate_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Systems/{computer_system_id}/VirtualMedia/{virtual_media_id}/ClientCertificates/{certificate_id}",
    response_model_exclude_none=True,
)
async def get60(
    computer_system_id: str,
    virtual_media_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
) -> Certificate:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "virtual_media_id": virtual_media_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
    }
    m = cast(Certificate, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/Systems/{computer_system_id}/VirtualMedia/{virtual_media_id}/ClientCertificates/{certificate_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch60(
    computer_system_id: str,
    virtual_media_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
    body: CertificateOnUpdate,
) -> Certificate:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "virtual_media_id": virtual_media_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Certificate, s.patch(**b))


@router.post(
    "/redfish/v1/Systems/{computer_system_id}/VirtualMedia/{virtual_media_id}/ClientCertificates/{certificate_id}/Actions/Certificate.Rekey",
    response_model_exclude_none=True,
)
@authenticate
async def rekey60(
    computer_system_id: str,
    virtual_media_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
    body: RekeyRequest,
) -> RedfishError:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "virtual_media_id": virtual_media_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Rekey",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Systems/{computer_system_id}/VirtualMedia/{virtual_media_id}/ClientCertificates/{certificate_id}/Actions/Certificate.Renew",
    response_model_exclude_none=True,
)
@authenticate
async def renew60(
    computer_system_id: str,
    virtual_media_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
    body: RenewRequest,
) -> RedfishError:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "virtual_media_id": virtual_media_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Renew",
    }
    return s.action(**b)


@router.delete(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/VirtualMedia/{virtual_media_id}/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete61(
    resource_block_id: str,
    computer_system_id: str,
    virtual_media_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
) -> None:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "virtual_media_id": virtual_media_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
    }
    return s.delete(**b)


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/VirtualMedia/{virtual_media_id}/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/VirtualMedia/{virtual_media_id}/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
async def get61(
    resource_block_id: str,
    computer_system_id: str,
    virtual_media_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
) -> Certificate:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "virtual_media_id": virtual_media_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
    }
    m = cast(Certificate, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/VirtualMedia/{virtual_media_id}/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch61(
    resource_block_id: str,
    computer_system_id: str,
    virtual_media_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
    body: CertificateOnUpdate,
) -> Certificate:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "virtual_media_id": virtual_media_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Certificate, s.patch(**b))


@router.post(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/VirtualMedia/{virtual_media_id}/Certificates/{certificate_id}/Actions/Certificate.Rekey",
    response_model_exclude_none=True,
)
@authenticate
async def rekey61(
    resource_block_id: str,
    computer_system_id: str,
    virtual_media_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
    body: RekeyRequest,
) -> RedfishError:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "virtual_media_id": virtual_media_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Rekey",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/VirtualMedia/{virtual_media_id}/Certificates/{certificate_id}/Actions/Certificate.Renew",
    response_model_exclude_none=True,
)
@authenticate
async def renew61(
    resource_block_id: str,
    computer_system_id: str,
    virtual_media_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
    body: RenewRequest,
) -> RedfishError:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "virtual_media_id": virtual_media_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Renew",
    }
    return s.action(**b)


@router.delete(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/VirtualMedia/{virtual_media_id}/ClientCertificates/{certificate_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete62(
    resource_block_id: str,
    computer_system_id: str,
    virtual_media_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
) -> None:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "virtual_media_id": virtual_media_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
    }
    return s.delete(**b)


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/VirtualMedia/{virtual_media_id}/ClientCertificates/{certificate_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/VirtualMedia/{virtual_media_id}/ClientCertificates/{certificate_id}",
    response_model_exclude_none=True,
)
async def get62(
    resource_block_id: str,
    computer_system_id: str,
    virtual_media_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
) -> Certificate:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "virtual_media_id": virtual_media_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
    }
    m = cast(Certificate, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/VirtualMedia/{virtual_media_id}/ClientCertificates/{certificate_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch62(
    resource_block_id: str,
    computer_system_id: str,
    virtual_media_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
    body: CertificateOnUpdate,
) -> Certificate:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "virtual_media_id": virtual_media_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Certificate, s.patch(**b))


@router.post(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/VirtualMedia/{virtual_media_id}/ClientCertificates/{certificate_id}/Actions/Certificate.Rekey",
    response_model_exclude_none=True,
)
@authenticate
async def rekey62(
    resource_block_id: str,
    computer_system_id: str,
    virtual_media_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
    body: RekeyRequest,
) -> RedfishError:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "virtual_media_id": virtual_media_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Rekey",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/VirtualMedia/{virtual_media_id}/ClientCertificates/{certificate_id}/Actions/Certificate.Renew",
    response_model_exclude_none=True,
)
@authenticate
async def renew62(
    resource_block_id: str,
    computer_system_id: str,
    virtual_media_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
    body: RenewRequest,
) -> RedfishError:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "virtual_media_id": virtual_media_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Renew",
    }
    return s.action(**b)


@router.delete(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/VirtualMedia/{virtual_media_id}/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete63(
    resource_block_id: str,
    computer_system_id: str,
    virtual_media_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
) -> None:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "virtual_media_id": virtual_media_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
    }
    return s.delete(**b)


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/VirtualMedia/{virtual_media_id}/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/VirtualMedia/{virtual_media_id}/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
async def get63(
    resource_block_id: str,
    computer_system_id: str,
    virtual_media_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
) -> Certificate:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "virtual_media_id": virtual_media_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
    }
    m = cast(Certificate, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/VirtualMedia/{virtual_media_id}/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch63(
    resource_block_id: str,
    computer_system_id: str,
    virtual_media_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
    body: CertificateOnUpdate,
) -> Certificate:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "virtual_media_id": virtual_media_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Certificate, s.patch(**b))


@router.post(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/VirtualMedia/{virtual_media_id}/Certificates/{certificate_id}/Actions/Certificate.Rekey",
    response_model_exclude_none=True,
)
@authenticate
async def rekey63(
    resource_block_id: str,
    computer_system_id: str,
    virtual_media_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
    body: RekeyRequest,
) -> RedfishError:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "virtual_media_id": virtual_media_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Rekey",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/VirtualMedia/{virtual_media_id}/Certificates/{certificate_id}/Actions/Certificate.Renew",
    response_model_exclude_none=True,
)
@authenticate
async def renew63(
    resource_block_id: str,
    computer_system_id: str,
    virtual_media_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
    body: RenewRequest,
) -> RedfishError:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "virtual_media_id": virtual_media_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Renew",
    }
    return s.action(**b)


@router.delete(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/VirtualMedia/{virtual_media_id}/ClientCertificates/{certificate_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete64(
    resource_block_id: str,
    computer_system_id: str,
    virtual_media_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
) -> None:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "virtual_media_id": virtual_media_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
    }
    return s.delete(**b)


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/VirtualMedia/{virtual_media_id}/ClientCertificates/{certificate_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/VirtualMedia/{virtual_media_id}/ClientCertificates/{certificate_id}",
    response_model_exclude_none=True,
)
async def get64(
    resource_block_id: str,
    computer_system_id: str,
    virtual_media_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
) -> Certificate:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "virtual_media_id": virtual_media_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
    }
    m = cast(Certificate, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/VirtualMedia/{virtual_media_id}/ClientCertificates/{certificate_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch64(
    resource_block_id: str,
    computer_system_id: str,
    virtual_media_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
    body: CertificateOnUpdate,
) -> Certificate:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "virtual_media_id": virtual_media_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Certificate, s.patch(**b))


@router.post(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/VirtualMedia/{virtual_media_id}/ClientCertificates/{certificate_id}/Actions/Certificate.Rekey",
    response_model_exclude_none=True,
)
@authenticate
async def rekey64(
    resource_block_id: str,
    computer_system_id: str,
    virtual_media_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
    body: RekeyRequest,
) -> RedfishError:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "virtual_media_id": virtual_media_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Rekey",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/VirtualMedia/{virtual_media_id}/ClientCertificates/{certificate_id}/Actions/Certificate.Renew",
    response_model_exclude_none=True,
)
@authenticate
async def renew64(
    resource_block_id: str,
    computer_system_id: str,
    virtual_media_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
    body: RenewRequest,
) -> RedfishError:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "virtual_media_id": virtual_media_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Renew",
    }
    return s.action(**b)


@router.delete(
    "/redfish/v1/UpdateService/RemoteServerCertificates/{certificate_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete65(certificate_id: str, request: Request, response: Response) -> None:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
    }
    return s.delete(**b)


@router.get(
    "/redfish/v1/UpdateService/RemoteServerCertificates/{certificate_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/UpdateService/RemoteServerCertificates/{certificate_id}",
    response_model_exclude_none=True,
)
async def get65(certificate_id: str, request: Request, response: Response) -> Certificate:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
    }
    m = cast(Certificate, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/UpdateService/RemoteServerCertificates/{certificate_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch65(
    certificate_id: str, request: Request, response: Response, body: CertificateOnUpdate
) -> Certificate:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Certificate, s.patch(**b))


@router.post(
    "/redfish/v1/UpdateService/RemoteServerCertificates/{certificate_id}/Actions/Certificate.Rekey",
    response_model_exclude_none=True,
)
@authenticate
async def rekey65(
    certificate_id: str, request: Request, response: Response, body: RekeyRequest
) -> RedfishError:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Rekey",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/UpdateService/RemoteServerCertificates/{certificate_id}/Actions/Certificate.Renew",
    response_model_exclude_none=True,
)
@authenticate
async def renew65(
    certificate_id: str, request: Request, response: Response, body: RenewRequest
) -> RedfishError:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Renew",
    }
    return s.action(**b)


@router.delete(
    "/redfish/v1/UpdateService/ClientCertificates/{certificate_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete66(certificate_id: str, request: Request, response: Response) -> None:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
    }
    return s.delete(**b)


@router.get(
    "/redfish/v1/UpdateService/ClientCertificates/{certificate_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/UpdateService/ClientCertificates/{certificate_id}",
    response_model_exclude_none=True,
)
async def get66(certificate_id: str, request: Request, response: Response) -> Certificate:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
    }
    m = cast(Certificate, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/UpdateService/ClientCertificates/{certificate_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch66(
    certificate_id: str, request: Request, response: Response, body: CertificateOnUpdate
) -> Certificate:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Certificate, s.patch(**b))


@router.post(
    "/redfish/v1/UpdateService/ClientCertificates/{certificate_id}/Actions/Certificate.Rekey",
    response_model_exclude_none=True,
)
@authenticate
async def rekey66(
    certificate_id: str, request: Request, response: Response, body: RekeyRequest
) -> RedfishError:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Rekey",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/UpdateService/ClientCertificates/{certificate_id}/Actions/Certificate.Renew",
    response_model_exclude_none=True,
)
@authenticate
async def renew66(
    certificate_id: str, request: Request, response: Response, body: RenewRequest
) -> RedfishError:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Renew",
    }
    return s.action(**b)


@router.delete(
    "/redfish/v1/Managers/{manager_id}/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete67(
    manager_id: str, certificate_id: str, request: Request, response: Response
) -> None:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "manager_id": manager_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
    }
    return s.delete(**b)


@router.get(
    "/redfish/v1/Managers/{manager_id}/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Managers/{manager_id}/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
async def get67(
    manager_id: str, certificate_id: str, request: Request, response: Response
) -> Certificate:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "manager_id": manager_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
    }
    m = cast(Certificate, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/Managers/{manager_id}/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch67(
    manager_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
    body: CertificateOnUpdate,
) -> Certificate:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "manager_id": manager_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Certificate, s.patch(**b))


@router.post(
    "/redfish/v1/Managers/{manager_id}/Certificates/{certificate_id}/Actions/Certificate.Rekey",
    response_model_exclude_none=True,
)
@authenticate
async def rekey67(
    manager_id: str, certificate_id: str, request: Request, response: Response, body: RekeyRequest
) -> RedfishError:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "manager_id": manager_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Rekey",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Managers/{manager_id}/Certificates/{certificate_id}/Actions/Certificate.Renew",
    response_model_exclude_none=True,
)
@authenticate
async def renew67(
    manager_id: str, certificate_id: str, request: Request, response: Response, body: RenewRequest
) -> RedfishError:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "manager_id": manager_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Renew",
    }
    return s.action(**b)


@router.delete(
    "/redfish/v1/Systems/{computer_system_id}/KeyManagement/KMIPCertificates/{certificate_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete68(
    computer_system_id: str, certificate_id: str, request: Request, response: Response
) -> None:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
    }
    return s.delete(**b)


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/KeyManagement/KMIPCertificates/{certificate_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Systems/{computer_system_id}/KeyManagement/KMIPCertificates/{certificate_id}",
    response_model_exclude_none=True,
)
async def get68(
    computer_system_id: str, certificate_id: str, request: Request, response: Response
) -> Certificate:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
    }
    m = cast(Certificate, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/Systems/{computer_system_id}/KeyManagement/KMIPCertificates/{certificate_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch68(
    computer_system_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
    body: CertificateOnUpdate,
) -> Certificate:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Certificate, s.patch(**b))


@router.post(
    "/redfish/v1/Systems/{computer_system_id}/KeyManagement/KMIPCertificates/{certificate_id}/Actions/Certificate.Rekey",
    response_model_exclude_none=True,
)
@authenticate
async def rekey68(
    computer_system_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
    body: RekeyRequest,
) -> RedfishError:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Rekey",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Systems/{computer_system_id}/KeyManagement/KMIPCertificates/{certificate_id}/Actions/Certificate.Renew",
    response_model_exclude_none=True,
)
@authenticate
async def renew68(
    computer_system_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
    body: RenewRequest,
) -> RedfishError:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Renew",
    }
    return s.action(**b)


@router.delete(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/KeyManagement/KMIPCertificates/{certificate_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete69(
    resource_block_id: str,
    computer_system_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
) -> None:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
    }
    return s.delete(**b)


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/KeyManagement/KMIPCertificates/{certificate_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/KeyManagement/KMIPCertificates/{certificate_id}",
    response_model_exclude_none=True,
)
async def get69(
    resource_block_id: str,
    computer_system_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
) -> Certificate:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
    }
    m = cast(Certificate, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/KeyManagement/KMIPCertificates/{certificate_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch69(
    resource_block_id: str,
    computer_system_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
    body: CertificateOnUpdate,
) -> Certificate:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Certificate, s.patch(**b))


@router.post(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/KeyManagement/KMIPCertificates/{certificate_id}/Actions/Certificate.Rekey",
    response_model_exclude_none=True,
)
@authenticate
async def rekey69(
    resource_block_id: str,
    computer_system_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
    body: RekeyRequest,
) -> RedfishError:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Rekey",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/KeyManagement/KMIPCertificates/{certificate_id}/Actions/Certificate.Renew",
    response_model_exclude_none=True,
)
@authenticate
async def renew69(
    resource_block_id: str,
    computer_system_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
    body: RenewRequest,
) -> RedfishError:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Renew",
    }
    return s.action(**b)


@router.delete(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/KeyManagement/KMIPCertificates/{certificate_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete70(
    resource_block_id: str,
    computer_system_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
) -> None:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
    }
    return s.delete(**b)


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/KeyManagement/KMIPCertificates/{certificate_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/KeyManagement/KMIPCertificates/{certificate_id}",
    response_model_exclude_none=True,
)
async def get70(
    resource_block_id: str,
    computer_system_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
) -> Certificate:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
    }
    m = cast(Certificate, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/KeyManagement/KMIPCertificates/{certificate_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch70(
    resource_block_id: str,
    computer_system_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
    body: CertificateOnUpdate,
) -> Certificate:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Certificate, s.patch(**b))


@router.post(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/KeyManagement/KMIPCertificates/{certificate_id}/Actions/Certificate.Rekey",
    response_model_exclude_none=True,
)
@authenticate
async def rekey70(
    resource_block_id: str,
    computer_system_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
    body: RekeyRequest,
) -> RedfishError:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Rekey",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/KeyManagement/KMIPCertificates/{certificate_id}/Actions/Certificate.Renew",
    response_model_exclude_none=True,
)
@authenticate
async def renew70(
    resource_block_id: str,
    computer_system_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
    body: RenewRequest,
) -> RedfishError:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Renew",
    }
    return s.action(**b)


@router.delete(
    "/redfish/v1/Managers/{manager_id}/SecurityPolicy/SPDM/TrustedCertificates/{certificate_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete71(
    manager_id: str, certificate_id: str, request: Request, response: Response
) -> None:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "manager_id": manager_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
    }
    return s.delete(**b)


@router.get(
    "/redfish/v1/Managers/{manager_id}/SecurityPolicy/SPDM/TrustedCertificates/{certificate_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Managers/{manager_id}/SecurityPolicy/SPDM/TrustedCertificates/{certificate_id}",
    response_model_exclude_none=True,
)
async def get71(
    manager_id: str, certificate_id: str, request: Request, response: Response
) -> Certificate:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "manager_id": manager_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
    }
    m = cast(Certificate, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/Managers/{manager_id}/SecurityPolicy/SPDM/TrustedCertificates/{certificate_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch71(
    manager_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
    body: CertificateOnUpdate,
) -> Certificate:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "manager_id": manager_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Certificate, s.patch(**b))


@router.post(
    "/redfish/v1/Managers/{manager_id}/SecurityPolicy/SPDM/TrustedCertificates/{certificate_id}/Actions/Certificate.Rekey",
    response_model_exclude_none=True,
)
@authenticate
async def rekey71(
    manager_id: str, certificate_id: str, request: Request, response: Response, body: RekeyRequest
) -> RedfishError:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "manager_id": manager_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Rekey",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Managers/{manager_id}/SecurityPolicy/SPDM/TrustedCertificates/{certificate_id}/Actions/Certificate.Renew",
    response_model_exclude_none=True,
)
@authenticate
async def renew71(
    manager_id: str, certificate_id: str, request: Request, response: Response, body: RenewRequest
) -> RedfishError:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "manager_id": manager_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Renew",
    }
    return s.action(**b)


@router.delete(
    "/redfish/v1/Managers/{manager_id}/SecurityPolicy/SPDM/RevokedCertificates/{certificate_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete72(
    manager_id: str, certificate_id: str, request: Request, response: Response
) -> None:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "manager_id": manager_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
    }
    return s.delete(**b)


@router.get(
    "/redfish/v1/Managers/{manager_id}/SecurityPolicy/SPDM/RevokedCertificates/{certificate_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Managers/{manager_id}/SecurityPolicy/SPDM/RevokedCertificates/{certificate_id}",
    response_model_exclude_none=True,
)
async def get72(
    manager_id: str, certificate_id: str, request: Request, response: Response
) -> Certificate:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "manager_id": manager_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
    }
    m = cast(Certificate, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/Managers/{manager_id}/SecurityPolicy/SPDM/RevokedCertificates/{certificate_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch72(
    manager_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
    body: CertificateOnUpdate,
) -> Certificate:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "manager_id": manager_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Certificate, s.patch(**b))


@router.post(
    "/redfish/v1/Managers/{manager_id}/SecurityPolicy/SPDM/RevokedCertificates/{certificate_id}/Actions/Certificate.Rekey",
    response_model_exclude_none=True,
)
@authenticate
async def rekey72(
    manager_id: str, certificate_id: str, request: Request, response: Response, body: RekeyRequest
) -> RedfishError:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "manager_id": manager_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Rekey",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Managers/{manager_id}/SecurityPolicy/SPDM/RevokedCertificates/{certificate_id}/Actions/Certificate.Renew",
    response_model_exclude_none=True,
)
@authenticate
async def renew72(
    manager_id: str, certificate_id: str, request: Request, response: Response, body: RenewRequest
) -> RedfishError:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "manager_id": manager_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Renew",
    }
    return s.action(**b)


@router.delete(
    "/redfish/v1/Managers/{manager_id}/SecurityPolicy/TLS/Client/TrustedCertificates/{certificate_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete73(
    manager_id: str, certificate_id: str, request: Request, response: Response
) -> None:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "manager_id": manager_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
    }
    return s.delete(**b)


@router.get(
    "/redfish/v1/Managers/{manager_id}/SecurityPolicy/TLS/Client/TrustedCertificates/{certificate_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Managers/{manager_id}/SecurityPolicy/TLS/Client/TrustedCertificates/{certificate_id}",
    response_model_exclude_none=True,
)
async def get73(
    manager_id: str, certificate_id: str, request: Request, response: Response
) -> Certificate:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "manager_id": manager_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
    }
    m = cast(Certificate, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/Managers/{manager_id}/SecurityPolicy/TLS/Client/TrustedCertificates/{certificate_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch73(
    manager_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
    body: CertificateOnUpdate,
) -> Certificate:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "manager_id": manager_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Certificate, s.patch(**b))


@router.post(
    "/redfish/v1/Managers/{manager_id}/SecurityPolicy/TLS/Client/TrustedCertificates/{certificate_id}/Actions/Certificate.Rekey",
    response_model_exclude_none=True,
)
@authenticate
async def rekey73(
    manager_id: str, certificate_id: str, request: Request, response: Response, body: RekeyRequest
) -> RedfishError:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "manager_id": manager_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Rekey",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Managers/{manager_id}/SecurityPolicy/TLS/Client/TrustedCertificates/{certificate_id}/Actions/Certificate.Renew",
    response_model_exclude_none=True,
)
@authenticate
async def renew73(
    manager_id: str, certificate_id: str, request: Request, response: Response, body: RenewRequest
) -> RedfishError:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "manager_id": manager_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Renew",
    }
    return s.action(**b)


@router.delete(
    "/redfish/v1/Managers/{manager_id}/SecurityPolicy/TLS/Client/RevokedCertificates/{certificate_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete74(
    manager_id: str, certificate_id: str, request: Request, response: Response
) -> None:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "manager_id": manager_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
    }
    return s.delete(**b)


@router.get(
    "/redfish/v1/Managers/{manager_id}/SecurityPolicy/TLS/Client/RevokedCertificates/{certificate_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Managers/{manager_id}/SecurityPolicy/TLS/Client/RevokedCertificates/{certificate_id}",
    response_model_exclude_none=True,
)
async def get74(
    manager_id: str, certificate_id: str, request: Request, response: Response
) -> Certificate:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "manager_id": manager_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
    }
    m = cast(Certificate, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/Managers/{manager_id}/SecurityPolicy/TLS/Client/RevokedCertificates/{certificate_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch74(
    manager_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
    body: CertificateOnUpdate,
) -> Certificate:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "manager_id": manager_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Certificate, s.patch(**b))


@router.post(
    "/redfish/v1/Managers/{manager_id}/SecurityPolicy/TLS/Client/RevokedCertificates/{certificate_id}/Actions/Certificate.Rekey",
    response_model_exclude_none=True,
)
@authenticate
async def rekey74(
    manager_id: str, certificate_id: str, request: Request, response: Response, body: RekeyRequest
) -> RedfishError:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "manager_id": manager_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Rekey",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Managers/{manager_id}/SecurityPolicy/TLS/Client/RevokedCertificates/{certificate_id}/Actions/Certificate.Renew",
    response_model_exclude_none=True,
)
@authenticate
async def renew74(
    manager_id: str, certificate_id: str, request: Request, response: Response, body: RenewRequest
) -> RedfishError:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "manager_id": manager_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Renew",
    }
    return s.action(**b)


@router.delete(
    "/redfish/v1/Managers/{manager_id}/SecurityPolicy/TLS/Server/TrustedCertificates/{certificate_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete75(
    manager_id: str, certificate_id: str, request: Request, response: Response
) -> None:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "manager_id": manager_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
    }
    return s.delete(**b)


@router.get(
    "/redfish/v1/Managers/{manager_id}/SecurityPolicy/TLS/Server/TrustedCertificates/{certificate_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Managers/{manager_id}/SecurityPolicy/TLS/Server/TrustedCertificates/{certificate_id}",
    response_model_exclude_none=True,
)
async def get75(
    manager_id: str, certificate_id: str, request: Request, response: Response
) -> Certificate:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "manager_id": manager_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
    }
    m = cast(Certificate, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/Managers/{manager_id}/SecurityPolicy/TLS/Server/TrustedCertificates/{certificate_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch75(
    manager_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
    body: CertificateOnUpdate,
) -> Certificate:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "manager_id": manager_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Certificate, s.patch(**b))


@router.post(
    "/redfish/v1/Managers/{manager_id}/SecurityPolicy/TLS/Server/TrustedCertificates/{certificate_id}/Actions/Certificate.Rekey",
    response_model_exclude_none=True,
)
@authenticate
async def rekey75(
    manager_id: str, certificate_id: str, request: Request, response: Response, body: RekeyRequest
) -> RedfishError:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "manager_id": manager_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Rekey",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Managers/{manager_id}/SecurityPolicy/TLS/Server/TrustedCertificates/{certificate_id}/Actions/Certificate.Renew",
    response_model_exclude_none=True,
)
@authenticate
async def renew75(
    manager_id: str, certificate_id: str, request: Request, response: Response, body: RenewRequest
) -> RedfishError:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "manager_id": manager_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Renew",
    }
    return s.action(**b)


@router.delete(
    "/redfish/v1/Managers/{manager_id}/SecurityPolicy/TLS/Server/RevokedCertificates/{certificate_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete76(
    manager_id: str, certificate_id: str, request: Request, response: Response
) -> None:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "manager_id": manager_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
    }
    return s.delete(**b)


@router.get(
    "/redfish/v1/Managers/{manager_id}/SecurityPolicy/TLS/Server/RevokedCertificates/{certificate_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Managers/{manager_id}/SecurityPolicy/TLS/Server/RevokedCertificates/{certificate_id}",
    response_model_exclude_none=True,
)
async def get76(
    manager_id: str, certificate_id: str, request: Request, response: Response
) -> Certificate:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "manager_id": manager_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
    }
    m = cast(Certificate, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/Managers/{manager_id}/SecurityPolicy/TLS/Server/RevokedCertificates/{certificate_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch76(
    manager_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
    body: CertificateOnUpdate,
) -> Certificate:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "manager_id": manager_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Certificate, s.patch(**b))


@router.post(
    "/redfish/v1/Managers/{manager_id}/SecurityPolicy/TLS/Server/RevokedCertificates/{certificate_id}/Actions/Certificate.Rekey",
    response_model_exclude_none=True,
)
@authenticate
async def rekey76(
    manager_id: str, certificate_id: str, request: Request, response: Response, body: RekeyRequest
) -> RedfishError:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "manager_id": manager_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Rekey",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Managers/{manager_id}/SecurityPolicy/TLS/Server/RevokedCertificates/{certificate_id}/Actions/Certificate.Renew",
    response_model_exclude_none=True,
)
@authenticate
async def renew76(
    manager_id: str, certificate_id: str, request: Request, response: Response, body: RenewRequest
) -> RedfishError:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "manager_id": manager_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Renew",
    }
    return s.action(**b)


@router.delete(
    "/redfish/v1/Chassis/{chassis_id}/TrustedComponents/{trusted_component_id}/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete77(
    chassis_id: str,
    trusted_component_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
) -> None:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "trusted_component_id": trusted_component_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
    }
    return s.delete(**b)


@router.get(
    "/redfish/v1/Chassis/{chassis_id}/TrustedComponents/{trusted_component_id}/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Chassis/{chassis_id}/TrustedComponents/{trusted_component_id}/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
async def get77(
    chassis_id: str,
    trusted_component_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
) -> Certificate:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "trusted_component_id": trusted_component_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
    }
    m = cast(Certificate, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/Chassis/{chassis_id}/TrustedComponents/{trusted_component_id}/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch77(
    chassis_id: str,
    trusted_component_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
    body: CertificateOnUpdate,
) -> Certificate:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "trusted_component_id": trusted_component_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Certificate, s.patch(**b))


@router.post(
    "/redfish/v1/Chassis/{chassis_id}/TrustedComponents/{trusted_component_id}/Certificates/{certificate_id}/Actions/Certificate.Rekey",
    response_model_exclude_none=True,
)
@authenticate
async def rekey77(
    chassis_id: str,
    trusted_component_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
    body: RekeyRequest,
) -> RedfishError:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "trusted_component_id": trusted_component_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Rekey",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Chassis/{chassis_id}/TrustedComponents/{trusted_component_id}/Certificates/{certificate_id}/Actions/Certificate.Renew",
    response_model_exclude_none=True,
)
@authenticate
async def renew77(
    chassis_id: str,
    trusted_component_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
    body: RenewRequest,
) -> RedfishError:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "trusted_component_id": trusted_component_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Renew",
    }
    return s.action(**b)


@router.delete(
    "/redfish/v1/AccountService/OutboundConnections/{outbound_connection_id}/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete78(
    outbound_connection_id: str, certificate_id: str, request: Request, response: Response
) -> None:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "outbound_connection_id": outbound_connection_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
    }
    return s.delete(**b)


@router.get(
    "/redfish/v1/AccountService/OutboundConnections/{outbound_connection_id}/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/AccountService/OutboundConnections/{outbound_connection_id}/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
async def get78(
    outbound_connection_id: str, certificate_id: str, request: Request, response: Response
) -> Certificate:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "outbound_connection_id": outbound_connection_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
    }
    m = cast(Certificate, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/AccountService/OutboundConnections/{outbound_connection_id}/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch78(
    outbound_connection_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
    body: CertificateOnUpdate,
) -> Certificate:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "outbound_connection_id": outbound_connection_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Certificate, s.patch(**b))


@router.post(
    "/redfish/v1/AccountService/OutboundConnections/{outbound_connection_id}/Certificates/{certificate_id}/Actions/Certificate.Rekey",
    response_model_exclude_none=True,
)
@authenticate
async def rekey78(
    outbound_connection_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
    body: RekeyRequest,
) -> RedfishError:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "outbound_connection_id": outbound_connection_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Rekey",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/AccountService/OutboundConnections/{outbound_connection_id}/Certificates/{certificate_id}/Actions/Certificate.Renew",
    response_model_exclude_none=True,
)
@authenticate
async def renew78(
    outbound_connection_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
    body: RenewRequest,
) -> RedfishError:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "outbound_connection_id": outbound_connection_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Renew",
    }
    return s.action(**b)


@router.delete(
    "/redfish/v1/AccountService/OutboundConnections/{outbound_connection_id}/ClientCertificates/{certificate_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete79(
    outbound_connection_id: str, certificate_id: str, request: Request, response: Response
) -> None:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "outbound_connection_id": outbound_connection_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
    }
    return s.delete(**b)


@router.get(
    "/redfish/v1/AccountService/OutboundConnections/{outbound_connection_id}/ClientCertificates/{certificate_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/AccountService/OutboundConnections/{outbound_connection_id}/ClientCertificates/{certificate_id}",
    response_model_exclude_none=True,
)
async def get79(
    outbound_connection_id: str, certificate_id: str, request: Request, response: Response
) -> Certificate:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "outbound_connection_id": outbound_connection_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
    }
    m = cast(Certificate, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/AccountService/OutboundConnections/{outbound_connection_id}/ClientCertificates/{certificate_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch79(
    outbound_connection_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
    body: CertificateOnUpdate,
) -> Certificate:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "outbound_connection_id": outbound_connection_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Certificate, s.patch(**b))


@router.post(
    "/redfish/v1/AccountService/OutboundConnections/{outbound_connection_id}/ClientCertificates/{certificate_id}/Actions/Certificate.Rekey",
    response_model_exclude_none=True,
)
@authenticate
async def rekey79(
    outbound_connection_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
    body: RekeyRequest,
) -> RedfishError:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "outbound_connection_id": outbound_connection_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Rekey",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/AccountService/OutboundConnections/{outbound_connection_id}/ClientCertificates/{certificate_id}/Actions/Certificate.Renew",
    response_model_exclude_none=True,
)
@authenticate
async def renew79(
    outbound_connection_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
    body: RenewRequest,
) -> RedfishError:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "outbound_connection_id": outbound_connection_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Renew",
    }
    return s.action(**b)


@router.delete(
    "/redfish/v1/Chassis/{chassis_id}/PowerSubsystem/PowerSupplies/{power_supply_id}/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete80(
    chassis_id: str,
    power_supply_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
) -> None:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "power_supply_id": power_supply_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
    }
    return s.delete(**b)


@router.get(
    "/redfish/v1/Chassis/{chassis_id}/PowerSubsystem/PowerSupplies/{power_supply_id}/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Chassis/{chassis_id}/PowerSubsystem/PowerSupplies/{power_supply_id}/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
async def get80(
    chassis_id: str,
    power_supply_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
) -> Certificate:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "power_supply_id": power_supply_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
    }
    m = cast(Certificate, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/Chassis/{chassis_id}/PowerSubsystem/PowerSupplies/{power_supply_id}/Certificates/{certificate_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch80(
    chassis_id: str,
    power_supply_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
    body: CertificateOnUpdate,
) -> Certificate:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "power_supply_id": power_supply_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Certificate, s.patch(**b))


@router.post(
    "/redfish/v1/Chassis/{chassis_id}/PowerSubsystem/PowerSupplies/{power_supply_id}/Certificates/{certificate_id}/Actions/Certificate.Rekey",
    response_model_exclude_none=True,
)
@authenticate
async def rekey80(
    chassis_id: str,
    power_supply_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
    body: RekeyRequest,
) -> RedfishError:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "power_supply_id": power_supply_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Rekey",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Chassis/{chassis_id}/PowerSubsystem/PowerSupplies/{power_supply_id}/Certificates/{certificate_id}/Actions/Certificate.Renew",
    response_model_exclude_none=True,
)
@authenticate
async def renew80(
    chassis_id: str,
    power_supply_id: str,
    certificate_id: str,
    request: Request,
    response: Response,
    body: RenewRequest,
) -> RedfishError:
    s: Service = get_service(Certificate, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "power_supply_id": power_supply_id,
        "certificate_id": certificate_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Renew",
    }
    return s.action(**b)
