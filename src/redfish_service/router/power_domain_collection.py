from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.power_domain import PowerDomain, PowerDomainOnCreate
from ..model.power_domain_collection import PowerDomainCollection
from ..service import Service, ServiceCollection, find_service, find_service_collection

router = APIRouter()


@router.get("/redfish/v1/Facilities/{facility_id}/PowerDomains", response_model_exclude_none=True)
@router.head("/redfish/v1/Facilities/{facility_id}/PowerDomains", response_model_exclude_none=True)
async def get1(facility_id: str, request: Request, response: Response) -> PowerDomainCollection:
    s: Service = find_service(PowerDomainCollection)
    b: dict[str, Any] = {"facility_id": facility_id, "request": request, "response": response}

    response.headers["OData-Version"] = "4.0"

    return cast(PowerDomainCollection, s.get(**b))


@router.post("/redfish/v1/Facilities/{facility_id}/PowerDomains", response_model_exclude_none=True)
@router.post(
    "/redfish/v1/Facilities/{facility_id}/PowerDomains/Members", response_model_exclude_none=True
)
@authenticate
async def post1(
    facility_id: str, request: Request, response: Response, body: PowerDomainOnCreate
) -> PowerDomain:
    s: ServiceCollection = find_service_collection(PowerDomainCollection)
    b: dict[str, Any] = {
        "facility_id": facility_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(PowerDomain, s.post(**b))
