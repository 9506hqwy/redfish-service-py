from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..model.json_schema_file import JsonSchemaFile
from ..service import Service
from ..util import get_service, set_link_header

router = APIRouter()


@router.get("/redfish/v1/JsonSchemas/{json_schema_file_id}", response_model_exclude_none=True)
@router.head("/redfish/v1/JsonSchemas/{json_schema_file_id}", response_model_exclude_none=True)
async def get1(json_schema_file_id: str, request: Request, response: Response) -> JsonSchemaFile:
    s: Service = get_service(JsonSchemaFile, request)
    b: dict[str, Any] = {
        "json_schema_file_id": json_schema_file_id,
        "request": request,
        "response": response,
    }
    m = cast(JsonSchemaFile, s.get(**b))
    set_link_header(m, response)
    return m
