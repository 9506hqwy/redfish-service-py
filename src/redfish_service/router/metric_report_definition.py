from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.metric_report_definition import MetricReportDefinition
from ..service import Service, find_service

router = APIRouter()


@router.get(
    "/redfish/v1/TelemetryService/MetricReportDefinitions/{metric_report_definition_id}",
    response_model_exclude_none=True,
)
@authenticate
async def get1(
    metric_report_definition_id: str, request: Request, response: Response
) -> MetricReportDefinition:
    s: Service = find_service(MetricReportDefinition)
    b: dict[str, Any] = {
        "metric_report_definition_id": metric_report_definition_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(MetricReportDefinition, s.get(**b))
