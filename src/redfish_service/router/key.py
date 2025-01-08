from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..model.key import Key
from ..service import Service, find_service

router = APIRouter()


@router.get("/redfish/v1/KeyService/NVMeoFSecrets/{key_id}", response_model_exclude_none=True)
@router.head("/redfish/v1/KeyService/NVMeoFSecrets/{key_id}", response_model_exclude_none=True)
async def get1(key_id: str, request: Request, response: Response) -> Key:
    s: Service = find_service(Key)
    b: dict[str, Any] = {"key_id": key_id, "request": request, "response": response}

    response.headers["OData-Version"] = "4.0"

    return cast(Key, s.get(**b))


@router.get(
    "/redfish/v1/UpdateService/RemoteServerSSHKeys/{key_id}", response_model_exclude_none=True
)
@router.head(
    "/redfish/v1/UpdateService/RemoteServerSSHKeys/{key_id}", response_model_exclude_none=True
)
async def get2(key_id: str, request: Request, response: Response) -> Key:
    s: Service = find_service(Key)
    b: dict[str, Any] = {"key_id": key_id, "request": request, "response": response}

    response.headers["OData-Version"] = "4.0"

    return cast(Key, s.get(**b))


@router.get(
    "/redfish/v1/UpdateService/PublicIdentitySSHKey/{key_id}", response_model_exclude_none=True
)
@router.head(
    "/redfish/v1/UpdateService/PublicIdentitySSHKey/{key_id}", response_model_exclude_none=True
)
async def get3(key_id: str, request: Request, response: Response) -> Key:
    s: Service = find_service(Key)
    b: dict[str, Any] = {"key_id": key_id, "request": request, "response": response}

    response.headers["OData-Version"] = "4.0"

    return cast(Key, s.get(**b))


@router.get(
    "/redfish/v1/AccountService/Accounts/{manager_account_id}/Keys/{key_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/AccountService/Accounts/{manager_account_id}/Keys/{key_id}",
    response_model_exclude_none=True,
)
async def get4(manager_account_id: str, key_id: str, request: Request, response: Response) -> Key:
    s: Service = find_service(Key)
    b: dict[str, Any] = {
        "manager_account_id": manager_account_id,
        "key_id": key_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(Key, s.get(**b))


@router.get(
    "/redfish/v1/Managers/{manager_id}/RemoteAccountService/Accounts/{manager_account_id}/Keys/{key_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Managers/{manager_id}/RemoteAccountService/Accounts/{manager_account_id}/Keys/{key_id}",
    response_model_exclude_none=True,
)
async def get5(
    manager_id: str, manager_account_id: str, key_id: str, request: Request, response: Response
) -> Key:
    s: Service = find_service(Key)
    b: dict[str, Any] = {
        "manager_id": manager_id,
        "manager_account_id": manager_account_id,
        "key_id": key_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(Key, s.get(**b))


@router.get(
    "/redfish/v1/AggregationService/AggregationSources/{aggregation_source_id}/TrustedPublicHostKeys/{key_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/AggregationService/AggregationSources/{aggregation_source_id}/TrustedPublicHostKeys/{key_id}",
    response_model_exclude_none=True,
)
async def get6(
    aggregation_source_id: str, key_id: str, request: Request, response: Response
) -> Key:
    s: Service = find_service(Key)
    b: dict[str, Any] = {
        "aggregation_source_id": aggregation_source_id,
        "key_id": key_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(Key, s.get(**b))


@router.get(
    "/redfish/v1/AggregationService/AggregationSources/{aggregation_source_id}/PresentedPublicHostKey",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/AggregationService/AggregationSources/{aggregation_source_id}/PresentedPublicHostKey",
    response_model_exclude_none=True,
)
async def get7(aggregation_source_id: str, request: Request, response: Response) -> Key:
    s: Service = find_service(Key)
    b: dict[str, Any] = {
        "aggregation_source_id": aggregation_source_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(Key, s.get(**b))


@router.get(
    "/redfish/v1/AggregationService/AggregationSources/{aggregation_source_id}/PublicIdentityKey",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/AggregationService/AggregationSources/{aggregation_source_id}/PublicIdentityKey",
    response_model_exclude_none=True,
)
async def get8(aggregation_source_id: str, request: Request, response: Response) -> Key:
    s: Service = find_service(Key)
    b: dict[str, Any] = {
        "aggregation_source_id": aggregation_source_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(Key, s.get(**b))
