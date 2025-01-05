from typing import Any, cast

from fastapi import APIRouter

from ..authenticate import authenticate
from ..model.task import Task
from ..service import Service, find_service

router = APIRouter()


@router.get("/redfish/v1/TaskService/Tasks/{task_id}", response_model_exclude_none=True)
@authenticate
async def get1(task_id: str) -> Task:
    s: Service = find_service(Task)
    b: dict[str, Any] = {"task_id": task_id}
    return cast(Task, s.get(**b))


@router.get(
    "/redfish/v1/TaskService/Tasks/{task_id}/SubTasks/{task_id2}", response_model_exclude_none=True
)
@authenticate
async def get2(task_id: str, task_id2: str) -> Task:
    s: Service = find_service(Task)
    b: dict[str, Any] = {"task_id": task_id, "task_id2": task_id2}
    return cast(Task, s.get(**b))
