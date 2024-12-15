from http import HTTPStatus

from .v1 import RedfishError as Error


class RedfishError(Exception):
    def __init__(self, status_code: int, error: Error):
        self.status_code = status_code
        self.error = error


class InvalidURIError(RedfishError):
    def __init__(self, uri: str):
        info = {
            "error": {
                "code": "Base.1.19.0.InvalidURI",
                "message": f"The URI {uri} was not found.",
            }
        }
        error = Error.model_validate(info)
        super().__init__(HTTPStatus.NOT_FOUND, error)


class InternalErrorError(RedfishError):
    def __init__(self, status_code: int = HTTPStatus.INTERNAL_SERVER_ERROR):
        info = {
            "error": {
                "code": "Base.1.19.0.InternalError",
                "message": "The request failed due to an internal service error. "
                + "The service is still operational.",
            }
        }
        error = Error.model_validate(info)
        super().__init__(status_code, error)


class ResourceAtUriUnauthorizedError(RedfishError):
    def __init__(self, uri: str, message: str):
        info = {
            "error": {
                "code": "Base.1.19.0.ResourceAtUriUnauthorized",
                "message": f"While accessing the resource at '{uri}', "
                + f"the service received an authorization error '{message}'.",
            }
        }
        error = Error.model_validate(info)
        super().__init__(HTTPStatus.UNAUTHORIZED, error)
