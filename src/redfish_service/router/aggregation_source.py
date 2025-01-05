from typing import Any, cast

from fastapi import APIRouter

from ..authenticate import authenticate
from ..model.aggregation_source import AggregationSource
from ..service import Service, find_service

router = APIRouter()


@router.get(
    "/redfish/v1/AggregationService/AggregationSources/{aggregation_source_id}",
    response_model_exclude_none=True,
)
@authenticate
async def get1(aggregation_source_id: str) -> AggregationSource:
    s: Service = find_service(AggregationSource)
    b: dict[str, Any] = {"aggregation_source_id": aggregation_source_id}
    return cast(AggregationSource, s.get(**b))
