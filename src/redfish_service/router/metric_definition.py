from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.metric_definition import MetricDefinition
from ..service import Service, find_service

router = APIRouter()


@router.delete(
    "/redfish/v1/TelemetryService/MetricDefinitions/{metric_definition_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete1(metric_definition_id: str, request: Request, response: Response) -> None:
    s: Service = find_service(MetricDefinition)
    b: dict[str, Any] = {
        "metric_definition_id": metric_definition_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return s.delete(**b)


@router.get(
    "/redfish/v1/TelemetryService/MetricDefinitions/{metric_definition_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/TelemetryService/MetricDefinitions/{metric_definition_id}",
    response_model_exclude_none=True,
)
async def get1(
    metric_definition_id: str, request: Request, response: Response
) -> MetricDefinition:
    s: Service = find_service(MetricDefinition)
    b: dict[str, Any] = {
        "metric_definition_id": metric_definition_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(MetricDefinition, s.get(**b))
