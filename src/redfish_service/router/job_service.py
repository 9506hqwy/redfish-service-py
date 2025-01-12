from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.job_service import JobService, JobServiceOnUpdate
from ..service import Service
from ..util import get_service

router = APIRouter()


@router.get("/redfish/v1/JobService", response_model_exclude_none=True)
@router.head("/redfish/v1/JobService", response_model_exclude_none=True)
async def get1(request: Request, response: Response) -> JobService:
    s: Service = get_service(JobService, request)
    b: dict[str, Any] = {"request": request, "response": response}
    return cast(JobService, s.get(**b))


@router.patch("/redfish/v1/JobService", response_model_exclude_none=True)
@authenticate
async def patch1(request: Request, response: Response, body: JobServiceOnUpdate) -> JobService:
    s: Service = get_service(JobService, request)
    b: dict[str, Any] = {"request": request, "response": response, "body": body}
    return cast(JobService, s.patch(**b))
