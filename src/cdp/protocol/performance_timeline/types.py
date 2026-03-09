"""CDP PerformanceTimeline Types"""
from __future__ import annotations
from typing import TypedDict, NotRequired, Required, Literal, Any, Dict, Union, Optional, List, Set, Tuple

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from cdp.protocol.dom.types import BackendNodeId
    from cdp.protocol.dom.types import Rect
    from cdp.protocol.network.types import TimeSinceEpoch
    from cdp.protocol.page.types import FrameId

class LargestContentfulPaint(TypedDict, total=True):
    """See https://github.com/WICG/LargestContentfulPaint and largest_contentful_paint.idl"""
    renderTime: TimeSinceEpoch
    loadTime: TimeSinceEpoch
    size: float
    """The number of pixels being painted."""
    elementId: NotRequired[str]
    """The id attribute of the element, if available."""
    url: NotRequired[str]
    """The URL of the image (may be trimmed)."""
    nodeId: NotRequired[BackendNodeId]
class LayoutShiftAttribution(TypedDict, total=True):
    previousRect: Rect
    currentRect: Rect
    nodeId: NotRequired[BackendNodeId]
class LayoutShift(TypedDict, total=True):
    """See https://wicg.github.io/layout-instability/#sec-layout-shift and layout_shift.idl"""
    value: float
    """Score increment produced by this event."""
    hadRecentInput: bool
    lastInputTime: TimeSinceEpoch
    sources: List[LayoutShiftAttribution]
class TimelineEvent(TypedDict, total=True):
    frameId: FrameId
    """Identifies the frame that this event is related to. Empty for non-frame targets."""
    type: str
    """The event type, as specified in https://w3c.github.io/performance-timeline/#dom-performanceentry-entrytype This determines which of the optional details fields is present."""
    name: str
    """Name may be empty depending on the type."""
    time: TimeSinceEpoch
    """Time in seconds since Epoch, monotonically increasing within document lifetime."""
    duration: NotRequired[float]
    """Event duration, if applicable."""
    lcpDetails: NotRequired[LargestContentfulPaint]
    layoutShiftDetails: NotRequired[LayoutShift]