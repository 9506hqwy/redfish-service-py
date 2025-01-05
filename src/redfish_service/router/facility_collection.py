from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.facility_collection import FacilityCollection
from ..service import Service, find_service

router = APIRouter()


@router.get("/redfish/v1/Facilities", response_model_exclude_none=True)
@authenticate
async def get1(request: Request, response: Response) -> FacilityCollection:
    s: Service = find_service(FacilityCollection)
    b: dict[str, Any] = {"request": request, "response": response}

    response.headers["OData-Version"] = "4.0"

    return cast(FacilityCollection, s.get(**b))
