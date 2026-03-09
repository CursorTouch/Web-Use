"""CDP Runtime Events"""
from __future__ import annotations
from typing import TypedDict, NotRequired, Required, Literal, Any, Dict, Union, Optional, List, Set, Tuple

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from cdp.protocol.runtime.types import ExceptionDetails
    from cdp.protocol.runtime.types import ExecutionContextDescription
    from cdp.protocol.runtime.types import ExecutionContextId
    from cdp.protocol.runtime.types import RemoteObject
    from cdp.protocol.runtime.types import StackTrace
    from cdp.protocol.runtime.types import Timestamp

class bindingCalledEvent(TypedDict, total=True):
    name: str
    payload: str
    executionContextId: ExecutionContextId
    """Identifier of the context where the call was made."""
class consoleAPICalledEvent(TypedDict, total=True):
    type: Literal["log", "debug", "info", "error", "warning", "dir", "dirxml", "table", "trace", "clear", "startGroup", "startGroupCollapsed", "endGroup", "assert", "profile", "profileEnd", "count", "timeEnd"]
    """Type of the call."""
    args: List[RemoteObject]
    """Call arguments."""
    executionContextId: ExecutionContextId
    """Identifier of the context where the call was made."""
    timestamp: Timestamp
    """Call timestamp."""
    stackTrace: NotRequired[StackTrace]
    """Stack trace captured when the call was made. The async stack chain is automatically reported for the following call types: assert, error, trace, warning. For other types the async call chain can be retrieved using Debugger.getStackTrace and stackTrace.parentId field."""
    context: NotRequired[str]
    """Console context descriptor for calls on non-default console context (not console.*): 'anonymous#unique-logger-id' for call on unnamed context, 'name#unique-logger-id' for call on named context."""
class exceptionRevokedEvent(TypedDict, total=True):
    reason: str
    """Reason describing why exception was revoked."""
    exceptionId: int
    """The id of revoked exception, as reported in exceptionThrown."""
class exceptionThrownEvent(TypedDict, total=True):
    timestamp: Timestamp
    """Timestamp of the exception."""
    exceptionDetails: ExceptionDetails
class executionContextCreatedEvent(TypedDict, total=True):
    context: ExecutionContextDescription
    """A newly created execution context."""
class executionContextDestroyedEvent(TypedDict, total=True):
    executionContextId: ExecutionContextId
    """Id of the destroyed context"""
    executionContextUniqueId: str
    """Unique Id of the destroyed context"""
class executionContextsClearedEvent(TypedDict, total=True):
    pass
class inspectRequestedEvent(TypedDict, total=True):
    object: RemoteObject
    hints: Dict[str, Any]
    executionContextId: NotRequired[ExecutionContextId]
    """Identifier of the context where the call was made."""