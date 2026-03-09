"""CDP Animation Types"""
from __future__ import annotations
from typing import TypedDict, NotRequired, Required, Literal, Any, Dict, Union, Optional, List, Set, Tuple

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from cdp.protocol.dom.types import BackendNodeId
    from cdp.protocol.dom.types import ScrollOrientation

class Animation(TypedDict, total=True):
    """Animation instance."""
    id: str
    """Animation's id."""
    name: str
    """Animation's name."""
    pausedState: bool
    """Animation's internal paused state."""
    playState: str
    """Animation's play state."""
    playbackRate: float
    """Animation's playback rate."""
    startTime: float
    """Animation's start time. Milliseconds for time based animations and percentage [0 - 100] for scroll driven animations (i.e. when viewOrScrollTimeline exists)."""
    currentTime: float
    """Animation's current time."""
    type: Literal["CSSTransition", "CSSAnimation", "WebAnimation"]
    """Animation type of Animation."""
    source: NotRequired[AnimationEffect]
    """Animation's source animation node."""
    cssId: NotRequired[str]
    """A unique ID for Animation representing the sources that triggered this CSS animation/transition."""
    viewOrScrollTimeline: NotRequired[ViewOrScrollTimeline]
    """View or scroll timeline"""
class ViewOrScrollTimeline(TypedDict, total=True):
    """Timeline instance"""
    axis: ScrollOrientation
    """Orientation of the scroll"""
    sourceNodeId: NotRequired[BackendNodeId]
    """Scroll container node"""
    startOffset: NotRequired[float]
    """Represents the starting scroll position of the timeline as a length offset in pixels from scroll origin."""
    endOffset: NotRequired[float]
    """Represents the ending scroll position of the timeline as a length offset in pixels from scroll origin."""
    subjectNodeId: NotRequired[BackendNodeId]
    """The element whose principal box's visibility in the scrollport defined the progress of the timeline. Does not exist for animations with ScrollTimeline"""
class AnimationEffect(TypedDict, total=True):
    """AnimationEffect instance"""
    delay: float
    """AnimationEffect's delay."""
    endDelay: float
    """AnimationEffect's end delay."""
    iterationStart: float
    """AnimationEffect's iteration start."""
    duration: float
    """AnimationEffect's iteration duration. Milliseconds for time based animations and percentage [0 - 100] for scroll driven animations (i.e. when viewOrScrollTimeline exists)."""
    direction: str
    """AnimationEffect's playback direction."""
    fill: str
    """AnimationEffect's fill mode."""
    easing: str
    """AnimationEffect's timing function."""
    iterations: NotRequired[float]
    """AnimationEffect's iterations. Omitted if the value is infinite."""
    backendNodeId: NotRequired[BackendNodeId]
    """AnimationEffect's target node."""
    keyframesRule: NotRequired[KeyframesRule]
    """AnimationEffect's keyframes."""
class KeyframesRule(TypedDict, total=True):
    """Keyframes Rule"""
    keyframes: List[KeyframeStyle]
    """List of animation keyframes."""
    name: NotRequired[str]
    """CSS keyframed animation's name."""
class KeyframeStyle(TypedDict, total=True):
    """Keyframe Style"""
    offset: str
    """Keyframe's time offset."""
    easing: str
    """AnimationEffect's timing function."""