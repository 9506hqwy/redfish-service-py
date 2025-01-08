from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.job import Job, JobOnCreate
from ..model.job_collection import JobCollection
from ..service import Service, ServiceCollection, find_service, find_service_collection

router = APIRouter()


@router.get("/redfish/v1/JobService/Jobs", response_model_exclude_none=True)
@router.head("/redfish/v1/JobService/Jobs", response_model_exclude_none=True)
async def get1(request: Request, response: Response) -> JobCollection:
    s: Service = find_service(JobCollection)
    b: dict[str, Any] = {"request": request, "response": response}

    response.headers["OData-Version"] = "4.0"

    return cast(JobCollection, s.get(**b))


@router.post("/redfish/v1/JobService/Jobs", response_model_exclude_none=True)
@router.post("/redfish/v1/JobService/Jobs/Members", response_model_exclude_none=True)
@authenticate
async def post1(request: Request, response: Response, body: JobOnCreate) -> Job:
    s: ServiceCollection = find_service_collection(JobCollection)
    b: dict[str, Any] = {"request": request, "response": response, "body": body}

    response.headers["OData-Version"] = "4.0"

    return cast(Job, s.post(**b))


@router.get("/redfish/v1/JobService/Jobs/{job_id}/Steps", response_model_exclude_none=True)
@router.head("/redfish/v1/JobService/Jobs/{job_id}/Steps", response_model_exclude_none=True)
async def get2(job_id: str, request: Request, response: Response) -> JobCollection:
    s: Service = find_service(JobCollection)
    b: dict[str, Any] = {"job_id": job_id, "request": request, "response": response}

    response.headers["OData-Version"] = "4.0"

    return cast(JobCollection, s.get(**b))


@router.post("/redfish/v1/JobService/Jobs/{job_id}/Steps", response_model_exclude_none=True)
@router.post(
    "/redfish/v1/JobService/Jobs/{job_id}/Steps/Members", response_model_exclude_none=True
)
@authenticate
async def post2(job_id: str, request: Request, response: Response, body: JobOnCreate) -> Job:
    s: ServiceCollection = find_service_collection(JobCollection)
    b: dict[str, Any] = {"job_id": job_id, "request": request, "response": response, "body": body}

    response.headers["OData-Version"] = "4.0"

    return cast(Job, s.post(**b))
