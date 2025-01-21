from ..model.account_service import AccountService
from ..model.role_collection import RoleCollection
from ..model.service_root import ServiceRoot
from ..model.session_collection import SessionCollection
from ..util import create_etag
from .instance import instances

PATH_REDFISH = "/redfish/v1/"
PATH_ACCOUNT_SERVICE = f"{PATH_REDFISH}AccountService"
PATH_ROLE_COLLECTION = f"{PATH_REDFISH}AccountService/Roles"
PATH_SESSION_COLLECTION = f"{PATH_REDFISH}SessionService/Sessions"


def init_instances() -> None:
    etag = create_etag()

    account_service = AccountService.model_validate(
        {
            "odata_etag": etag,
            "odata_id": PATH_ACCOUNT_SERVICE,
            "id": "AccountService",
            "name": "Account Service",
            "roles": {
                "odata_id": PATH_ROLE_COLLECTION,
            },
        }
    )
    instances.add(account_service)

    role_collection = RoleCollection.model_validate(
        {
            "odata_etag": etag,
            "odata_id": PATH_ROLE_COLLECTION,
            "members": [],
            "members_odata_count": 0,
            "name": "Role Collection",
        }
    )
    instances.add(role_collection)

    service_root = ServiceRoot.model_validate(
        {
            "odata_etag": etag,
            "odata_id": PATH_REDFISH,
            "id": "ServiceRoot",
            "name": "Service Root",
            "links": {
                "sessions": {
                    "odata_id": PATH_SESSION_COLLECTION,
                },
            },
        }
    )
    instances.add(service_root)

    session_collection = SessionCollection.model_validate(
        {
            "odata_etag": etag,
            "odata_id": PATH_SESSION_COLLECTION,
            "members": [],
            "members_odata_count": 0,
            "name": "Session Collection",
        }
    )
    instances.add(session_collection)
