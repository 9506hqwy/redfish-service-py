from typing import Any, cast

from fastapi import APIRouter

from ..authenticate import authenticate
from ..model.cable_collection import CableCollection
from ..service import Service, find_service

router = APIRouter()


@router.get("/redfish/v1/Cables", response_model_exclude_none=True)
@authenticate
async def get1() -> CableCollection:
    s: Service = find_service(CableCollection)
    b: dict[str, Any] = {}
    return cast(CableCollection, s.get(**b))
