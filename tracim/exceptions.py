# -*- coding: utf-8 -*-


class TracimError(Exception):
    pass


class TracimException(Exception):
    pass


class RunTimeError(TracimError):
    pass


class ContentRevisionUpdateError(RuntimeError):
    pass


class ContentRevisionDeleteError(ContentRevisionUpdateError):
    pass


class ConfigurationError(TracimError):
    pass


class UserAlreadyExistError(TracimError):
    pass


class BadCommandError(TracimError):
    pass


class DaemonException(TracimException):
    pass


class AlreadyRunningDaemon(DaemonException):
    pass


class CalendarException(TracimException):
    pass


class UnknownCalendarType(CalendarException):
    pass


class NotFound(TracimException):
    pass


class SameValueError(ValueError):
    pass


class NotAuthenticated(TracimException):
    pass


class WorkspaceNotFound(NotFound):
    pass


class WorkspaceNotFoundInTracimRequest(NotFound):
    pass


class InsufficientUserRoleInWorkspace(TracimException):
    pass


class InsufficientUserProfile(TracimException):
    pass


class ImmutableAttribute(TracimException):
    pass


class DigestAuthNotImplemented(Exception):
    pass


class AuthenticationFailed(TracimException):
    pass


class WrongUserPassword(TracimException):
    pass


class NotificationNotSend(TracimException):
    pass


class GroupDoesNotExist(TracimError):
    pass


class ContentStatusNotExist(TracimError):
    pass


class ContentTypeNotExist(TracimError):
    pass


class UserDoesNotExist(TracimException):
    pass


class UserNotFoundInTracimRequest(TracimException):
    pass


class ContentNotFoundInTracimRequest(TracimException):
    pass


class ContentNotFound(TracimException):
    pass


class ContentTypeNotAllowed(TracimException):
    pass


class WorkspacesDoNotMatch(TracimException):
    pass


class EmptyValueNotAllowed(TracimException):
    pass


class EmptyLabelNotAllowed(EmptyValueNotAllowed):
    pass


class EmptyRawContentNotAllowed(EmptyValueNotAllowed):
    pass


class RoleDoesNotExist(TracimException):
    pass


class EmailValidationFailed(TracimException):
    pass


class UserCreationFailed(TracimException):
    pass
