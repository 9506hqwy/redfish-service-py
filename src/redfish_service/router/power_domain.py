from typing import Any, cast

from fastapi import APIRouter

from ..model.power_domain import PowerDomain
from ..service import Service, find_service
from . import authenticate

router = APIRouter()


@router.get(
    "/redfish/v1/Facilities/{facility_id}/PowerDomains/{power_domain_id}",
    response_model_exclude_none=True,
)
@authenticate
async def get1(facility_id: str, power_domain_id: str) -> PowerDomain:
    s: Service = find_service(PowerDomain)
    b: dict[str, Any] = {"facility_id": facility_id, "power_domain_id": power_domain_id}
    return cast(PowerDomain, s.get(**b))
