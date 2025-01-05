from typing import Any, cast

from fastapi import APIRouter

from ..authenticate import authenticate
from ..model.facility_collection import FacilityCollection
from ..service import Service, find_service

router = APIRouter()


@router.get("/redfish/v1/Facilities", response_model_exclude_none=True)
@authenticate
async def get1() -> FacilityCollection:
    s: Service = find_service(FacilityCollection)
    b: dict[str, Any] = {}
    return cast(FacilityCollection, s.get(**b))
