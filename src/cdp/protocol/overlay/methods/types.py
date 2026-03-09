"""CDP Overlay Methods Types"""
from __future__ import annotations
from typing import TypedDict, NotRequired, Required, Literal, Any, Dict, Union, Optional, List, Set, Tuple

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from cdp.protocol.dom.types import BackendNodeId
    from cdp.protocol.dom.types import NodeId
    from cdp.protocol.dom.types import Quad
    from cdp.protocol.dom.types import RGBA
    from cdp.protocol.overlay.types import ColorFormat
    from cdp.protocol.overlay.types import ContainerQueryHighlightConfig
    from cdp.protocol.overlay.types import FlexNodeHighlightConfig
    from cdp.protocol.overlay.types import GridNodeHighlightConfig
    from cdp.protocol.overlay.types import HighlightConfig
    from cdp.protocol.overlay.types import HingeConfig
    from cdp.protocol.overlay.types import InspectMode
    from cdp.protocol.overlay.types import InspectedElementAnchorConfig
    from cdp.protocol.overlay.types import IsolatedElementHighlightConfig
    from cdp.protocol.overlay.types import ScrollSnapHighlightConfig
    from cdp.protocol.overlay.types import SourceOrderConfig
    from cdp.protocol.overlay.types import WindowControlsOverlayConfig
    from cdp.protocol.runtime.types import RemoteObjectId



class getHighlightObjectForTestParameters(TypedDict, total=True):
    nodeId: NodeId
    """Id of the node to get highlight object for."""
    includeDistance: NotRequired[bool]
    """Whether to include distance info."""
    includeStyle: NotRequired[bool]
    """Whether to include style info."""
    colorFormat: NotRequired[ColorFormat]
    """The color format to get config with (default: hex)."""
    showAccessibilityInfo: NotRequired[bool]
    """Whether to show accessibility info (default: true)."""
class getGridHighlightObjectsForTestParameters(TypedDict, total=True):
    nodeIds: List[NodeId]
    """Ids of the node to get highlight object for."""
class getSourceOrderHighlightObjectForTestParameters(TypedDict, total=True):
    nodeId: NodeId
    """Id of the node to highlight."""

class highlightNodeParameters(TypedDict, total=True):
    highlightConfig: HighlightConfig
    """A descriptor for the highlight appearance."""
    nodeId: NotRequired[NodeId]
    """Identifier of the node to highlight."""
    backendNodeId: NotRequired[BackendNodeId]
    """Identifier of the backend node to highlight."""
    objectId: NotRequired[RemoteObjectId]
    """JavaScript object id of the node to be highlighted."""
    selector: NotRequired[str]
    """Selectors to highlight relevant nodes."""
class highlightQuadParameters(TypedDict, total=True):
    quad: Quad
    """Quad to highlight"""
    color: NotRequired[RGBA]
    """The highlight fill color (default: transparent)."""
    outlineColor: NotRequired[RGBA]
    """The highlight outline color (default: transparent)."""
class highlightRectParameters(TypedDict, total=True):
    x: int
    """X coordinate"""
    y: int
    """Y coordinate"""
    width: int
    """Rectangle width"""
    height: int
    """Rectangle height"""
    color: NotRequired[RGBA]
    """The highlight fill color (default: transparent)."""
    outlineColor: NotRequired[RGBA]
    """The highlight outline color (default: transparent)."""
class highlightSourceOrderParameters(TypedDict, total=True):
    sourceOrderConfig: SourceOrderConfig
    """A descriptor for the appearance of the overlay drawing."""
    nodeId: NotRequired[NodeId]
    """Identifier of the node to highlight."""
    backendNodeId: NotRequired[BackendNodeId]
    """Identifier of the backend node to highlight."""
    objectId: NotRequired[RemoteObjectId]
    """JavaScript object id of the node to be highlighted."""
class setInspectModeParameters(TypedDict, total=True):
    mode: InspectMode
    """Set an inspection mode."""
    highlightConfig: NotRequired[HighlightConfig]
    """A descriptor for the highlight appearance of hovered-over nodes. May be omitted if enabled == false."""
class setShowAdHighlightsParameters(TypedDict, total=True):
    show: bool
    """True for showing ad highlights"""
class setPausedInDebuggerMessageParameters(TypedDict, total=False):
    message: NotRequired[str]
    """The message to display, also triggers resume and step over controls."""
class setShowDebugBordersParameters(TypedDict, total=True):
    show: bool
    """True for showing debug borders"""
class setShowFPSCounterParameters(TypedDict, total=True):
    show: bool
    """True for showing the FPS counter"""
class setShowGridOverlaysParameters(TypedDict, total=True):
    gridNodeHighlightConfigs: List[GridNodeHighlightConfig]
    """An array of node identifiers and descriptors for the highlight appearance."""
class setShowFlexOverlaysParameters(TypedDict, total=True):
    flexNodeHighlightConfigs: List[FlexNodeHighlightConfig]
    """An array of node identifiers and descriptors for the highlight appearance."""
class setShowScrollSnapOverlaysParameters(TypedDict, total=True):
    scrollSnapHighlightConfigs: List[ScrollSnapHighlightConfig]
    """An array of node identifiers and descriptors for the highlight appearance."""
class setShowContainerQueryOverlaysParameters(TypedDict, total=True):
    containerQueryHighlightConfigs: List[ContainerQueryHighlightConfig]
    """An array of node identifiers and descriptors for the highlight appearance."""
class setShowInspectedElementAnchorParameters(TypedDict, total=True):
    inspectedElementAnchorConfig: InspectedElementAnchorConfig
    """Node identifier for which to show an anchor for."""
class setShowPaintRectsParameters(TypedDict, total=True):
    result: bool
    """True for showing paint rectangles"""
class setShowLayoutShiftRegionsParameters(TypedDict, total=True):
    result: bool
    """True for showing layout shift regions"""
class setShowScrollBottleneckRectsParameters(TypedDict, total=True):
    show: bool
    """True for showing scroll bottleneck rects"""
class setShowViewportSizeOnResizeParameters(TypedDict, total=True):
    show: bool
    """Whether to paint size or not."""
class setShowHingeParameters(TypedDict, total=False):
    hingeConfig: NotRequired[HingeConfig]
    """hinge data, null means hideHinge"""
class setShowIsolatedElementsParameters(TypedDict, total=True):
    isolatedElementHighlightConfigs: List[IsolatedElementHighlightConfig]
    """An array of node identifiers and descriptors for the highlight appearance."""
class setShowWindowControlsOverlayParameters(TypedDict, total=False):
    windowControlsOverlayConfig: NotRequired[WindowControlsOverlayConfig]
    """Window Controls Overlay data, null means hide Window Controls Overlay"""


class getHighlightObjectForTestReturns(TypedDict):
    highlight: Dict[str, Any]
    """Highlight data for the node."""
class getGridHighlightObjectsForTestReturns(TypedDict):
    highlights: Dict[str, Any]
    """Grid Highlight data for the node ids provided."""
class getSourceOrderHighlightObjectForTestReturns(TypedDict):
    highlight: Dict[str, Any]
    """Source order highlight data for the node id provided."""