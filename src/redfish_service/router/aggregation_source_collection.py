from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.aggregation_source import AggregationSource, AggregationSourceOnCreate
from ..model.aggregation_source_collection import AggregationSourceCollection
from ..service import Service, ServiceCollection
from ..util import get_service, get_service_collection

router = APIRouter()


@router.get("/redfish/v1/AggregationService/AggregationSources", response_model_exclude_none=True)
@router.head("/redfish/v1/AggregationService/AggregationSources", response_model_exclude_none=True)
async def get1(request: Request, response: Response) -> AggregationSourceCollection:
    s: Service = get_service(AggregationSourceCollection, request)
    b: dict[str, Any] = {"request": request, "response": response}
    return cast(AggregationSourceCollection, s.get(**b))


@router.post("/redfish/v1/AggregationService/AggregationSources", response_model_exclude_none=True)
@router.post(
    "/redfish/v1/AggregationService/AggregationSources/Members", response_model_exclude_none=True
)
@authenticate
async def post1(
    request: Request, response: Response, body: AggregationSourceOnCreate
) -> AggregationSource:
    s: ServiceCollection = get_service_collection(AggregationSourceCollection, request)
    b: dict[str, Any] = {"request": request, "response": response, "body": body}
    return cast(AggregationSource, s.post(**b))
