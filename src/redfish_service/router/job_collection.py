from typing import Any, cast

from fastapi import APIRouter

from ..authenticate import authenticate
from ..model.job_collection import JobCollection
from ..service import Service, find_service

router = APIRouter()


@router.get("/redfish/v1/JobService/Jobs", response_model_exclude_none=True)
@authenticate
async def get1() -> JobCollection:
    s: Service = find_service(JobCollection)
    b: dict[str, Any] = {}
    return cast(JobCollection, s.get(**b))


@router.get("/redfish/v1/JobService/Jobs/{job_id}/Steps", response_model_exclude_none=True)
@authenticate
async def get2(job_id: str) -> JobCollection:
    s: Service = find_service(JobCollection)
    b: dict[str, Any] = {"job_id": job_id}
    return cast(JobCollection, s.get(**b))
