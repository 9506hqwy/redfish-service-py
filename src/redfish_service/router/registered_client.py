from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.registered_client import RegisteredClient, RegisteredClientOnUpdate
from ..service import Service, find_service

router = APIRouter()


@router.delete(
    "/redfish/v1/RegisteredClients/{registered_client_id}", response_model_exclude_none=True
)
@authenticate
async def delete1(registered_client_id: str, request: Request, response: Response) -> None:
    s: Service = find_service(RegisteredClient)
    b: dict[str, Any] = {
        "registered_client_id": registered_client_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return s.delete(**b)


@router.get(
    "/redfish/v1/RegisteredClients/{registered_client_id}", response_model_exclude_none=True
)
@router.head(
    "/redfish/v1/RegisteredClients/{registered_client_id}", response_model_exclude_none=True
)
async def get1(
    registered_client_id: str, request: Request, response: Response
) -> RegisteredClient:
    s: Service = find_service(RegisteredClient)
    b: dict[str, Any] = {
        "registered_client_id": registered_client_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(RegisteredClient, s.get(**b))


@router.patch(
    "/redfish/v1/RegisteredClients/{registered_client_id}", response_model_exclude_none=True
)
@authenticate
async def patch1(
    registered_client_id: str, request: Request, response: Response, body: RegisteredClientOnUpdate
) -> RegisteredClient:
    s: Service = find_service(RegisteredClient)
    b: dict[str, Any] = {
        "registered_client_id": registered_client_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(RegisteredClient, s.patch(**b))
