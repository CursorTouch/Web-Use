"""CDP BackgroundService Types"""
from __future__ import annotations
from typing import TypedDict, NotRequired, Required, Literal, Any, Dict, Union, Optional, List, Set, Tuple

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from cdp.protocol.network.types import TimeSinceEpoch
    from cdp.protocol.serviceworker.types import RegistrationID

ServiceName = Literal['backgroundFetch','backgroundSync','pushMessaging','notifications','paymentHandler','periodicBackgroundSync']
"""The Background Service that will be associated with the commands/events. Every Background Service operates independently, but they share the same API."""
class EventMetadata(TypedDict, total=True):
    """A key-value pair for additional event information to pass along."""
    key: str
    value: str
class BackgroundServiceEvent(TypedDict, total=True):
    timestamp: TimeSinceEpoch
    """Timestamp of the event (in seconds)."""
    origin: str
    """The origin this event belongs to."""
    serviceWorkerRegistrationId: RegistrationID
    """The Service Worker ID that initiated the event."""
    service: ServiceName
    """The Background Service this event belongs to."""
    eventName: str
    """A description of the event."""
    instanceId: str
    """An identifier that groups related events together."""
    eventMetadata: List[EventMetadata]
    """A list of event-specific information."""
    storageKey: str
    """Storage key this event belongs to."""