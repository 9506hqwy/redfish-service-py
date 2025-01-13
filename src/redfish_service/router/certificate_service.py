from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.certificate_service import (
    CertificateService,
    GenerateCsrRequest,
    ReplaceCertificateRequest,
)
from ..model.redfish_error import RedfishError
from ..service import Service
from ..util import get_service

router = APIRouter()


@router.get("/redfish/v1/CertificateService", response_model_exclude_none=True)
@router.head("/redfish/v1/CertificateService", response_model_exclude_none=True)
async def get1(request: Request, response: Response) -> CertificateService:
    s: Service = get_service(CertificateService, request)
    b: dict[str, Any] = {"request": request, "response": response}
    return cast(CertificateService, s.get(**b))


@router.post(
    "/redfish/v1/CertificateService/Actions/CertificateService.GenerateCSR",
    response_model_exclude_none=True,
)
@authenticate
async def generate_csr1(
    request: Request, response: Response, body: GenerateCsrRequest
) -> RedfishError:
    s: Service = get_service(CertificateService, request)
    b: dict[str, Any] = {
        "request": request,
        "response": response,
        "body": body,
        "action": "GenerateCSR",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/CertificateService/Actions/CertificateService.ReplaceCertificate",
    response_model_exclude_none=True,
)
@authenticate
async def replace_certificate1(
    request: Request, response: Response, body: ReplaceCertificateRequest
) -> RedfishError:
    s: Service = get_service(CertificateService, request)
    b: dict[str, Any] = {
        "request": request,
        "response": response,
        "body": body,
        "action": "ReplaceCertificate",
    }
    return s.action(**b)
