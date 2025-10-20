from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.certificate_enrollment import (
    CertificateEnrollment,
    CertificateEnrollmentOnUpdate,
)
from ..service import Service
from ..util import get_service, set_link_header

router = APIRouter()


@router.delete(
    "/redfish/v1/CertificateService/CertificateEnrollments/{certificate_enrollment_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete1(certificate_enrollment_id: str, request: Request, response: Response) -> None:
    s: Service = get_service(CertificateEnrollment, request)
    b: dict[str, Any] = {
        "certificate_enrollment_id": certificate_enrollment_id,
        "request": request,
        "response": response,
    }
    return s.delete(**b)


@router.get(
    "/redfish/v1/CertificateService/CertificateEnrollments/{certificate_enrollment_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/CertificateService/CertificateEnrollments/{certificate_enrollment_id}",
    response_model_exclude_none=True,
)
async def get1(
    certificate_enrollment_id: str, request: Request, response: Response
) -> CertificateEnrollment:
    s: Service = get_service(CertificateEnrollment, request)
    b: dict[str, Any] = {
        "certificate_enrollment_id": certificate_enrollment_id,
        "request": request,
        "response": response,
    }
    m = cast(CertificateEnrollment, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/CertificateService/CertificateEnrollments/{certificate_enrollment_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch1(
    certificate_enrollment_id: str,
    request: Request,
    response: Response,
    body: CertificateEnrollmentOnUpdate,
) -> CertificateEnrollment:
    s: Service = get_service(CertificateEnrollment, request)
    b: dict[str, Any] = {
        "certificate_enrollment_id": certificate_enrollment_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(CertificateEnrollment, s.patch(**b))
