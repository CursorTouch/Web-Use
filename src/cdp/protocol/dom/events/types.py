"""CDP DOM Events"""
from __future__ import annotations
from typing import TypedDict, NotRequired, Required, Literal, Any, Dict, Union, Optional, List, Set, Tuple

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from cdp.protocol.dom.types import BackendNode
    from cdp.protocol.dom.types import Node
    from cdp.protocol.dom.types import NodeId
    from cdp.protocol.dom.types import StyleSheetId

class attributeModifiedEvent(TypedDict, total=True):
    nodeId: NodeId
    """Id of the node that has changed."""
    name: str
    """Attribute name."""
    value: str
    """Attribute value."""
class adoptedStyleSheetsModifiedEvent(TypedDict, total=True):
    nodeId: NodeId
    """Id of the node that has changed."""
    adoptedStyleSheets: List[StyleSheetId]
    """New adoptedStyleSheets array."""
class attributeRemovedEvent(TypedDict, total=True):
    nodeId: NodeId
    """Id of the node that has changed."""
    name: str
    """A ttribute name."""
class characterDataModifiedEvent(TypedDict, total=True):
    nodeId: NodeId
    """Id of the node that has changed."""
    characterData: str
    """New text value."""
class childNodeCountUpdatedEvent(TypedDict, total=True):
    nodeId: NodeId
    """Id of the node that has changed."""
    childNodeCount: int
    """New node count."""
class childNodeInsertedEvent(TypedDict, total=True):
    parentNodeId: NodeId
    """Id of the node that has changed."""
    previousNodeId: NodeId
    """Id of the previous sibling."""
    node: Node
    """Inserted node data."""
class childNodeRemovedEvent(TypedDict, total=True):
    parentNodeId: NodeId
    """Parent id."""
    nodeId: NodeId
    """Id of the node that has been removed."""
class distributedNodesUpdatedEvent(TypedDict, total=True):
    insertionPointId: NodeId
    """Insertion point where distributed nodes were updated."""
    distributedNodes: List[BackendNode]
    """Distributed nodes for given insertion point."""
class documentUpdatedEvent(TypedDict, total=True):
    pass
class inlineStyleInvalidatedEvent(TypedDict, total=True):
    nodeIds: List[NodeId]
    """Ids of the nodes for which the inline styles have been invalidated."""
class pseudoElementAddedEvent(TypedDict, total=True):
    parentId: NodeId
    """Pseudo element's parent element id."""
    pseudoElement: Node
    """The added pseudo element."""
class topLayerElementsUpdatedEvent(TypedDict, total=True):
    pass
class scrollableFlagUpdatedEvent(TypedDict, total=True):
    nodeId: NodeId
    """The id of the node."""
    isScrollable: bool
    """If the node is scrollable."""
class adRelatedStateUpdatedEvent(TypedDict, total=True):
    nodeId: NodeId
    """The id of the node."""
    isAdRelated: bool
    """If the node is ad related."""
class affectedByStartingStylesFlagUpdatedEvent(TypedDict, total=True):
    nodeId: NodeId
    """The id of the node."""
    affectedByStartingStyles: bool
    """If the node has starting styles."""
class pseudoElementRemovedEvent(TypedDict, total=True):
    parentId: NodeId
    """Pseudo element's parent element id."""
    pseudoElementId: NodeId
    """The removed pseudo element id."""
class setChildNodesEvent(TypedDict, total=True):
    parentId: NodeId
    """Parent node id to populate with children."""
    nodes: List[Node]
    """Child nodes array."""
class shadowRootPoppedEvent(TypedDict, total=True):
    hostId: NodeId
    """Host element id."""
    rootId: NodeId
    """Shadow root id."""
class shadowRootPushedEvent(TypedDict, total=True):
    hostId: NodeId
    """Host element id."""
    root: Node
    """Shadow root."""