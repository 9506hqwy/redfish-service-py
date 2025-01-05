from typing import Any, cast

from fastapi import APIRouter

from ..model.composition_reservation_collection import CompositionReservationCollection
from ..service import Service, find_service
from . import authenticate

router = APIRouter()


@router.get(
    "/redfish/v1/CompositionService/CompositionReservations", response_model_exclude_none=True
)
@authenticate
async def get1() -> CompositionReservationCollection:
    s: Service = find_service(CompositionReservationCollection)
    b: dict[str, Any] = {}
    return cast(CompositionReservationCollection, s.get(**b))
