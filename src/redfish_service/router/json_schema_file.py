from typing import Any, cast

from fastapi import APIRouter

from ..model.json_schema_file import JsonSchemaFile
from ..service import Service, find_service
from . import authenticate

router = APIRouter()


@router.get("/redfish/v1/JsonSchemas/{json_schema_file_id}", response_model_exclude_none=True)
@authenticate
async def get1(json_schema_file_id: str) -> JsonSchemaFile:
    s: Service = find_service(JsonSchemaFile)
    b: dict[str, Any] = {"json_schema_file_id": json_schema_file_id}
    return cast(JsonSchemaFile, s.get(**b))
