from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..model.json_schema_file_collection import JsonSchemaFileCollection
from ..service import Service
from ..util import get_service, set_link_header

router = APIRouter()


@router.get("/redfish/v1/JsonSchemas", response_model_exclude_none=True)
@router.head("/redfish/v1/JsonSchemas", response_model_exclude_none=True)
async def get1(request: Request, response: Response) -> JsonSchemaFileCollection:
    s: Service = get_service(JsonSchemaFileCollection, request)
    b: dict[str, Any] = {"request": request, "response": response}
    m = cast(JsonSchemaFileCollection, s.get(**b))
    set_link_header(m, response)
    return m
