"""CDP DOMDebugger Types"""
from __future__ import annotations
from typing import TypedDict, NotRequired, Required, Literal, Any, Dict, Union, Optional, List, Set, Tuple

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from cdp.protocol.dom.types import BackendNodeId
    from cdp.protocol.runtime.types import RemoteObject
    from cdp.protocol.runtime.types import ScriptId

DOMBreakpointType = Literal['subtree-modified','attribute-modified','node-removed']
"""DOM breakpoint type."""
CSPViolationType = Literal['trustedtype-sink-violation','trustedtype-policy-violation']
"""CSP Violation type."""
class EventListener(TypedDict, total=True):
    """Object event listener."""
    type: str
    """EventListener's type."""
    useCapture: bool
    """EventListener's useCapture."""
    passive: bool
    """EventListener's passive flag."""
    once: bool
    """EventListener's once flag."""
    scriptId: ScriptId
    """Script id of the handler code."""
    lineNumber: int
    """Line number in the script (0-based)."""
    columnNumber: int
    """Column number in the script (0-based)."""
    handler: NotRequired[RemoteObject]
    """Event handler function value."""
    originalHandler: NotRequired[RemoteObject]
    """Event original handler function value."""
    backendNodeId: NotRequired[BackendNodeId]
    """Node the listener is added to (if any)."""