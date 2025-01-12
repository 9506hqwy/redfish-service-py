from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.composition_reservation import CompositionReservation
from ..service import Service
from ..util import get_service

router = APIRouter()


@router.delete(
    "/redfish/v1/CompositionService/CompositionReservations/{composition_reservation_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete1(composition_reservation_id: str, request: Request, response: Response) -> None:
    s: Service = get_service(CompositionReservation, request)
    b: dict[str, Any] = {
        "composition_reservation_id": composition_reservation_id,
        "request": request,
        "response": response,
    }
    return s.delete(**b)


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
    s: Service = get_service(CompositionReservation, request)
    b: dict[str, Any] = {
        "composition_reservation_id": composition_reservation_id,
        "request": request,
        "response": response,
    }
    return cast(CompositionReservation, s.get(**b))
