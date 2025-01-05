from typing import Any, cast

from fastapi import APIRouter

from ..model.metric_report_collection import MetricReportCollection
from ..service import Service, find_service
from . import authenticate

router = APIRouter()


@router.get("/redfish/v1/TelemetryService/MetricReports", response_model_exclude_none=True)
@authenticate
async def get1() -> MetricReportCollection:
    s: Service = find_service(MetricReportCollection)
    b: dict[str, Any] = {}
    return cast(MetricReportCollection, s.get(**b))
