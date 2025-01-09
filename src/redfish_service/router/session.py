from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.session import Session
from ..service import Service, find_service

router = APIRouter()


@router.delete(
    "/redfish/v1/SessionService/Sessions/{session_id}", response_model_exclude_none=True
)
@authenticate
async def delete1(session_id: str, request: Request, response: Response) -> None:
    s: Service = find_service(Session)
    b: dict[str, Any] = {"session_id": session_id, "request": request, "response": response}

    response.headers["OData-Version"] = "4.0"

    return s.delete(**b)


@router.get("/redfish/v1/SessionService/Sessions/{session_id}", response_model_exclude_none=True)
@router.head("/redfish/v1/SessionService/Sessions/{session_id}", response_model_exclude_none=True)
async def get1(session_id: str, request: Request, response: Response) -> Session:
    s: Service = find_service(Session)
    b: dict[str, Any] = {"session_id": session_id, "request": request, "response": response}

    response.headers["OData-Version"] = "4.0"

    return cast(Session, s.get(**b))
