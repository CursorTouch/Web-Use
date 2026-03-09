"""CDP Overlay Events"""
from __future__ import annotations
from typing import TypedDict, NotRequired, Required, Literal, Any, Dict, Union, Optional, List, Set, Tuple

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from cdp.protocol.dom.types import BackendNodeId
    from cdp.protocol.dom.types import NodeId
    from cdp.protocol.page.types import Viewport

class inspectNodeRequestedEvent(TypedDict, total=True):
    backendNodeId: BackendNodeId
    """Id of the node to inspect."""
class nodeHighlightRequestedEvent(TypedDict, total=True):
    nodeId: NodeId
class screenshotRequestedEvent(TypedDict, total=True):
    viewport: Viewport
    """Viewport to capture, in device independent pixels (dip)."""
class inspectPanelShowRequestedEvent(TypedDict, total=True):
    backendNodeId: BackendNodeId
    """Id of the node to show in the panel."""
class inspectedElementWindowRestoredEvent(TypedDict, total=True):
    backendNodeId: BackendNodeId
    """Id of the node to restore the floating window for."""
class inspectModeCanceledEvent(TypedDict, total=True):
    pass