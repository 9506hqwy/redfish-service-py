from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..model.message_registry_file import MessageRegistryFile
from ..service import Service, find_service

router = APIRouter()


@router.get("/redfish/v1/Registries/{message_registry_file_id}", response_model_exclude_none=True)
@router.head("/redfish/v1/Registries/{message_registry_file_id}", response_model_exclude_none=True)
async def get1(
    message_registry_file_id: str, request: Request, response: Response
) -> MessageRegistryFile:
    s: Service = find_service(MessageRegistryFile)
    b: dict[str, Any] = {
        "message_registry_file_id": message_registry_file_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(MessageRegistryFile, s.get(**b))
