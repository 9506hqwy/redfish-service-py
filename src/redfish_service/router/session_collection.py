from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.session import Session, SessionOnCreate
from ..model.session_collection import SessionCollection
from ..service import Service, ServiceCollection, find_service, find_service_collection

router = APIRouter()


@router.get("/redfish/v1/SessionService/Sessions", response_model_exclude_none=True)
@router.head("/redfish/v1/SessionService/Sessions", response_model_exclude_none=True)
@authenticate
async def get1(request: Request, response: Response) -> SessionCollection:
    s: Service = find_service(SessionCollection)
    b: dict[str, Any] = {"request": request, "response": response}

    response.headers["OData-Version"] = "4.0"

    return cast(SessionCollection, s.get(**b))


@router.post("/redfish/v1/SessionService/Sessions", response_model_exclude_none=True)
@router.post("/redfish/v1/SessionService/Sessions/Members", response_model_exclude_none=True)
@authenticate
async def post1(request: Request, response: Response, body: SessionOnCreate) -> Session:
    s: ServiceCollection = find_service_collection(SessionCollection)
    b: dict[str, Any] = {"request": request, "response": response, "body": body}

    response.headers["OData-Version"] = "4.0"

    return cast(Session, s.post(**b))
