from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.metric_report_definition import MetricReportDefinition, MetricReportDefinitionOnCreate
from ..model.metric_report_definition_collection import MetricReportDefinitionCollection
from ..service import Service, ServiceCollection
from ..util import get_service, get_service_collection

router = APIRouter()


@router.get(
    "/redfish/v1/TelemetryService/MetricReportDefinitions", response_model_exclude_none=True
)
@router.head(
    "/redfish/v1/TelemetryService/MetricReportDefinitions", response_model_exclude_none=True
)
async def get1(request: Request, response: Response) -> MetricReportDefinitionCollection:
    s: Service = get_service(MetricReportDefinitionCollection, request)
    b: dict[str, Any] = {"request": request, "response": response}

    response.headers["OData-Version"] = "4.0"

    return cast(MetricReportDefinitionCollection, s.get(**b))


@router.post(
    "/redfish/v1/TelemetryService/MetricReportDefinitions", response_model_exclude_none=True
)
@router.post(
    "/redfish/v1/TelemetryService/MetricReportDefinitions/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post1(
    request: Request, response: Response, body: MetricReportDefinitionOnCreate
) -> MetricReportDefinition:
    s: ServiceCollection = get_service_collection(MetricReportDefinitionCollection, request)
    b: dict[str, Any] = {"request": request, "response": response, "body": body}

    response.headers["OData-Version"] = "4.0"

    return cast(MetricReportDefinition, s.post(**b))
