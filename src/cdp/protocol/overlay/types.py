"""CDP Overlay Types"""
from __future__ import annotations
from typing import TypedDict, NotRequired, Required, Literal, Any, Dict, Union, Optional, List, Set, Tuple

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from cdp.protocol.dom.types import BackendNodeId
    from cdp.protocol.dom.types import NodeId
    from cdp.protocol.dom.types import RGBA
    from cdp.protocol.dom.types import Rect

class SourceOrderConfig(TypedDict, total=True):
    """Configuration data for drawing the source order of an elements children."""
    parentOutlineColor: RGBA
    """the color to outline the given element in."""
    childOutlineColor: RGBA
    """the color to outline the child elements in."""
class GridHighlightConfig(TypedDict, total=False):
    """Configuration data for the highlighting of Grid elements."""
    showGridExtensionLines: NotRequired[bool]
    """Whether the extension lines from grid cells to the rulers should be shown (default: false)."""
    showPositiveLineNumbers: NotRequired[bool]
    """Show Positive line number labels (default: false)."""
    showNegativeLineNumbers: NotRequired[bool]
    """Show Negative line number labels (default: false)."""
    showAreaNames: NotRequired[bool]
    """Show area name labels (default: false)."""
    showLineNames: NotRequired[bool]
    """Show line name labels (default: false)."""
    showTrackSizes: NotRequired[bool]
    """Show track size labels (default: false)."""
    gridBorderColor: NotRequired[RGBA]
    """The grid container border highlight color (default: transparent)."""
    rowLineColor: NotRequired[RGBA]
    """The row line color (default: transparent)."""
    columnLineColor: NotRequired[RGBA]
    """The column line color (default: transparent)."""
    gridBorderDash: NotRequired[bool]
    """Whether the grid border is dashed (default: false)."""
    rowLineDash: NotRequired[bool]
    """Whether row lines are dashed (default: false)."""
    columnLineDash: NotRequired[bool]
    """Whether column lines are dashed (default: false)."""
    rowGapColor: NotRequired[RGBA]
    """The row gap highlight fill color (default: transparent)."""
    rowHatchColor: NotRequired[RGBA]
    """The row gap hatching fill color (default: transparent)."""
    columnGapColor: NotRequired[RGBA]
    """The column gap highlight fill color (default: transparent)."""
    columnHatchColor: NotRequired[RGBA]
    """The column gap hatching fill color (default: transparent)."""
    areaBorderColor: NotRequired[RGBA]
    """The named grid areas border color (Default: transparent)."""
    gridBackgroundColor: NotRequired[RGBA]
    """The grid container background color (Default: transparent)."""
class FlexContainerHighlightConfig(TypedDict, total=False):
    """Configuration data for the highlighting of Flex container elements."""
    containerBorder: NotRequired[LineStyle]
    """The style of the container border"""
    lineSeparator: NotRequired[LineStyle]
    """The style of the separator between lines"""
    itemSeparator: NotRequired[LineStyle]
    """The style of the separator between items"""
    mainDistributedSpace: NotRequired[BoxStyle]
    """Style of content-distribution space on the main axis (justify-content)."""
    crossDistributedSpace: NotRequired[BoxStyle]
    """Style of content-distribution space on the cross axis (align-content)."""
    rowGapSpace: NotRequired[BoxStyle]
    """Style of empty space caused by row gaps (gap/row-gap)."""
    columnGapSpace: NotRequired[BoxStyle]
    """Style of empty space caused by columns gaps (gap/column-gap)."""
    crossAlignment: NotRequired[LineStyle]
    """Style of the self-alignment line (align-items)."""
class FlexItemHighlightConfig(TypedDict, total=False):
    """Configuration data for the highlighting of Flex item elements."""
    baseSizeBox: NotRequired[BoxStyle]
    """Style of the box representing the item's base size"""
    baseSizeBorder: NotRequired[LineStyle]
    """Style of the border around the box representing the item's base size"""
    flexibilityArrow: NotRequired[LineStyle]
    """Style of the arrow representing if the item grew or shrank"""
class LineStyle(TypedDict, total=False):
    """Style information for drawing a line."""
    color: NotRequired[RGBA]
    """The color of the line (default: transparent)"""
    pattern: NotRequired[Literal["dashed", "dotted"]]
    """The line pattern (default: solid)"""
class BoxStyle(TypedDict, total=False):
    """Style information for drawing a box."""
    fillColor: NotRequired[RGBA]
    """The background color for the box (default: transparent)"""
    hatchColor: NotRequired[RGBA]
    """The hatching color for the box (default: transparent)"""
ContrastAlgorithm = Literal['aa','aaa','apca']
class HighlightConfig(TypedDict, total=False):
    """Configuration data for the highlighting of page elements."""
    showInfo: NotRequired[bool]
    """Whether the node info tooltip should be shown (default: false)."""
    showStyles: NotRequired[bool]
    """Whether the node styles in the tooltip (default: false)."""
    showRulers: NotRequired[bool]
    """Whether the rulers should be shown (default: false)."""
    showAccessibilityInfo: NotRequired[bool]
    """Whether the a11y info should be shown (default: true)."""
    showExtensionLines: NotRequired[bool]
    """Whether the extension lines from node to the rulers should be shown (default: false)."""
    contentColor: NotRequired[RGBA]
    """The content box highlight fill color (default: transparent)."""
    paddingColor: NotRequired[RGBA]
    """The padding highlight fill color (default: transparent)."""
    borderColor: NotRequired[RGBA]
    """The border highlight fill color (default: transparent)."""
    marginColor: NotRequired[RGBA]
    """The margin highlight fill color (default: transparent)."""
    eventTargetColor: NotRequired[RGBA]
    """The event target element highlight fill color (default: transparent)."""
    shapeColor: NotRequired[RGBA]
    """The shape outside fill color (default: transparent)."""
    shapeMarginColor: NotRequired[RGBA]
    """The shape margin fill color (default: transparent)."""
    cssGridColor: NotRequired[RGBA]
    """The grid layout color (default: transparent)."""
    colorFormat: NotRequired[ColorFormat]
    """The color format used to format color styles (default: hex)."""
    gridHighlightConfig: NotRequired[GridHighlightConfig]
    """The grid layout highlight configuration (default: all transparent)."""
    flexContainerHighlightConfig: NotRequired[FlexContainerHighlightConfig]
    """The flex container highlight configuration (default: all transparent)."""
    flexItemHighlightConfig: NotRequired[FlexItemHighlightConfig]
    """The flex item highlight configuration (default: all transparent)."""
    contrastAlgorithm: NotRequired[ContrastAlgorithm]
    """The contrast algorithm to use for the contrast ratio (default: aa)."""
    containerQueryContainerHighlightConfig: NotRequired[ContainerQueryContainerHighlightConfig]
    """The container query container highlight configuration (default: all transparent)."""
ColorFormat = Literal['rgb','hsl','hwb','hex']
class GridNodeHighlightConfig(TypedDict, total=True):
    """Configurations for Persistent Grid Highlight"""
    gridHighlightConfig: GridHighlightConfig
    """A descriptor for the highlight appearance."""
    nodeId: NodeId
    """Identifier of the node to highlight."""
class FlexNodeHighlightConfig(TypedDict, total=True):
    flexContainerHighlightConfig: FlexContainerHighlightConfig
    """A descriptor for the highlight appearance of flex containers."""
    nodeId: NodeId
    """Identifier of the node to highlight."""
class ScrollSnapContainerHighlightConfig(TypedDict, total=False):
    snapportBorder: NotRequired[LineStyle]
    """The style of the snapport border (default: transparent)"""
    snapAreaBorder: NotRequired[LineStyle]
    """The style of the snap area border (default: transparent)"""
    scrollMarginColor: NotRequired[RGBA]
    """The margin highlight fill color (default: transparent)."""
    scrollPaddingColor: NotRequired[RGBA]
    """The padding highlight fill color (default: transparent)."""
class ScrollSnapHighlightConfig(TypedDict, total=True):
    scrollSnapContainerHighlightConfig: ScrollSnapContainerHighlightConfig
    """A descriptor for the highlight appearance of scroll snap containers."""
    nodeId: NodeId
    """Identifier of the node to highlight."""
class HingeConfig(TypedDict, total=True):
    """Configuration for dual screen hinge"""
    rect: Rect
    """A rectangle represent hinge"""
    contentColor: NotRequired[RGBA]
    """The content box highlight fill color (default: a dark color)."""
    outlineColor: NotRequired[RGBA]
    """The content box highlight outline color (default: transparent)."""
class WindowControlsOverlayConfig(TypedDict, total=True):
    """Configuration for Window Controls Overlay"""
    showCSS: bool
    """Whether the title bar CSS should be shown when emulating the Window Controls Overlay."""
    selectedPlatform: str
    """Selected platforms to show the overlay."""
    themeColor: str
    """The theme color defined in app manifest."""
class ContainerQueryHighlightConfig(TypedDict, total=True):
    containerQueryContainerHighlightConfig: ContainerQueryContainerHighlightConfig
    """A descriptor for the highlight appearance of container query containers."""
    nodeId: NodeId
    """Identifier of the container node to highlight."""
class ContainerQueryContainerHighlightConfig(TypedDict, total=False):
    containerBorder: NotRequired[LineStyle]
    """The style of the container border."""
    descendantBorder: NotRequired[LineStyle]
    """The style of the descendants' borders."""
class IsolatedElementHighlightConfig(TypedDict, total=True):
    isolationModeHighlightConfig: IsolationModeHighlightConfig
    """A descriptor for the highlight appearance of an element in isolation mode."""
    nodeId: NodeId
    """Identifier of the isolated element to highlight."""
class IsolationModeHighlightConfig(TypedDict, total=False):
    resizerColor: NotRequired[RGBA]
    """The fill color of the resizers (default: transparent)."""
    resizerHandleColor: NotRequired[RGBA]
    """The fill color for resizer handles (default: transparent)."""
    maskColor: NotRequired[RGBA]
    """The fill color for the mask covering non-isolated elements (default: transparent)."""
InspectMode = Literal['searchForNode','searchForUAShadowDOM','captureAreaScreenshot','none']
class InspectedElementAnchorConfig(TypedDict, total=False):
    nodeId: NotRequired[NodeId]
    """Identifier of the node to highlight."""
    backendNodeId: NotRequired[BackendNodeId]
    """Identifier of the backend node to highlight."""