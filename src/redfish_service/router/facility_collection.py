from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.facility import Facility, FacilityOnCreate
from ..model.facility_collection import FacilityCollection
from ..service import Service, ServiceCollection
from ..util import get_service, get_service_collection, set_link_header

router = APIRouter()


@router.get("/redfish/v1/Facilities", response_model_exclude_none=True)
@router.head("/redfish/v1/Facilities", response_model_exclude_none=True)
async def get1(request: Request, response: Response) -> FacilityCollection:
    s: Service = get_service(FacilityCollection, request)
    b: dict[str, Any] = {"request": request, "response": response}
    m = cast(FacilityCollection, s.get(**b))
    set_link_header(m, response)
    return m


@router.post("/redfish/v1/Facilities", response_model_exclude_none=True)
@router.post("/redfish/v1/Facilities/Members", response_model_exclude_none=True)
@authenticate
async def post1(request: Request, response: Response, body: FacilityOnCreate) -> Facility:
    s: ServiceCollection = get_service_collection(FacilityCollection, request)
    b: dict[str, Any] = {"request": request, "response": response, "body": body}
    return cast(Facility, s.post(**b))
