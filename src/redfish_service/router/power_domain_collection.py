from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.power_domain_collection import PowerDomainCollection
from ..service import Service, find_service

router = APIRouter()


@router.get("/redfish/v1/Facilities/{facility_id}/PowerDomains", response_model_exclude_none=True)
@authenticate
async def get1(facility_id: str, request: Request, response: Response) -> PowerDomainCollection:
    s: Service = find_service(PowerDomainCollection)
    b: dict[str, Any] = {"facility_id": facility_id, "request": request, "response": response}

    response.headers["OData-Version"] = "4.0"

    return cast(PowerDomainCollection, s.get(**b))
