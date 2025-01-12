from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..model.circuit_collection import CircuitCollection
from ..service import Service
from ..util import get_service

router = APIRouter()


@router.get(
    "/redfish/v1/PowerEquipment/RackPDUs/{power_distribution_id}/Mains",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/PowerEquipment/RackPDUs/{power_distribution_id}/Mains",
    response_model_exclude_none=True,
)
async def get1(
    power_distribution_id: str, request: Request, response: Response
) -> CircuitCollection:
    s: Service = get_service(CircuitCollection, request)
    b: dict[str, Any] = {
        "power_distribution_id": power_distribution_id,
        "request": request,
        "response": response,
    }
    return cast(CircuitCollection, s.get(**b))


@router.get(
    "/redfish/v1/PowerEquipment/RackPDUs/{power_distribution_id}/Branches",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/PowerEquipment/RackPDUs/{power_distribution_id}/Branches",
    response_model_exclude_none=True,
)
async def get2(
    power_distribution_id: str, request: Request, response: Response
) -> CircuitCollection:
    s: Service = get_service(CircuitCollection, request)
    b: dict[str, Any] = {
        "power_distribution_id": power_distribution_id,
        "request": request,
        "response": response,
    }
    return cast(CircuitCollection, s.get(**b))


@router.get(
    "/redfish/v1/PowerEquipment/FloorPDUs/{power_distribution_id}/Mains",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/PowerEquipment/FloorPDUs/{power_distribution_id}/Mains",
    response_model_exclude_none=True,
)
async def get3(
    power_distribution_id: str, request: Request, response: Response
) -> CircuitCollection:
    s: Service = get_service(CircuitCollection, request)
    b: dict[str, Any] = {
        "power_distribution_id": power_distribution_id,
        "request": request,
        "response": response,
    }
    return cast(CircuitCollection, s.get(**b))


@router.get(
    "/redfish/v1/PowerEquipment/FloorPDUs/{power_distribution_id}/Branches",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/PowerEquipment/FloorPDUs/{power_distribution_id}/Branches",
    response_model_exclude_none=True,
)
async def get4(
    power_distribution_id: str, request: Request, response: Response
) -> CircuitCollection:
    s: Service = get_service(CircuitCollection, request)
    b: dict[str, Any] = {
        "power_distribution_id": power_distribution_id,
        "request": request,
        "response": response,
    }
    return cast(CircuitCollection, s.get(**b))


@router.get(
    "/redfish/v1/PowerEquipment/FloorPDUs/{power_distribution_id}/Subfeeds",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/PowerEquipment/FloorPDUs/{power_distribution_id}/Subfeeds",
    response_model_exclude_none=True,
)
async def get5(
    power_distribution_id: str, request: Request, response: Response
) -> CircuitCollection:
    s: Service = get_service(CircuitCollection, request)
    b: dict[str, Any] = {
        "power_distribution_id": power_distribution_id,
        "request": request,
        "response": response,
    }
    return cast(CircuitCollection, s.get(**b))


@router.get(
    "/redfish/v1/PowerEquipment/TransferSwitches/{power_distribution_id}/Mains",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/PowerEquipment/TransferSwitches/{power_distribution_id}/Mains",
    response_model_exclude_none=True,
)
async def get6(
    power_distribution_id: str, request: Request, response: Response
) -> CircuitCollection:
    s: Service = get_service(CircuitCollection, request)
    b: dict[str, Any] = {
        "power_distribution_id": power_distribution_id,
        "request": request,
        "response": response,
    }
    return cast(CircuitCollection, s.get(**b))


@router.get(
    "/redfish/v1/PowerEquipment/TransferSwitches/{power_distribution_id}/Branches",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/PowerEquipment/TransferSwitches/{power_distribution_id}/Branches",
    response_model_exclude_none=True,
)
async def get7(
    power_distribution_id: str, request: Request, response: Response
) -> CircuitCollection:
    s: Service = get_service(CircuitCollection, request)
    b: dict[str, Any] = {
        "power_distribution_id": power_distribution_id,
        "request": request,
        "response": response,
    }
    return cast(CircuitCollection, s.get(**b))


@router.get(
    "/redfish/v1/PowerEquipment/TransferSwitches/{power_distribution_id}/Feeders",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/PowerEquipment/TransferSwitches/{power_distribution_id}/Feeders",
    response_model_exclude_none=True,
)
async def get8(
    power_distribution_id: str, request: Request, response: Response
) -> CircuitCollection:
    s: Service = get_service(CircuitCollection, request)
    b: dict[str, Any] = {
        "power_distribution_id": power_distribution_id,
        "request": request,
        "response": response,
    }
    return cast(CircuitCollection, s.get(**b))


@router.get(
    "/redfish/v1/PowerEquipment/PowerShelves/{power_distribution_id}/Mains",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/PowerEquipment/PowerShelves/{power_distribution_id}/Mains",
    response_model_exclude_none=True,
)
async def get9(
    power_distribution_id: str, request: Request, response: Response
) -> CircuitCollection:
    s: Service = get_service(CircuitCollection, request)
    b: dict[str, Any] = {
        "power_distribution_id": power_distribution_id,
        "request": request,
        "response": response,
    }
    return cast(CircuitCollection, s.get(**b))


@router.get(
    "/redfish/v1/PowerEquipment/PowerShelves/{power_distribution_id}/Branches",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/PowerEquipment/PowerShelves/{power_distribution_id}/Branches",
    response_model_exclude_none=True,
)
async def get10(
    power_distribution_id: str, request: Request, response: Response
) -> CircuitCollection:
    s: Service = get_service(CircuitCollection, request)
    b: dict[str, Any] = {
        "power_distribution_id": power_distribution_id,
        "request": request,
        "response": response,
    }
    return cast(CircuitCollection, s.get(**b))


@router.get(
    "/redfish/v1/PowerEquipment/Switchgear/{power_distribution_id}/Mains",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/PowerEquipment/Switchgear/{power_distribution_id}/Mains",
    response_model_exclude_none=True,
)
async def get11(
    power_distribution_id: str, request: Request, response: Response
) -> CircuitCollection:
    s: Service = get_service(CircuitCollection, request)
    b: dict[str, Any] = {
        "power_distribution_id": power_distribution_id,
        "request": request,
        "response": response,
    }
    return cast(CircuitCollection, s.get(**b))


@router.get(
    "/redfish/v1/PowerEquipment/Switchgear/{power_distribution_id}/Subfeeds",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/PowerEquipment/Switchgear/{power_distribution_id}/Subfeeds",
    response_model_exclude_none=True,
)
async def get12(
    power_distribution_id: str, request: Request, response: Response
) -> CircuitCollection:
    s: Service = get_service(CircuitCollection, request)
    b: dict[str, Any] = {
        "power_distribution_id": power_distribution_id,
        "request": request,
        "response": response,
    }
    return cast(CircuitCollection, s.get(**b))


@router.get(
    "/redfish/v1/PowerEquipment/Switchgear/{power_distribution_id}/Feeders",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/PowerEquipment/Switchgear/{power_distribution_id}/Feeders",
    response_model_exclude_none=True,
)
async def get13(
    power_distribution_id: str, request: Request, response: Response
) -> CircuitCollection:
    s: Service = get_service(CircuitCollection, request)
    b: dict[str, Any] = {
        "power_distribution_id": power_distribution_id,
        "request": request,
        "response": response,
    }
    return cast(CircuitCollection, s.get(**b))


@router.get(
    "/redfish/v1/PowerEquipment/Switchgear/{power_distribution_id}/Branches",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/PowerEquipment/Switchgear/{power_distribution_id}/Branches",
    response_model_exclude_none=True,
)
async def get14(
    power_distribution_id: str, request: Request, response: Response
) -> CircuitCollection:
    s: Service = get_service(CircuitCollection, request)
    b: dict[str, Any] = {
        "power_distribution_id": power_distribution_id,
        "request": request,
        "response": response,
    }
    return cast(CircuitCollection, s.get(**b))


@router.get(
    "/redfish/v1/PowerEquipment/ElectricalBuses/{power_distribution_id}/Mains",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/PowerEquipment/ElectricalBuses/{power_distribution_id}/Mains",
    response_model_exclude_none=True,
)
async def get15(
    power_distribution_id: str, request: Request, response: Response
) -> CircuitCollection:
    s: Service = get_service(CircuitCollection, request)
    b: dict[str, Any] = {
        "power_distribution_id": power_distribution_id,
        "request": request,
        "response": response,
    }
    return cast(CircuitCollection, s.get(**b))


@router.get(
    "/redfish/v1/PowerEquipment/ElectricalBuses/{power_distribution_id}/Branches",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/PowerEquipment/ElectricalBuses/{power_distribution_id}/Branches",
    response_model_exclude_none=True,
)
async def get16(
    power_distribution_id: str, request: Request, response: Response
) -> CircuitCollection:
    s: Service = get_service(CircuitCollection, request)
    b: dict[str, Any] = {
        "power_distribution_id": power_distribution_id,
        "request": request,
        "response": response,
    }
    return cast(CircuitCollection, s.get(**b))
