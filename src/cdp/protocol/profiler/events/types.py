"""CDP Profiler Events"""
from __future__ import annotations
from typing import TypedDict, NotRequired, Required, Literal, Any, Dict, Union, Optional, List, Set, Tuple

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from cdp.protocol.debugger.types import Location
    from cdp.protocol.profiler.types import Profile
    from cdp.protocol.profiler.types import ScriptCoverage

class consoleProfileFinishedEvent(TypedDict, total=True):
    id: str
    location: Location
    """Location of console.profileEnd()."""
    profile: Profile
    title: NotRequired[str]
    """Profile title passed as an argument to console.profile()."""
class consoleProfileStartedEvent(TypedDict, total=True):
    id: str
    location: Location
    """Location of console.profile()."""
    title: NotRequired[str]
    """Profile title passed as an argument to console.profile()."""
class preciseCoverageDeltaUpdateEvent(TypedDict, total=True):
    timestamp: float
    """Monotonically increasing time (in seconds) when the coverage update was taken in the backend."""
    occasion: str
    """Identifier for distinguishing coverage events."""
    result: List[ScriptCoverage]
    """Coverage data for the current isolate."""