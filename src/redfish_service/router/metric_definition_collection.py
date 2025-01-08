from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.metric_definition import MetricDefinition, MetricDefinitionOnCreate
from ..model.metric_definition_collection import MetricDefinitionCollection
from ..service import Service, ServiceCollection, find_service, find_service_collection

router = APIRouter()


@router.get("/redfish/v1/TelemetryService/MetricDefinitions", response_model_exclude_none=True)
@router.head("/redfish/v1/TelemetryService/MetricDefinitions", response_model_exclude_none=True)
async def get1(request: Request, response: Response) -> MetricDefinitionCollection:
    s: Service = find_service(MetricDefinitionCollection)
    b: dict[str, Any] = {"request": request, "response": response}

    response.headers["OData-Version"] = "4.0"

    return cast(MetricDefinitionCollection, s.get(**b))


@router.post("/redfish/v1/TelemetryService/MetricDefinitions", response_model_exclude_none=True)
@router.post(
    "/redfish/v1/TelemetryService/MetricDefinitions/Members", response_model_exclude_none=True
)
@authenticate
async def post1(
    request: Request, response: Response, body: MetricDefinitionOnCreate
) -> MetricDefinition:
    s: ServiceCollection = find_service_collection(MetricDefinitionCollection)
    b: dict[str, Any] = {"request": request, "response": response, "body": body}

    response.headers["OData-Version"] = "4.0"

    return cast(MetricDefinition, s.post(**b))
