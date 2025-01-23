from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..model.composition_reservation_collection import CompositionReservationCollection
from ..service import Service
from ..util import get_service, set_link_header

router = APIRouter()


@router.get(
    "/redfish/v1/CompositionService/CompositionReservations", response_model_exclude_none=True
)
@router.head(
    "/redfish/v1/CompositionService/CompositionReservations", response_model_exclude_none=True
)
async def get1(request: Request, response: Response) -> CompositionReservationCollection:
    s: Service = get_service(CompositionReservationCollection, request)
    b: dict[str, Any] = {"request": request, "response": response}
    m = cast(CompositionReservationCollection, s.get(**b))
    set_link_header(m, response)
    return m
