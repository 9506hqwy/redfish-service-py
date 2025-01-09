from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.aggregation_source import AggregationSource
from ..service import Service, find_service

router = APIRouter()


@router.delete(
    "/redfish/v1/AggregationService/AggregationSources/{aggregation_source_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete1(aggregation_source_id: str, request: Request, response: Response) -> None:
    s: Service = find_service(AggregationSource)
    b: dict[str, Any] = {
        "aggregation_source_id": aggregation_source_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return s.delete(**b)


@router.get(
    "/redfish/v1/AggregationService/AggregationSources/{aggregation_source_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/AggregationService/AggregationSources/{aggregation_source_id}",
    response_model_exclude_none=True,
)
async def get1(
    aggregation_source_id: str, request: Request, response: Response
) -> AggregationSource:
    s: Service = find_service(AggregationSource)
    b: dict[str, Any] = {
        "aggregation_source_id": aggregation_source_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(AggregationSource, s.get(**b))
