"""CDP Accessibility Methods Types"""
from __future__ import annotations
from typing import TypedDict, NotRequired, Required, Literal, Any, Dict, Union, Optional, List, Set, Tuple

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from cdp.protocol.accessibility.types import AXNode
    from cdp.protocol.accessibility.types import AXNodeId
    from cdp.protocol.dom.types import BackendNodeId
    from cdp.protocol.dom.types import NodeId
    from cdp.protocol.page.types import FrameId
    from cdp.protocol.runtime.types import RemoteObjectId



class getPartialAXTreeParameters(TypedDict, total=False):
    nodeId: NotRequired[NodeId]
    """Identifier of the node to get the partial accessibility tree for."""
    backendNodeId: NotRequired[BackendNodeId]
    """Identifier of the backend node to get the partial accessibility tree for."""
    objectId: NotRequired[RemoteObjectId]
    """JavaScript object id of the node wrapper to get the partial accessibility tree for."""
    fetchRelatives: NotRequired[bool]
    """Whether to fetch this node's ancestors, siblings and children. Defaults to true."""
class getFullAXTreeParameters(TypedDict, total=False):
    depth: NotRequired[int]
    """The maximum depth at which descendants of the root node should be retrieved. If omitted, the full tree is returned."""
    frameId: NotRequired[FrameId]
    """The frame for whose document the AX tree should be retrieved. If omitted, the root frame is used."""
class getRootAXNodeParameters(TypedDict, total=False):
    frameId: NotRequired[FrameId]
    """The frame in whose document the node resides. If omitted, the root frame is used."""
class getAXNodeAndAncestorsParameters(TypedDict, total=False):
    nodeId: NotRequired[NodeId]
    """Identifier of the node to get."""
    backendNodeId: NotRequired[BackendNodeId]
    """Identifier of the backend node to get."""
    objectId: NotRequired[RemoteObjectId]
    """JavaScript object id of the node wrapper to get."""
class getChildAXNodesParameters(TypedDict, total=True):
    id: AXNodeId
    frameId: NotRequired[FrameId]
    """The frame in whose document the node resides. If omitted, the root frame is used."""
class queryAXTreeParameters(TypedDict, total=False):
    nodeId: NotRequired[NodeId]
    """Identifier of the node for the root to query."""
    backendNodeId: NotRequired[BackendNodeId]
    """Identifier of the backend node for the root to query."""
    objectId: NotRequired[RemoteObjectId]
    """JavaScript object id of the node wrapper for the root to query."""
    accessibleName: NotRequired[str]
    """Find nodes with this computed name."""
    role: NotRequired[str]
    """Find nodes with this computed role."""


class getPartialAXTreeReturns(TypedDict):
    nodes: List[AXNode]
    """The Accessibility.AXNode for this DOM node, if it exists, plus its ancestors, siblings and children, if requested."""
class getFullAXTreeReturns(TypedDict):
    nodes: List[AXNode]
class getRootAXNodeReturns(TypedDict):
    node: AXNode
class getAXNodeAndAncestorsReturns(TypedDict):
    nodes: List[AXNode]
class getChildAXNodesReturns(TypedDict):
    nodes: List[AXNode]
class queryAXTreeReturns(TypedDict):
    nodes: List[AXNode]
    """A list of Accessibility.AXNode matching the specified attributes, including nodes that are ignored for accessibility."""