"""CDP LayerTree Types"""
from __future__ import annotations
from typing import TypedDict, NotRequired, Required, Literal, Any, Dict, Union, Optional, List, Set, Tuple

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from cdp.protocol.dom.types import BackendNodeId
    from cdp.protocol.dom.types import Rect

LayerId = str
"""Unique Layer identifier."""
SnapshotId = str
"""Unique snapshot identifier."""
class ScrollRect(TypedDict, total=True):
    """Rectangle where scrolling happens on the main thread."""
    rect: Rect
    """Rectangle itself."""
    type: Literal["RepaintsOnScroll", "TouchEventHandler", "WheelEventHandler"]
    """Reason for rectangle to force scrolling on the main thread"""
class StickyPositionConstraint(TypedDict, total=True):
    """Sticky position constraints."""
    stickyBoxRect: Rect
    """Layout rectangle of the sticky element before being shifted"""
    containingBlockRect: Rect
    """Layout rectangle of the containing block of the sticky element"""
    nearestLayerShiftingStickyBox: NotRequired[LayerId]
    """The nearest sticky layer that shifts the sticky box"""
    nearestLayerShiftingContainingBlock: NotRequired[LayerId]
    """The nearest sticky layer that shifts the containing block"""
class PictureTile(TypedDict, total=True):
    """Serialized fragment of layer picture along with its offset within the layer."""
    x: float
    """Offset from owning layer left boundary"""
    y: float
    """Offset from owning layer top boundary"""
    picture: str
    """Base64-encoded snapshot data. (Encoded as a base64 string when passed over JSON)"""
class Layer(TypedDict, total=True):
    """Information about a compositing layer."""
    layerId: LayerId
    """The unique id for this layer."""
    offsetX: float
    """Offset from parent layer, X coordinate."""
    offsetY: float
    """Offset from parent layer, Y coordinate."""
    width: float
    """Layer width."""
    height: float
    """Layer height."""
    paintCount: int
    """Indicates how many time this layer has painted."""
    drawsContent: bool
    """Indicates whether this layer hosts any content, rather than being used for transform/scrolling purposes only."""
    parentLayerId: NotRequired[LayerId]
    """The id of parent (not present for root)."""
    backendNodeId: NotRequired[BackendNodeId]
    """The backend id for the node associated with this layer."""
    transform: NotRequired[List[float]]
    """Transformation matrix for layer, default is identity matrix"""
    anchorX: NotRequired[float]
    """Transform anchor point X, absent if no transform specified"""
    anchorY: NotRequired[float]
    """Transform anchor point Y, absent if no transform specified"""
    anchorZ: NotRequired[float]
    """Transform anchor point Z, absent if no transform specified"""
    invisible: NotRequired[bool]
    """Set if layer is not visible."""
    scrollRects: NotRequired[List[ScrollRect]]
    """Rectangles scrolling on main thread only."""
    stickyPositionConstraint: NotRequired[StickyPositionConstraint]
    """Sticky position constraint information"""
PaintProfile = List[float]
"""Array of timings, one per paint step."""