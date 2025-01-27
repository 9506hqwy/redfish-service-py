from ..model.account_service import AccountService
from ..model.manager_account import ManagerAccount
from ..model.manager_account_collection import ManagerAccountCollection
from ..model.privileges import PrivilegeType
from ..model.role import Role
from ..model.role_collection import RoleCollection
from ..model.service_root import ServiceRoot
from ..model.session_collection import SessionCollection
from ..model.values import AccountTypes
from ..util import create_etag
from .instance import instances

PATH_REDFISH = "/redfish/v1/"
PATH_ACCOUNT_SERVICE = f"{PATH_REDFISH}AccountService"
PATH_ACCOUNT_COLLECTION = f"{PATH_REDFISH}AccountService/Accounts"
PATH_ROLE_COLLECTION = f"{PATH_REDFISH}AccountService/Roles"
PATH_SESSION_COLLECTION = f"{PATH_REDFISH}SessionService/Sessions"


def init_instances() -> None:
    etag = create_etag()

    account_service = AccountService.model_validate(
        {
            "odata_etag": etag,
            "odata_id": PATH_ACCOUNT_SERVICE,
            "accounts": {
                "odata_id": PATH_ACCOUNT_COLLECTION,
            },
            "id": "AccountService",
            "name": "Account Service",
            "roles": {
                "odata_id": PATH_ROLE_COLLECTION,
            },
        }
    )
    instances.add(account_service)

    account_collection = ManagerAccountCollection.model_validate(
        {
            "odata_etag": etag,
            "odata_id": PATH_ACCOUNT_COLLECTION,
            "members": [],
            "members_odata_count": 0,
            "name": "Account Collection",
        }
    )
    instances.add(account_collection)

    account_admin = ManagerAccount.model_validate(
        {
            "odata_etag": etag,
            "odata_id": f"{PATH_ACCOUNT_COLLECTION}/admin",
            "account_types": [AccountTypes.REDFISH],
            "id": "admin",
            "name": "admin",
        }
    )
    account_admin.extra_fields["password"] = "admin"  # noqa: S105
    instances.add(account_admin)

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

    role_admin = Role.model_validate(
        {
            "odata_etag": etag,
            "odata_id": f"{PATH_ROLE_COLLECTION}/Administrator",
            "assigned_privileges": [
                PrivilegeType.LOGIN,
                PrivilegeType.CONFIGURE_MANAGER,
                PrivilegeType.CONFIGURE_USERS,
                PrivilegeType.CONFIGURE_COMPONENTS,
                PrivilegeType.CONFIGURE_SELF,
            ],
            "id": "Administrator",
            "is_predefined": True,
            "name": "Administrator",
            "role_id": "Administrator",
        }
    )
    instances.add(role_admin)

    role_operator = Role.model_validate(
        {
            "odata_etag": etag,
            "odata_id": f"{PATH_ROLE_COLLECTION}/Operator",
            "assigned_privileges": [
                PrivilegeType.LOGIN,
                PrivilegeType.CONFIGURE_COMPONENTS,
                PrivilegeType.CONFIGURE_SELF,
            ],
            "id": "Operator",
            "is_predefined": True,
            "name": "Operator",
            "role_id": "Operator",
        }
    )
    instances.add(role_operator)

    role_readonly = Role.model_validate(
        {
            "odata_etag": etag,
            "odata_id": f"{PATH_ROLE_COLLECTION}/ReadOnly",
            "assigned_privileges": [
                PrivilegeType.LOGIN,
                PrivilegeType.CONFIGURE_SELF,
            ],
            "id": "ReadOnly",
            "is_predefined": True,
            "name": "ReadOnly",
            "role_id": "ReadOnly",
        }
    )
    instances.add(role_readonly)

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
