"""CDP DOMDebugger Methods Types"""
from __future__ import annotations
from typing import TypedDict, NotRequired, Required, Literal, Any, Dict, Union, Optional, List, Set, Tuple

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from cdp.protocol.dom.types import NodeId
    from cdp.protocol.dom_debugger.types import CSPViolationType
    from cdp.protocol.dom_debugger.types import DOMBreakpointType
    from cdp.protocol.dom_debugger.types import EventListener
    from cdp.protocol.runtime.types import RemoteObjectId

class getEventListenersParameters(TypedDict, total=True):
    objectId: RemoteObjectId
    """Identifier of the object to return listeners for."""
    depth: NotRequired[int]
    """The maximum depth at which Node children should be retrieved, defaults to 1. Use -1 for the entire subtree or provide an integer larger than 0."""
    pierce: NotRequired[bool]
    """Whether or not iframes and shadow roots should be traversed when returning the subtree (default is false). Reports listeners for all contexts if pierce is enabled."""
class removeDOMBreakpointParameters(TypedDict, total=True):
    nodeId: NodeId
    """Identifier of the node to remove breakpoint from."""
    type: DOMBreakpointType
    """Type of the breakpoint to remove."""
class removeEventListenerBreakpointParameters(TypedDict, total=True):
    eventName: str
    """Event name."""
    targetName: NotRequired[str]
    """EventTarget interface name."""
class removeXHRBreakpointParameters(TypedDict, total=True):
    url: str
    """Resource URL substring."""
class setBreakOnCSPViolationParameters(TypedDict, total=True):
    violationTypes: List[CSPViolationType]
    """CSP Violations to stop upon."""
class setDOMBreakpointParameters(TypedDict, total=True):
    nodeId: NodeId
    """Identifier of the node to set breakpoint on."""
    type: DOMBreakpointType
    """Type of the operation to stop upon."""
class setEventListenerBreakpointParameters(TypedDict, total=True):
    eventName: str
    """DOM Event name to stop on (any DOM event will do)."""
    targetName: NotRequired[str]
    """EventTarget interface name to stop on. If equal to "*" or not provided, will stop on any EventTarget."""
class setXHRBreakpointParameters(TypedDict, total=True):
    url: str
    """Resource URL substring. All XHRs having this substring in the URL will get stopped upon."""
class getEventListenersReturns(TypedDict):
    listeners: List[EventListener]
    """Array of relevant listeners."""