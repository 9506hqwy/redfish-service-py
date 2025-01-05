from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.power_domain import PowerDomain
from ..service import Service, find_service

router = APIRouter()


@router.get(
    "/redfish/v1/Facilities/{facility_id}/PowerDomains/{power_domain_id}",
    response_model_exclude_none=True,
)
@authenticate
async def get1(
    facility_id: str, power_domain_id: str, request: Request, response: Response
) -> PowerDomain:
    s: Service = find_service(PowerDomain)
    b: dict[str, Any] = {
        "facility_id": facility_id,
        "power_domain_id": power_domain_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(PowerDomain, s.get(**b))
