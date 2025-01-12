from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..model.message_registry_file_collection import MessageRegistryFileCollection
from ..service import Service
from ..util import get_service

router = APIRouter()


@router.get("/redfish/v1/Registries", response_model_exclude_none=True)
@router.head("/redfish/v1/Registries", response_model_exclude_none=True)
async def get1(request: Request, response: Response) -> MessageRegistryFileCollection:
    s: Service = get_service(MessageRegistryFileCollection, request)
    b: dict[str, Any] = {"request": request, "response": response}

    response.headers["OData-Version"] = "4.0"

    return cast(MessageRegistryFileCollection, s.get(**b))
