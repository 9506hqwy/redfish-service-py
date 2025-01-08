from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.triggers import Triggers, TriggersOnCreate
from ..model.triggers_collection import TriggersCollection
from ..service import Service, ServiceCollection, find_service, find_service_collection

router = APIRouter()


@router.get("/redfish/v1/TelemetryService/Triggers", response_model_exclude_none=True)
@router.head("/redfish/v1/TelemetryService/Triggers", response_model_exclude_none=True)
async def get1(request: Request, response: Response) -> TriggersCollection:
    s: Service = find_service(TriggersCollection)
    b: dict[str, Any] = {"request": request, "response": response}

    response.headers["OData-Version"] = "4.0"

    return cast(TriggersCollection, s.get(**b))


@router.post("/redfish/v1/TelemetryService/Triggers", response_model_exclude_none=True)
@router.post("/redfish/v1/TelemetryService/Triggers/Members", response_model_exclude_none=True)
@authenticate
async def post1(request: Request, response: Response, body: TriggersOnCreate) -> Triggers:
    s: ServiceCollection = find_service_collection(TriggersCollection)
    b: dict[str, Any] = {"request": request, "response": response, "body": body}

    response.headers["OData-Version"] = "4.0"

    return cast(Triggers, s.post(**b))
