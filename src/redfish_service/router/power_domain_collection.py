from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.power_domain import PowerDomain, PowerDomainOnCreate
from ..model.power_domain_collection import PowerDomainCollection
from ..service import Service, ServiceCollection
from ..util import get_service, get_service_collection, set_link_header

router = APIRouter()


@router.get("/redfish/v1/Facilities/{facility_id}/PowerDomains", response_model_exclude_none=True)
@router.head("/redfish/v1/Facilities/{facility_id}/PowerDomains", response_model_exclude_none=True)
async def get1(facility_id: str, request: Request, response: Response) -> PowerDomainCollection:
    s: Service = get_service(PowerDomainCollection, request)
    b: dict[str, Any] = {"facility_id": facility_id, "request": request, "response": response}
    m = cast(PowerDomainCollection, s.get(**b))
    set_link_header(m, response)
    return m


@router.post("/redfish/v1/Facilities/{facility_id}/PowerDomains", response_model_exclude_none=True)
@router.post(
    "/redfish/v1/Facilities/{facility_id}/PowerDomains/Members", response_model_exclude_none=True
)
@authenticate
async def post1(
    facility_id: str, request: Request, response: Response, body: PowerDomainOnCreate
) -> PowerDomain:
    s: ServiceCollection = get_service_collection(PowerDomainCollection, request)
    b: dict[str, Any] = {
        "facility_id": facility_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(PowerDomain, s.post(**b))
