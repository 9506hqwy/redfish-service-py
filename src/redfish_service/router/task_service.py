from typing import Any, cast

from fastapi import APIRouter

from ..authenticate import authenticate
from ..model.task_service import TaskService
from ..service import Service, find_service

router = APIRouter()


@router.get("/redfish/v1/TaskService", response_model_exclude_none=True)
@authenticate
async def get1() -> TaskService:
    s: Service = find_service(TaskService)
    b: dict[str, Any] = {}
    return cast(TaskService, s.get(**b))
