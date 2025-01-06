from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.json_schema_file import JsonSchemaFile
from ..service import Service, find_service

router = APIRouter()


@router.get("/redfish/v1/JsonSchemas/{json_schema_file_id}", response_model_exclude_none=True)
@router.head("/redfish/v1/JsonSchemas/{json_schema_file_id}", response_model_exclude_none=True)
@authenticate
async def get1(json_schema_file_id: str, request: Request, response: Response) -> JsonSchemaFile:
    s: Service = find_service(JsonSchemaFile)
    b: dict[str, Any] = {
        "json_schema_file_id": json_schema_file_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(JsonSchemaFile, s.get(**b))
