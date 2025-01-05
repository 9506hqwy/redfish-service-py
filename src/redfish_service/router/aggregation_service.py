from typing import Any, cast

from fastapi import APIRouter

from ..authenticate import authenticate
from ..model.aggregation_service import AggregationService
from ..service import Service, find_service

router = APIRouter()


@router.get("/redfish/v1/AggregationService", response_model_exclude_none=True)
@authenticate
async def get1() -> AggregationService:
    s: Service = find_service(AggregationService)
    b: dict[str, Any] = {}
    return cast(AggregationService, s.get(**b))
