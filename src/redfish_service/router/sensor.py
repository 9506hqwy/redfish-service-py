from typing import Any, cast

from fastapi import APIRouter

from ..model.sensor import Sensor
from ..service import Service, find_service
from . import authenticate

router = APIRouter()


@router.get(
    "/redfish/v1/Chassis/{chassis_id}/Sensors/{sensor_id}", response_model_exclude_none=True
)
@authenticate
async def get1(chassis_id: str, sensor_id: str) -> Sensor:
    s: Service = find_service(Sensor)
    b: dict[str, Any] = {"chassis_id": chassis_id, "sensor_id": sensor_id}
    return cast(Sensor, s.get(**b))


@router.get(
    "/redfish/v1/PowerEquipment/RackPDUs/{power_distribution_id}/Sensors/{sensor_id}",
    response_model_exclude_none=True,
)
@authenticate
async def get2(power_distribution_id: str, sensor_id: str) -> Sensor:
    s: Service = find_service(Sensor)
    b: dict[str, Any] = {"power_distribution_id": power_distribution_id, "sensor_id": sensor_id}
    return cast(Sensor, s.get(**b))


@router.get(
    "/redfish/v1/PowerEquipment/FloorPDUs/{power_distribution_id}/Sensors/{sensor_id}",
    response_model_exclude_none=True,
)
@authenticate
async def get3(power_distribution_id: str, sensor_id: str) -> Sensor:
    s: Service = find_service(Sensor)
    b: dict[str, Any] = {"power_distribution_id": power_distribution_id, "sensor_id": sensor_id}
    return cast(Sensor, s.get(**b))


@router.get(
    "/redfish/v1/PowerEquipment/Switchgear/{power_distribution_id}/Sensors/{sensor_id}",
    response_model_exclude_none=True,
)
@authenticate
async def get4(power_distribution_id: str, sensor_id: str) -> Sensor:
    s: Service = find_service(Sensor)
    b: dict[str, Any] = {"power_distribution_id": power_distribution_id, "sensor_id": sensor_id}
    return cast(Sensor, s.get(**b))


@router.get(
    "/redfish/v1/PowerEquipment/TransferSwitches/{power_distribution_id}/Sensors/{sensor_id}",
    response_model_exclude_none=True,
)
@authenticate
async def get5(power_distribution_id: str, sensor_id: str) -> Sensor:
    s: Service = find_service(Sensor)
    b: dict[str, Any] = {"power_distribution_id": power_distribution_id, "sensor_id": sensor_id}
    return cast(Sensor, s.get(**b))


@router.get(
    "/redfish/v1/PowerEquipment/PowerShelves/{power_distribution_id}/Sensors/{sensor_id}",
    response_model_exclude_none=True,
)
@authenticate
async def get6(power_distribution_id: str, sensor_id: str) -> Sensor:
    s: Service = find_service(Sensor)
    b: dict[str, Any] = {"power_distribution_id": power_distribution_id, "sensor_id": sensor_id}
    return cast(Sensor, s.get(**b))
