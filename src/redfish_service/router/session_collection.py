from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..model.session import Session, SessionOnCreate
from ..model.session_collection import SessionCollection
from ..service import Service, ServiceCollection
from ..util import get_service, get_service_collection

router = APIRouter()


@router.get("/redfish/v1/SessionService/Sessions", response_model_exclude_none=True)
@router.head("/redfish/v1/SessionService/Sessions", response_model_exclude_none=True)
async def get1(request: Request, response: Response) -> SessionCollection:
    s: Service = get_service(SessionCollection, request)
    b: dict[str, Any] = {"request": request, "response": response}

    response.headers["OData-Version"] = "4.0"

    return cast(SessionCollection, s.get(**b))


@router.post("/redfish/v1/SessionService/Sessions", response_model_exclude_none=True)
@router.post("/redfish/v1/SessionService/Sessions/Members", response_model_exclude_none=True)
async def post1(request: Request, response: Response, body: SessionOnCreate) -> Session:
    s: ServiceCollection = get_service_collection(SessionCollection, request)
    b: dict[str, Any] = {"request": request, "response": response, "body": body}

    response.headers["OData-Version"] = "4.0"

    return cast(Session, s.post(**b))
