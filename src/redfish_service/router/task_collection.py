from typing import Any, cast

from fastapi import APIRouter

from ..authenticate import authenticate
from ..model.task_collection import TaskCollection
from ..service import Service, find_service

router = APIRouter()


@router.get("/redfish/v1/TaskService/Tasks", response_model_exclude_none=True)
@authenticate
async def get1() -> TaskCollection:
    s: Service = find_service(TaskCollection)
    b: dict[str, Any] = {}
    return cast(TaskCollection, s.get(**b))


@router.get("/redfish/v1/TaskService/Tasks/{task_id}/SubTasks", response_model_exclude_none=True)
@authenticate
async def get2(task_id: str) -> TaskCollection:
    s: Service = find_service(TaskCollection)
    b: dict[str, Any] = {"task_id": task_id}
    return cast(TaskCollection, s.get(**b))
