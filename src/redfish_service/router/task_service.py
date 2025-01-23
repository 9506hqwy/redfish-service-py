from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.task_service import TaskService, TaskServiceOnUpdate
from ..service import Service
from ..util import get_service, set_link_header

router = APIRouter()


@router.get("/redfish/v1/TaskService", response_model_exclude_none=True)
@router.head("/redfish/v1/TaskService", response_model_exclude_none=True)
async def get1(request: Request, response: Response) -> TaskService:
    s: Service = get_service(TaskService, request)
    b: dict[str, Any] = {"request": request, "response": response}
    m = cast(TaskService, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch("/redfish/v1/TaskService", response_model_exclude_none=True)
@authenticate
async def patch1(request: Request, response: Response, body: TaskServiceOnUpdate) -> TaskService:
    s: Service = get_service(TaskService, request)
    b: dict[str, Any] = {"request": request, "response": response, "body": body}
    return cast(TaskService, s.patch(**b))
