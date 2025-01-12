from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..model.metric_report_collection import MetricReportCollection
from ..service import Service
from ..util import get_service

router = APIRouter()


@router.get("/redfish/v1/TelemetryService/MetricReports", response_model_exclude_none=True)
@router.head("/redfish/v1/TelemetryService/MetricReports", response_model_exclude_none=True)
async def get1(request: Request, response: Response) -> MetricReportCollection:
    s: Service = get_service(MetricReportCollection, request)
    b: dict[str, Any] = {"request": request, "response": response}
    return cast(MetricReportCollection, s.get(**b))
