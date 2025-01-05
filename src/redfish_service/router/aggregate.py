from typing import Any, cast

from fastapi import APIRouter

from ..authenticate import authenticate
from ..model.aggregate import Aggregate
from ..service import Service, find_service

router = APIRouter()


@router.get(
    "/redfish/v1/AggregationService/Aggregates/{aggregate_id}", response_model_exclude_none=True
)
@authenticate
async def get1(aggregate_id: str) -> Aggregate:
    s: Service = find_service(Aggregate)
    b: dict[str, Any] = {"aggregate_id": aggregate_id}
    return cast(Aggregate, s.get(**b))
