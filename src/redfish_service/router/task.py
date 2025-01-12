from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.task import Task
from ..service import Service
from ..util import get_service

router = APIRouter()


@router.delete("/redfish/v1/TaskService/Tasks/{task_id}", response_model_exclude_none=True)
@authenticate
async def delete1(task_id: str, request: Request, response: Response) -> None:
    s: Service = get_service(Task, request)
    b: dict[str, Any] = {"task_id": task_id, "request": request, "response": response}
    return s.delete(**b)


@router.get("/redfish/v1/TaskService/Tasks/{task_id}", response_model_exclude_none=True)
@router.head("/redfish/v1/TaskService/Tasks/{task_id}", response_model_exclude_none=True)
async def get1(task_id: str, request: Request, response: Response) -> Task:
    s: Service = get_service(Task, request)
    b: dict[str, Any] = {"task_id": task_id, "request": request, "response": response}
    return cast(Task, s.get(**b))


@router.delete(
    "/redfish/v1/TaskService/Tasks/{task_id}/SubTasks/{task_id2}", response_model_exclude_none=True
)
@authenticate
async def delete2(task_id: str, task_id2: str, request: Request, response: Response) -> None:
    s: Service = get_service(Task, request)
    b: dict[str, Any] = {
        "task_id": task_id,
        "task_id2": task_id2,
        "request": request,
        "response": response,
    }
    return s.delete(**b)


@router.get(
    "/redfish/v1/TaskService/Tasks/{task_id}/SubTasks/{task_id2}", response_model_exclude_none=True
)
@router.head(
    "/redfish/v1/TaskService/Tasks/{task_id}/SubTasks/{task_id2}", response_model_exclude_none=True
)
async def get2(task_id: str, task_id2: str, request: Request, response: Response) -> Task:
    s: Service = get_service(Task, request)
    b: dict[str, Any] = {
        "task_id": task_id,
        "task_id2": task_id2,
        "request": request,
        "response": response,
    }
    return cast(Task, s.get(**b))
