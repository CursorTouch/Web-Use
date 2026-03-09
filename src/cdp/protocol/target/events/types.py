"""CDP Target Events"""
from __future__ import annotations
from typing import TypedDict, NotRequired, Required, Literal, Any, Dict, Union, Optional, List, Set, Tuple

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from cdp.protocol.target.types import SessionID
    from cdp.protocol.target.types import TargetID
    from cdp.protocol.target.types import TargetInfo

class attachedToTargetEvent(TypedDict, total=True):
    sessionId: SessionID
    """Identifier assigned to the session used to send/receive messages."""
    targetInfo: TargetInfo
    waitingForDebugger: bool
class detachedFromTargetEvent(TypedDict, total=True):
    sessionId: SessionID
    """Detached session identifier."""
    targetId: NotRequired[TargetID]
    """Deprecated."""
class receivedMessageFromTargetEvent(TypedDict, total=True):
    sessionId: SessionID
    """Identifier of a session which sends a message."""
    message: str
    targetId: NotRequired[TargetID]
    """Deprecated."""
class targetCreatedEvent(TypedDict, total=True):
    targetInfo: TargetInfo
class targetDestroyedEvent(TypedDict, total=True):
    targetId: TargetID
class targetCrashedEvent(TypedDict, total=True):
    targetId: TargetID
    status: str
    """Termination status type."""
    errorCode: int
    """Termination error code."""
class targetInfoChangedEvent(TypedDict, total=True):
    targetInfo: TargetInfo