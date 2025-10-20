from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.certificate_enrollment import CertificateEnrollment, CertificateEnrollmentOnCreate
from ..model.certificate_enrollment_collection import CertificateEnrollmentCollection
from ..service import Service, ServiceCollection
from ..util import get_service, get_service_collection, set_link_header

router = APIRouter()


@router.get(
    "/redfish/v1/CertificateService/CertificateEnrollments", response_model_exclude_none=True
)
@router.head(
    "/redfish/v1/CertificateService/CertificateEnrollments", response_model_exclude_none=True
)
async def get1(request: Request, response: Response) -> CertificateEnrollmentCollection:
    s: Service = get_service(CertificateEnrollmentCollection, request)
    b: dict[str, Any] = {"request": request, "response": response}
    m = cast(CertificateEnrollmentCollection, s.get(**b))
    set_link_header(m, response)
    return m


@router.post(
    "/redfish/v1/CertificateService/CertificateEnrollments", response_model_exclude_none=True
)
@router.post(
    "/redfish/v1/CertificateService/CertificateEnrollments/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post1(
    request: Request, response: Response, body: CertificateEnrollmentOnCreate
) -> CertificateEnrollment:
    s: ServiceCollection = get_service_collection(CertificateEnrollmentCollection, request)
    b: dict[str, Any] = {"request": request, "response": response, "body": body}
    return cast(CertificateEnrollment, s.post(**b))
