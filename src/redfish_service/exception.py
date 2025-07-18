from http import HTTPStatus
from typing import Any

from .model.redfish_error import RedfishError as Error


class RedfishError(Exception):
    def __init__(self, status_code: int, error: Error) -> None:
        self.status_code = status_code
        self.error = error


class GeneralErrorError(RedfishError):
    def __init__(self, status_code: int = HTTPStatus.INTERNAL_SERVER_ERROR) -> None:
        info = {
            "error": {
                "code": "Base.1.19.0.GeneralError",
                "message": "A general error has occurred."
                + " See Resolution for information on how to resolve the error,"
                + " or @Message.ExtendedInfo if Resolution is not provided.",
            }
        }
        error = Error.model_validate(info)
        super().__init__(status_code, error)


class InvalidURIError(RedfishError):
    def __init__(self, uri: str) -> None:
        info = {
            "error": {
                "code": "Base.1.19.0.InvalidURI",
                "message": f"The URI {uri} was not found.",
            }
        }
        error = Error.model_validate(info)
        super().__init__(HTTPStatus.NOT_FOUND, error)


class InternalErrorError(RedfishError):
    def __init__(self, status_code: int = HTTPStatus.INTERNAL_SERVER_ERROR) -> None:
        info = {
            "error": {
                "code": "Base.1.19.0.InternalError",
                "message": "The request failed due to an internal service error. "
                + "The service is still operational.",
            }
        }
        error = Error.model_validate(info)
        super().__init__(status_code, error)


class MalformedJsonError(RedfishError):
    def __init__(self, status_code: int = HTTPStatus.UNPROCESSABLE_ENTITY) -> None:
        info = {
            "error": {
                "code": "Base.1.19.0.MalformedJSON",
                "message": "The request body submitted was malformed JSON and"
                + " could not be parsed by the receiving service.",
            }
        }
        error = Error.model_validate(info)
        super().__init__(status_code, error)


class OperationNotAllowedError(RedfishError):
    def __init__(self, service: Any) -> None:  # noqa: ANN401
        self.service = service
        info = {
            "error": {
                "code": "Base.1.19.0.OperationNotAllowed",
                "message": "The HTTP method is not allowed on this resource.",
            }
        }
        error = Error.model_validate(info)
        super().__init__(HTTPStatus.METHOD_NOT_ALLOWED, error)


class PreconditionFailedError(RedfishError):
    def __init__(self) -> None:
        info = {
            "error": {
                "code": "Base.1.19.0.PreconditionFailed",
                "message": "The ETag supplied did not match the ETag required"
                + " to change this resource.",
            }
        }
        error = Error.model_validate(info)
        super().__init__(HTTPStatus.PRECONDITION_FAILED, error)


class PreconditionRequiredError(RedfishError):
    def __init__(self) -> None:
        info = {
            "error": {
                "code": "Base.1.19.0.PreconditionRequired",
                "message": "A precondition header or annotation is required"
                + " to change this resource.",
            }
        }
        error = Error.model_validate(info)
        super().__init__(HTTPStatus.PRECONDITION_REQUIRED, error)


class ResourceAtUriUnauthorizedError(RedfishError):
    def __init__(self, uri: str, message: str) -> None:
        info = {
            "error": {
                "code": "Base.1.19.0.ResourceAtUriUnauthorized",
                "message": f"While accessing the resource at '{uri}', "
                + f"the service received an authorization error '{message}'.",
            }
        }
        error = Error.model_validate(info)
        super().__init__(HTTPStatus.UNAUTHORIZED, error)


class ResourceNotFoundError(RedfishError):
    def __init__(self, type: str, id: str) -> None:
        info = {
            "error": {
                "code": "Base.1.19.0.ResourceNotFound",
                "message": f"The requested resource of type {type} named {id} was not found.",
            }
        }
        error = Error.model_validate(info)
        super().__init__(HTTPStatus.NOT_FOUND, error)
