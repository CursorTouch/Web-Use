"""CDP Memory Methods Types"""
from __future__ import annotations
from typing import TypedDict, NotRequired, Required, Literal, Any, Dict, Union, Optional, List, Set, Tuple

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from cdp.protocol.memory.types import DOMCounter
    from cdp.protocol.memory.types import PressureLevel
    from cdp.protocol.memory.types import SamplingProfile





class setPressureNotificationsSuppressedParameters(TypedDict, total=True):
    suppressed: bool
    """If true, memory pressure notifications will be suppressed."""
class simulatePressureNotificationParameters(TypedDict, total=True):
    level: PressureLevel
    """Memory pressure level of the notification."""
class startSamplingParameters(TypedDict, total=False):
    samplingInterval: NotRequired[int]
    """Average number of bytes between samples."""
    suppressRandomness: NotRequired[bool]
    """Do not randomize intervals between samples."""




class getDOMCountersReturns(TypedDict):
    documents: int
    nodes: int
    jsEventListeners: int
class getDOMCountersForLeakDetectionReturns(TypedDict):
    counters: List[DOMCounter]
    """DOM object counters."""






class getAllTimeSamplingProfileReturns(TypedDict):
    profile: SamplingProfile
class getBrowserSamplingProfileReturns(TypedDict):
    profile: SamplingProfile
class getSamplingProfileReturns(TypedDict):
    profile: SamplingProfile