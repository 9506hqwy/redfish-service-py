from typing import Any, cast

from fastapi import APIRouter

from ..authenticate import authenticate
from ..model.json_schema_file_collection import JsonSchemaFileCollection
from ..service import Service, find_service

router = APIRouter()


@router.get("/redfish/v1/JsonSchemas", response_model_exclude_none=True)
@authenticate
async def get1() -> JsonSchemaFileCollection:
    s: Service = find_service(JsonSchemaFileCollection)
    b: dict[str, Any] = {}
    return cast(JsonSchemaFileCollection, s.get(**b))
