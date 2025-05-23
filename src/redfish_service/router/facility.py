from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.facility import Facility, FacilityOnUpdate
from ..service import Service
from ..util import get_service, set_link_header

router = APIRouter()


@router.delete("/redfish/v1/Facilities/{facility_id}", response_model_exclude_none=True)
@authenticate
async def delete1(facility_id: str, request: Request, response: Response) -> None:
    s: Service = get_service(Facility, request)
    b: dict[str, Any] = {"facility_id": facility_id, "request": request, "response": response}
    return s.delete(**b)


@router.get("/redfish/v1/Facilities/{facility_id}", response_model_exclude_none=True)
@router.head("/redfish/v1/Facilities/{facility_id}", response_model_exclude_none=True)
async def get1(facility_id: str, request: Request, response: Response) -> Facility:
    s: Service = get_service(Facility, request)
    b: dict[str, Any] = {"facility_id": facility_id, "request": request, "response": response}
    m = cast(Facility, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch("/redfish/v1/Facilities/{facility_id}", response_model_exclude_none=True)
@authenticate
async def patch1(
    facility_id: str, request: Request, response: Response, body: FacilityOnUpdate
) -> Facility:
    s: Service = get_service(Facility, request)
    b: dict[str, Any] = {
        "facility_id": facility_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Facility, s.patch(**b))
