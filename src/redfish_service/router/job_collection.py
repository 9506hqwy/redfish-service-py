from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.job_collection import JobCollection
from ..service import Service, find_service

router = APIRouter()


@router.get("/redfish/v1/JobService/Jobs", response_model_exclude_none=True)
@authenticate
async def get1(request: Request, response: Response) -> JobCollection:
    s: Service = find_service(JobCollection)
    b: dict[str, Any] = {"request": request, "response": response}

    response.headers["OData-Version"] = "4.0"

    return cast(JobCollection, s.get(**b))


@router.get("/redfish/v1/JobService/Jobs/{job_id}/Steps", response_model_exclude_none=True)
@authenticate
async def get2(job_id: str, request: Request, response: Response) -> JobCollection:
    s: Service = find_service(JobCollection)
    b: dict[str, Any] = {"job_id": job_id, "request": request, "response": response}

    response.headers["OData-Version"] = "4.0"

    return cast(JobCollection, s.get(**b))
