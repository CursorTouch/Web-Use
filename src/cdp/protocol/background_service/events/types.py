"""CDP BackgroundService Events"""
from __future__ import annotations
from typing import TypedDict, NotRequired, Required, Literal, Any, Dict, Union, Optional, List, Set, Tuple

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from cdp.protocol.background_service.types import BackgroundServiceEvent
    from cdp.protocol.background_service.types import ServiceName

class recordingStateChangedEvent(TypedDict, total=True):
    isRecording: bool
    service: ServiceName
class backgroundServiceEventReceivedEvent(TypedDict, total=True):
    backgroundServiceEvent: BackgroundServiceEvent