from typing import Any, cast

from fastapi import APIRouter

from ..authenticate import authenticate
from ..model.power_supply import PowerSupply
from ..service import Service, find_service

router = APIRouter()


@router.get(
    "/redfish/v1/Chassis/{chassis_id}/PowerSubsystem/PowerSupplies/{power_supply_id}",
    response_model_exclude_none=True,
)
@authenticate
async def get1(chassis_id: str, power_supply_id: str) -> PowerSupply:
    s: Service = find_service(PowerSupply)
    b: dict[str, Any] = {"chassis_id": chassis_id, "power_supply_id": power_supply_id}
    return cast(PowerSupply, s.get(**b))


@router.get(
    "/redfish/v1/PowerEquipment/PowerShelves/{power_distribution_id}/PowerSupplies/{power_supply_id}",
    response_model_exclude_none=True,
)
@authenticate
async def get2(power_distribution_id: str, power_supply_id: str) -> PowerSupply:
    s: Service = find_service(PowerSupply)
    b: dict[str, Any] = {
        "power_distribution_id": power_distribution_id,
        "power_supply_id": power_supply_id,
    }
    return cast(PowerSupply, s.get(**b))
