from typing import Any, cast

from fastapi import APIRouter

from ..authenticate import authenticate
from ..model.composition_reservation import CompositionReservation
from ..service import Service, find_service

router = APIRouter()


@router.get(
    "/redfish/v1/CompositionService/CompositionReservations/{composition_reservation_id}",
    response_model_exclude_none=True,
)
@authenticate
async def get1(composition_reservation_id: str) -> CompositionReservation:
    s: Service = find_service(CompositionReservation)
    b: dict[str, Any] = {"composition_reservation_id": composition_reservation_id}
    return cast(CompositionReservation, s.get(**b))
