"""CDP DOM Methods Types"""
from __future__ import annotations
from typing import TypedDict, NotRequired, Required, Literal, Any, Dict, Union, Optional, List, Set, Tuple

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from cdp.protocol.dom.types import BackendNodeId
    from cdp.protocol.dom.types import BoxModel
    from cdp.protocol.dom.types import CSSComputedStyleProperty
    from cdp.protocol.dom.types import DetachedElementInfo
    from cdp.protocol.dom.types import LogicalAxes
    from cdp.protocol.dom.types import Node
    from cdp.protocol.dom.types import NodeId
    from cdp.protocol.dom.types import PhysicalAxes
    from cdp.protocol.dom.types import Quad
    from cdp.protocol.dom.types import Rect
    from cdp.protocol.page.types import FrameId
    from cdp.protocol.runtime.types import ExecutionContextId
    from cdp.protocol.runtime.types import RemoteObject
    from cdp.protocol.runtime.types import RemoteObjectId
    from cdp.protocol.runtime.types import StackTrace

class collectClassNamesFromSubtreeParameters(TypedDict, total=True):
    nodeId: NodeId
    """Id of the node to collect class names."""
class copyToParameters(TypedDict, total=True):
    nodeId: NodeId
    """Id of the node to copy."""
    targetNodeId: NodeId
    """Id of the element to drop the copy into."""
    insertBeforeNodeId: NotRequired[NodeId]
    """Drop the copy before this node (if absent, the copy becomes the last child of targetNodeId)."""
class describeNodeParameters(TypedDict, total=False):
    nodeId: NotRequired[NodeId]
    """Identifier of the node."""
    backendNodeId: NotRequired[BackendNodeId]
    """Identifier of the backend node."""
    objectId: NotRequired[RemoteObjectId]
    """JavaScript object id of the node wrapper."""
    depth: NotRequired[int]
    """The maximum depth at which children should be retrieved, defaults to 1. Use -1 for the entire subtree or provide an integer larger than 0."""
    pierce: NotRequired[bool]
    """Whether or not iframes and shadow roots should be traversed when returning the subtree (default is false)."""
class scrollIntoViewIfNeededParameters(TypedDict, total=False):
    nodeId: NotRequired[NodeId]
    """Identifier of the node."""
    backendNodeId: NotRequired[BackendNodeId]
    """Identifier of the backend node."""
    objectId: NotRequired[RemoteObjectId]
    """JavaScript object id of the node wrapper."""
    rect: NotRequired[Rect]
    """The rect to be scrolled into view, relative to the node's border box, in CSS pixels. When omitted, center of the node will be used, similar to Element.scrollIntoView."""

class discardSearchResultsParameters(TypedDict, total=True):
    searchId: str
    """Unique search session identifier."""
class enableParameters(TypedDict, total=False):
    includeWhitespace: NotRequired[Literal["none", "all"]]
    """Whether to include whitespaces in the children array of returned Nodes."""
class focusParameters(TypedDict, total=False):
    nodeId: NotRequired[NodeId]
    """Identifier of the node."""
    backendNodeId: NotRequired[BackendNodeId]
    """Identifier of the backend node."""
    objectId: NotRequired[RemoteObjectId]
    """JavaScript object id of the node wrapper."""
class getAttributesParameters(TypedDict, total=True):
    nodeId: NodeId
    """Id of the node to retrieve attributes for."""
class getBoxModelParameters(TypedDict, total=False):
    nodeId: NotRequired[NodeId]
    """Identifier of the node."""
    backendNodeId: NotRequired[BackendNodeId]
    """Identifier of the backend node."""
    objectId: NotRequired[RemoteObjectId]
    """JavaScript object id of the node wrapper."""
class getContentQuadsParameters(TypedDict, total=False):
    nodeId: NotRequired[NodeId]
    """Identifier of the node."""
    backendNodeId: NotRequired[BackendNodeId]
    """Identifier of the backend node."""
    objectId: NotRequired[RemoteObjectId]
    """JavaScript object id of the node wrapper."""
class getDocumentParameters(TypedDict, total=False):
    depth: NotRequired[int]
    """The maximum depth at which children should be retrieved, defaults to 1. Use -1 for the entire subtree or provide an integer larger than 0."""
    pierce: NotRequired[bool]
    """Whether or not iframes and shadow roots should be traversed when returning the subtree (default is false)."""
class getNodesForSubtreeByStyleParameters(TypedDict, total=True):
    nodeId: NodeId
    """Node ID pointing to the root of a subtree."""
    computedStyles: List[CSSComputedStyleProperty]
    """The style to filter nodes by (includes nodes if any of properties matches)."""
    pierce: NotRequired[bool]
    """Whether or not iframes and shadow roots in the same target should be traversed when returning the results (default is false)."""
class getNodeForLocationParameters(TypedDict, total=True):
    x: int
    """X coordinate."""
    y: int
    """Y coordinate."""
    includeUserAgentShadowDOM: NotRequired[bool]
    """False to skip to the nearest non-UA shadow root ancestor (default: false)."""
    ignorePointerEventsNone: NotRequired[bool]
    """Whether to ignore pointer-events: none on elements and hit test them."""
class getOuterHTMLParameters(TypedDict, total=False):
    nodeId: NotRequired[NodeId]
    """Identifier of the node."""
    backendNodeId: NotRequired[BackendNodeId]
    """Identifier of the backend node."""
    objectId: NotRequired[RemoteObjectId]
    """JavaScript object id of the node wrapper."""
    includeShadowDOM: NotRequired[bool]
    """Include all shadow roots. Equals to false if not specified."""
class getRelayoutBoundaryParameters(TypedDict, total=True):
    nodeId: NodeId
    """Id of the node."""
class getSearchResultsParameters(TypedDict, total=True):
    searchId: str
    """Unique search session identifier."""
    fromIndex: int
    """Start index of the search result to be returned."""
    toIndex: int
    """End index of the search result to be returned."""




class moveToParameters(TypedDict, total=True):
    nodeId: NodeId
    """Id of the node to move."""
    targetNodeId: NodeId
    """Id of the element to drop the moved node into."""
    insertBeforeNodeId: NotRequired[NodeId]
    """Drop node before this one (if absent, the moved node becomes the last child of targetNodeId)."""
class performSearchParameters(TypedDict, total=True):
    query: str
    """Plain text or query selector or XPath search query."""
    includeUserAgentShadowDOM: NotRequired[bool]
    """True to search in user agent shadow DOM."""
class pushNodeByPathToFrontendParameters(TypedDict, total=True):
    path: str
    """Path to node in the proprietary format."""
class pushNodesByBackendIdsToFrontendParameters(TypedDict, total=True):
    backendNodeIds: List[BackendNodeId]
    """The array of backend node ids."""
class querySelectorParameters(TypedDict, total=True):
    nodeId: NodeId
    """Id of the node to query upon."""
    selector: str
    """Selector string."""
class querySelectorAllParameters(TypedDict, total=True):
    nodeId: NodeId
    """Id of the node to query upon."""
    selector: str
    """Selector string."""

class getElementByRelationParameters(TypedDict, total=True):
    nodeId: NodeId
    """Id of the node from which to query the relation."""
    relation: Literal["PopoverTarget", "InterestTarget", "CommandFor"]
    """Type of relation to get."""

class removeAttributeParameters(TypedDict, total=True):
    nodeId: NodeId
    """Id of the element to remove attribute from."""
    name: str
    """Name of the attribute to remove."""
class removeNodeParameters(TypedDict, total=True):
    nodeId: NodeId
    """Id of the node to remove."""
class requestChildNodesParameters(TypedDict, total=True):
    nodeId: NodeId
    """Id of the node to get children for."""
    depth: NotRequired[int]
    """The maximum depth at which children should be retrieved, defaults to 1. Use -1 for the entire subtree or provide an integer larger than 0."""
    pierce: NotRequired[bool]
    """Whether or not iframes and shadow roots should be traversed when returning the sub-tree (default is false)."""
class requestNodeParameters(TypedDict, total=True):
    objectId: RemoteObjectId
    """JavaScript object id to convert into node."""
class resolveNodeParameters(TypedDict, total=False):
    nodeId: NotRequired[NodeId]
    """Id of the node to resolve."""
    backendNodeId: NotRequired[BackendNodeId]
    """Backend identifier of the node to resolve."""
    objectGroup: NotRequired[str]
    """Symbolic group name that can be used to release multiple objects."""
    executionContextId: NotRequired[ExecutionContextId]
    """Execution context in which to resolve the node."""
class setAttributeValueParameters(TypedDict, total=True):
    nodeId: NodeId
    """Id of the element to set attribute for."""
    name: str
    """Attribute name."""
    value: str
    """Attribute value."""
class setAttributesAsTextParameters(TypedDict, total=True):
    nodeId: NodeId
    """Id of the element to set attributes for."""
    text: str
    """Text with a number of attributes. Will parse this text using HTML parser."""
    name: NotRequired[str]
    """Attribute name to replace with new attributes derived from text in case text parsed successfully."""
class setFileInputFilesParameters(TypedDict, total=True):
    files: List[str]
    """Array of file paths to set."""
    nodeId: NotRequired[NodeId]
    """Identifier of the node."""
    backendNodeId: NotRequired[BackendNodeId]
    """Identifier of the backend node."""
    objectId: NotRequired[RemoteObjectId]
    """JavaScript object id of the node wrapper."""
class setNodeStackTracesEnabledParameters(TypedDict, total=True):
    enable: bool
    """Enable or disable."""
class getNodeStackTracesParameters(TypedDict, total=True):
    nodeId: NodeId
    """Id of the node to get stack traces for."""
class getFileInfoParameters(TypedDict, total=True):
    objectId: RemoteObjectId
    """JavaScript object id of the node wrapper."""

class setInspectedNodeParameters(TypedDict, total=True):
    nodeId: NodeId
    """DOM node id to be accessible by means of $x command line API."""
class setNodeNameParameters(TypedDict, total=True):
    nodeId: NodeId
    """Id of the node to set name for."""
    name: str
    """New node's name."""
class setNodeValueParameters(TypedDict, total=True):
    nodeId: NodeId
    """Id of the node to set value for."""
    value: str
    """New node's value."""
class setOuterHTMLParameters(TypedDict, total=True):
    nodeId: NodeId
    """Id of the node to set markup for."""
    outerHTML: str
    """Outer HTML markup to set."""

class getFrameOwnerParameters(TypedDict, total=True):
    frameId: FrameId
class getContainerForNodeParameters(TypedDict, total=True):
    nodeId: NodeId
    containerName: NotRequired[str]
    physicalAxes: NotRequired[PhysicalAxes]
    logicalAxes: NotRequired[LogicalAxes]
    queriesScrollState: NotRequired[bool]
    queriesAnchored: NotRequired[bool]
class getQueryingDescendantsForContainerParameters(TypedDict, total=True):
    nodeId: NodeId
    """Id of the container node to find querying descendants from."""
class getAnchorElementParameters(TypedDict, total=True):
    nodeId: NodeId
    """Id of the positioned element from which to find the anchor."""
    anchorSpecifier: NotRequired[str]
    """An optional anchor specifier, as defined in https://www.w3.org/TR/css-anchor-position-1/#anchor-specifier. If not provided, it will return the implicit anchor element for the given positioned element."""
class forceShowPopoverParameters(TypedDict, total=True):
    nodeId: NodeId
    """Id of the popover HTMLElement"""
    enable: bool
    """If true, opens the popover and keeps it open. If false, closes the popover if it was previously force-opened."""
class collectClassNamesFromSubtreeReturns(TypedDict):
    classNames: List[str]
    """Class name list."""
class copyToReturns(TypedDict):
    nodeId: NodeId
    """Id of the node clone."""
class describeNodeReturns(TypedDict):
    node: Node
    """Node description."""





class getAttributesReturns(TypedDict):
    attributes: List[str]
    """An interleaved array of node attribute names and values."""
class getBoxModelReturns(TypedDict):
    model: BoxModel
    """Box model for the node."""
class getContentQuadsReturns(TypedDict):
    quads: List[Quad]
    """Quads that describe node layout relative to viewport."""
class getDocumentReturns(TypedDict):
    root: Node
    """Resulting node."""
class getNodesForSubtreeByStyleReturns(TypedDict):
    nodeIds: List[NodeId]
    """Resulting nodes."""
class getNodeForLocationReturns(TypedDict):
    backendNodeId: BackendNodeId
    """Resulting node."""
    frameId: FrameId
    """Frame this node belongs to."""
    nodeId: NodeId
    """Id of the node at given coordinates, only when enabled and requested document."""
class getOuterHTMLReturns(TypedDict):
    outerHTML: str
    """Outer HTML markup."""
class getRelayoutBoundaryReturns(TypedDict):
    nodeId: NodeId
    """Relayout boundary node id for the given node."""
class getSearchResultsReturns(TypedDict):
    nodeIds: List[NodeId]
    """Ids of the search result nodes."""




class moveToReturns(TypedDict):
    nodeId: NodeId
    """New id of the moved node."""
class performSearchReturns(TypedDict):
    searchId: str
    """Unique search session identifier."""
    resultCount: int
    """Number of search results."""
class pushNodeByPathToFrontendReturns(TypedDict):
    nodeId: NodeId
    """Id of the node for given path."""
class pushNodesByBackendIdsToFrontendReturns(TypedDict):
    nodeIds: List[NodeId]
    """The array of ids of pushed nodes that correspond to the backend ids specified in backendNodeIds."""
class querySelectorReturns(TypedDict):
    nodeId: NodeId
    """Query selector result."""
class querySelectorAllReturns(TypedDict):
    nodeIds: List[NodeId]
    """Query selector result."""
class getTopLayerElementsReturns(TypedDict):
    nodeIds: List[NodeId]
    """NodeIds of top layer elements"""
class getElementByRelationReturns(TypedDict):
    nodeId: NodeId
    """NodeId of the element matching the queried relation."""




class requestNodeReturns(TypedDict):
    nodeId: NodeId
    """Node id for given object."""
class resolveNodeReturns(TypedDict):
    object: RemoteObject
    """JavaScript object wrapper for given node."""




class getNodeStackTracesReturns(TypedDict):
    creation: StackTrace
    """Creation stack trace, if available."""
class getFileInfoReturns(TypedDict):
    path: str
class getDetachedDomNodesReturns(TypedDict):
    detachedNodes: List[DetachedElementInfo]
    """The list of detached nodes"""

class setNodeNameReturns(TypedDict):
    nodeId: NodeId
    """New node's id."""



class getFrameOwnerReturns(TypedDict):
    backendNodeId: BackendNodeId
    """Resulting node."""
    nodeId: NodeId
    """Id of the node at given coordinates, only when enabled and requested document."""
class getContainerForNodeReturns(TypedDict):
    nodeId: NodeId
    """The container node for the given node, or null if not found."""
class getQueryingDescendantsForContainerReturns(TypedDict):
    nodeIds: List[NodeId]
    """Descendant nodes with container queries against the given container."""
class getAnchorElementReturns(TypedDict):
    nodeId: NodeId
    """The anchor element of the given anchor query."""
class forceShowPopoverReturns(TypedDict):
    nodeIds: List[NodeId]
    """List of popovers that were closed in order to respect popover stacking order."""