from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.power_domain import PowerDomain, PowerDomainOnUpdate
from ..service import Service
from ..util import get_service, set_link_header

router = APIRouter()


@router.delete(
    "/redfish/v1/Facilities/{facility_id}/PowerDomains/{power_domain_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete1(
    facility_id: str, power_domain_id: str, request: Request, response: Response
) -> None:
    s: Service = get_service(PowerDomain, request)
    b: dict[str, Any] = {
        "facility_id": facility_id,
        "power_domain_id": power_domain_id,
        "request": request,
        "response": response,
    }
    return s.delete(**b)


@router.get(
    "/redfish/v1/Facilities/{facility_id}/PowerDomains/{power_domain_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Facilities/{facility_id}/PowerDomains/{power_domain_id}",
    response_model_exclude_none=True,
)
async def get1(
    facility_id: str, power_domain_id: str, request: Request, response: Response
) -> PowerDomain:
    s: Service = get_service(PowerDomain, request)
    b: dict[str, Any] = {
        "facility_id": facility_id,
        "power_domain_id": power_domain_id,
        "request": request,
        "response": response,
    }
    m = cast(PowerDomain, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/Facilities/{facility_id}/PowerDomains/{power_domain_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch1(
    facility_id: str,
    power_domain_id: str,
    request: Request,
    response: Response,
    body: PowerDomainOnUpdate,
) -> PowerDomain:
    s: Service = get_service(PowerDomain, request)
    b: dict[str, Any] = {
        "facility_id": facility_id,
        "power_domain_id": power_domain_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(PowerDomain, s.patch(**b))
