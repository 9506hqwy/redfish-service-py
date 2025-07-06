from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.job_document import JobDocument, JobDocumentOnCreate
from ..model.job_document_collection import JobDocumentCollection
from ..service import Service, ServiceCollection
from ..util import get_service, get_service_collection, set_link_header

router = APIRouter()


@router.get("/redfish/v1/JobService/Documents", response_model_exclude_none=True)
@router.head("/redfish/v1/JobService/Documents", response_model_exclude_none=True)
async def get1(request: Request, response: Response) -> JobDocumentCollection:
    s: Service = get_service(JobDocumentCollection, request)
    b: dict[str, Any] = {"request": request, "response": response}
    m = cast(JobDocumentCollection, s.get(**b))
    set_link_header(m, response)
    return m


@router.post("/redfish/v1/JobService/Documents", response_model_exclude_none=True)
@router.post("/redfish/v1/JobService/Documents/Members", response_model_exclude_none=True)
@authenticate
async def post1(request: Request, response: Response, body: JobDocumentOnCreate) -> JobDocument:
    s: ServiceCollection = get_service_collection(JobDocumentCollection, request)
    b: dict[str, Any] = {"request": request, "response": response, "body": body}
    return cast(JobDocument, s.post(**b))
