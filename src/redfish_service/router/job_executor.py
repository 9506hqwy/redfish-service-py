from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.job_executor import JobExecutor
from ..service import Service
from ..util import get_service, set_link_header

router = APIRouter()


@router.delete(
    "/redfish/v1/JobService/Executors/{job_executor_id}", response_model_exclude_none=True
)
@authenticate
async def delete1(job_executor_id: str, request: Request, response: Response) -> None:
    s: Service = get_service(JobExecutor, request)
    b: dict[str, Any] = {
        "job_executor_id": job_executor_id,
        "request": request,
        "response": response,
    }
    return s.delete(**b)


@router.get("/redfish/v1/JobService/Executors/{job_executor_id}", response_model_exclude_none=True)
@router.head(
    "/redfish/v1/JobService/Executors/{job_executor_id}", response_model_exclude_none=True
)
async def get1(job_executor_id: str, request: Request, response: Response) -> JobExecutor:
    s: Service = get_service(JobExecutor, request)
    b: dict[str, Any] = {
        "job_executor_id": job_executor_id,
        "request": request,
        "response": response,
    }
    m = cast(JobExecutor, s.get(**b))
    set_link_header(m, response)
    return m
