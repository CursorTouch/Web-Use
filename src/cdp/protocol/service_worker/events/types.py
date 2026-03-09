"""CDP ServiceWorker Events"""
from __future__ import annotations
from typing import TypedDict, NotRequired, Required, Literal, Any, Dict, Union, Optional, List, Set, Tuple

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from cdp.protocol.service_worker.types import ServiceWorkerErrorMessage
    from cdp.protocol.service_worker.types import ServiceWorkerRegistration
    from cdp.protocol.service_worker.types import ServiceWorkerVersion

class workerErrorReportedEvent(TypedDict, total=True):
    errorMessage: ServiceWorkerErrorMessage
class workerRegistrationUpdatedEvent(TypedDict, total=True):
    registrations: List[ServiceWorkerRegistration]
class workerVersionUpdatedEvent(TypedDict, total=True):
    versions: List[ServiceWorkerVersion]