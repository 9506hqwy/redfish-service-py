from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.job import Job, JobOnUpdate, ResubmitRequest
from ..model.redfish_error import RedfishError
from ..service import Service
from ..util import get_service, set_link_header

router = APIRouter()


@router.delete("/redfish/v1/JobService/Jobs/{job_id}", response_model_exclude_none=True)
@authenticate
async def delete1(job_id: str, request: Request, response: Response) -> None:
    s: Service = get_service(Job, request)
    b: dict[str, Any] = {"job_id": job_id, "request": request, "response": response}
    return s.delete(**b)


@router.get("/redfish/v1/JobService/Jobs/{job_id}", response_model_exclude_none=True)
@router.head("/redfish/v1/JobService/Jobs/{job_id}", response_model_exclude_none=True)
async def get1(job_id: str, request: Request, response: Response) -> Job:
    s: Service = get_service(Job, request)
    b: dict[str, Any] = {"job_id": job_id, "request": request, "response": response}
    m = cast(Job, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch("/redfish/v1/JobService/Jobs/{job_id}", response_model_exclude_none=True)
@authenticate
async def patch1(job_id: str, request: Request, response: Response, body: JobOnUpdate) -> Job:
    s: Service = get_service(Job, request)
    b: dict[str, Any] = {"job_id": job_id, "request": request, "response": response, "body": body}
    return cast(Job, s.patch(**b))


@router.post(
    "/redfish/v1/JobService/Jobs/{job_id}/Actions/Job.Resubmit", response_model_exclude_none=True
)
@authenticate
async def resubmit1(
    job_id: str, request: Request, response: Response, body: ResubmitRequest
) -> RedfishError:
    s: Service = get_service(Job, request)
    b: dict[str, Any] = {
        "job_id": job_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Resubmit",
    }
    return s.action(**b)


@router.delete(
    "/redfish/v1/JobService/Jobs/{job_id}/Steps/{job_id2}", response_model_exclude_none=True
)
@authenticate
async def delete2(job_id: str, job_id2: str, request: Request, response: Response) -> None:
    s: Service = get_service(Job, request)
    b: dict[str, Any] = {
        "job_id": job_id,
        "job_id2": job_id2,
        "request": request,
        "response": response,
    }
    return s.delete(**b)


@router.get(
    "/redfish/v1/JobService/Jobs/{job_id}/Steps/{job_id2}", response_model_exclude_none=True
)
@router.head(
    "/redfish/v1/JobService/Jobs/{job_id}/Steps/{job_id2}", response_model_exclude_none=True
)
async def get2(job_id: str, job_id2: str, request: Request, response: Response) -> Job:
    s: Service = get_service(Job, request)
    b: dict[str, Any] = {
        "job_id": job_id,
        "job_id2": job_id2,
        "request": request,
        "response": response,
    }
    m = cast(Job, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/JobService/Jobs/{job_id}/Steps/{job_id2}", response_model_exclude_none=True
)
@authenticate
async def patch2(
    job_id: str, job_id2: str, request: Request, response: Response, body: JobOnUpdate
) -> Job:
    s: Service = get_service(Job, request)
    b: dict[str, Any] = {
        "job_id": job_id,
        "job_id2": job_id2,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Job, s.patch(**b))


@router.post(
    "/redfish/v1/JobService/Jobs/{job_id}/Steps/{job_id2}/Actions/Job.Resubmit",
    response_model_exclude_none=True,
)
@authenticate
async def resubmit2(
    job_id: str, job_id2: str, request: Request, response: Response, body: ResubmitRequest
) -> RedfishError:
    s: Service = get_service(Job, request)
    b: dict[str, Any] = {
        "job_id": job_id,
        "job_id2": job_id2,
        "request": request,
        "response": response,
        "body": body,
        "action": "Resubmit",
    }
    return s.action(**b)
