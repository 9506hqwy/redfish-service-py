from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.circuit import Circuit
from ..service import Service, find_service

router = APIRouter()


@router.get(
    "/redfish/v1/PowerEquipment/RackPDUs/{power_distribution_id}/Mains/{circuit_id}",
    response_model_exclude_none=True,
)
@authenticate
async def get1(
    power_distribution_id: str, circuit_id: str, request: Request, response: Response
) -> Circuit:
    s: Service = find_service(Circuit)
    b: dict[str, Any] = {
        "power_distribution_id": power_distribution_id,
        "circuit_id": circuit_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(Circuit, s.get(**b))


@router.get(
    "/redfish/v1/PowerEquipment/RackPDUs/{power_distribution_id}/Branches/{circuit_id}",
    response_model_exclude_none=True,
)
@authenticate
async def get2(
    power_distribution_id: str, circuit_id: str, request: Request, response: Response
) -> Circuit:
    s: Service = find_service(Circuit)
    b: dict[str, Any] = {
        "power_distribution_id": power_distribution_id,
        "circuit_id": circuit_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(Circuit, s.get(**b))


@router.get(
    "/redfish/v1/PowerEquipment/FloorPDUs/{power_distribution_id}/Mains/{circuit_id}",
    response_model_exclude_none=True,
)
@authenticate
async def get3(
    power_distribution_id: str, circuit_id: str, request: Request, response: Response
) -> Circuit:
    s: Service = find_service(Circuit)
    b: dict[str, Any] = {
        "power_distribution_id": power_distribution_id,
        "circuit_id": circuit_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(Circuit, s.get(**b))


@router.get(
    "/redfish/v1/PowerEquipment/FloorPDUs/{power_distribution_id}/Branches/{circuit_id}",
    response_model_exclude_none=True,
)
@authenticate
async def get4(
    power_distribution_id: str, circuit_id: str, request: Request, response: Response
) -> Circuit:
    s: Service = find_service(Circuit)
    b: dict[str, Any] = {
        "power_distribution_id": power_distribution_id,
        "circuit_id": circuit_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(Circuit, s.get(**b))


@router.get(
    "/redfish/v1/PowerEquipment/FloorPDUs/{power_distribution_id}/Subfeeds/{circuit_id}",
    response_model_exclude_none=True,
)
@authenticate
async def get5(
    power_distribution_id: str, circuit_id: str, request: Request, response: Response
) -> Circuit:
    s: Service = find_service(Circuit)
    b: dict[str, Any] = {
        "power_distribution_id": power_distribution_id,
        "circuit_id": circuit_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(Circuit, s.get(**b))


@router.get(
    "/redfish/v1/PowerEquipment/TransferSwitches/{power_distribution_id}/Mains/{circuit_id}",
    response_model_exclude_none=True,
)
@authenticate
async def get6(
    power_distribution_id: str, circuit_id: str, request: Request, response: Response
) -> Circuit:
    s: Service = find_service(Circuit)
    b: dict[str, Any] = {
        "power_distribution_id": power_distribution_id,
        "circuit_id": circuit_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(Circuit, s.get(**b))


@router.get(
    "/redfish/v1/PowerEquipment/TransferSwitches/{power_distribution_id}/Branches/{circuit_id}",
    response_model_exclude_none=True,
)
@authenticate
async def get7(
    power_distribution_id: str, circuit_id: str, request: Request, response: Response
) -> Circuit:
    s: Service = find_service(Circuit)
    b: dict[str, Any] = {
        "power_distribution_id": power_distribution_id,
        "circuit_id": circuit_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(Circuit, s.get(**b))


@router.get(
    "/redfish/v1/PowerEquipment/TransferSwitches/{power_distribution_id}/Feeders/{circuit_id}",
    response_model_exclude_none=True,
)
@authenticate
async def get8(
    power_distribution_id: str, circuit_id: str, request: Request, response: Response
) -> Circuit:
    s: Service = find_service(Circuit)
    b: dict[str, Any] = {
        "power_distribution_id": power_distribution_id,
        "circuit_id": circuit_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(Circuit, s.get(**b))


@router.get(
    "/redfish/v1/PowerEquipment/PowerShelves/{power_distribution_id}/Mains/{circuit_id}",
    response_model_exclude_none=True,
)
@authenticate
async def get9(
    power_distribution_id: str, circuit_id: str, request: Request, response: Response
) -> Circuit:
    s: Service = find_service(Circuit)
    b: dict[str, Any] = {
        "power_distribution_id": power_distribution_id,
        "circuit_id": circuit_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(Circuit, s.get(**b))


@router.get(
    "/redfish/v1/PowerEquipment/PowerShelves/{power_distribution_id}/Branches/{circuit_id}",
    response_model_exclude_none=True,
)
@authenticate
async def get10(
    power_distribution_id: str, circuit_id: str, request: Request, response: Response
) -> Circuit:
    s: Service = find_service(Circuit)
    b: dict[str, Any] = {
        "power_distribution_id": power_distribution_id,
        "circuit_id": circuit_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(Circuit, s.get(**b))


@router.get(
    "/redfish/v1/PowerEquipment/Switchgear/{power_distribution_id}/Mains/{circuit_id}",
    response_model_exclude_none=True,
)
@authenticate
async def get11(
    power_distribution_id: str, circuit_id: str, request: Request, response: Response
) -> Circuit:
    s: Service = find_service(Circuit)
    b: dict[str, Any] = {
        "power_distribution_id": power_distribution_id,
        "circuit_id": circuit_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(Circuit, s.get(**b))


@router.get(
    "/redfish/v1/PowerEquipment/Switchgear/{power_distribution_id}/Subfeeds/{circuit_id}",
    response_model_exclude_none=True,
)
@authenticate
async def get12(
    power_distribution_id: str, circuit_id: str, request: Request, response: Response
) -> Circuit:
    s: Service = find_service(Circuit)
    b: dict[str, Any] = {
        "power_distribution_id": power_distribution_id,
        "circuit_id": circuit_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(Circuit, s.get(**b))


@router.get(
    "/redfish/v1/PowerEquipment/Switchgear/{power_distribution_id}/Feeders/{circuit_id}",
    response_model_exclude_none=True,
)
@authenticate
async def get13(
    power_distribution_id: str, circuit_id: str, request: Request, response: Response
) -> Circuit:
    s: Service = find_service(Circuit)
    b: dict[str, Any] = {
        "power_distribution_id": power_distribution_id,
        "circuit_id": circuit_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(Circuit, s.get(**b))


@router.get(
    "/redfish/v1/PowerEquipment/Switchgear/{power_distribution_id}/Branches/{circuit_id}",
    response_model_exclude_none=True,
)
@authenticate
async def get14(
    power_distribution_id: str, circuit_id: str, request: Request, response: Response
) -> Circuit:
    s: Service = find_service(Circuit)
    b: dict[str, Any] = {
        "power_distribution_id": power_distribution_id,
        "circuit_id": circuit_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(Circuit, s.get(**b))


@router.get(
    "/redfish/v1/PowerEquipment/ElectricalBuses/{power_distribution_id}/Mains/{circuit_id}",
    response_model_exclude_none=True,
)
@authenticate
async def get15(
    power_distribution_id: str, circuit_id: str, request: Request, response: Response
) -> Circuit:
    s: Service = find_service(Circuit)
    b: dict[str, Any] = {
        "power_distribution_id": power_distribution_id,
        "circuit_id": circuit_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(Circuit, s.get(**b))


@router.get(
    "/redfish/v1/PowerEquipment/ElectricalBuses/{power_distribution_id}/Branches/{circuit_id}",
    response_model_exclude_none=True,
)
@authenticate
async def get16(
    power_distribution_id: str, circuit_id: str, request: Request, response: Response
) -> Circuit:
    s: Service = find_service(Circuit)
    b: dict[str, Any] = {
        "power_distribution_id": power_distribution_id,
        "circuit_id": circuit_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(Circuit, s.get(**b))
