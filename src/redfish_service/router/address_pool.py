from typing import Any, cast

from fastapi import APIRouter

from ..model.address_pool import AddressPool
from ..service import Service, find_service
from . import authenticate

router = APIRouter()


@router.get(
    "/redfish/v1/Fabrics/{fabric_id}/AddressPools/{address_pool_id}",
    response_model_exclude_none=True,
)
@authenticate
async def get1(fabric_id: str, address_pool_id: str) -> AddressPool:
    s: Service = find_service(AddressPool)
    b: dict[str, Any] = {"fabric_id": fabric_id, "address_pool_id": address_pool_id}
    return cast(AddressPool, s.get(**b))
