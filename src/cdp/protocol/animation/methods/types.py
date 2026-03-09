"""CDP Animation Methods Types"""
from __future__ import annotations
from typing import TypedDict, NotRequired, Required, Literal, Any, Dict, Union, Optional, List, Set, Tuple

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from cdp.protocol.runtime.types import RemoteObject



class getCurrentTimeParameters(TypedDict, total=True):
    id: str
    """Id of animation."""

class releaseAnimationsParameters(TypedDict, total=True):
    animations: List[str]
    """List of animation ids to seek."""
class resolveAnimationParameters(TypedDict, total=True):
    animationId: str
    """Animation id."""
class seekAnimationsParameters(TypedDict, total=True):
    animations: List[str]
    """List of animation ids to seek."""
    currentTime: float
    """Set the current time of each animation."""
class setPausedParameters(TypedDict, total=True):
    animations: List[str]
    """Animations to set the pause state of."""
    paused: bool
    """Paused state to set to."""
class setPlaybackRateParameters(TypedDict, total=True):
    playbackRate: float
    """Playback rate for animations on page"""
class setTimingParameters(TypedDict, total=True):
    animationId: str
    """Animation id."""
    duration: float
    """Duration of the animation."""
    delay: float
    """Delay of the animation."""


class getCurrentTimeReturns(TypedDict):
    currentTime: float
    """Current time of the page."""
class getPlaybackRateReturns(TypedDict):
    playbackRate: float
    """Playback rate for animations on page."""

class resolveAnimationReturns(TypedDict):
    remoteObject: RemoteObject
    """Corresponding remote object."""