from typing import Any, cast

from fastapi import APIRouter

from ..model.power_domain_collection import PowerDomainCollection
from ..service import Service, find_service
from . import authenticate

router = APIRouter()


@router.get("/redfish/v1/Facilities/{facility_id}/PowerDomains", response_model_exclude_none=True)
@authenticate
async def get1(facility_id: str) -> PowerDomainCollection:
    s: Service = find_service(PowerDomainCollection)
    b: dict[str, Any] = {"facility_id": facility_id}
    return cast(PowerDomainCollection, s.get(**b))
