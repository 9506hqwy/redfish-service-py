from typing import Any, cast

from fastapi import APIRouter

from ..model.cable import Cable
from ..service import Service, find_service
from . import authenticate

router = APIRouter()


@router.get("/redfish/v1/Cables/{cable_id}", response_model_exclude_none=True)
@authenticate
async def get1(cable_id: str) -> Cable:
    s: Service = find_service(Cable)
    b: dict[str, Any] = {"cable_id": cable_id}
    return cast(Cable, s.get(**b))
