from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.job_executor import JobExecutor, JobExecutorOnCreate
from ..model.job_executor_collection import JobExecutorCollection
from ..service import Service, ServiceCollection
from ..util import get_service, get_service_collection, set_link_header

router = APIRouter()


@router.get("/redfish/v1/JobService/Executors", response_model_exclude_none=True)
@router.head("/redfish/v1/JobService/Executors", response_model_exclude_none=True)
async def get1(request: Request, response: Response) -> JobExecutorCollection:
    s: Service = get_service(JobExecutorCollection, request)
    b: dict[str, Any] = {"request": request, "response": response}
    m = cast(JobExecutorCollection, s.get(**b))
    set_link_header(m, response)
    return m


@router.post("/redfish/v1/JobService/Executors", response_model_exclude_none=True)
@router.post("/redfish/v1/JobService/Executors/Members", response_model_exclude_none=True)
@authenticate
async def post1(request: Request, response: Response, body: JobExecutorOnCreate) -> JobExecutor:
    s: ServiceCollection = get_service_collection(JobExecutorCollection, request)
    b: dict[str, Any] = {"request": request, "response": response, "body": body}
    return cast(JobExecutor, s.post(**b))
