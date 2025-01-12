from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.metric_definition import MetricDefinition, MetricDefinitionOnCreate
from ..model.metric_definition_collection import MetricDefinitionCollection
from ..service import Service, ServiceCollection
from ..util import get_service, get_service_collection

router = APIRouter()


@router.get("/redfish/v1/TelemetryService/MetricDefinitions", response_model_exclude_none=True)
@router.head("/redfish/v1/TelemetryService/MetricDefinitions", response_model_exclude_none=True)
async def get1(request: Request, response: Response) -> MetricDefinitionCollection:
    s: Service = get_service(MetricDefinitionCollection, request)
    b: dict[str, Any] = {"request": request, "response": response}
    return cast(MetricDefinitionCollection, s.get(**b))


@router.post("/redfish/v1/TelemetryService/MetricDefinitions", response_model_exclude_none=True)
@router.post(
    "/redfish/v1/TelemetryService/MetricDefinitions/Members", response_model_exclude_none=True
)
@authenticate
async def post1(
    request: Request, response: Response, body: MetricDefinitionOnCreate
) -> MetricDefinition:
    s: ServiceCollection = get_service_collection(MetricDefinitionCollection, request)
    b: dict[str, Any] = {"request": request, "response": response, "body": body}
    return cast(MetricDefinition, s.post(**b))
