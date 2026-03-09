"""CDP DOMSnapshot Methods Types"""
from __future__ import annotations
from typing import TypedDict, NotRequired, Required, Literal, Any, Dict, Union, Optional, List, Set, Tuple

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from cdp.protocol.dom_snapshot.types import DocumentSnapshot



class captureSnapshotParameters(TypedDict, total=True):
    computedStyles: List[str]
    """Whitelist of computed styles to return."""
    includePaintOrder: NotRequired[bool]
    """Whether to include layout object paint orders into the snapshot."""
    includeDOMRects: NotRequired[bool]
    """Whether to include DOM rectangles (offsetRects, clientRects, scrollRects) into the snapshot"""
    includeBlendedBackgroundColors: NotRequired[bool]
    """Whether to include blended background colors in the snapshot (default: false). Blended background color is achieved by blending background colors of all elements that overlap with the current element."""
    includeTextColorOpacities: NotRequired[bool]
    """Whether to include text color opacity in the snapshot (default: false). An element might have the opacity property set that affects the text color of the element. The final text color opacity is computed based on the opacity of all overlapping elements."""


class captureSnapshotReturns(TypedDict):
    documents: List[DocumentSnapshot]
    """The nodes in the DOM tree. The DOMNode at index 0 corresponds to the root document."""
    strings: List[str]
    """Shared string table that all string properties refer to with indexes."""