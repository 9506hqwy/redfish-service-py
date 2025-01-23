from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..model.power_supply_collection import PowerSupplyCollection
from ..service import Service
from ..util import get_service, set_link_header

router = APIRouter()


@router.get(
    "/redfish/v1/Chassis/{chassis_id}/PowerSubsystem/PowerSupplies",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Chassis/{chassis_id}/PowerSubsystem/PowerSupplies",
    response_model_exclude_none=True,
)
async def get1(chassis_id: str, request: Request, response: Response) -> PowerSupplyCollection:
    s: Service = get_service(PowerSupplyCollection, request)
    b: dict[str, Any] = {"chassis_id": chassis_id, "request": request, "response": response}
    m = cast(PowerSupplyCollection, s.get(**b))
    set_link_header(m, response)
    return m


@router.get(
    "/redfish/v1/PowerEquipment/PowerShelves/{power_distribution_id}/PowerSupplies",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/PowerEquipment/PowerShelves/{power_distribution_id}/PowerSupplies",
    response_model_exclude_none=True,
)
async def get2(
    power_distribution_id: str, request: Request, response: Response
) -> PowerSupplyCollection:
    s: Service = get_service(PowerSupplyCollection, request)
    b: dict[str, Any] = {
        "power_distribution_id": power_distribution_id,
        "request": request,
        "response": response,
    }
    m = cast(PowerSupplyCollection, s.get(**b))
    set_link_header(m, response)
    return m
