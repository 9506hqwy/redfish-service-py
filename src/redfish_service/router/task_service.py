from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.task_service import TaskService
from ..service import Service, find_service

router = APIRouter()


@router.get("/redfish/v1/TaskService", response_model_exclude_none=True)
@router.head("/redfish/v1/TaskService", response_model_exclude_none=True)
@authenticate
async def get1(request: Request, response: Response) -> TaskService:
    s: Service = find_service(TaskService)
    b: dict[str, Any] = {"request": request, "response": response}

    response.headers["OData-Version"] = "4.0"

    return cast(TaskService, s.get(**b))
