from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.composition_reservation_collection import CompositionReservationCollection
from ..service import Service, find_service

router = APIRouter()


@router.get(
    "/redfish/v1/CompositionService/CompositionReservations", response_model_exclude_none=True
)
@authenticate
async def get1(request: Request, response: Response) -> CompositionReservationCollection:
    s: Service = find_service(CompositionReservationCollection)
    b: dict[str, Any] = {"request": request, "response": response}

    response.headers["OData-Version"] = "4.0"

    return cast(CompositionReservationCollection, s.get(**b))
