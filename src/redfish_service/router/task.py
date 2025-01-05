from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.task import Task
from ..service import Service, find_service

router = APIRouter()


@router.get("/redfish/v1/TaskService/Tasks/{task_id}", response_model_exclude_none=True)
@authenticate
async def get1(task_id: str, request: Request, response: Response) -> Task:
    s: Service = find_service(Task)
    b: dict[str, Any] = {"task_id": task_id, "request": request, "response": response}

    response.headers["OData-Version"] = "4.0"

    return cast(Task, s.get(**b))


@router.get(
    "/redfish/v1/TaskService/Tasks/{task_id}/SubTasks/{task_id2}", response_model_exclude_none=True
)
@authenticate
async def get2(task_id: str, task_id2: str, request: Request, response: Response) -> Task:
    s: Service = find_service(Task)
    b: dict[str, Any] = {
        "task_id": task_id,
        "task_id2": task_id2,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(Task, s.get(**b))
