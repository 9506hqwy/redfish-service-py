from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..model.task_collection import TaskCollection
from ..service import Service, find_service

router = APIRouter()


@router.get("/redfish/v1/TaskService/Tasks", response_model_exclude_none=True)
@router.head("/redfish/v1/TaskService/Tasks", response_model_exclude_none=True)
async def get1(request: Request, response: Response) -> TaskCollection:
    s: Service = find_service(TaskCollection)
    b: dict[str, Any] = {"request": request, "response": response}

    response.headers["OData-Version"] = "4.0"

    return cast(TaskCollection, s.get(**b))


@router.get("/redfish/v1/TaskService/Tasks/{task_id}/SubTasks", response_model_exclude_none=True)
@router.head("/redfish/v1/TaskService/Tasks/{task_id}/SubTasks", response_model_exclude_none=True)
async def get2(task_id: str, request: Request, response: Response) -> TaskCollection:
    s: Service = find_service(TaskCollection)
    b: dict[str, Any] = {"task_id": task_id, "request": request, "response": response}

    response.headers["OData-Version"] = "4.0"

    return cast(TaskCollection, s.get(**b))
