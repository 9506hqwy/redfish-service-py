from typing import Any, cast

from fastapi import APIRouter

from ..model.metric_report_definition import MetricReportDefinition
from ..service import Service, find_service
from . import authenticate

router = APIRouter()


@router.get(
    "/redfish/v1/TelemetryService/MetricReportDefinitions/{metric_report_definition_id}",
    response_model_exclude_none=True,
)
@authenticate
async def get1(metric_report_definition_id: str) -> MetricReportDefinition:
    s: Service = find_service(MetricReportDefinition)
    b: dict[str, Any] = {"metric_report_definition_id": metric_report_definition_id}
    return cast(MetricReportDefinition, s.get(**b))
