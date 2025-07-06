from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..model.automation_node_collection import AutomationNodeCollection
from ..service import Service
from ..util import get_service, set_link_header

router = APIRouter()


@router.get("/redfish/v1/AutomationNodes", response_model_exclude_none=True)
@router.head("/redfish/v1/AutomationNodes", response_model_exclude_none=True)
async def get1(request: Request, response: Response) -> AutomationNodeCollection:
    s: Service = get_service(AutomationNodeCollection, request)
    b: dict[str, Any] = {"request": request, "response": response}
    m = cast(AutomationNodeCollection, s.get(**b))
    set_link_header(m, response)
    return m
