"""CDP ServiceWorker Methods Types"""
from __future__ import annotations
from typing import TypedDict, NotRequired, Required, Literal, Any, Dict, Union, Optional, List, Set, Tuple

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from cdp.protocol.service_worker.types import RegistrationID

class deliverPushMessageParameters(TypedDict, total=True):
    origin: str
    registrationId: RegistrationID
    data: str

class dispatchSyncEventParameters(TypedDict, total=True):
    origin: str
    registrationId: RegistrationID
    tag: str
    lastChance: bool
class dispatchPeriodicSyncEventParameters(TypedDict, total=True):
    origin: str
    registrationId: RegistrationID
    tag: str

class setForceUpdateOnPageLoadParameters(TypedDict, total=True):
    forceUpdateOnPageLoad: bool
class skipWaitingParameters(TypedDict, total=True):
    scopeURL: str
class startWorkerParameters(TypedDict, total=True):
    scopeURL: str

class stopWorkerParameters(TypedDict, total=True):
    versionId: str
class unregisterParameters(TypedDict, total=True):
    scopeURL: str
class updateRegistrationParameters(TypedDict, total=True):
    scopeURL: str