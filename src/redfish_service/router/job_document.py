from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.job_document import JobDocument, SubmitJobRequest
from ..model.redfish_error import RedfishError
from ..service import Service
from ..util import get_service, set_link_header

router = APIRouter()


@router.delete(
    "/redfish/v1/JobService/Documents/{job_document_id}", response_model_exclude_none=True
)
@authenticate
async def delete1(job_document_id: str, request: Request, response: Response) -> None:
    s: Service = get_service(JobDocument, request)
    b: dict[str, Any] = {
        "job_document_id": job_document_id,
        "request": request,
        "response": response,
    }
    return s.delete(**b)


@router.get("/redfish/v1/JobService/Documents/{job_document_id}", response_model_exclude_none=True)
@router.head(
    "/redfish/v1/JobService/Documents/{job_document_id}", response_model_exclude_none=True
)
async def get1(job_document_id: str, request: Request, response: Response) -> JobDocument:
    s: Service = get_service(JobDocument, request)
    b: dict[str, Any] = {
        "job_document_id": job_document_id,
        "request": request,
        "response": response,
    }
    m = cast(JobDocument, s.get(**b))
    set_link_header(m, response)
    return m


@router.post(
    "/redfish/v1/JobService/Documents/{job_document_id}/Actions/JobDocument.SubmitJob",
    response_model_exclude_none=True,
)
@authenticate
async def submit_job1(
    job_document_id: str, request: Request, response: Response, body: SubmitJobRequest
) -> RedfishError:
    s: Service = get_service(JobDocument, request)
    b: dict[str, Any] = {
        "job_document_id": job_document_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "SubmitJob",
    }
    return s.action(**b)
