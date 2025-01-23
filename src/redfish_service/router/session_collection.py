from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..model.session import Session, SessionOnCreate
from ..model.session_collection import SessionCollection
from ..service import Service, ServiceCollection
from ..util import get_service, get_service_collection, set_link_header

router = APIRouter()


@router.get("/redfish/v1/SessionService/Sessions", response_model_exclude_none=True)
@router.head("/redfish/v1/SessionService/Sessions", response_model_exclude_none=True)
async def get1(request: Request, response: Response) -> SessionCollection:
    s: Service = get_service(SessionCollection, request)
    b: dict[str, Any] = {"request": request, "response": response}
    m = cast(SessionCollection, s.get(**b))
    set_link_header(m, response)
    return m


@router.post("/redfish/v1/SessionService/Sessions", response_model_exclude_none=True)
@router.post("/redfish/v1/SessionService/Sessions/Members", response_model_exclude_none=True)
async def post1(request: Request, response: Response, body: SessionOnCreate) -> Session:
    s: ServiceCollection = get_service_collection(SessionCollection, request)
    b: dict[str, Any] = {"request": request, "response": response, "body": body}
    return cast(Session, s.post(**b))
