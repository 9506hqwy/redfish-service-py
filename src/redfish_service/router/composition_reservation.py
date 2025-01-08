from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..model.composition_reservation import CompositionReservation
from ..service import Service, find_service

router = APIRouter()


@router.get(
    "/redfish/v1/CompositionService/CompositionReservations/{composition_reservation_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/CompositionService/CompositionReservations/{composition_reservation_id}",
    response_model_exclude_none=True,
)
async def get1(
    composition_reservation_id: str, request: Request, response: Response
) -> CompositionReservation:
    s: Service = find_service(CompositionReservation)
    b: dict[str, Any] = {
        "composition_reservation_id": composition_reservation_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(CompositionReservation, s.get(**b))
