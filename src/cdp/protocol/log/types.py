"""CDP Log Types"""
from __future__ import annotations
from typing import TypedDict, NotRequired, Required, Literal, Any, Dict, Union, Optional, List, Set, Tuple

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from cdp.protocol.network.types import RequestId
    from cdp.protocol.runtime.types import RemoteObject
    from cdp.protocol.runtime.types import StackTrace
    from cdp.protocol.runtime.types import Timestamp

class LogEntry(TypedDict, total=True):
    """Log entry."""
    source: Literal["xml", "javascript", "network", "storage", "appcache", "rendering", "security", "deprecation", "worker", "violation", "intervention", "recommendation", "other"]
    """Log entry source."""
    level: Literal["verbose", "info", "warning", "error"]
    """Log entry severity."""
    text: str
    """Logged text."""
    timestamp: Timestamp
    """Timestamp when this entry was added."""
    category: NotRequired[Literal["cors"]]
    url: NotRequired[str]
    """URL of the resource if known."""
    lineNumber: NotRequired[int]
    """Line number in the resource."""
    stackTrace: NotRequired[StackTrace]
    """JavaScript stack trace."""
    networkRequestId: NotRequired[RequestId]
    """Identifier of the network request associated with this entry."""
    workerId: NotRequired[str]
    """Identifier of the worker associated with this entry."""
    args: NotRequired[List[RemoteObject]]
    """Call arguments."""
class ViolationSetting(TypedDict, total=True):
    """Violation configuration setting."""
    name: Literal["longTask", "longLayout", "blockedEvent", "blockedParser", "discouragedAPIUse", "handler", "recurringHandler"]
    """Violation type."""
    threshold: float
    """Time threshold to trigger upon."""