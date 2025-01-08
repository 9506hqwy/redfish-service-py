from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..model.aggregation_service import AggregationService
from ..service import Service, find_service

router = APIRouter()


@router.get("/redfish/v1/AggregationService", response_model_exclude_none=True)
@router.head("/redfish/v1/AggregationService", response_model_exclude_none=True)
async def get1(request: Request, response: Response) -> AggregationService:
    s: Service = find_service(AggregationService)
    b: dict[str, Any] = {"request": request, "response": response}

    response.headers["OData-Version"] = "4.0"

    return cast(AggregationService, s.get(**b))
