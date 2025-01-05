from typing import Any, cast

from fastapi import APIRouter

from ..authenticate import authenticate
from ..model.facility import Facility
from ..service import Service, find_service

router = APIRouter()


@router.get("/redfish/v1/Facilities/{facility_id}", response_model_exclude_none=True)
@authenticate
async def get1(facility_id: str) -> Facility:
    s: Service = find_service(Facility)
    b: dict[str, Any] = {"facility_id": facility_id}
    return cast(Facility, s.get(**b))
