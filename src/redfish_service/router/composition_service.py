from typing import Any, cast

from fastapi import APIRouter

from ..authenticate import authenticate
from ..model.composition_service import CompositionService
from ..service import Service, find_service

router = APIRouter()


@router.get("/redfish/v1/CompositionService", response_model_exclude_none=True)
@authenticate
async def get1() -> CompositionService:
    s: Service = find_service(CompositionService)
    b: dict[str, Any] = {}
    return cast(CompositionService, s.get(**b))
