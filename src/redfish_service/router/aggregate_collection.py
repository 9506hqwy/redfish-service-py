from typing import Any, cast

from fastapi import APIRouter

from ..authenticate import authenticate
from ..model.aggregate_collection import AggregateCollection
from ..service import Service, find_service

router = APIRouter()


@router.get("/redfish/v1/AggregationService/Aggregates", response_model_exclude_none=True)
@authenticate
async def get1() -> AggregateCollection:
    s: Service = find_service(AggregateCollection)
    b: dict[str, Any] = {}
    return cast(AggregateCollection, s.get(**b))
