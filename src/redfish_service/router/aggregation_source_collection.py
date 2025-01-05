from typing import Any, cast

from fastapi import APIRouter

from ..authenticate import authenticate
from ..model.aggregation_source_collection import AggregationSourceCollection
from ..service import Service, find_service

router = APIRouter()


@router.get("/redfish/v1/AggregationService/AggregationSources", response_model_exclude_none=True)
@authenticate
async def get1() -> AggregationSourceCollection:
    s: Service = find_service(AggregationSourceCollection)
    b: dict[str, Any] = {}
    return cast(AggregationSourceCollection, s.get(**b))
