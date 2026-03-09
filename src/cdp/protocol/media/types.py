"""CDP Media Types"""
from __future__ import annotations
from typing import TypedDict, NotRequired, Required, Literal, Any, Dict, Union, Optional, List, Set, Tuple

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from cdp.protocol.dom.types import BackendNodeId

PlayerId = str
"""Players will get an ID that is unique within the agent context."""
Timestamp = float
class PlayerMessage(TypedDict, total=True):
    """Have one type per entry in MediaLogRecord::Type Corresponds to kMessage"""
    level: Literal["error", "warning", "info", "debug"]
    """Keep in sync with MediaLogMessageLevel We are currently keeping the message level 'error' separate from the PlayerError type because right now they represent different things, this one being a DVLOG(ERROR) style log message that gets printed based on what log level is selected in the UI, and the other is a representation of a media::PipelineStatus object. Soon however we're going to be moving away from using PipelineStatus for errors and introducing a new error type which should hopefully let us integrate the error log level into the PlayerError type."""
    message: str
class PlayerProperty(TypedDict, total=True):
    """Corresponds to kMediaPropertyChange"""
    name: str
    value: str
class PlayerEvent(TypedDict, total=True):
    """Corresponds to kMediaEventTriggered"""
    timestamp: Timestamp
    value: str
class PlayerErrorSourceLocation(TypedDict, total=True):
    """Represents logged source line numbers reported in an error. NOTE: file and line are from chromium c++ implementation code, not js."""
    file: str
    line: int
class PlayerError(TypedDict, total=True):
    """Corresponds to kMediaError"""
    errorType: str
    code: int
    """Code is the numeric enum entry for a specific set of error codes, such as PipelineStatusCodes in media/base/pipeline_status.h"""
    stack: List[PlayerErrorSourceLocation]
    """A trace of where this error was caused / where it passed through."""
    cause: List[PlayerError]
    """Errors potentially have a root cause error, ie, a DecoderError might be caused by an WindowsError"""
    data: Dict[str, Any]
    """Extra data attached to an error, such as an HRESULT, Video Codec, etc."""
class Player(TypedDict, total=True):
    playerId: PlayerId
    domNodeId: NotRequired[BackendNodeId]