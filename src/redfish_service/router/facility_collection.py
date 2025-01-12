from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.facility import Facility, FacilityOnCreate
from ..model.facility_collection import FacilityCollection
from ..service import Service, ServiceCollection
from ..util import get_service, get_service_collection

router = APIRouter()


@router.get("/redfish/v1/Facilities", response_model_exclude_none=True)
@router.head("/redfish/v1/Facilities", response_model_exclude_none=True)
async def get1(request: Request, response: Response) -> FacilityCollection:
    s: Service = get_service(FacilityCollection, request)
    b: dict[str, Any] = {"request": request, "response": response}

    response.headers["OData-Version"] = "4.0"

    return cast(FacilityCollection, s.get(**b))


@router.post("/redfish/v1/Facilities", response_model_exclude_none=True)
@router.post("/redfish/v1/Facilities/Members", response_model_exclude_none=True)
@authenticate
async def post1(request: Request, response: Response, body: FacilityOnCreate) -> Facility:
    s: ServiceCollection = get_service_collection(FacilityCollection, request)
    b: dict[str, Any] = {"request": request, "response": response, "body": body}

    response.headers["OData-Version"] = "4.0"

    return cast(Facility, s.post(**b))
