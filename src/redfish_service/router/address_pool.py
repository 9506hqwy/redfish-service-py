from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.address_pool import AddressPool
from ..service import Service, find_service

router = APIRouter()


@router.delete(
    "/redfish/v1/Fabrics/{fabric_id}/AddressPools/{address_pool_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete1(
    fabric_id: str, address_pool_id: str, request: Request, response: Response
) -> None:
    s: Service = find_service(AddressPool)
    b: dict[str, Any] = {
        "fabric_id": fabric_id,
        "address_pool_id": address_pool_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return s.delete(**b)


@router.get(
    "/redfish/v1/Fabrics/{fabric_id}/AddressPools/{address_pool_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Fabrics/{fabric_id}/AddressPools/{address_pool_id}",
    response_model_exclude_none=True,
)
async def get1(
    fabric_id: str, address_pool_id: str, request: Request, response: Response
) -> AddressPool:
    s: Service = find_service(AddressPool)
    b: dict[str, Any] = {
        "fabric_id": fabric_id,
        "address_pool_id": address_pool_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(AddressPool, s.get(**b))
