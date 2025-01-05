from typing import Any, cast

from fastapi import APIRouter

from ..authenticate import authenticate
from ..model.job_service import JobService
from ..service import Service, find_service

router = APIRouter()


@router.get("/redfish/v1/JobService", response_model_exclude_none=True)
@authenticate
async def get1() -> JobService:
    s: Service = find_service(JobService)
    b: dict[str, Any] = {}
    return cast(JobService, s.get(**b))
