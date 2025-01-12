from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.metric_report_definition import MetricReportDefinition, MetricReportDefinitionOnUpdate
from ..service import Service
from ..util import get_service

router = APIRouter()


@router.delete(
    "/redfish/v1/TelemetryService/MetricReportDefinitions/{metric_report_definition_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete1(metric_report_definition_id: str, request: Request, response: Response) -> None:
    s: Service = get_service(MetricReportDefinition, request)
    b: dict[str, Any] = {
        "metric_report_definition_id": metric_report_definition_id,
        "request": request,
        "response": response,
    }
    return s.delete(**b)


@router.get(
    "/redfish/v1/TelemetryService/MetricReportDefinitions/{metric_report_definition_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/TelemetryService/MetricReportDefinitions/{metric_report_definition_id}",
    response_model_exclude_none=True,
)
async def get1(
    metric_report_definition_id: str, request: Request, response: Response
) -> MetricReportDefinition:
    s: Service = get_service(MetricReportDefinition, request)
    b: dict[str, Any] = {
        "metric_report_definition_id": metric_report_definition_id,
        "request": request,
        "response": response,
    }
    return cast(MetricReportDefinition, s.get(**b))


@router.patch(
    "/redfish/v1/TelemetryService/MetricReportDefinitions/{metric_report_definition_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch1(
    metric_report_definition_id: str,
    request: Request,
    response: Response,
    body: MetricReportDefinitionOnUpdate,
) -> MetricReportDefinition:
    s: Service = get_service(MetricReportDefinition, request)
    b: dict[str, Any] = {
        "metric_report_definition_id": metric_report_definition_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(MetricReportDefinition, s.patch(**b))
