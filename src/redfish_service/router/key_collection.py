from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.key import Key, KeyOnCreate
from ..model.key_collection import KeyCollection
from ..service import Service, ServiceCollection, find_service, find_service_collection

router = APIRouter()


@router.get("/redfish/v1/KeyService/NVMeoFSecrets", response_model_exclude_none=True)
@router.head("/redfish/v1/KeyService/NVMeoFSecrets", response_model_exclude_none=True)
@authenticate
async def get1(request: Request, response: Response) -> KeyCollection:
    s: Service = find_service(KeyCollection)
    b: dict[str, Any] = {"request": request, "response": response}

    response.headers["OData-Version"] = "4.0"

    return cast(KeyCollection, s.get(**b))


@router.post("/redfish/v1/KeyService/NVMeoFSecrets", response_model_exclude_none=True)
@router.post("/redfish/v1/KeyService/NVMeoFSecrets/Members", response_model_exclude_none=True)
@authenticate
async def post1(request: Request, response: Response, body: KeyOnCreate) -> Key:
    s: ServiceCollection = find_service_collection(KeyCollection)
    b: dict[str, Any] = {"request": request, "response": response, "body": body}

    response.headers["OData-Version"] = "4.0"

    return cast(Key, s.post(**b))


@router.get("/redfish/v1/UpdateService/RemoteServerSSHKeys", response_model_exclude_none=True)
@router.head("/redfish/v1/UpdateService/RemoteServerSSHKeys", response_model_exclude_none=True)
@authenticate
async def get2(request: Request, response: Response) -> KeyCollection:
    s: Service = find_service(KeyCollection)
    b: dict[str, Any] = {"request": request, "response": response}

    response.headers["OData-Version"] = "4.0"

    return cast(KeyCollection, s.get(**b))


@router.post("/redfish/v1/UpdateService/RemoteServerSSHKeys", response_model_exclude_none=True)
@router.post(
    "/redfish/v1/UpdateService/RemoteServerSSHKeys/Members", response_model_exclude_none=True
)
@authenticate
async def post2(request: Request, response: Response, body: KeyOnCreate) -> Key:
    s: ServiceCollection = find_service_collection(KeyCollection)
    b: dict[str, Any] = {"request": request, "response": response, "body": body}

    response.headers["OData-Version"] = "4.0"

    return cast(Key, s.post(**b))


@router.get(
    "/redfish/v1/AccountService/Accounts/{manager_account_id}/Keys",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/AccountService/Accounts/{manager_account_id}/Keys",
    response_model_exclude_none=True,
)
@authenticate
async def get3(manager_account_id: str, request: Request, response: Response) -> KeyCollection:
    s: Service = find_service(KeyCollection)
    b: dict[str, Any] = {
        "manager_account_id": manager_account_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(KeyCollection, s.get(**b))


@router.post(
    "/redfish/v1/AccountService/Accounts/{manager_account_id}/Keys",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/AccountService/Accounts/{manager_account_id}/Keys/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post3(
    manager_account_id: str, request: Request, response: Response, body: KeyOnCreate
) -> Key:
    s: ServiceCollection = find_service_collection(KeyCollection)
    b: dict[str, Any] = {
        "manager_account_id": manager_account_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(Key, s.post(**b))


@router.get(
    "/redfish/v1/Managers/{manager_id}/RemoteAccountService/Accounts/{manager_account_id}/Keys",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Managers/{manager_id}/RemoteAccountService/Accounts/{manager_account_id}/Keys",
    response_model_exclude_none=True,
)
@authenticate
async def get4(
    manager_id: str, manager_account_id: str, request: Request, response: Response
) -> KeyCollection:
    s: Service = find_service(KeyCollection)
    b: dict[str, Any] = {
        "manager_id": manager_id,
        "manager_account_id": manager_account_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(KeyCollection, s.get(**b))


@router.post(
    "/redfish/v1/Managers/{manager_id}/RemoteAccountService/Accounts/{manager_account_id}/Keys",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/Managers/{manager_id}/RemoteAccountService/Accounts/{manager_account_id}/Keys/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post4(
    manager_id: str,
    manager_account_id: str,
    request: Request,
    response: Response,
    body: KeyOnCreate,
) -> Key:
    s: ServiceCollection = find_service_collection(KeyCollection)
    b: dict[str, Any] = {
        "manager_id": manager_id,
        "manager_account_id": manager_account_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(Key, s.post(**b))


@router.get(
    "/redfish/v1/AggregationService/AggregationSources/{aggregation_source_id}/TrustedPublicHostKeys",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/AggregationService/AggregationSources/{aggregation_source_id}/TrustedPublicHostKeys",
    response_model_exclude_none=True,
)
@authenticate
async def get5(aggregation_source_id: str, request: Request, response: Response) -> KeyCollection:
    s: Service = find_service(KeyCollection)
    b: dict[str, Any] = {
        "aggregation_source_id": aggregation_source_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(KeyCollection, s.get(**b))


@router.post(
    "/redfish/v1/AggregationService/AggregationSources/{aggregation_source_id}/TrustedPublicHostKeys",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/AggregationService/AggregationSources/{aggregation_source_id}/TrustedPublicHostKeys/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post5(
    aggregation_source_id: str, request: Request, response: Response, body: KeyOnCreate
) -> Key:
    s: ServiceCollection = find_service_collection(KeyCollection)
    b: dict[str, Any] = {
        "aggregation_source_id": aggregation_source_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(Key, s.post(**b))
