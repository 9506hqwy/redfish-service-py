from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.automation_instrumentation import (
    AutomationInstrumentation,
    AutomationInstrumentationOnUpdate,
)
from ..service import Service
from ..util import get_service, set_link_header

router = APIRouter()


@router.get(
    "/redfish/v1/AutomationNodes/{automation_node_id}/AutomationInstrumentation",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/AutomationNodes/{automation_node_id}/AutomationInstrumentation",
    response_model_exclude_none=True,
)
async def get1(
    automation_node_id: str, request: Request, response: Response
) -> AutomationInstrumentation:
    s: Service = get_service(AutomationInstrumentation, request)
    b: dict[str, Any] = {
        "automation_node_id": automation_node_id,
        "request": request,
        "response": response,
    }
    m = cast(AutomationInstrumentation, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/AutomationNodes/{automation_node_id}/AutomationInstrumentation",
    response_model_exclude_none=True,
)
@authenticate
async def patch1(
    automation_node_id: str,
    request: Request,
    response: Response,
    body: AutomationInstrumentationOnUpdate,
) -> AutomationInstrumentation:
    s: Service = get_service(AutomationInstrumentation, request)
    b: dict[str, Any] = {
        "automation_node_id": automation_node_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(AutomationInstrumentation, s.patch(**b))
