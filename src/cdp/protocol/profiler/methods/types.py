"""CDP Profiler Methods Types"""
from __future__ import annotations
from typing import TypedDict, NotRequired, Required, Literal, Any, Dict, Union, Optional, List, Set, Tuple

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from cdp.protocol.profiler.types import Profile
    from cdp.protocol.profiler.types import ScriptCoverage




class setSamplingIntervalParameters(TypedDict, total=True):
    interval: int
    """New sampling interval in microseconds."""

class startPreciseCoverageParameters(TypedDict, total=False):
    callCount: NotRequired[bool]
    """Collect accurate call counts beyond simple 'covered' or 'not covered'."""
    detailed: NotRequired[bool]
    """Collect block-based coverage."""
    allowTriggeredUpdates: NotRequired[bool]
    """Allow the backend to send updates on its own initiative"""





class getBestEffortCoverageReturns(TypedDict):
    result: List[ScriptCoverage]
    """Coverage data for the current isolate."""


class startPreciseCoverageReturns(TypedDict):
    timestamp: float
    """Monotonically increasing time (in seconds) when the coverage update was taken in the backend."""
class stopReturns(TypedDict):
    profile: Profile
    """Recorded profile."""

class takePreciseCoverageReturns(TypedDict):
    result: List[ScriptCoverage]
    """Coverage data for the current isolate."""
    timestamp: float
    """Monotonically increasing time (in seconds) when the coverage update was taken in the backend."""