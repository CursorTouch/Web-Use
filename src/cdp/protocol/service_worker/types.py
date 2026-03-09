"""CDP ServiceWorker Types"""
from __future__ import annotations
from typing import TypedDict, NotRequired, Required, Literal, Any, Dict, Union, Optional, List, Set, Tuple

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from cdp.protocol.target.types import TargetID

RegistrationID = str
class ServiceWorkerRegistration(TypedDict, total=True):
    """ServiceWorker registration."""
    registrationId: RegistrationID
    scopeURL: str
    isDeleted: bool
ServiceWorkerVersionRunningStatus = Literal['stopped','starting','running','stopping']
ServiceWorkerVersionStatus = Literal['new','installing','installed','activating','activated','redundant']
class ServiceWorkerVersion(TypedDict, total=True):
    """ServiceWorker version."""
    versionId: str
    registrationId: RegistrationID
    scriptURL: str
    runningStatus: ServiceWorkerVersionRunningStatus
    status: ServiceWorkerVersionStatus
    scriptLastModified: NotRequired[float]
    """The Last-Modified header value of the main script."""
    scriptResponseTime: NotRequired[float]
    """The time at which the response headers of the main script were received from the server. For cached script it is the last time the cache entry was validated."""
    controlledClients: NotRequired[List[TargetID]]
    targetId: NotRequired[TargetID]
    routerRules: NotRequired[str]
class ServiceWorkerErrorMessage(TypedDict, total=True):
    """ServiceWorker error message."""
    errorMessage: str
    registrationId: RegistrationID
    versionId: str
    sourceURL: str
    lineNumber: int
    columnNumber: int