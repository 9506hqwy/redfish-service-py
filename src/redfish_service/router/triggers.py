from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..model.triggers import Triggers
from ..service import Service, find_service

router = APIRouter()


@router.get(
    "/redfish/v1/TelemetryService/Triggers/{triggers_id}", response_model_exclude_none=True
)
@router.head(
    "/redfish/v1/TelemetryService/Triggers/{triggers_id}", response_model_exclude_none=True
)
async def get1(triggers_id: str, request: Request, response: Response) -> Triggers:
    s: Service = find_service(Triggers)
    b: dict[str, Any] = {"triggers_id": triggers_id, "request": request, "response": response}

    response.headers["OData-Version"] = "4.0"

    return cast(Triggers, s.get(**b))
