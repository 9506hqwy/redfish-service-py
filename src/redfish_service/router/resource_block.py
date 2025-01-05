from typing import Any, cast

from fastapi import APIRouter

from ..authenticate import authenticate
from ..model.resource_block import ResourceBlock
from ..service import Service, find_service

router = APIRouter()


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}",
    response_model_exclude_none=True,
)
@authenticate
async def get1(resource_block_id: str) -> ResourceBlock:
    s: Service = find_service(ResourceBlock)
    b: dict[str, Any] = {"resource_block_id": resource_block_id}
    return cast(ResourceBlock, s.get(**b))


@router.get("/redfish/v1/ResourceBlocks/{resource_block_id}", response_model_exclude_none=True)
@authenticate
async def get2(resource_block_id: str) -> ResourceBlock:
    s: Service = find_service(ResourceBlock)
    b: dict[str, Any] = {"resource_block_id": resource_block_id}
    return cast(ResourceBlock, s.get(**b))
