from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.aggregation_service import AggregationService, AggregationServiceOnUpdate
from ..service import Service
from ..util import get_service

router = APIRouter()


@router.get("/redfish/v1/AggregationService", response_model_exclude_none=True)
@router.head("/redfish/v1/AggregationService", response_model_exclude_none=True)
async def get1(request: Request, response: Response) -> AggregationService:
    s: Service = get_service(AggregationService, request)
    b: dict[str, Any] = {"request": request, "response": response}

    response.headers["OData-Version"] = "4.0"

    return cast(AggregationService, s.get(**b))


@router.patch("/redfish/v1/AggregationService", response_model_exclude_none=True)
@authenticate
async def patch1(
    request: Request, response: Response, body: AggregationServiceOnUpdate
) -> AggregationService:
    s: Service = get_service(AggregationService, request)
    b: dict[str, Any] = {"request": request, "response": response, "body": body}

    response.headers["OData-Version"] = "4.0"

    return cast(AggregationService, s.patch(**b))
