from typing import Any, cast

from fastapi import APIRouter

from ..model.job import Job
from ..service import Service, find_service
from . import authenticate

router = APIRouter()


@router.get("/redfish/v1/JobService/Jobs/{job_id}", response_model_exclude_none=True)
@authenticate
async def get1(job_id: str) -> Job:
    s: Service = find_service(Job)
    b: dict[str, Any] = {"job_id": job_id}
    return cast(Job, s.get(**b))


@router.get(
    "/redfish/v1/JobService/Jobs/{job_id}/Steps/{job_id2}", response_model_exclude_none=True
)
@authenticate
async def get2(job_id: str, job_id2: str) -> Job:
    s: Service = find_service(Job)
    b: dict[str, Any] = {"job_id": job_id, "job_id2": job_id2}
    return cast(Job, s.get(**b))
