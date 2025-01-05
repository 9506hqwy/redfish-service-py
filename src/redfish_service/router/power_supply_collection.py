from typing import Any, cast

from fastapi import APIRouter

from ..authenticate import authenticate
from ..model.power_supply_collection import PowerSupplyCollection
from ..service import Service, find_service

router = APIRouter()


@router.get(
    "/redfish/v1/Chassis/{chassis_id}/PowerSubsystem/PowerSupplies",
    response_model_exclude_none=True,
)
@authenticate
async def get1(chassis_id: str) -> PowerSupplyCollection:
    s: Service = find_service(PowerSupplyCollection)
    b: dict[str, Any] = {"chassis_id": chassis_id}
    return cast(PowerSupplyCollection, s.get(**b))


@router.get(
    "/redfish/v1/PowerEquipment/PowerShelves/{power_distribution_id}/PowerSupplies",
    response_model_exclude_none=True,
)
@authenticate
async def get2(power_distribution_id: str) -> PowerSupplyCollection:
    s: Service = find_service(PowerSupplyCollection)
    b: dict[str, Any] = {"power_distribution_id": power_distribution_id}
    return cast(PowerSupplyCollection, s.get(**b))
